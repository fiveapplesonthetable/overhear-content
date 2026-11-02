#!/usr/bin/env python3
"""Narrator method B: English narrator lines that contain Russian words are spliced from English (F5, sky) and native Russian
(Qwen3-TTS 1.7B + stress LoRA, ru-f1) parts. System python is enough here (planning + orchestration; no torch).

  narrator.py --scene ID[,ID] | --episode ID | --season N | --all  [--plan] [--retry-failed] [--store DIR]

Works on a rendered scene in the store: the dialogue and the English-only narrator lines are reused (decoded from the scene's
ORIGINAL render, kept in <store>/.narrator-before/<id>/ and keyed to its renderKey, and encoded once), only narrator sentences with
Russian are re-made; later spans and word timings shift by the length change. Every run re-applies all of a scene's lines to the
original, so a bumped version or a changed word never stacks generations of mp3 loss. Per-run Whisper check (Russian runs as Russian,
English as English); a sentence whose runs fail every take keeps its old audio, the failure is logged to
<store>/narrator-failures.jsonl and remembered per render key and version (retry with --retry-failed).
Locks: pipeline.lock for the whole run (unless the caller, the pipeline's own post-pass, holds it), a flock on the work dir, and the
publisher's publish.lock around each scene's commit. See narrator_work.py for the GPU steps.
"""
import argparse
import contextlib
import fcntl
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import narrator_ru as N  # noqa: E402
from store import sha256_file  # noqa: E402

HERE = Path(__file__).resolve().parent
TOKEN_RE = re.compile(r"[\w]", re.UNICODE)
_ID = re.compile(r"^([a-z-]+)-s(\d\d)e(\d\d)-scene-(\d\d)$")


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


def seg_tokens(text):
    return [t for t in text.split() if TOKEN_RE.search(t)]


def token_char_spans(text, toks):
    out, cur = [], 0
    for t in toks:
        at = text.find(t, cur)
        out.append((at, at + len(t)) if at >= 0 else None)
        if at >= 0:
            cur = at + len(t)
    return out


def _read(p):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except Exception:
        return None


def original_dir(store, sid):
    """-> (dir, live_meta, note). The scene's pristine (never narrated) render: the .narrator-before copy when it is keyed to the live
    renderKey and its audio matches its audioSha256, else the live scene when that is itself unnarrated. dir is None when the live scene
    carries narrator lines and no valid original exists (never guess: the caller skips the scene)."""
    store = Path(store)
    live, before = store / sid, store / ".narrator-before" / sid
    lm, bm = _read(live / "meta.json"), _read(before / "meta.json")
    if lm and not lm.get("narratorRu") and sha256_file(live / "audio.mp3") == lm.get("audioSha256"):
        return live, lm, "live"       # a pristine live copy is the original, whatever the before-copy holds
    if lm and bm and bm.get("renderKey") == lm.get("renderKey") and not bm.get("narratorRu") and (before / "audio.mp3").exists():
        if sha256_file(before / "audio.mp3") == bm.get("audioSha256"):
            return before, lm, "before"
    if lm and not lm.get("narratorRu"):
        return live, lm, "live"
    return None, lm, "no pristine original (live scene is narrated and .narrator-before is missing or stale)"


class Vocabs:
    """Scene / episode / show scopes of Russian words (content notes + rendered dialogue), cached across scenes."""

    def __init__(self, content_dir, store):
        self.cd, self.store = Path(content_dir), Path(store)
        self._ep, self._show, self._en = {}, {}, {}

    def _notes_scope(self, paths, extra_texts=()):
        sc = N.Scope()
        for p in paths:
            N.vocab_from_notes(sc, _read(p), ())
        for t in extra_texts:
            N.RuVocab.add(sc, t)
        return sc

    def en_show(self, show):
        """English words of the whole show's line translations (notes `trans`): a quoted run of only these is an English gloss, however much it
        looks like a transliteration ("cheeky", "oh, come on"). Glosses and the narrator's prose are NOT used here: they quote Russian words
        in Latin script ("shef", "ty", "vy") and would veto them."""
        if show not in self._en:
            ws = set()
            for p in sorted((self.cd / "out" / show).glob("s*e*/scene-*.notes.json")):
                for l in (_read(p) or {}).get("lines", []):
                    if isinstance(l, dict):
                        ws.update(w.lower() for w in re.findall(r"[A-Za-z]+", l.get("trans", "") or ""))
            self._en[show] = ws
        return self._en[show]

    def episode(self, show, season, ep):
        k = (show, season, ep)
        if k not in self._ep:
            d = self.cd / "out" / show / f"s{season:02d}e{ep:02d}"
            paths = sorted(d.glob("scene-*.notes.json"))
            texts = []
            for sp in sorted(self.store.glob(f"{show}-s{season:02d}e{ep:02d}-scene-*/spans.json")):
                for g in (_read(sp) or {}).get("segs", []):
                    if g.get("lang") == "ru" and g.get("v") != "narrator":
                        texts += [s["text"] for s in g["sentences"]]
            self._ep[k] = self._notes_scope(paths, texts)
        return self._ep[k]

    def show(self, show):
        if show not in self._show:
            sc = N.Scope()
            for p in sorted((self.cd / "out" / show).glob("s*e*/scene-*.notes.json")):
                N.vocab_from_notes(sc, _read(p), ())
            self._show[show] = sc
        return self._show[show]




