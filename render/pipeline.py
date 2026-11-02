#!/usr/bin/env python3
"""Overhear render orchestrator (system python is enough: no torch here).

  pipeline.py --changed                      render everything new or changed, in priority order (what the timer runs)
  pipeline.py --episode kukhnya-s01e01 ...   only those episodes (repeatable)       [--scene ID ...]  [--show S] [--season N]
  pipeline.py --status                       done / stale / pending / failed / skipped, hours, ETA at the measured rate
  pipeline.py --dry-run                      print the queue, run nothing
  pipeline.py --narrator-only --scene ID[,ID] | --episode E | --season N | --all   re-make only the narrator lines that contain Russian
                                             (method B, narrator.py) in already rendered scenes; dialogue and English-only lines are reused;
                                             add --dry-run to list the lines. A normal run applies the same pass to every scene it renders
                                             (--no-narrator skips it).
Options: --force (re-render even if up to date)  --limit N  --max-minutes M  --pull (git pull --ff-only the content
checkout; off by default because that checkout belongs to the content agent)  --retry-failed

Idempotent: a scene is up to date when store/<id>/meta.json has the render key computed from (content hash, voices and
their reference versions, TTS/assembly settings). The GPU lock (gpurun reservation) is held by a worker per slice of
scenes, not for the whole run, so other GPU jobs can interleave between slices.
"""
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config  # noqa: E402
import casting  # noqa: E402
import content  # noqa: E402
import clips  # noqa: E402
import forms  # noqa: E402
from plan import estimate_seconds, render_key  # noqa: E402
from store import Store  # noqa: E402
from voices import VoiceError, Voices  # noqa: E402
from plan import check_voices  # noqa: E402

HERE = Path(__file__).resolve().parent


def log(*a):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), *a, flush=True)


def select(args, scene):
    if args.scene and scene.id not in args.scene:
        return False
    if args.episode and scene.episode_id not in args.episode:
        return False
    if args.show and scene.show != args.show:
        return False
    if args.season and scene.season != args.season:
        return False
    return True


def plan_queue(args, settings, voices, store):
    """-> (todo, up_to_date, stale_ids, skips). `todo` is priority-ordered [(scene, key)]."""
    scenes, skips = content.discover(args.content, require_notes=not args.allow_no_notes)
    skips = [s for s in skips if "merged" not in s.reason]
    if args.status or args.clips_only or args.forms_only:     # read-only: never write casting files from --status or a backfill
        pass
    else:
        casting.ensure(scenes, getattr(content.discover, "casts", {}), voices, log=log)
    todo, done, stale = [], [], []
    for sc in scenes:
        if not select(args, sc):
            continue
        try:
            roles = check_voices(sc, voices)
        except VoiceError as e:
            skips.append(content.Skip(sc.id, str(sc.script_path), f"voice: {e}"))
            continue
        key = render_key(sc, voices, settings, roles)
        if store.is_done(sc.id, key) and not args.force:
            done.append(sc)
            continue
        if store.meta(sc.id):
            stale.append(sc.id)
        todo.append((sc, key))
    todo.sort(key=lambda t: content.priority_key(t[0], settings["priority"]))
    return todo, done, stale, skips, scenes


def rate_info(store, settings):
    """Measured wall-seconds per audio-second and audio seconds per generated character, from runs.jsonl / bench."""
    runs = store.runs()
    audio = sum(r.get("audioSec", 0) for r in runs)
    wall = sum(r.get("wallSec", 0) for r in runs)
    gen_s = sum(r.get("generatedSec", 0) for r in runs)
    gen_wall = sum(r.get("ttsSec", 0) for r in runs)
    if audio > 60 and wall > 0:
        return {"rtf": wall / audio, "ttsRtf": (gen_wall / gen_s) if gen_s else None, "source": f"{len(runs)} scenes rendered"}
    bench = HERE / "bench.json"
    if bench.exists():
        b = json.loads(bench.read_text())
        return {"rtf": b["rtf"], "ttsRtf": b["rtf"], "source": "bench.json"}
    return {"rtf": 4.0, "ttsRtf": 4.0, "source": "plan default (4x real time)"}


