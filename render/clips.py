"""Audio for the lexicon's written examples (the sentences the content agent writes for a word, not lines of a scene).

One clip per unique (pair, example text), read by a single neutral "dictionary" voice per language (settings.json `clips.voices`),
with the same Qwen3-TTS, stress policy and per-sentence cache as the scenes, levelled to the program loudness and encoded like a
scene (24 kHz mono LAME). Every clip is checked with Whisper; a failing one is retaken (other seed / temperature) up to
`clips.retakes` times and dropped when it still fails, so the app shows no speaker icon for it.

  <store>/clips/<id>.mp3 + <id>.json     a finished clip and its record (status "ok"), or a record alone (status "failed")
  <store>/clips/.work/<id>.{json,mp3}    a clip waiting for its Whisper check

`id` = clip_id(pair, text). The publisher derives the same id from an example's text, so it needs nothing else from here.
A record is current when its `ckey` equals the clip's render key (tts cache keys of its sentences + assembly settings).
"""
import hashlib
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path

import config
import textprep
from plan import cache_key


def clip_id(pair: str, text: str) -> str:
    """16 hex chars of sha256(pair NUL text). The publisher has the same function (publish/rulisten_pub/clips.py)."""
    return hashlib.sha256(f"{pair}\0{text}".encode("utf-8")).hexdigest()[:16]


def assembly_signature(settings) -> dict:
    c = {k: v for k, v in settings["clips"].items() if k not in ("gpu", "prio", "batch")}
    return {"clips": c, "audio": settings["audio"], "version": "c1"}


@dataclass
class Item:
    id: str
    pair: str
    lang: str
    text: str
    voice: str
    sents: list = field(default_factory=list)      # textprep.Sentence with .key
    ckey: str = ""


def examples(scene):
    """Unique example texts of one scene's lexicon, in entry order."""
    out, seen = [], set()
    for entry in (scene.notes.get("lexicon") or {}).values():
        for ex in entry.get("examples") or []:
            t = ex.get("text")
            if isinstance(t, str) and t.strip() and t not in seen:
                seen.add(t)
                out.append(t)
    return out


def warm_ruaccent(scenes, settings, ruaccent):
    """Accents every sentence that will need RuAccent in ONE call (it starts a model per call), so planning one scene at a time later
    only reads the cache. Planning happens before any GPU reservation is taken."""
    if ruaccent is None or not settings["stress"]["ruaccentFallback"]:
        return
    policy = config.stress_policy(settings)
    if policy == "none":
        return
    need = []
    for sc in scenes:
        if sc.lang != "ru":
            continue
        for text in examples(sc):
            _, _, missing = textprep.segment_inserts(text, None, policy)
            for a, b, sent in textprep.split_sentences(text):
                if any(a <= m0 and m1 <= b for m0, m1 in missing):
                    need.append(sent)
    if need:
        ruaccent(need)


def plan_scene(scene, settings, voices, ruaccent=None):
    """[Item] for every example of the scene (stress marks injected the way scenes do), or [] when no voice is set for the language."""
    voice = settings["clips"]["voices"].get(scene.lang)
    if not voice:
        return []
    ref = voices.ref_version(voice)
    # stage.py clips uses QwenEngine, independently of the scene engines.
    synth_settings = {k: v for k, v in settings.items() if k not in ("ttsRu", "ttsEn")}
    policy = config.stress_policy(settings)
    asig = config.sha(assembly_signature(settings))
    gap = settings["audio"]["interSentenceGap"][scene.lang]
    items = []
    for text in examples(scene):
        sents = textprep.prepare_segment(0, "clip", text, scene.lang, None, policy, 0.0, gap,
                                         ruaccent=ruaccent if (scene.lang == "ru" and settings["stress"]["ruaccentFallback"]) else None)
        for st in sents:
            st.voice = voice
            st.key = cache_key(synth_settings, voice, ref, scene.lang, st.tts)
        ckey = config.sha({"sents": [s.key for s in sents], "assembly": asig})
        items.append(Item(clip_id(scene.pair, text), scene.pair, scene.lang, text, voice, sents, ckey))
    return items