def _en_norm(t):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).split())


def _ru_tokens(*texts):
    return {N.strip_marks(w).lower() for t in texts for w in N.CYR.findall(t or "")}


def dialogue_ctx(text, notes, spans, seg):
    """Russian words (lowercase, unstressed) of the dialogue quote a narrator sentence is about: the notes lines whose English
    translation is quoted in the sentence (their words and their rendered Russian); when none is quoted, the nearest earlier Russian
    dialogue segment. Used to choose between transliteration candidates and to keep the wrong homophone out."""
    nt = f" {_en_norm(text)} "
    by_seg = {g["seg"]: g for g in spans["segs"]}

    def seg_words(k):
        g = by_seg.get(k)
        return _ru_tokens(*[s["text"] for s in g["sentences"]]) if g and g["v"] != "narrator" else set()

    words, hit = set(), False
    for l in (notes or {}).get("lines", []):
        if not isinstance(l, dict):
            continue
        tr = _en_norm(l.get("trans"))
        if len(tr) >= 8 and f" {tr} " in nt:
            hit = True
            words |= _ru_tokens(*[w.get("t", "") for w in l.get("words") or []]) | seg_words(l.get("seg"))
    if not hit:
        prev = [g for g in spans["segs"] if g["seg"] < seg and g["v"] != "narrator" and g["lang"] == "ru"]
        if prev:
            words = seg_words(prev[-1]["seg"])
    return words


def sentence_is_english(text):
    """Per sentence, not per segment: a sentence whose letters are mostly Cyrillic is Russian, whatever segment it sits in."""
    cy = len(re.findall(r"[А-Яа-яЁё]", text))
    la = len(re.findall(r"[A-Za-z]", text))
    return la > 0 and cy < la


class ContentMismatch(Exception):
    """The content checkout is not what the scenes were rendered from."""


def content_hash_of(content_dir, sid):
    """sha256(script bytes + notes bytes), exactly content.load_scene's contentHash; None when the script is missing."""
    import hashlib
    from content import scene_path
    p = scene_path(content_dir, sid)
    n = p.with_name(p.stem + ".notes.json")
    try:
        return hashlib.sha256(p.read_bytes() + (n.read_bytes() if n.exists() else b"")).hexdigest()
    except OSError:
        return None