def unique_speech_seconds(scenes, voices, settings):
    """Speech seconds still to synthesise, deduplicated on (voice, sentence): chars / cps."""
    import textprep
    seen, chars = set(), 0
    for sc in scenes:
        try:
            roles = check_voices(sc, voices)
        except VoiceError:
            continue
        for g in sc.script["segments"]:
            for _, _, s in textprep.split_sentences(g["t"]):
                k = (roles[g["v"]], s)
                if k not in seen:
                    seen.add(k)
                    chars += len(s)
    return chars / 14.0, len(seen)


def record_narrator_state(store, err, res):
    """The narrator pass's outcome in state.json, so --status shows a failed pass instead of it living only in a log."""
    st = store.state()
    st["narrator"] = {"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "error": err, "lines": res.get("lines", 0), "scenes": res.get("scenes", 0),
                      "failed": res.get("failed", 0)}
    store.save_state(st)


def cmd_status(args, settings, voices, store):
    todo, done, stale, skips, scenes = plan_queue(args, settings, voices, store)
    st = store.state()
    failed = {k: v for k, v in st.get("failed", {}).items() if any(t[0].id == k for t in todo)}
    rate = rate_info(store, settings)
    done_hours = sum((store.meta(s.id) or {}).get("durationSec", 0) for s in done) / 3600
    pend_scenes = [t[0] for t in todo]
    speech_s, uniq = unique_speech_seconds(pend_scenes, voices, settings)
    gpu_h = speech_s * (rate["ttsRtf"] or rate["rtf"]) / 3600
    by_show = {}
    for s in scenes:
        by_show.setdefault(s.show, [0, 0])
        by_show[s.show][1] += 1
    for s in done:
        by_show[s.show][0] += 1
    print(f"content commit: {content.git_commit(args.content)}   store: {store.root}")
    print(f"scenes renderable: {len(scenes)}   done: {len(done)} ({done_hours:.2f} h of audio)   pending: {len(todo)} "
          f"(of which stale: {len(stale)})   failed (will retry/blocked): {len(failed)}   skipped: {len(skips)}")
    for show, (d, n) in sorted(by_show.items()):
        print(f"  {show:18s} {d:4d}/{n:4d} rendered")
    print(f"measured rate: {rate['rtf']:.2f}x real time wall per audio second ({rate['source']})")
    print(f"pending: {uniq} unique sentences, ~{speech_s / 3600:.1f} h of speech to synthesise -> ETA ~{gpu_h:.1f} GPU-hours "
          f"(~{gpu_h / 24:.1f} days continuous)")
    if skips:
        by = {}
        for s in skips:
            by.setdefault(s.reason.split(":")[0][:70], []).append(s.id)
        print("skipped, by reason:")
        for r, ids in sorted(by.items(), key=lambda kv: -len(kv[1])):
            print(f"  {len(ids):5d}  {r}   e.g. {ids[0]}")
    for k, v in sorted(failed.items())[:10]:
        print(f"  FAILED {k}: {v.get('error')} (attempts {v.get('attempts')})")
    nst = st.get("narrator")
    if nst:
        print(f"narrator pass: last at {nst['at']}: {nst.get('lines', 0)} line(s) in {nst.get('scenes', 0)} scene(s), {nst.get('failed', 0)} failed"
              + (f"   ERROR: {nst['error']}" if nst.get("error") else ""))
    if args.json:
        print(json.dumps({"done": len(done), "pending": len(todo), "skipped": [{"id": s.id, "reason": s.reason} for s in skips]}, ensure_ascii=False))


def stage_cmd(args, settings, stage, sid, mib, extra=(), venv=None):
    cmd = ([config.GPURUN, str(mib)] if mib else []) + [f"{venv or config.VENV_QWEN}/bin/python", "-I", str(HERE / "stage.py"), stage, "--scene", sid,
           "--content", str(args.content), "--store", str(args.store)]
    if args.settings:
        cmd += ["--settings", args.settings]
    return cmd + list(extra)


