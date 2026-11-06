#!/usr/bin/env python3
"""Checks a render tree against the output contract (spec/OUTPUT-CONTRACT.md). Python 3 stdlib only.

  python3 tools/check_render.py RENDER_DIR                      # every scene of out/ that has a render folder
  python3 tools/check_render.py RENDER_DIR --episode kukhnya-s01e01   # one episode: every scene must be rendered
  python3 tools/check_render.py RENDER_DIR --scene dix-pour-cent-s01e01-scene-01
  options: --content DIR  content repo root (default: this repo)
           --strict       warnings count as errors

Errors are exactly the conditions under which the publisher drops a scene's render (publish/rulisten_pub/render_source.load)
or a clip/form (clips.py, forms.py), plus integrity checks of the pipeline's own records (sha256s, durations, monotonic spans).
A scene the publisher would drop is published with no audio, so every error here is a broken lesson. Exit 0 = clean, 1 = errors.
"""
import hashlib, json, math, re, sys
from pathlib import Path

import importlib.util

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("overhear_word_spans", Path(__file__).with_name("word_spans.py"))
_word_spans = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_word_spans)

NATIVE = ("ja", "zh", "ko", "ar")                 # languages whose word timing must be native MMS + uroman spans
NATIVE_PREFIX = "mms-uroman-wordspans/1;"
SCENE_FILES = ("audio.mp3", "spans.json", "timing.json", "meta.json", "report.json")
META_REQUIRED = ("sceneId", "contentHash", "contentCommit", "tts", "voicesVersion", "align", "pipelineVersion", "renderVersion",
                 "renderKey", "renderedAt", "durationSec", "sampleRate", "bitrateKbps", "audioSha256", "audioBytes",
                 "spansSha256", "timingSha256")
_WORD_CHARS = re.compile(r"[\w]", re.UNICODE)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, msg): self.errors.append(f"{where}: {msg}")
    def warn(self, where, msg): self.warnings.append(f"{where}: {msg}")


def sha256_bytes(b): return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def content_hash(script_path, notes_path):
    """The publisher's content hash: sha256 of the script's bytes followed by the notes' bytes (content_repo.content_hash)."""
    h = hashlib.sha256()
    h.update(Path(script_path).read_bytes())
    h.update(Path(notes_path).read_bytes())
    return h.hexdigest()


def tokenize(text):
    """Whitespace tokens with at least one letter or digit (publisher tokens.tokenize)."""
    return [t for t in text.split() if _WORD_CHARS.search(t)]


def token_spans(text, tokens):
    spans, cursor = [], 0
    for tok in tokens:
        at = text.find(tok, cursor)
        if at < 0:
            raise ValueError(f"token {tok!r} not found in order")
        spans.append((at, at + len(tok)))
        cursor = at + len(tok)
    return spans


def annotated_units(text, words, lang):
    """(tokens, character spans) the publisher aligns words to (tokens.annotated_units)."""
    spans = _word_spans.annotation_spans(text, words or [], required=lang in ("ja", "zh"))
    if spans is not None:
        return [text[a:b] for a, b in spans], spans
    toks = tokenize(text)
    return toks, token_spans(text, toks)


def clip_id(pair, text):
    return hashlib.sha256(f"{pair}\0{text}".encode("utf-8")).hexdigest()[:16]


def form_id(pair, lemma, title, row, column, cell):
    return hashlib.sha256("\0".join((pair, lemma, title, row, column, cell)).encode("utf-8")).hexdigest()[:16]


def num(x): return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def load_json(p, rep, where):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        rep.err(where, f"{Path(p).name}: {e}")
        return None


# ---------------------------------------------------------------- content side
def _content_roots(content, root=None, episode=None, scene=None):
    content = Path(content)
    if content.name in ("out", "originals") and not (content / "out").is_dir() and not (content / "originals").is_dir():
        return [content]
    if root in ("out", "originals"):
        return [content / root]
    if episode or scene:
        return [content / r for r in ("originals", "out") if (content / r).is_dir()]
    return [content / "out"]