class ClipStore:
    """<store>/<kind>/: the finished items of one kind ("clips": example sentences, "forms": table forms; same layout and records)."""
    def __init__(self, root, kind="clips"):
        self.dir = Path(root) / kind
        self.work = self.dir / ".work"
        self.work.mkdir(parents=True, exist_ok=True)

    def record(self, cid):
        try:
            return json.loads((self.dir / f"{cid}.json").read_text("utf-8"))
        except Exception:
            return None

    def is_done(self, item) -> bool:
        r = self.record(item.id)
        return bool(r) and r.get("ckey") == item.ckey and (r.get("status") == "failed" or (self.dir / f"{item.id}.mp3").exists())

    def work_record(self, cid):
        try:
            return json.loads((self.work / f"{cid}.json").read_text("utf-8"))
        except Exception:
            return None

    def write_work(self, cid, rec):
        p = self.work / f"{cid}.json"
        tmp = p.with_suffix(".tmp")
        tmp.write_text(json.dumps(rec, ensure_ascii=False, sort_keys=True), "utf-8")
        tmp.replace(p)

    def pending(self, items):
        return [it for it in items if not self.is_done(it)]


def pending_for(scenes, settings, voices, store_root, ruaccent=None):
    """{id: Item} not yet finished, over the scenes (deduplicated by id)."""
    cs = ClipStore(store_root)
    out = {}
    warm_ruaccent(scenes, settings, ruaccent)
    for sc in scenes:
        for it in plan_scene(sc, settings, voices, ruaccent):
            if it.id not in out and not cs.is_done(it):
                out[it.id] = it
    return out


# ---- GPU side (venv-qwen) ---------------------------------------------------------------------------------------
def render_items(items, engine, store, settings, attempt, log=print, kind="clips"):
    """Synthesis (attempt 0: missing sentences; attempt k: new takes of the items whose check failed k times) and assembly of
    each item to .work/<id>.mp3. Returns the ids to check."""
    import numpy as np
    import soundfile as sf
    import audio
    import tts
    cs = ClipStore(store.root, kind)
    cfg = settings[kind]
    sr = settings["audio"]["sampleRate"]
    if attempt == 0:
        uniq = {}
        for it in items:
            for st in it.sents:
                uniq.setdefault(st.key, {"key": st.key, "voice": it.voice, "lang": it.lang, "text_tts": st.tts, "text_plain": st.plain})
        stats = engine.synth_many(list(uniq.values()), store)
        log(f"{kind} synth: {stats}")
    else:
        temp = cfg["temperatures"][(attempt - 1) % len(cfg["temperatures"])]
        langs = settings["tts"]["languages"]
        flat, once = [], set()
        for it in items:
            for st in it.sents:
                if st.key not in once:          # items that share a sentence (the same form in two slots) share its retake
                    once.add(st.key)
                    flat.append((it, st))
        bs = max(1, int(cfg["batch"]))
        for i in range(0, len(flat), bs):
            chunk = flat[i:i + bs]
            seed = int(chunk[0][1].key[8:16], 16) + 1000 * attempt
            wavs = engine.generate([(it.voice, langs[it.lang], st.tts) for it, st in chunk], seed, temp)
            for (it, st), w in zip(chunk, wavs):
                p = store.tts_path(st.key)
                tmp = p.with_suffix(".tmp.flac")
                sf.write(str(tmp), w, tts.NATIVE_SR, format="FLAC", subtype="PCM_16")
                tmp.replace(p)
    ids = []
    pad = np.zeros(int(sr * cfg["padMs"] / 1000), dtype=np.float32)
    for it in items:
        line = []
        for st in it.sents:
            wav = tts.load_wav(store.tts_path(st.key))[0]
            line.append((audio.prepare_sentence(wav, sr, settings["audio"]), st.gap))
        sig, _ = audio.assemble([line], sr, settings["audio"])
        sig, gain, measured = audio.master(np.concatenate([pad, sig, pad]), sr, {"programLufs": cfg["programLufs"]})
        out = cs.work / f"{it.id}.mp3"
        tmp = cs.work / f"{it.id}.tmp.mp3"
        audio.encode_mp3(sig, sr, tmp, settings["audio"]["mp3Kbps"])
        tmp.replace(out)
        prev = cs.work_record(it.id) or {}
        cs.write_work(it.id, {"id": it.id, "pair": it.pair, "text": it.text, "lang": it.lang, "voice": it.voice, "ckey": it.ckey,
                              "tries": attempt, "keys": [s.key for s in it.sents], "tts": " ".join(s.tts for s in it.sents), "durationSec": round(len(sig) / sr, 3),
                              "history": prev.get("history", [])})
        ids.append(it.id)
    return ids