def run_stage(cmd, env=None):
    """Run one GPU step; return (tag, payload) from its single result line."""
    p = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, cwd="/tmp", env=env)
    for line in reversed(p.stdout.splitlines()):
        for tag in ("OK ", "RESULT ", "NEED_RETAKE ", "FAIL "):
            if line.startswith(tag):
                return tag.strip(), json.loads(line[len(tag):])
    return "FAIL", {"error": f"step exited {p.returncode} without a result"}


def cuda_libs():
    """LD_LIBRARY_PATH for faster-whisper in the ASR venv (the cublas/cudnn wheels; see render/setup/cudaenv.sh)."""
    libs = sorted(Path(config.VENV_ASR).glob("lib/python3*/site-packages/nvidia/*/lib"))
    keep = [str(p) for p in libs if p.parent.name in ("cublas", "cudnn")]
    return ":".join(keep + [os.environ["LD_LIBRARY_PATH"]] if os.environ.get("LD_LIBRARY_PATH") else keep)


def run_clip_group(args, settings, sids, log=log):
    """Example clips of a group of scenes: synthesis (Qwen), Whisper check, then up to `retakes` rounds for the failures.
    Low GPU priority, so the scene lanes are served first; a failed step is logged and the next run picks the work up again."""
    cfg = settings["clips"]
    env = {**os.environ, "GPURUN_PRIO": os.environ.get("OVERHEAR_CLIPS_PRIO", str(cfg["prio"]))}
    lock = open(Path(args.store) / "clips.lock", "w")      # one clip run at a time, whoever started it (a --clips-only backfill or a scene run)
    fcntl.flock(lock, fcntl.LOCK_EX)
    scenes = ",".join(sids)
    t0 = time.time()
    from ruaccent_fallback import RuAccent
    loaded = [x for x in (content.load_scene(content.scene_path(args.content, sid)) for sid in sids) if isinstance(x, content.Scene)]
    # accent the sentences first, on the CPU, so the GPU reservation below is not held while RuAccent starts
    clips.warm_ruaccent(loaded, settings, RuAccent(settings["stress"]["ruaccentPython"], Path(args.store) / "cache" / "ruaccent.json"))
    totals = {"passed": 0, "failed": 0}
    for attempt in range(cfg["retakes"] + 1):
        cmd = [config.GPURUN, str(cfg["gpu"]["ttsMiB"]), f"{config.VENV_QWEN}/bin/python", "-I", str(HERE / "stage.py"), "clips",
               "--scenes", scenes, "--attempt", str(attempt), "--content", str(args.content), "--store", str(args.store)]
        if args.settings:
            cmd += ["--settings", args.settings]
        tag, r = run_stage(cmd, env)
        if tag != "OK":
            log(f"clips FAILED ({len(sids)} scenes, attempt {attempt}): {r.get('error', '?')}")
            return totals
        if not r["ids"]:
            break
        cmd = [config.GPURUN, str(cfg["gpu"]["asrMiB"]), f"{config.VENV_ASR}/bin/python", "-I", str(HERE / "clip_asr.py"), "--store", str(args.store),
               "--cer-max", str(cfg["cerMax"]), "--retakes", str(cfg["retakes"]), *r["ids"]]
        tag, c = run_stage(cmd, {**env, "LD_LIBRARY_PATH": cuda_libs()})
        if tag != "OK":
            log(f"clip check FAILED (attempt {attempt}): {c.get('error', '?')}")
            return totals
        totals["passed"] += c["passed"]
        totals["failed"] += len(c["failed"])
        if not c["retry"]:
            break
    log(f"clips: {len(sids)} scenes, {totals['passed']} passed, {totals['failed']} dropped, {time.time() - t0:.0f}s")
    return totals


def rendered_scenes(args, store, scenes):
    return [sc for sc in scenes if select(args, sc) and (store.meta(sc.id) or {}).get("contentHash") == sc.content_hash]