def plan_scene(sid, store, content_dir, vocabs):
    """-> dict(scene, jobs, skipped, unresolved, renderKey, ...) or None when the scene cannot be planned. Reads the ORIGINAL render
    (see original_dir). A job = one narrator sentence with Russian. A sentence with an ambiguous / partly known run is skipped (it keeps
    its sky audio) and listed in `skipped`; every unresolved run is listed in `unresolved` with its candidates."""
    m = _ID.match(sid)
    d, lm, note = original_dir(store, sid)
    if d is None or not m:
        return {"scene": sid, "error": note, "jobs": [], "skipped": [], "unresolved": []} if lm and m else None
    spans, timing, meta = _read(d / "spans.json"), _read(d / "timing.json"), _read(d / "meta.json")
    if not (spans and timing and meta and (d / "audio.mp3").exists()):
        return None
    show, season, ep, sc_n = m[1], int(m[2]), int(m[3]), int(m[4])
    if meta.get("contentHash") and content_hash_of(content_dir, sid) != meta["contentHash"]:
        return {"scene": sid, "error": "content checkout differs from what the scene was rendered from (contentHash)", "mismatch": True,
                "jobs": [], "skipped": [], "unresolved": []}
    notes = _read(Path(content_dir) / "out" / show / f"s{season:02d}e{ep:02d}" / f"scene-{sc_n:02d}.notes.json")
    scope = N.Scope()
    texts = []
    for g in spans["segs"]:
        if g["lang"] == "ru" and g["v"] != "narrator":
            texts += [s["text"] for s in g["sentences"]]
    N.vocab_from_notes(scope, notes, texts)
    voc = N.RuVocab()
    voc.scopes = [scope, vocabs.episode(show, season, ep), vocabs.show(show)]
    narr_texts = [s["text"] for g in spans["segs"] if g["v"] == "narrator" for s in g["sentences"]]
    en_words = N.english_vocab(notes, narr_texts) | vocabs.en_show(show)
    jobs, unresolved, skipped = [], [], []
    for g in spans["segs"]:
        if g["v"] != "narrator" or g["lang"] != "en":
            continue
        for si, s in enumerate(g["sentences"]):
            if not sentence_is_english(s["text"]):
                continue
            ctx = dialogue_ctx(s["text"], notes, spans, g["seg"])
            runs, unres = N.find_runs(s["text"], voc, en_words, ctx, texts)
            blocking = [u for u in unres if u["kind"] in ("ambiguous", "partial")]
            for u in unres:
                unresolved.append({"scene": sid, "seg": g["seg"], "i": s["i"], "text": s["text"], "latin": u["inner"], "kind": u["kind"],
                                   "candidates": [{"lat": w["lat"], "cyr": w["cands"]} for w in u["words"]], "lineKeptSky": bool(blocking)})
            if blocking:
                skipped.append({"scene": sid, "seg": g["seg"], "i": s["i"], "text": s["text"], "why": [u["inner"] for u in blocking]})
                continue
            if not runs:
                continue
            parts = N.split_parts(s["text"], runs)
            jobs.append({"scene": sid, "seg": g["seg"], "si": si, "i": s["i"], "start": s["start"], "end": s["end"],
                         "text": s["text"], "parts": parts})
    return {"scene": sid, "jobs": jobs, "skipped": skipped, "unresolved": unresolved, "contentHash": meta.get("contentHash"),
            "renderKey": meta.get("renderKey"), "audioSha256": meta.get("audioSha256")}


def all_scene_ids(store, args):
    ids = sorted(p.name for p in Path(store).glob("*-s??e??-scene-??") if (p / "meta.json").exists())
    out = []
    for sid in ids:
        m = _ID.match(sid)
        if not m:
            continue
        if args.scene and sid not in args.scene:
            continue
        if args.episode and f"{m[1]}-s{m[2]}e{m[3]}" not in args.episode:
            continue
        if args.season and int(m[2]) != args.season:
            continue
        if args.show and m[1] != args.show:
            continue
        out.append(sid)
    return out