def retakes_among(items, cs, attempt):
    """The `items` whose work record says they failed `attempt` checks and are still current."""
    want = {}
    for it in items:
        w = cs.work_record(it.id)
        if w and w.get("ckey") == it.ckey and w.get("tries") == attempt - 1 and w.get("failedCheck") and not cs.is_done(it):
            want[it.id] = it
    return list(want.values())


def items_for_retake(scenes, settings, voices, store_root, attempt, ruaccent=None):
    """Example items whose work record says they failed `attempt` checks and are still current."""
    return retakes_among([it for sc in scenes for it in plan_scene(sc, settings, voices, ruaccent)], ClipStore(store_root), attempt)


# ---- ASR side (venv with faster-whisper): checks the work mp3s and commits or fails them -------------------------
def commit(store_root, cid, cer, hyp, cfg, kind="clips"):
    """Pass: .work/<id>.mp3 -> <kind>/<id>.mp3 and its record. Returns True."""
    import shutil
    cs = ClipStore(store_root, kind)
    w = cs.work_record(cid)
    src = cs.work / f"{cid}.mp3"
    data = src.read_bytes()
    rec = {k: w[k] for k in ("id", "pair", "text", "lang", "voice", "ckey", "durationSec")}
    rec.update(status="ok", cer=round(cer, 4), tries=w["tries"] + 1, audioSha256=hashlib.sha256(data).hexdigest(), audioBytes=len(data),
               renderedAt=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    tmp = cs.dir / f".{cid}.tmp.mp3"
    shutil.copyfile(src, tmp)
    tmp.replace(cs.dir / f"{cid}.mp3")
    (cs.dir / f".{cid}.tmp.json").write_text(json.dumps(rec, ensure_ascii=False, sort_keys=True, indent=1), "utf-8")
    (cs.dir / f".{cid}.tmp.json").replace(cs.dir / f"{cid}.json")
    src.unlink(missing_ok=True)
    (cs.work / f"{cid}.json").unlink(missing_ok=True)


def fail_final(store_root, cid, cer, hyp, kind="clips"):
    """Out of retakes: record the failure (so it is not retried until its inputs change) and drop the audio."""
    cs = ClipStore(store_root, kind)
    w = cs.work_record(cid)
    rec = {k: w[k] for k in ("id", "pair", "text", "lang", "voice", "ckey")}
    rec.update(status="failed", cer=round(cer, 4), hyp=hyp, tries=w["tries"] + 1,
               renderedAt=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    (cs.dir / f".{cid}.tmp.json").write_text(json.dumps(rec, ensure_ascii=False, sort_keys=True, indent=1), "utf-8")
    (cs.dir / f".{cid}.tmp.json").replace(cs.dir / f"{cid}.json")
    (cs.dir / f"{cid}.mp3").unlink(missing_ok=True)
    (cs.work / f"{cid}.mp3").unlink(missing_ok=True)
    (cs.work / f"{cid}.json").unlink(missing_ok=True)