def scenes_of(content, episode=None, scene=None, root=None):
    """[(sceneId, script path, notes path, merged)] in the content root, in order."""
    out = []
    for rdir in _content_roots(content, root=root, episode=episode, scene=scene):
        if not rdir.is_dir():
            continue
        for sj in sorted(rdir.glob("*/s??e??/scenes.json")):
            if sj.parent.parent.name.startswith("_"):
                continue
            d = json.loads(sj.read_text(encoding="utf-8"))
            ep = f"{d['show']}-s{d['season']:02d}e{d['episode']:02d}"
            if episode and ep != episode:
                continue
            for s in d["scenes"]:
                sid = f"{ep}-scene-{s['scene']:02d}"
                if scene and sid != scene:
                    continue
                out.append((sid, sj.parent / f"scene-{s['scene']:02d}.json", sj.parent / f"scene-{s['scene']:02d}.notes.json", s.get("merge") is not None))
    return out


# ---------------------------------------------------------------- one scene
def check_scene(render, sid, script_path, notes_path, rep):
    d = render / sid
    w = str(d)
    if not d.is_dir():
        return rep.err(w, "not rendered (folder missing)")
    for f in SCENE_FILES:
        if not (d / f).is_file():
            rep.err(w, f"missing {f}")
    script = json.loads(script_path.read_text(encoding="utf-8"))
    notes = json.loads(notes_path.read_text(encoding="utf-8"))
    segs = script["segments"]
    lang = script["pair"].split("-")[0]
    if any("sourceAudio" in s for s in segs):
        rep.err(str(script_path), "a segment carries sourceAudio: original show audio is never published")
    meta = load_json(d / "meta.json", rep, w) if (d / "meta.json").is_file() else None
    spans_doc = load_json(d / "spans.json", rep, w) if (d / "spans.json").is_file() else None
    timing = load_json(d / "timing.json", rep, w) if (d / "timing.json").is_file() else None
    if (d / "report.json").is_file():
        report = load_json(d / "report.json", rep, w)
        if report and (report.get("timing") or {}).get("notOk"):
            rep.warn(w, f"report.json: {report['timing']['notOk']} of {report['timing'].get('tokens')} tokens have ok=false timing")
        for x in (report or {}).get("warnings") or []:
            rep.warn(w, f"report.json warning: {x}")
    audio = d / "audio.mp3"
    if audio.is_file() and audio.stat().st_size == 0:
        rep.err(w, "audio.mp3 is empty")
    if meta is None or spans_doc is None:
        return
    # -- the publisher's rules (render_source.load)
    prov = meta.get("audioProvenance", {})
    if not isinstance(prov, dict):
        rep.err(w, "meta.audioProvenance must be an object")
    elif prov.get("kind") == "original-source" or meta.get("privateSourceAudio") or meta.get("containsOriginalSourceAudio"):
        rep.err(w, "meta marks original source audio: never publishable")
    want = content_hash(script_path, notes_path)
    if meta.get("contentHash") != want:
        rep.err(w, f"stale: meta.contentHash {str(meta.get('contentHash'))[:12]} != sha256(script+notes) {want[:12]} (re-render after any script/notes edit)")
    if meta.get("sceneId") != sid:
        rep.err(w, f"meta.sceneId {meta.get('sceneId')!r} != folder")
    for k in META_REQUIRED:
        if k not in meta:
            rep.err(w, f"meta.json lacks {k}")
    if not (isinstance(meta.get("tts"), str) or (isinstance(meta.get("tts"), dict) and meta["tts"].get("model"))):
        rep.err(w, "meta.tts must be a model name or an object with `model`")
    by_seg = {}
    for e in spans_doc.get("segs", []):
        if not (isinstance(e, dict) and isinstance(e.get("seg"), int) and num(e.get("start")) and num(e.get("end"))):
            rep.err(w, f"spans.json: bad entry {e!r}"); return
        if e["seg"] in by_seg:
            rep.err(w, f"spans.json: seg {e['seg']} listed twice")
        by_seg[e["seg"]] = (e["start"], e["end"])
    if sorted(by_seg) != list(range(len(segs))):
        return rep.err(w, f"spans.json has {len(by_seg)} segs for {len(segs)} script segments (needs exactly seg 0..{len(segs) - 1})")
    dur = spans_doc.get("durationSec")
    if not num(dur):
        rep.err(w, "spans.json: durationSec missing")
        dur = by_seg[len(segs) - 1][1]
    prev = 0.0
    for i in range(len(segs)):
        s, e = by_seg[i]
        if not (prev - 1e-3 <= s < e <= dur + 1e-3):
            rep.err(w, f"spans.json: seg {i} [{s}, {e}] not inside [previous end {prev}, duration {dur}] or empty")
        prev = e
    if num(meta.get("durationSec")) and abs(meta["durationSec"] - dur) > 0.05:
        rep.err(w, f"meta.durationSec {meta['durationSec']} != spans.durationSec {dur}")
    # -- integrity of the pipeline's own records
    if audio.is_file() and meta.get("audioSha256") and sha256_file(audio) != meta["audioSha256"]:
        rep.err(w, "audio.mp3 does not match meta.audioSha256")
    if audio.is_file() and meta.get("audioBytes") is not None and audio.stat().st_size != meta["audioBytes"]:
        rep.err(w, "audio.mp3 size != meta.audioBytes")
    for f, k in (("spans.json", "spansSha256"), ("timing.json", "timingSha256")):
        if (d / f).is_file() and meta.get(k):
            if sha256_file(d / f) != meta[k]:              # sha256 of the file's bytes as written
                rep.err(w, f"{f} does not match meta.{k} (edited after rendering?)")
    if meta.get("sampleRate") not in (None, 24000): rep.err(w, f"sampleRate {meta['sampleRate']} != 24000")
    if meta.get("bitrateKbps") not in (None, 96): rep.err(w, f"bitrateKbps {meta['bitrateKbps']} != 96")
    # -- word timing
    if not isinstance(timing, dict):
        return rep.err(w, "timing.json must be an object {\"<seg>\": [...]}")
    words_by_seg = {line["seg"]: line.get("words", []) for line in notes.get("lines", [])}
    native = lang in NATIVE
    conv = str(meta.get("nativeAlignment", ""))
    if native and not conv.startswith(NATIVE_PREFIX):
        rep.err(w, f"{lang}: meta.nativeAlignment must start with {NATIVE_PREFIX!r}")
    for i, seg in enumerate(segs):
        fine = timing.get(str(i), [])
        if seg["v"] == "narrator" and not native:
            toks = tokenize(seg["t"])
        elif seg["v"] == "narrator":
            continue
        else:
            try:
                toks, owned = annotated_units(seg["t"], words_by_seg.get(i), lang)
            except ValueError as e:
                rep.err(w, f"seg {i}: word units: {e}"); continue
        if len(fine) != len(toks):
            (rep.err if native else rep.warn)(w, f"seg {i}: timing has {len(fine)} items for {len(toks)} tokens" + ("" if native else " (the app falls back to proportional timing)"))
            continue
        p = by_seg[i][0]
        # native: inside the segment span, as the publisher demands; otherwise a word may run into the following pause
        limit = by_seg[i][1] if native else (by_seg[i + 1][0] if i + 1 < len(segs) else dur)
        for j, (tok, x) in enumerate(zip(toks, fine)):
            if not (isinstance(x, dict) and num(x.get("s")) and num(x.get("e"))):
                rep.err(w, f"seg {i} token {j}: bad timing item {x!r}"); break
            if x.get("t") != tok:
                (rep.err if native else rep.warn)(w, f"seg {i} token {j}: timing t {x.get('t')!r} != script token {tok!r}")
            if native:
                if x.get("span") != list(owned[j]) or x.get("ok") is not True or x.get("alignment") != conv:
                    rep.err(w, f"seg {i} token {j}: native timing needs span {list(owned[j])}, ok true, alignment == meta.nativeAlignment"); break
            if not (p - 1e-3 <= x["s"] < x["e"] <= limit + 1e-3):
                (rep.err if native else rep.warn)(w, f"seg {i} token {j}: [{x['s']}, {x['e']}] not monotonic inside [{by_seg[i][0]}, {limit}]")
            p = x["e"]