def run_forms(args, settings, voices, store, scenes, limit=0, log=log):
    """Audio for the forms of the lexicon tables of the rendered `scenes` that have none yet, `forms.chunk` forms per round
    (Qwen, Whisper check, up to `retakes` rounds for the failures), so progress is kept chunk by chunk. `limit`: stop after that many forms;
    `--max-minutes`: no new chunk after that long. Low GPU priority, like the example clips.
    Returns {"passed", "failed", "pending", "ambiguous"}, or None when another forms run is active."""
    cfg = settings["forms"]
    if not any(sc.lang in cfg["voices"] for sc in scenes):
        log("forms: no selected scenes have a configured form voice; keeping the existing plan")
        return {"passed": 0, "failed": 0, "pending": 0, "ambiguous": 0, "resolved_by_dictionary": 0}
    lock = open(Path(args.store) / "forms.lock", "w")      # one forms run at a time, whoever started it
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        log("forms skipped: forms run active")
        return None
    env = {**os.environ, "GPURUN_PRIO": os.environ.get("OVERHEAR_FORMS_PRIO", str(cfg["prio"]))}
    from ruaccent_fallback import RuAccent
    ruacc = RuAccent(settings["stress"]["ruaccentPython"], Path(args.store) / "cache" / "ruaccent.json") if settings["stress"]["ruaccentFallback"] else None
    t0 = time.time()
    items, stats = forms.plan(scenes, settings, voices, ruacc)       # accented on the CPU first, before any GPU reservation is taken
    forms.write_plan(items, args.store, replace_ids=forms.slot_ids(scenes, settings))
    review = Path(args.store) / "forms" / "review.jsonl"       # the slots left silent, with the stress candidates, for a person to settle
    forms.write_review(stats["review"], args.store, scenes, settings)
    todo = forms.pending(items, args.store)
    if limit:
        todo = todo[:limit]
    log(f"forms: {stats['slots']} slots in {len(scenes)} scenes; dictionary {'on' if stats['dictionary'] else 'OFF'}: it settled "
        f"{stats['resolved_by_dictionary']} of {stats['ambiguous_without_dictionary']} slots whose stress was uncertain, {stats['ambiguous']} left without audio "
        f"(see {review}); {len(items)} to have audio, {len(todo)} to make")
    totals = {"passed": 0, "failed": 0, "pending": len(todo), "ambiguous": stats["ambiguous"], "resolved_by_dictionary": stats["resolved_by_dictionary"]}
    step = int(cfg["chunk"])
    chunks = [(i // step, [it.id for it in todo[i:i + step]]) for i in range(0, len(todo), step)]
    n_form_workers = max(1, int(os.environ.get("OVERHEAR_FORM_WORKERS", "2")))
    import concurrent.futures
    import threading
    flock_ = threading.Lock()
    abort_forms = threading.Event()

    def do_form_chunk(ci_chunk):
        ci, chunk = ci_chunk
        if abort_forms.is_set() or (args.max_minutes and time.time() - t0 > args.max_minutes * 60):
            return
        ids_file = Path(args.store) / "forms" / (".chunk.json" if n_form_workers == 1 else f".chunk-{ci}.json")
        ids_file.write_text(json.dumps(chunk), "utf-8")
        try:
            for attempt in range(cfg["retakes"] + int(cfg.get("extraRetakes", 0)) + 1):
                cmd = [config.GPURUN, str(cfg["gpu"]["ttsMiB"]), f"{config.VENV_QWEN}/bin/python", "-I", str(HERE / "stage.py"), "forms",
                       "--ids-file", str(ids_file), "--attempt", str(attempt), "--store", str(args.store)]
                if args.settings:
                    cmd += ["--settings", args.settings]
                tag, r = run_stage(cmd, env)
                if tag != "OK":
                    log(f"forms FAILED (chunk {ci}, attempt {attempt}): {r.get('error', '?')}")
                    abort_forms.set()
                    return
                if not r["ids"]:
                    break
                cmd = [config.GPURUN, str(cfg["gpu"]["asrMiB"]), f"{config.VENV_ASR}/bin/python", "-I", str(HERE / "clip_asr.py"), "--store", str(args.store),
                       "--cer-max", str(cfg["cerMax"]), "--retakes", str(cfg["retakes"]), "--kind", forms.KIND, "--pad-sec", str(cfg["asrPadSec"]),
                       "--fold-vowels", "--extra-retakes", str(cfg.get("extraRetakes", 0)), *r["ids"]]
                tag, c = run_stage(cmd, {**env, "LD_LIBRARY_PATH": cuda_libs()})
                if tag != "OK":
                    log(f"forms check FAILED (chunk {ci}, attempt {attempt}): {c.get('error', '?')}")
                    abort_forms.set()
                    return
                with flock_:
                    totals["passed"] += c["passed"]
                    totals["failed"] += len(c["failed"])
                for fid in c["failed"]:          # the dropped forms, for a later look at whether Whisper is biased toward the dictionary form
                    rec = clips.ClipStore(args.store, forms.KIND).record(fid) or {}
                    log(f"forms dropped {fid}: {rec.get('text')!r} heard {rec.get('hyp')!r} cer {rec.get('cer')}")
                if not c["retry"]:
                    break
            with flock_:
                totals["pending"] = max(0, totals["pending"] - len(chunk))
                log(f"forms: {totals['passed']} passed, {totals['failed']} dropped, {totals['pending']} left, {time.time() - t0:.0f}s")
        finally:
            if n_form_workers > 1:
                ids_file.unlink(missing_ok=True)

    if chunks:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(n_form_workers, len(chunks))) as ex:
            list(ex.map(do_form_chunk, chunks))
    return totals


def clip_backlog(args, settings, voices, store, scenes):
    """Scene ids (of the already rendered `scenes`) that still have example clips to make."""
    from ruaccent_fallback import RuAccent
    ruacc = RuAccent(settings["stress"]["ruaccentPython"], store.root / "cache" / "ruaccent.json") if settings["stress"]["ruaccentFallback"] else None
    cs = clips.ClipStore(store.root)
    out = []
    clips.warm_ruaccent(scenes, settings, ruacc)
    for sc in scenes:
        try:
            if any(not cs.is_done(it) for it in clips.plan_scene(sc, settings, voices, ruacc)):
                out.append(sc.id)
        except VoiceError:
            pass
    return out


def run_pipeline(args, settings, voices, store, todo, backlog=()):
    """Two lanes so the steps overlap on the GPU: lane A = Qwen (synth, retake), lane B = alignment/finish.
    Each step is its own process under its own gpurun reservation; a scene = one synth + one finish
    (+ one retake + one more finish when the stress check flags lines)."""
    import queue
    import threading
    st = store.state()
    st.setdefault("failed", {})
    st["contentCommit"] = content.git_commit(args.content)
    queue_ = []
    for sc, key in todo:
        f = st["failed"].get(sc.id)
        if f and f.get("renderKey") == key and f.get("attempts", 0) >= 3 and not args.retry_failed:
            continue
        queue_.append((sc, key))
    if args.limit:
        queue_ = queue_[:args.limit]
    log(f"{len(queue_)} scene(s) to render")
    import concurrent.futures
    n_synth = max(1, int(os.environ.get("OVERHEAR_SYNTH_WORKERS", "4")))
    n_align = max(1, int(os.environ.get("OVERHEAR_ALIGN_WORKERS", "4")))
    clips_wait = float(os.environ.get("OVERHEAR_CLIPS_WAIT_SEC", "12"))
    gpu = settings["gpu"]
    keys = {sc.id: key for sc, key in queue_}
    qa = queue.PriorityQueue()          # (phase, order, sid, payload): phase 0 = retakes go first
    qb = queue.Queue(maxsize=max(3, n_synth * 3))  # backpressure scaled to concurrent synth workers
    lock = threading.Lock()
    synth_alive = {"n": n_synth}
    t_run = time.time()
    times = {}
    done = {"n": 0, "fail": 0}
    stop = threading.Event()
    cond = threading.Condition()
    out = {"n": 0}
    qc = queue.Queue()                  # scenes whose example clips are to be made (lane C, low GPU priority)
    clips_on = not args.no_clips and bool(settings.get("clips"))
    clip_totals = {"passed": 0, "failed": 0}

    def settle():
        with cond:
            out["n"] -= 1
            cond.notify_all()

    def fail(sid, err):
        with lock:
            f = st["failed"].get(sid, {})
            n = f.get("attempts", 0) + 1 if f.get("renderKey") == keys.get(sid) else 1
            st["failed"][sid] = {"renderKey": keys.get(sid), "error": err, "attempts": n, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
            store.save_state(st)
            done["fail"] += 1
        log(f"FAILED {sid}: {err}")
        settle()

    def lane_a():
        while True:
            phase, order, sid, payload = qa.get()
            if sid is None:
                with lock:
                    synth_alive["n"] -= 1
                    last = synth_alive["n"] == 0
                if last:
                    for _ in range(n_align):
                        qb.put(None)
                return
            if stop.is_set() and phase == 1:
                settle()
                continue
            t = time.time()
            ru, en = bool(config.ru_engine(settings)), bool(config.en_engine(settings))
            if phase == 1:
                tag, r = "OK", {"audio_s": 0.0, "n": 0, "cached": 0}
                # ESpeech (ru) and F5 (en) run in the F5 venv, Qwen (the rest) in its own; each is a no-op when all cached
                steps = ([("synth-ru", gpu["ruMiB"], config.VENV_F5)] if ru else []) + \
                        ([("synth-en", gpu["enMiB"], config.VENV_F5)] if en else []) + \
                        ([("synth-ar", gpu.get("arMiB", gpu["ttsMiB"]), config.VENV_AR)] if config.ar_engine(settings) else []) + \
                        [("synth", gpu["ttsMiB"], None)]
                tag, miss = run_stage(stage_cmd(args, settings, "missing", sid, 0))      # no GPU reservation for a step with nothing to do
                if tag != "OK":
                    miss = {"ru": 1, "en": 1, "other": 1}
                active = [(stage, mib, venv) for stage, mib, venv in steps
                          if miss.get({"synth-ru": "ru", "synth-en": "en", "synth-ar": "ar", "synth": "other"}[stage], 1)]
                if len(active) > 1:
                    with concurrent.futures.ThreadPoolExecutor(max_workers=len(active)) as pool:
                        results = list(pool.map(lambda s: run_stage(stage_cmd(args, settings, s[0], sid, s[1], venv=s[2])), active))
                else:
                    results = [run_stage(stage_cmd(args, settings, s[0], sid, s[1], venv=s[2])) for s in active]
                tag = "OK"
                for tag1, r1 in results:
                    if tag1 != "OK":
                        tag, r = tag1, r1
                        break
                    r = {"audio_s": r["audio_s"] + r1.get("audio_s", 0.0), "n": r["n"] + r1.get("n", 0), "cached": r["cached"] + r1.get("cached", 0)}
                key = "synth"
            else:
                f5 = ru or en
                tag, r = run_stage(stage_cmd(args, settings, "retake", sid, max(gpu["ruMiB"], gpu["enMiB"]) if f5 else gpu["ttsMiB"],
                                             ["--keys", ",".join(payload)], venv=config.VENV_F5 if f5 else None))
                key = "retake"
            if tag != "OK":
                fail(sid, r.get("error", "?"))
                continue
            with lock:
                tm = times.setdefault(sid, {})
                tm[key] = tm.get(key, 0) + (time.time() - t)
                if key == "synth":
                    tm.update(generatedSec=r.get("audio_s", 0.0), generated=r.get("n", 0), cached=r.get("cached", 0))
            qb.put((sid, phase != 1))

    def lane_b():
        while True:
            item = qb.get()
            if item is None:
                return
            sid, final = item
            with lock:
                t_json = json.dumps(times.get(sid, {}))
            tag, r = run_stage(stage_cmd(args, settings, "finish", sid, gpu["alignMiB"],
                                         ["--times", t_json] + (["--no-retake"] if final else [])))
            if tag == "NEED_RETAKE":
                qa.put((0, order_of[sid], sid, r["keys"]))
            elif tag == "RESULT":
                if clips_on:
                    qc.put(sid)
                with lock:
                    st["failed"].pop(sid, None)
                    store.log_run({"at": time.strftime("%Y-%m-%dT%H:%M:%S"), **{k: r[k] for k in ("sceneId", "audioSec", "wallSec", "ttsSec", "generatedSec", "generated", "cached", "flagged", "stillFlagged", "russian", "timingNotOk")}})
                    st["lastRun"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                    store.save_state(st)
                    done["n"] += 1
                settle()
                log(f"{sid}: {r['audioSec']:.0f}s audio, wall {r['wallSec']:.0f}s, flagged {r['flagged']}/{r['russian']} -> {r['stillFlagged']} after retakes")
            else:
                fail(sid, r.get("error", "?"))

    def lane_c():
        per = int(settings["clips"]["scenesPerRun"])
        while True:
            first = qc.get()
            if first is None:
                return
            group, end = [first], False
            deadline = time.time() + clips_wait      # let a few scenes gather: one model load serves the whole group
            while len(group) < per and time.time() < deadline and not end:
                try:
                    nxt = qc.get(timeout=1)
                except queue.Empty:
                    if lanes_done.is_set():
                        break
                    continue
                if nxt is None:
                    end = True
                else:
                    group.append(nxt)
            t = run_clip_group(args, settings, group)
            clip_totals["passed"] += t["passed"]
            clip_totals["failed"] += t["failed"]
            if end:
                return

    lanes_done = threading.Event()
    order_of = {sc.id: i for i, (sc, _) in enumerate(queue_)}
    tas = [threading.Thread(target=lane_a) for _ in range(n_synth)]
    tbs = [threading.Thread(target=lane_b) for _ in range(n_align)]
    tc = threading.Thread(target=lane_c)
    for t in tas:
        t.start()
    for t in tbs:
        t.start()
    if clips_on:
        for sid in backlog:
            qc.put(sid)
        tc.start()
    # feed scenes in priority order; retakes (phase 0) jump the queue
    max_q = max(4, n_synth * 3)
    for i, (sc, _) in enumerate(queue_):
        if args.max_minutes and time.time() - t_run > args.max_minutes * 60:
            log("run time budget reached; finishing what is in flight")
            stop.set()
            break
        while qa.qsize() > max_q and not stop.is_set():
            time.sleep(0.5)         # keep the feed short so priority/time budgets stay meaningful
        with cond:
            out["n"] += 1
        qa.put((1, i, sc.id, None))
    with cond:
        while out["n"] > 0:
            cond.wait(timeout=2)
    for _ in range(n_synth):
        qa.put((9, 10 ** 9, None, None))
    for t in tas:
        t.join()
    for t in tbs:
        t.join()
    lanes_done.set()
    if clips_on:
        qc.put(None)
        tc.join()
    if not args.no_narrator and settings.get("narratorRu") and not args.dry_run:
        import narrator
        ok = [sid for sid in keys if sid not in st["failed"] or st["failed"][sid].get("renderKey") != keys[sid]]
        args.plan, args.work, args.out, args.all = False, "", "", False
        err, res = None, {}
        try:      # runs inside this process's pipeline.lock, so it must not take it again
            _, res = narrator.run(args, settings, sorted(ok))
        except Exception as e:      # the scenes stay valid with the old narrator audio; --narrator-only redoes them later
            err = f"{type(e).__name__}: {e}"
            log(f"narrator pass failed: {err}")
        record_narrator_state(store, err, res)
    log(f"run finished: {done['n']} rendered, {done['fail']} failed, clips {clip_totals['passed']} made / {clip_totals['failed']} dropped, "
        f"{time.time() - t_run:.0f}s")
    return 1 if done["fail"] and not done["n"] else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--changed", action="store_true")
    ap.add_argument("--scene", action="append", default=[])
    ap.add_argument("--episode", action="append", default=[])
    ap.add_argument("--show")
    ap.add_argument("--season", type=int)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-minutes", type=float, default=0)
    ap.add_argument("--pull", action="store_true")
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("--no-clips", action="store_true", help="skip the example clips of the lexicon (default: made after each scene)")
    ap.add_argument("--narrator-only", action="store_true", help="only re-make the narrator lines with Russian in rendered scenes (see narrator.py)")
    ap.add_argument("--no-narrator", action="store_true", help="skip the narrator pass (Russian words in narrator lines) after rendering")
    ap.add_argument("--all", action="store_true", help="with --narrator-only: every rendered scene")
    ap.add_argument("--clips-only", action="store_true", help="only make the missing example clips of already rendered scenes")
    ap.add_argument("--no-forms", action="store_true", help="skip the audio of the lexicon's table forms (default: made after the scenes)")
    ap.add_argument("--forms-only", action="store_true", help="only make the missing table-form audio of already rendered scenes")
    ap.add_argument("--forms-limit", type=int, default=0, help="stop after this many forms (a checkpoint)")
    ap.add_argument("--allow-no-notes", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--content", default=str(config.CONTENT_DIR))
    ap.add_argument("--store", default=str(config.STORE))
    ap.add_argument("--settings", default=None)
    args = ap.parse_args()
    # Use the same selection syntax for renders and backfills as narrator-only.
    args.scene = [x for value in args.scene for x in value.split(",") if x]
    args.episode = [x for value in args.episode for x in value.split(",") if x]
    if args.settings:
        args.settings = str(Path(args.settings).resolve())

    settings = config.load_settings(args.settings)
    voices = Voices()
    store = Store(args.store)
    if args.pull:
        r = subprocess.run(["git", "-C", args.content, "pull", "--ff-only"], capture_output=True, text=True)
        log("git pull:", (r.stdout + r.stderr).strip().splitlines()[-1:] or "")
    if args.status:
        return cmd_status(args, settings, voices, store)
    if args.narrator_only:
        import narrator
        args.plan = args.dry_run
        args.work = args.out = ""
        args.season = args.season or 0
        args.show = args.show or ""
        ids = narrator.all_scene_ids(args.store, args)
        if not (args.scene or args.episode or args.season or args.show or args.all):
            log("--narrator-only needs --scene/--episode/--season/--show/--all")
            return 2
        if args.plan:        # --dry-run: read-only, needs no lock
            plan, res = narrator.run(args, settings, ids)
        else:                # the same lock a rendering run holds: no scene is re-rendered between the narrator's read and its commit
            try:
                with narrator.pipeline_lock(store.root):
                    err = None
                    try:
                        plan, res = narrator.run(args, settings, ids)
                    except narrator.Busy:
                        raise
                    except Exception as e:
                        err = f"{type(e).__name__}: {e}"
                        log(f"narrator-only failed: {err}")
                        record_narrator_state(store, err, {})
                        return 1
                    record_narrator_state(store, None, res)
            except narrator.Busy as e:
                log(str(e))
                return 75
        log(f"narrator-only: {sum(len(x['jobs']) for x in plan['scenes'])} line(s) in {len(plan['scenes'])} scene(s); {res}")
        return 1 if res.get("failed") else 0

    lock = open(store.root / ("clips.run.lock" if args.clips_only else "forms.run.lock" if args.forms_only else "pipeline.lock"), "w")   # these never render scenes
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        log("another pipeline run is active; exiting")
        return 0
    todo, done, stale, skips, scenes = plan_queue(args, settings, voices, store)
    st = store.state()
    st["skipped"] = {s.id: s.reason for s in skips}
    store.save_state(st)
    log(f"{len(scenes)} renderable, {len(done)} up to date, {len(todo)} to render, {len(skips)} skipped")
    if args.dry_run:
        for sc, key in todo[:args.limit or 50]:
            print(f"  {sc.id}  {estimate_seconds(sc):.0f}s est  key {key[:10]}")
        return 0
    # example clips and form audio go with every scene that has a current render (same test as the publisher's: the render's contentHash), whatever voices cast it
    rendered = rendered_scenes(args, store, scenes)
    if args.forms_only:
        run_forms(args, settings, voices, store, rendered, args.forms_limit)
        return 0
    backlog = [] if args.no_clips else clip_backlog(args, settings, voices, store, rendered)
    if args.clips_only:
        todo = []
    log(f"{len(backlog)} rendered scene(s) with example clips to make")
    rc = 0
    if todo or backlog:
        rc = run_pipeline(args, settings, voices, store, todo, backlog)
    else:
        log("nothing to do")
    if not args.no_forms and not args.clips_only and not args.max_minutes and rc == 0:
        # the scenes rendered by this run count too: read what is rendered now
        run_forms(args, settings, voices, store, rendered_scenes(args, store, scenes), args.forms_limit)
    return rc


if __name__ == "__main__":
    sys.exit(main() or 0)
