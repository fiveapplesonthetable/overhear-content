"""Render one scene: TTS (cloned voices) -> assemble -> MMS alignment -> stress check -> (ElevenLabs fallback) -> store.

GPU work; the caller (worker.py) holds gpurun reservation.
"""
import datetime
import json
import re
import time
from pathlib import Path

import numpy as np

import audio
import config
import stresscheck
import textprep
import tts
import native_text
from plan import check_voices, render_key, voice_clashes
from store import sha256_file

TOKEN_RE = re.compile(r"[\w]", re.UNICODE)


def seg_tokens(text, words=None):
    """Tokens timed per segment: the whitespace tokens that contain a letter or digit, exactly the publisher's
    tokens.tokenize(), so render_source.word_times() finds one timing entry per token."""
    return [t for t in text.split() if TOKEN_RE.search(t)]


class Ctx:
    def __init__(self, scene, roles, rkey, sents, uniq):
        self.scene, self.roles, self.rkey, self.sents, self.uniq = scene, roles, rkey, sents, uniq


class Renderer:
    """Three GPU-light steps, each run in its own process under its own VRAM reservation (see stage.py):
    synth (Qwen, 4.8 GB) -> finish (MMS_FA alignment, 1.5 GB) -> [retake (Qwen) -> finish]."""

    def __init__(self, settings, voices, store, ruaccent=None, log=print):
        self.s, self.voices, self.store = settings, voices, store
        self.ruaccent, self.log = ruaccent, log
        self.sr = settings["audio"]["sampleRate"]
        self.policy = config.stress_policy(settings)

    # -- planning -------------------------------------------------------------------------------------------
    def prepare(self, scene):
        if any("sourceAudio" in seg for seg in scene.script["segments"]):
            raise ValueError("original show sourceAudio is private verification only; public render requires validated native synthesis")
        roles = check_voices(scene, self.voices)
        rkey = render_key(scene, self.voices, self.s, roles)
        notes_by_seg = {l["seg"]: l.get("words") or [] for l in scene.notes.get("lines", []) if isinstance(l, dict)}
        sents = []
        isent_cfg = self.s["audio"]["interSentenceGap"]
        for i, g in enumerate(scene.script["segments"]):
            voice = roles[g["v"]]
            lang = self.voices.lang_of(voice)
            native_words = native_text.words_for_segment(g["t"], notes_by_seg.get(i), lang) if lang in native_text.LANGUAGES else ()
            for st in textprep.prepare_segment(
                    i, g["v"], g["t"], lang, notes_by_seg.get(i), self.policy, float(g.get("gap", 0.35) or 0), isent_cfg.get(lang, isent_cfg["en"]),
                    ruaccent=self.ruaccent if (lang == "ru" and self.s["stress"]["ruaccentFallback"]) else None):
                st.voice = voice
                st.key = tts.cache_key(self.s, voice, self.voices.ref_version(voice), lang, st.tts)
                if native_words:
                    end = st.start + len(st.plain)
                    overlapping = [word for word in native_words if word.start < end and word.end > st.start]
                    if any(word.start < st.start or word.end > end for word in overlapping):
                        raise native_text.NativeAlignmentError("an authored native word crosses a sentence boundary")
                    st.alignment_words = tuple(native_text.Word(word.text, word.start - st.start, word.end - st.start, word.reading) for word in overlapping)
                    st.key = config.sha({"ttsKey": st.key, "nativeAlignment": native_text.VERSION,
                                         "words": [[word.text, word.start, word.end, word.reading] for word in st.alignment_words]})
                sents.append(st)
        uniq = {}
        for st in sents:
            uniq.setdefault(st.key, {"key": st.key, "voice": st.voice, "lang": st.lang, "text_tts": st.tts, "text_plain": st.plain})
        return Ctx(scene, roles, rkey, sents, uniq)

    # -- step 1: synthesis ------------------------------------------------------------------------------------
    def synth(self, ctx, engine, lang=None, not_lang=None):
        """Missing sentences of the scene; `lang` / `not_lang` pick the engine's share (Russian goes to ESpeech when ttsRu is set)."""
        items = [it for it in ctx.uniq.values() if (lang is None or it["lang"] == lang) and (not_lang is None or it["lang"] != not_lang)]
        return engine.synth_many(items, self.store)

    # -- step 3: stress retakes (local, other seeds / temperatures) --------------------------------------------
    def cand_path(self, key, k):
        return self.store.tts_path(key).with_name(f"{key}.c{k}.flac")

    def marker(self, key):
        return self.store.tts_path(key).with_name(f"{key}.cands.json")

    def retake(self, ctx, engine, keys):
        import soundfile as sf
        cfg = self.s["stressRetry"]
        items = [ctx.uniq[k] for k in keys]
        bs = max(1, int(self.s["tts"]["batch"]))
        made = {k: [] for k in keys}
        for t in range(cfg["attempts"]):
            temp = cfg["temperatures"][t % len(cfg["temperatures"])]
            for i in range(0, len(items), bs):
                chunk = items[i:i + bs]
                seed = int(chunk[0]["key"][8:16], 16) + 1000 * (t + 1)
                langs = self.s["tts"]["languages"]
                wavs = engine.generate([(c["voice"], langs[c["lang"]], c["text_tts"]) for c in chunk], seed, temp)
                for c, w in zip(chunk, wavs):
                    if tts.plausible(c["text_plain"], len(w) / tts.NATIVE_SR):
                        sf.write(str(self.cand_path(c["key"], t)), w, tts.NATIVE_SR, format="FLAC", subtype="PCM_16")
                        made[c["key"]].append(t)
        for k in keys:
            self.marker(k).write_text(json.dumps({"attempts": cfg["attempts"], "made": made[k]}))
        return {"retaken": len(keys), "takes": sum(len(v) for v in made.values())}

    # -- step 2: align, check, assemble, store -----------------------------------------------------------------
    def finish(self, ctx, aligner, content_commit=None, allow_retake=True, times=None):
        """("retake", [keys]) when flagged sentences have no local retakes yet, else ("done", result)."""
        t_start = time.time()
        import soundfile as sf
        s, sents, scene, roles, voices = self.s, ctx.sents, ctx.scene, ctx.roles, self.voices
        sr = self.sr

        def evaluate(st, wav):
            clip = audio.prepare_sentence(wav, sr, s["audio"])
            if st.lang in native_text.LANGUAGES:
                ct, x16 = aligner.word_times(clip, sr, st.plain, st.lang, st.alignment_words)
            else:
                ct, x16 = aligner.char_times(clip, sr, st.plain, st.lang)
            return clip, ct, x16, self.check(st, ct)

        first = {}
        for st in sents:
            first.setdefault(st.key, st)
        best = {}
        for key, st in first.items():
            wav = tts.load_wav(self.store.tts_path(key))[0]
            clip, ct, x16, ck = evaluate(st, wav)
            best[key] = {"bad": self.badness(ck), "wav": wav, "clip": clip, "ct": ct, "x16": x16, "ck": ck, "take": 0}
        
        # New Retake Stats Aggregation from .gates.json (created by synth_many gates)
        retake = {"sentences": [], "takes": 0, "retakes": 0, "length": 0, "repeat": 0, "transient": 0, "similarity": 0, "cer": 0}
        for key, st in first.items():
            if self.store.tts_path(key).with_name(f"{key}.gates.json").exists():
                try:
                    counts = json.loads(self.store.tts_path(key).with_name(f"{key}.gates.json").read_text())
                    if "takes" in counts:
                        retake["takes"] += counts.get("takes", 0)
                        retake["retakes"] += counts.get("retakes", 0)
                        retake["length"] += counts.get("length", 0)
                        retake["repeat"] += counts.get("repeat", 0)
                        retake["transient"] += counts.get("transient", 0)
                        retake["similarity"] += counts.get("similarity", 0)
                        retake["cer"] += counts.get("cer", 0)
                except Exception:
                    pass

        flagged_keys = [k for k, b in best.items() if b["bad"][0] > 0]
        # Legacy retake marker handling (if any fallback)
        need = [k for k in flagged_keys if not self.marker(k).exists()]
        if need and allow_retake and s["stressRetry"]["attempts"] > 0:
            return "retake", need
            
        for key in flagged_keys:
            st, b = first[key], best[key]
            made = []
            if self.store.tts_path(key).with_name(f"{key}.gates.json").exists():
                try:
                    cands = json.loads(self.store.tts_path(key).with_name(f"{key}.gates.json").read_text())
                    made = cands.get("made", [])
                except:
                    made = []
            for t in made:
                p = self.cand_path(key, t)
                if not p.exists():
                    continue
                w = tts.load_wav(p)[0]
                clip, ct, x16, ck = evaluate(st, w)
                bad = self.badness(ck)
                if bad < b["bad"]:
                    b.update(bad=bad, wav=w, clip=clip, ct=ct, x16=x16, ck=ck, take=t + 1)
            if b["take"]:   # keep the better take for good
                cp = self.store.tts_path(key)
                tmpf = cp.with_suffix(".tmp.flac")
                sf.write(str(tmpf), b["wav"], tts.NATIVE_SR, format="FLAC", subtype="PCM_16")
                tmpf.replace(cp)
            retake["sentences"].append({"seg": st.seg, "idx": st.idx, "text": st.plain, "takesTried": len(made),
                                        "bestTake": b["take"], "stillFlagged": b["bad"][0] > 0})
            for t in made:
                self.cand_path(key, t).unlink(missing_ok=True)

        warnings = [f"voice {k} is shared by roles {rs} in this scene" for k, rs in voice_clashes(roles).items()]
        clips = [best[st.key]["clip"] for st in sents]
        checks = {n: best[st.key]["ck"] for n, st in enumerate(sents)}
        x16s = {n: best[st.key]["x16"] for n, st in enumerate(sents)}
        char_times = {n: best[st.key]["ct"] for n, st in enumerate(sents)}
        flagged_first = len(flagged_keys)
        t_align = time.time() - t_start

        lines = {}
        for st, x in zip(sents, clips):
            lines.setdefault(st.seg, []).append((x, st.gap))
        sig, lay = audio.assemble([lines[k] for k in sorted(lines)], sr, s["audio"])
        sig, gain, measured = audio.master(sig, sr, s["audio"])
        tmp = self.store.root / f".{scene.id}.{int(time.time())}.mp3"
        audio.encode_mp3(sig, sr, tmp, s["audio"]["mp3Kbps"])
        dur_mp3 = audio.mp3_duration(tmp, sr)
        duration = len(sig) / sr

        spans_segments, timing = [], {}
        by_seg = {}
        for n, st in enumerate(sents):
            by_seg.setdefault(st.seg, []).append(n)
        notes_by_seg = {l["seg"]: l.get("words") or [] for l in scene.notes.get("lines", []) if isinstance(l, dict)}
        timing_bad = 0
        for si, g in enumerate(scene.script["segments"]):
            start, end, nxt, sent_spans = lay[si]
            ids = by_seg[si]
            spans_segments.append({
                "seg": si, "v": g["v"], "voice": roles[g["v"]], "lang": sents[ids[0]].lang,
                "start": round(start, 3), "end": round(end, 3), "nextStart": round(nxt, 3),
                "sentences": [{"i": sents[n].idx, "start": round(a, 3), "end": round(b, 3), "text": sents[n].plain,
                               "engine": config.engine_label(s, sents[n].lang)} for n, (a, b) in zip(ids, sent_spans)]})
            native = sents[ids[0]].lang in native_text.LANGUAGES
            units = native_text.words_for_segment(g["t"], notes_by_seg.get(si), sents[ids[0]].lang) if native else ()
            toks = [word.text for word in units] if native else seg_tokens(g["t"], notes_by_seg.get(si))
            tspans = [(word.start, word.end) for word in units] if native else textprep.token_spans(g["t"], toks)
            words = [None] * len(toks)
            for n, (a, b) in zip(ids, sent_spans):
                st = sents[n]
                idx = [j for j, sp in enumerate(tspans) if sp is not None and st.start <= sp[0] < st.start + len(st.plain)]
                if not idx:
                    continue
                rel = [(tspans[j][0] - st.start, tspans[j][1] - st.start) for j in idx]
                if native:
                    wt = char_times[n]
                    if len(wt) != len(idx) or any(not word["ok"] for word in wt):
                        raise native_text.NativeAlignmentError("incomplete native acoustic word alignment; interpolation is forbidden")
                else:
                    env, hop = audio_env(x16s[n])
                    wt = align_words(char_times[n], rel, env, hop, s["align"]["snapMaxMs"])
                for j, w in zip(idx, wt):
                    words[j] = {"t": toks[j], "s": round(a + w["s"], 3), "e": round(a + w["e"], 3), "ok": w["ok"], "why": w["why"]}
                    if native:
                        words[j].update(span=list(tspans[j]), confidence=w["confidence"], alignment=native_text.VERSION)
            prev = start
            for j, w in enumerate(words):
                if w is None:
                    if native:
                        raise native_text.NativeAlignmentError("missing native word timing; interpolation is forbidden")
                    words[j] = {"t": toks[j], "s": round(prev, 3), "e": round(prev, 3), "ok": False, "why": "missing"}
                prev = words[j]["e"]
            timing_bad += sum(1 for w in words if not w["ok"])
            timing[str(si)] = words

        still = []
        checked = flagged_words = 0
        for n, c in checks.items():
            checked += len(c)
            flagged_words += sum(w["flag"] for w in c)
            if any(w["flag"] for w in c):
                still.append({"seg": sents[n].seg, "idx": sents[n].idx, "text": sents[n].plain, "words": [w for w in c if w["flag"]]})
        ru_sents = [n for n, st in enumerate(sents) if st.lang == "ru" and st.role != "narrator"]
        uniq_still = {x["text"] for x in still}
        report = {
            "version": 1, "sceneId": scene.id,
            "stress": {"policy": self.policy, "scope": s["stressCheck"]["scope"], "ratio": s["stressCheck"]["ratio"],
                       "russianSentences": len(ru_sents), "wordsChecked": checked, "wordsFlagged": flagged_words,
                       "sentencesFlaggedInitially": flagged_first, "stillFlagged": len(uniq_still),
                       "flaggedRatio": round(flagged_first / max(1, len({sents[n].key for n in ru_sents})), 4),
                       "unresolved": still,
                       "missingMarks": [{"seg": st.seg, "idx": st.idx, "tokens": st.missing} for st in sents if st.missing]},
            "retake": retake,
            "tts": {"sentences": len(sents), "unique": len(ctx.uniq)},
            "timing": {"tokens": sum(len(v) for v in timing.values()), "notOk": timing_bad},
            "audio": {"seconds": round(duration, 3), "mp3Seconds": round(dur_mp3, 3), "programLufsBefore": round(measured, 2),
                      "gainDb": round(gain, 2)},
            "warnings": warnings,
        }
        spans = {"version": 1, "sceneId": scene.id, "sampleRate": sr, "durationSec": round(duration, 3), "segs": spans_segments}
        timing_doc = timing          # publisher shape: {"<seg>": [{t, s, e, ok, why}]}, nothing else at the top level
        jb = lambda o: (json.dumps(o, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
        spans_b, timing_b, report_b = jb(spans), jb(timing_doc), jb(report)
        times = times or {}
        meta = {
            "sceneId": scene.id, "renderKey": ctx.rkey, "contentHash": scene.content_hash, "contentCommit": content_commit,
            **({"nativeAlignment": native_text.VERSION} if scene.lang in native_text.LANGUAGES else {}),
            "pipelineVersion": config.PIPELINE_VERSION, "renderVersion": s["renderVersion"],
            "tts": {"model": (f"{config.engine_label(s, 'ar')}+{config.engine_label(s, 'en')}" if scene.lang == "ar" and config.ar_engine(s) else s["tts"]["model"]),
                    "lora": (s["lora"]["tag"] if s["lora"]["enabled"] else None), "stressPolicy": self.policy, "gen": config.tts_signature(s)["gen"],
                    **({"nativeEngine": config.engine_label(s, scene.lang)} if scene.lang in native_text.LANGUAGES else {}),
                    **({"nativeGen": {key: value for key, value in config.ar_engine(s).items() if key in ("temperature", "cfg_weight", "exaggeration", "repetition_penalty", "min_p", "top_p")}} if scene.lang == "ar" and config.ar_engine(s) else {})},
            "voicesVersion": voices.voices_version(),
            "voices": {r: {"voice": k, "refVersion": voices.ref_version(k)} for r, k in sorted(roles.items())},
            "align": f"mms_fa/{s['align']['version']}",
            "renderedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "durationSec": round(duration, 3), "sampleRate": sr, "bitrateKbps": s["audio"]["mp3Kbps"],
            "audioSha256": sha256_file(tmp), "audioBytes": tmp.stat().st_size,
            "spansSha256": config.sha(spans_b), "timingSha256": config.sha(timing_b),
            "wall": {"total": round(times.get("synth", 0) + times.get("retake", 0) + time.time() - t_start, 2),
                     "tts": round(times.get("synth", 0) + times.get("retake", 0), 2), "align": round(time.time() - t_start, 2)},
        }
        self.store.commit_scene(scene.id, {"audio.mp3": tmp, "spans.json": spans_b, "timing.json": timing_b,
                                           "report.json": report_b, "meta.json": jb(meta)})
        tmp.unlink(missing_ok=True)
        return "done", {"sceneId": scene.id, "renderKey": ctx.rkey, "audioSec": duration, "wallSec": meta["wall"]["total"],
                        "ttsSec": meta["wall"]["tts"], "generatedSec": times.get("generatedSec", 0.0),
                        "generated": times.get("generated", 0), "cached": times.get("cached", 0),
                        "flagged": flagged_first, "stillFlagged": len(uniq_still), "russian": len(ru_sents), "timingNotOk": timing_bad}

    @staticmethod
    def badness(ck):
        """(flagged words, worst off-ratio): lower is better."""
        fl = [w for w in ck if w["flag"]]
        return (len(fl), max([w["ratio"] for w in fl], default=0.0))

    def check(self, st, char_times):
        if st.lang != "ru" or st.role == "narrator" or not st.expected:
            return []
        return stresscheck.check_sentence(st.plain, st.expected, char_times, self.s["stressCheck"]["scope"], self.s["stressCheck"]["ratio"])


def audio_env(x16):
    from align import envelope
    return envelope(x16)


def align_words(char_times, spans, env, hop, snap_ms):
    from align import words_from_chars
    return words_from_chars(char_times, spans, env, hop, snap_ms)