# ---------------------------------------------------------------- clips and forms
def check_audio_record(dirp, rid, text, rep, kind, current=None):
    """'ok' | 'failed' | 'missing' | 'bad' for one clip/form record."""
    jf, mp3 = dirp / f"{rid}.json", dirp / f"{rid}.mp3"
    if not jf.is_file():
        return "missing"
    try:
        rec = json.loads(jf.read_text(encoding="utf-8"))
    except ValueError as e:
        rep.err(str(jf), f"not JSON: {e}"); return "bad"
    if rec.get("status") == "failed":
        return "failed"
    if rec.get("status") != "ok":
        rep.err(str(jf), f"status must be ok or failed, not {rec.get('status')!r}"); return "bad"
    if rec.get("text") != text:
        rep.err(str(jf), f"text {rec.get('text')!r} != {text!r}"); return "bad"
    if not mp3.is_file() or mp3.stat().st_size == 0:
        rep.err(str(jf), "status ok but the mp3 is missing or empty"); return "bad"
    if rec.get("audioSha256") and sha256_file(mp3) != rec["audioSha256"]:
        rep.err(str(jf), "mp3 does not match audioSha256"); return "bad"
    if kind == "form" and current is not None and current.get(rid) != rec.get("ckey"):
        rep.warn(str(jf), "not in forms/.plan.json with this ckey: stale, the publisher will not ship it"); return "stale"
    return "ok"