def parse_args(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", action="append", default=[])
    ap.add_argument("--episode", action="append", default=[])
    ap.add_argument("--season", type=int, default=0)
    ap.add_argument("--show", default="")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--plan", action="store_true", help="only list the lines that would be re-made")
    ap.add_argument("--retry-failed", action="store_true", help="also try the lines that already failed for this render key and version")
    ap.add_argument("--store", default=str(config.STORE))
    ap.add_argument("--content", default=str(config.CONTENT_DIR))
    ap.add_argument("--work", default="")
    ap.add_argument("--settings", default=None)
    ap.add_argument("--out", default="", help="write the new scenes here instead of replacing them in the store (dry run: no commit, no failure memory)")
    a = ap.parse_args(argv)
    a.scene = [x for s in a.scene for x in s.split(",") if x]
    a.episode = [x for s in a.episode for x in s.split(",") if x]
    return a


# ---- orchestration ---------------------------------------------------------------------------------------------------
def part_id(kind, voice, text, s, syllable=False):
    nr = s["narratorRu"]
    sig = {"kind": kind, "voice": voice, "text": text, "v": nr["version"],
           "eng": (s["ttsEn"]["nfe"], s["ttsEn"]["cfg"]) if kind == "en" else (s["lora"]["tag"], nr["temperatures"])}
    if syllable:
        sig["syllable"] = True          # judged differently from a word of the same letters (narrator_work.passes)
    return config.sha(sig)[:16]


def job_sig(job):
    """What a spliced line is made of: its part ids (text, stress, voices, settings and the narrator version are all in them)."""
    return config.sha([p["id"] for p in job["parts"]])[:12]


def stressed_for(parts, ruaccent, stress_mode="all"):
    """Fill part["text"] (what Qwen reads) and part["plain"] for every part. stress_mode: all = content stress, then RuAccent for the
    words it has none for (one subprocess call for the whole batch, cached on disk; the dialogue sentence is its context when the run
    occurs in one); content = only what the content has; none = no marks."""
    if stress_mode == "all" and ruaccent is not None:
        need = set()
        for p in parts:
            if p["kind"] == "ru":
                r = p["run"]
                if r.get("kind") != "fragment" and any(not s and N.vowels(c) > 1 and "ё" not in c for c, s in zip(r["cyr"], r["stressed"])):
                    need.add(r.get("context") or " ".join(r["cyr"]))
                    need.add(" ".join(r["cyr"]))
        if need:
            ruaccent(sorted(need))        # warms the cache
    for p in parts:
        if p["kind"] == "ru":
            r = p["run"]
            p["plain"] = " ".join(r["cyr"])
            if stress_mode == "none" or r.get("kind") == "fragment":      # a bare ending / prefix has no stress of its own to look up
                p["text"] = p["plain"]
            else:
                p["text"] = N.stress_text(r["cyr"], r["stressed"], ruaccent if stress_mode == "all" else None, r.get("context"))


def f5_text(t):
    """What F5 reads for an English part: the line without quote marks. Given 'is "vile", and' F5 skips the quoted word in most
    takes and says "and"; unquoted it says it. The part's `plain` keeps the quotes, so the Whisper check still requires each
    quote to be heard."""
    return re.sub(r'["\u201c\u201d]', "", t)


def failed_key(sid, render_key, job):
    return f"{sid}|{render_key}|{job['seg']}|{job['i']}|{job['sig']}"


def load_failed(work):
    return _read(Path(work) / "failed.json") or {}


def build_plan(args, settings, scene_ids, store, work=None):
    """Plan every selected scene; a scene is in the result only when its lines are not already what the store has (same sig, same
    version) or it holds lines that no longer qualify. A pending scene lists ALL its lines: the build re-applies them to the original."""
    voc = Vocabs(args.content, store)
    nr = settings["narratorRu"]
    planned, unresolved, skipped, errors = [], [], [], []
    for sid in scene_ids:
        p = plan_scene(sid, store, args.content, voc)
        if not p:
            continue
        if p.get("error"):
            errors.append({"scene": sid, "why": p["error"], "mismatch": bool(p.get("mismatch"))})
            continue
        unresolved += p["unresolved"]
        skipped += p["skipped"]
        if p["jobs"] or (_read(Path(store) / sid / "meta.json") or {}).get("narratorRu"):
            planned.append(p)
    bad = [e["scene"] for e in errors if e["mismatch"]]
    if bad:
        raise ContentMismatch(f"{len(bad)} scene(s) were rendered from different content than {args.content} (contentHash differs; first {bad[:3]}). "
                              f"Point OVERHEAR_CONTENT / --content at the checkout the scenes were rendered from. Nothing was done.")
    stress_mode = nr.get("stress", "all")
    ruacc = None
    if stress_mode == "all":
        from ruaccent_fallback import RuAccent
        ruacc = RuAccent(settings["stress"]["ruaccentPython"], Path(store) / "cache" / "ruaccent.json")
    allparts = [pt for sc in planned for j in sc["jobs"] for pt in j["parts"]]
    stressed_for(allparts, ruacc, stress_mode)
    for pt in allparts:
        if pt["kind"] == "en":
            pt["plain"] = pt["text"]
            pt["text"] = f5_text(pt["text"])
        pt["syllable"] = pt["kind"] == "ru" and pt["run"]["kind"] == "fragment"
        pt["id"] = part_id(pt["kind"], nr["enVoice"] if pt["kind"] == "en" else nr["ruVoice"], pt["text"], settings, pt["syllable"])
    failed = load_failed(work) if work else {}
    scenes, known_failed, homographs = [], 0, []
    for sc in planned:
        sid = sc["scene"]
        for j in sc["jobs"]:
            j["sig"] = job_sig(j)
            for pt in j["parts"]:
                if pt["kind"] == "ru":
                    for w, h, st in zip(pt["run"]["cyr"], pt["run"]["homograph"], pt["run"]["stressed"]):
                        if h:
                            homographs.append({"scene": sid, "seg": j["seg"], "i": j["i"], "word": w, "stress": st or "RuAccent"})
        if not args.retry_failed:
            keep = []
            for j in sc["jobs"]:
                if failed_key(sid, sc["renderKey"], j) in failed:
                    known_failed += 1
                else:
                    keep.append(j)
            sc["jobs"] = keep
        live = (_read(Path(store) / sid / "meta.json") or {}).get("narratorRu") or {}
        done = {(l["seg"], l["i"], l.get("sig")) for l in live.get("lines", []) if l.get("version", live.get("version")) == nr["version"]}
        want = {(j["seg"], j["i"], j["sig"]) for j in sc["jobs"]}
        have = {(l["seg"], l["i"], l.get("sig")) for l in live.get("lines", [])}
        if want == done and want == have:
            continue          # the store already has exactly these lines at this version
        sc["revert"] = not sc["jobs"]
        scenes.append(sc)
    uniq = {}
    for sc in scenes:
        for j in sc["jobs"]:
            for pt in j["parts"]:
                uniq.setdefault(pt["id"], {"id": pt["id"], "kind": pt["kind"], "text": pt["text"], "plain": pt["plain"],
                                                "syllable": pt["syllable"]})
    return {"scenes": scenes, "parts": list(uniq.values()), "unresolved": unresolved, "skipped": skipped, "errors": errors,
            "homographs": homographs, "knownFailed": known_failed}


def run_step(cmd, env_extra=None, what=""):
    env = dict(os.environ, OMP_NUM_THREADS="4", MKL_NUM_THREADS="4", PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True")
    env.update(env_extra or {})
    cpuset = os.environ.get("OVERHEAR_CPUSET", "")  # optional CPU pinning, e.g. "36-39"
    full = ((["taskset", "-c", cpuset] if cpuset else []) + ["nice", "-n", "19"]) + cmd
    p = subprocess.run(full, stdout=subprocess.PIPE, text=True, cwd="/tmp", env=env)
    for line in reversed(p.stdout.splitlines()):
        for tag in ("OK ", "FAIL "):
            if line.startswith(tag):
                return tag.strip(), json.loads(line[len(tag):])
    return "FAIL", {"error": f"{what} exited {p.returncode} without a result"}


def cuda_libs():
    libs = sorted(Path(config.VENV_ASR).glob("lib/python3*/site-packages/nvidia/*/lib"))
    keep = [str(p) for p in libs if p.parent.name in ("cublas", "cudnn")]
    old = os.environ.get("LD_LIBRARY_PATH")
    return ":".join(keep + ([old] if old else []))


class Busy(RuntimeError):
    pass


@contextlib.contextmanager
def pipeline_lock(store_root):
    """pipeline.lock, the same lock a rendering run holds (non-blocking: raises Busy). Held for a whole narrator run so a scene cannot be
    re-rendered between the narrator's read and its commit."""
    f = open(Path(store_root) / "pipeline.lock", "w")
    try:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Busy("another pipeline run is active (pipeline.lock)")
        yield f
    finally:
        f.close()


@contextlib.contextmanager
def work_lock(work):
    """One narrator run per work dir (plan.json, todo files and checks.json are shared state)."""
    Path(work).mkdir(parents=True, exist_ok=True)
    f = open(Path(work) / "run.lock", "w")
    try:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Busy(f"another narrator run is using {work}")
        yield f
    finally:
        f.close()


def run(args, settings, scene_ids, log=log):
    """Plan, make the missing takes, check them, splice. The caller holds pipeline.lock (see main() / pipeline.py)."""
    store = Path(args.store)
    nr = settings["narratorRu"]
    work = Path(args.work) if args.work else store / "cache" / f"narrator-{nr['version']}"
    if args.plan:
        return _run_locked(args, settings, scene_ids, store, nr, work, log)
    with work_lock(work):
        return _run_locked(args, settings, scene_ids, store, nr, work, log)


def _run_locked(args, settings, scene_ids, store, nr, work, log):
    plan = build_plan(args, settings, scene_ids, store, work)
    lines = sum(len(sc["jobs"]) for sc in plan["scenes"])
    log(f"narrator: {lines} line(s) with Russian in {len(plan['scenes'])} scene(s), {len(plan['parts'])} unique parts; "
        f"{len(plan['skipped'])} line(s) kept sky (unresolved), {plan['knownFailed']} known-failed line(s) not retried"
        f"{' (--retry-failed to retry)' if plan['knownFailed'] else ''}, {len(plan['homographs'])} homograph stress guess(es)")
    for e in plan["errors"]:
        log("NOT PLANNED:", e["scene"], e["why"])
    if args.plan or not plan["scenes"]:
        return plan, {"lines": lines}
    (work / "takes").mkdir(parents=True, exist_ok=True)
    (work / "plan.json").write_text(json.dumps(plan, ensure_ascii=False), "utf-8")
    (work / "homographs.json").write_text(json.dumps(plan["homographs"], ensure_ascii=False, indent=1), "utf-8")
    worker = str(HERE / "narrator_work.py")
    common = ["--work", str(work)] + (["--settings", args.settings] if getattr(args, "settings", None) else [])
    for r in range(nr["rounds"]):
        checks = _read(work / "checks.json") or {}
        lacking = []
        for p in plan["parts"]:
            have = sorted(int(f.name.rsplit(".t", 1)[1][:-4]) for f in (work / "takes").glob(f"{p['id']}.t*.wav"))
            if any(checks.get(f"{p['id']}.t{k}", {}).get("pass") for k in have):
                continue
            nxt = (max(have) + 1) if have else 0
            # first round also covers takes that exist but were never checked
            lacking.append({**p, "takes": [k for k in have if f"{p['id']}.t{k}" not in checks] + list(range(nxt, nxt + nr["takesPerRound"]))})
        if not lacking:
            break
        # takes that exist already need no synthesis, only a check
        for kind, key in (("en", "todo_en.json"), ("ru", "todo_ru.json")):
            todo = []
            for p in lacking:
                if p["kind"] != kind:
                    continue
                new = [k for k in p["takes"] if not (work / "takes" / f"{p['id']}.t{k}.wav").exists()]
                if new:
                    todo.append({"id": p["id"], "text": p["text"], "plain": p["plain"], "takes": new})
            (work / key).write_text(json.dumps(todo, ensure_ascii=False), "utf-8")
        log(f"round {r + 1}/{nr['rounds']}: {len(lacking)} part(s) without a passing take")
        for kind, venv, mib in (("en", config.VENV_F5, nr["enMiB"]), ("ru", config.VENV_QWEN, nr["ruMiB"])):
            if json.loads((work / f"todo_{kind}.json").read_text()):
                tag, res = run_step([config.GPURUN, str(mib), f"{venv}/bin/python", "-I", worker, kind] + common, what=kind)
                log(kind, tag, res)
                if tag != "OK":
                    raise RuntimeError(f"narrator {kind} step failed: {res}")
        tag, res = run_step([config.GPURUN, str(nr["checkMiB"]), f"{config.VENV_ASR}/bin/python", "-I", worker, "check"] + common,
                            {"LD_LIBRARY_PATH": cuda_libs()}, "check")
        log("check", tag, res)
        if tag != "OK":
            raise RuntimeError(f"narrator check step failed: {res}")
    tag, res = run_step([f"{config.VENV_ASR}/bin/python", "-I", worker, "build", "--store", str(store)] + common +
                        (["--out", args.out] if args.out else []), what="build")
    log("build", tag, {k: v for k, v in res.items() if k != "failures"})
    for f in res.get("failures", []):
        log("FALLBACK (old audio kept):" if f.get("sticky", True) else "SKIPPED (will retry next run):", f["scene"], f.get("seg"), f.get("i"), f["why"])
    if tag != "OK":
        raise RuntimeError(f"narrator build failed: {res}")
    return plan, res


def main(argv=None):
    a = parse_args(argv)
    settings = config.load_settings(getattr(a, "settings", None))
    ids = all_scene_ids(a.store, a) if (a.scene or a.episode or a.season or a.show or a.all) else []
    if not ids:
        print("select scenes with --scene/--episode/--season/--show/--all", file=sys.stderr)
        return 2
    try:
        if a.plan:
            plan, res = run(a, settings, ids)
        else:
            with pipeline_lock(a.store):
                plan, res = run(a, settings, ids)
    except Busy as e:
        log(str(e))
        return 75
    print(json.dumps({"scenes": len(plan["scenes"]), "lines": sum(len(s["jobs"]) for s in plan["scenes"]),
                      "parts": len(plan["parts"]), **{k: v for k, v in res.items() if k != "failures"}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