def check_clips_forms(render, scene_list, rep):
    tally = {"clip": {}, "form": {}}
    plan = None
    pf = render / "forms" / ".plan.json"
    if pf.is_file():
        try:
            plan = {r["id"]: r["ckey"] for r in json.loads(pf.read_text(encoding="utf-8"))}
        except (ValueError, TypeError, KeyError) as e:
            rep.err(str(pf), f"must be a JSON list of {{id, ckey, ...}}: {e}"); plan = {}
    seen = set()
    for sid, sp, npth, merged in scene_list:
        if merged or not npth.is_file():
            continue
        pair = json.loads(sp.read_text(encoding="utf-8"))["pair"]
        lex = json.loads(npth.read_text(encoding="utf-8")).get("lexicon", {})
        for e in lex.values():
            for ex in e.get("examples", []):
                cid = clip_id(pair, ex["text"])
                if cid in seen: continue
                seen.add(cid)
                st = check_audio_record(render / "clips", cid, ex["text"], rep, "clip")
                tally["clip"][st] = tally["clip"].get(st, 0) + 1
            for t in ([e["forms"]] if e.get("forms") else []) + list(e.get("moreForms") or []):
                heads = t.get("columns") or []
                for row in t["rows"]:
                    for c, cell in enumerate(row["cells"][1:], 1):
                        if not cell: continue
                        fid = form_id(pair, e["lemma"], t.get("title", ""), row["cells"][0], heads[c] if c < len(heads) else "", cell)
                        if fid in seen: continue
                        seen.add(fid)
                        if plan is not None and fid not in plan and not (render / "forms" / f"{fid}.json").is_file():
                            st = "unplanned"
                        else:
                            st = check_audio_record(render / "forms", fid, cell, rep, "form", plan)
                        tally["form"][st] = tally["form"].get(st, 0) + 1
    if (render / "forms").is_dir() and plan is None:
        rep.err(str(render / "forms"), "missing .plan.json: without it the publisher ships no form audio")
    return tally


def main(argv):
    opts = {a.split("=")[0]: a for a in argv}
    args, i = [], 0
    content, episode, scene, root = ROOT, None, None, None
    while i < len(argv):
        a = argv[i]
        if a in ("--content", "--episode", "--scene", "--root"):
            val = argv[i + 1]; i += 2
            if a == "--content": content = Path(val).resolve()
            elif a == "--episode": episode = val
            elif a == "--root": root = val
            else: scene = val
            continue
        if a.startswith("--root="):
            root = a.split("=", 1)[1]; i += 1; continue
        if not a.startswith("--"): args.append(a)
        i += 1
    if not args:
        print(__doc__); return 2
    if root is not None and root not in ("out", "originals"):
        print(f"ERROR --root must be 'out' or 'originals', got {root!r}")
        return 2
    render = Path(args[0]).resolve()
    rep = Report()
    scene_list = scenes_of(content, episode, scene, root=root)
    if not scene_list:
        rep.err(str(content / (root or "out")), "no matching scenes")
    checked = 0
    for sid, sp, npth, merged in scene_list:
        if merged:
            if (render / sid).is_dir(): rep.warn(str(render / sid), "scene is merged (scenes.json merge): it is not published, do not render it")
            continue
        if not episode and not scene and not (render / sid).is_dir():
            continue           # whole-tree mode checks what exists; --episode/--scene require every scene
        if not sp.is_file() or not npth.is_file():
            rep.err(sid, f"script or notes missing in {sp.parent.parent.parent.name}/"); continue
        check_scene(render, sid, sp, npth, rep)
        checked += 1
    tally = check_clips_forms(render, [s for s in scene_list if (render / s[0]).is_dir()], rep)
    for x in rep.warnings[:200]: print("WARN ", x)
    if len(rep.warnings) > 200: print(f"... {len(rep.warnings) - 200} more warnings")
    for x in rep.errors: print("ERROR", x)
    print(f"scenes checked: {checked}; clips: {tally['clip']}; forms: {tally['form']}")
    bad = rep.errors or ("--strict" in opts and rep.warnings)
    print(f"{'FAIL' if bad else 'OK'}: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
