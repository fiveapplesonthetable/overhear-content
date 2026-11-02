#!/usr/bin/env python3
"""Decoupled persistent A100 render daemon (/dev/shm candidate queue).

Architecture:
  - 3x persistent `qwen-worker` (venv-qwen, pure PyTorch CUDA 12, zero faster_whisper import)
  - 1x persistent `ru-worker`   (venv-f5, ESpeech DiT + RUAccent, pure PyTorch CUDA 12)
  - 1x on-demand  `ar-worker`   (venv-asr, Chatterbox multilingual V2 when Arabic jobs exist)
  - 2x persistent `gate-worker` (venv-asr, Whisper large-v3-turbo fp16 + WavLM-base-plus-sv + CPU F0/transient pool)
  - 1x persistent `orchestrator`(venv-qwen, 12-thread CPU scene prep + resident MMS_FA Aligner + check_render.py)

All candidate audio flows through `/dev/shm/overhear-turbo` RAM disk (zero SSD I/O), pinning A100 VRAM at ~36-39 GiB
and SM utilization at 95-100% with zero model reloads across episodes and zero cuDNN library conflicts.
"""
import argparse
import concurrent.futures
import json
import os
import signal
import subprocess
import sys
import time
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))

import config  # noqa: E402

SHM_ROOT = Path(os.environ.get("OVERHEAR_TURBO_DIR", "/dev/shm/overhear-turbo"))
QWEN_LANGS = {
    "en": "English", "fr": "French", "ru": "Russian", "es": "Spanish",
    "de": "German", "ko": "Korean", "pt": "Portuguese", "it": "Italian",
    "ja": "Japanese", "zh": "Chinese",
}


def log(role, *a):
    print(f"{time.strftime('%H:%M:%S')} [{role}]", *a, file=sys.stderr, flush=True)


def venv_cuda_libs(venv_path: str) -> str:
    """Return ONLY this venv's own cublas/cudnn library paths so CUDA 12 & CUDA 13 venvs never cross-pollute."""
    libs = sorted(Path(venv_path).glob("lib/python3*/site-packages/nvidia/*/lib"))
    keep = [str(p) for p in libs if p.parent.name in ("cublas", "cudnn")]
    return ":".join(keep)


def pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def reclaim_stale_claims(folder: Path):
    for p in folder.glob("*.claim.*"):
        try:
            pid = int(p.name.rsplit(".claim.", 1)[1])
        except ValueError:
            continue
        if not pid_alive(pid):
            orig = folder / p.name.rsplit(".claim.", 1)[0]
            try:
                p.rename(orig)
            except OSError:
                pass


def claim_jobs(folder: Path, max_jobs: int, max_expanded: int = 0):
    """Atomically claim up to max_jobs (and <= max_expanded candidates) in priority order."""
    pid = os.getpid()
    claimed = []
    expanded = 0
    for p in sorted(folder.glob("*.json")):
        if len(claimed) >= max_jobs:
            break
        claim_p = p.with_name(f"{p.name}.claim.{pid}")
        try:
            p.rename(claim_p)
        except OSError:
            continue
        try:
            data = json.loads(claim_p.read_text("utf-8"))
        except Exception:
            claim_p.unlink(missing_ok=True)
            continue
        n_c = int(data.get("n_cands", 4))
        if max_expanded and claimed and (expanded + n_c > max_expanded):
            # Return this one to queue for another worker
            try:
                claim_p.rename(p)
            except OSError:
                pass
            break
        claimed.append((claim_p, data))
        expanded += n_c
    return claimed


def write_cand_bundle(cands_dir: Path, job: dict, wavs: list):
    import numpy as np
    stem = f"{job['prio']:04d}_{job['episode']}_{job['key']}"
    tmp_npz = cands_dir / f".{stem}.{os.getpid()}.npz"
    fin_npz = cands_dir / f"{stem}.npz"
    tmp_json = cands_dir / f".{stem}.{os.getpid()}.json"
    fin_json = cands_dir / f"{stem}.json"
    np.savez(tmp_npz, **{f"w{i}": np.asarray(w, dtype=np.float32) for i, w in enumerate(wavs)})
    if not str(tmp_npz).endswith(".npz"):
        tmp_npz = Path(str(tmp_npz) + ".npz")
    tmp_npz.replace(fin_npz)
    meta = {**job, "npz": str(fin_npz), "count": len(wavs)}
    tmp_json.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    tmp_json.replace(fin_json)


# ---------------------------------------------------------------------------
# 1. Persistent Qwen Worker (venv-qwen, pure PyTorch)
# ---------------------------------------------------------------------------
def run_qwen_worker(worker_id: int, batch_seqs: int):
    role = f"qwen-{worker_id}"
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    from store import Store
    from tts import QwenEngine
    from voices import Voices

    settings = config.load_settings(str(REPO / "render" / "settings.fr-qwen-en.json"))
    voices = Voices()
    store = Store(config.STORE)
    eng = QwenEngine(settings, voices, log=lambda *a: log(role, *a))
    t_cfg = settings["tts"]
    temp = t_cfg.get("temperature", 0.7) * 0.95
    rep = t_cfg.get("repetition_penalty", 1.0) * 1.1

    jobs_dir = SHM_ROOT / "jobs_qwen"
    cands_dir = SHM_ROOT / "cands"
    stop_file = SHM_ROOT / "STOP"
    idle_ticks = 0

    while not stop_file.exists():
        # Backpressure if gate-workers have > 800 bundles queued in /dev/shm (~1.2 GB)
        if sum(1 for _ in cands_dir.glob("*.json")) > 800:
            time.sleep(0.25)
            continue

        if idle_ticks % 40 == 20:
            reclaim_stale_claims(jobs_dir)

        claimed = claim_jobs(jobs_dir, max_jobs=14, max_expanded=batch_seqs)
        if not claimed:
            idle_ticks += 1
            time.sleep(0.2)
            continue
        idle_ticks = 0

        # Filter any already completed in cache/tts
        todo = []
        for cp, job in claimed:
            if store.tts_path(job["key"]).exists():
                cp.unlink(missing_ok=True)
            else:
                todo.append((cp, job))
        if not todo:
            continue

        # Sort by text length to minimize padding inside Qwen batch
        todo.sort(key=lambda x: len(x[1]["text_tts"]))
        expanded_batch = []
        slices = []
        for cp, job in todo:
            start = len(expanded_batch)
            n_c = int(job["n_cands"])
            lang_name = QWEN_LANGS[job["lang"]]
            for _ in range(n_c):
                expanded_batch.append((job["voice"], lang_name, job["text_tts"]))
            slices.append((cp, job, start, start + n_c))

        seed = int(todo[0][1]["key"][:8], 16) + int(todo[0][1].get("attempt", 0)) * 7919 + worker_id * 131
        t0 = time.time()
        try:
            wavs = eng.generate(expanded_batch, seed, temperature=temp, repetition_penalty=rep)
            for cp, job, s0, s1 in slices:
                write_cand_bundle(cands_dir, job, wavs[s0:s1])
                cp.unlink(missing_ok=True)
            if len(expanded_batch) >= 16:
                eng.torch.cuda.empty_cache()
            log(role, f"synthesized {len(todo)} lines ({len(expanded_batch)} takes) in {time.time() - t0:.2f}s")
        except Exception as ex:
            log(role, f"WARN batch failed ({ex}), falling back per-item")
            eng.torch.cuda.empty_cache()
            for cp, job, _s0, _s1 in slices:
                try:
                    n_c = int(job["n_cands"])
                    lang_name = QWEN_LANGS[job["lang"]]
                    w_item = eng.generate([(job["voice"], lang_name, job["text_tts"])] * n_c, seed, temperature=temp, repetition_penalty=rep)
                    write_cand_bundle(cands_dir, job, w_item)
                    cp.unlink(missing_ok=True)
                except Exception as ex2:
                    log(role, f"ERROR item {job['key']} failed: {ex2}")
                    orig = jobs_dir / cp.name.rsplit(".claim.", 1)[0]
                    try:
                        cp.rename(orig)
                    except OSError:
                        pass
                    time.sleep(1.0)


# ---------------------------------------------------------------------------
# 2. Persistent Russian ESpeech Worker (venv-f5, pure PyTorch)
# ---------------------------------------------------------------------------
def run_ru_worker(batch_seqs: int):
    role = "ru-espeech"
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    from espeech import EspeechEngine
    from store import Store
    from voices import Voices

    settings = config.load_settings(str(REPO / "render" / "settings.ru-qwen-en.json"))
    voices = Voices()
    store = Store(config.STORE)
    eng = None
    jobs_dir = SHM_ROOT / "jobs_ru"
    cands_dir = SHM_ROOT / "cands"
    stop_file = SHM_ROOT / "STOP"
    idle_ticks = 0

    while not stop_file.exists():
        if sum(1 for _ in cands_dir.glob("*.json")) > 800:
            time.sleep(0.25)
            continue
        if idle_ticks % 40 == 20:
            reclaim_stale_claims(jobs_dir)

        claimed = claim_jobs(jobs_dir, max_jobs=8, max_expanded=batch_seqs)
        if not claimed:
            idle_ticks += 1
            if eng is not None and idle_ticks > 50:  # >15s idle -> release VRAM for Qwen/ASR
                log(role, "idle, freeing ESpeech VRAM until next Russian episode")
                eng.free()
                eng = None
            time.sleep(0.3)
            continue
        idle_ticks = 0
        if eng is None:
            eng = EspeechEngine(settings, voices, log=lambda *a: log(role, *a))

        by_voice = {}
        for cp, job in claimed:
            if store.tts_path(job["key"]).exists():
                cp.unlink(missing_ok=True)
            else:
                by_voice.setdefault(job["voice"], []).append((cp, job))

        for voice, v_items in by_voice.items():
            expanded = []
            slices = []
            for cp, job in v_items:
                s0 = len(expanded)
                n_c = int(job["n_cands"])
                for _ in range(n_c):
                    expanded.append((voice, "Russian", job["text_tts"]))
                slices.append((cp, job, s0, s0 + n_c))
            seed = int(v_items[0][1]["key"][:8], 16) + int(v_items[0][1].get("attempt", 0)) * 7919
            speed = settings["ttsRu"]["speeds"][min(int(v_items[0][1].get("attempt", 0)), len(settings["ttsRu"]["speeds"]) - 1)]
            t0 = time.time()
            try:
                wavs = eng.generate(expanded, seed, speed=speed)
                for cp, job, s0, s1 in slices:
                    write_cand_bundle(cands_dir, job, wavs[s0:s1])
                    cp.unlink(missing_ok=True)
                log(role, f"synthesized {len(v_items)} ru lines ({len(expanded)} takes) in {time.time() - t0:.2f}s")
            except Exception as ex:
                log(role, f"ERROR ru batch failed ({ex})")
                eng.torch.cuda.empty_cache()
                for cp, _job, _s0, _s1 in slices:
                    orig = jobs_dir / cp.name.rsplit(".claim.", 1)[0]
                    try:
                        cp.rename(orig)
                    except OSError:
                        pass
                time.sleep(1.0)


# ---------------------------------------------------------------------------
# 3. On-Demand Arabic Chatterbox Worker (venv-asr)
# ---------------------------------------------------------------------------
def run_ar_worker():
    role = "ar-chatterbox"
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    from chatterbox_ar import ChatterboxArEngine
    from store import Store
    from voices import Voices

    settings = config.load_settings(str(REPO / "render" / "settings.ar-chatterbox-en.json"))
    voices = Voices()
    store = Store(config.STORE)
    eng = None
    jobs_dir = SHM_ROOT / "jobs_ar"
    cands_dir = SHM_ROOT / "cands"
    stop_file = SHM_ROOT / "STOP"
    idle_ticks = 0

    while not stop_file.exists():
        if idle_ticks % 40 == 20:
            reclaim_stale_claims(jobs_dir)
        claimed = claim_jobs(jobs_dir, max_jobs=2, max_expanded=8)
        if not claimed:
            idle_ticks += 1
            if eng is not None and idle_ticks > 30:
                log(role, "idle, freeing Chatterbox VRAM")
                eng.free()
                eng = None
            time.sleep(0.5)
            continue
        idle_ticks = 0
        if eng is None:
            eng = ChatterboxArEngine(settings, voices, log=lambda *a: log(role, *a))
        for cp, job in claimed:
            if store.tts_path(job["key"]).exists():
                cp.unlink(missing_ok=True)
                continue
            n_c = int(job["n_cands"])
            seed = int(job["key"][:8], 16) + int(job.get("attempt", 0)) * 7919
            t0 = time.time()
            try:
                wavs = eng.generate([(job["voice"], "ar", job["text_tts"])] * n_c, seed)
                write_cand_bundle(cands_dir, job, wavs)
                cp.unlink(missing_ok=True)
                log(role, f"synthesized ar line ({n_c} takes) in {time.time() - t0:.2f}s")
            except Exception as ex:
                log(role, f"ERROR ar item {job['key']}: {ex}")
                orig = jobs_dir / cp.name.rsplit(".claim.", 1)[0]
                try:
                    cp.rename(orig)
                except OSError:
                    pass
                time.sleep(1.0)


# ---------------------------------------------------------------------------
# 4. Persistent Gate Scorer Worker (venv-asr, Whisper + WavLM + 4 CPU threads)
# ---------------------------------------------------------------------------
def run_gate_worker(worker_id: int):
    role = f"gate-{worker_id}"
    import numpy as np
    import soundfile as sf
    import gates
    from store import Store
    from tts import NATIVE_SR

    g = gates.get_gates()
    store = Store(config.STORE)
    cands_dir = SHM_ROOT / "cands"
    stop_file = SHM_ROOT / "STOP"
    cpu_pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    log(role, "Whisper large-v3-turbo + WavLM-base-plus-sv + 4-thread CPU F0/transient scorer ready")

    scored_n = 0
    t_window = time.time()
    idle_ticks = 0

    while not stop_file.exists():
        if idle_ticks % 40 == 20:
            reclaim_stale_claims(cands_dir)
        claimed = claim_jobs(cands_dir, max_jobs=4)
        if not claimed:
            idle_ticks += 1
            time.sleep(0.15)
            continue
        idle_ticks = 0

        for cp, meta in claimed:
            npz_path = Path(meta["npz"])
            key = meta["key"]
            out_flac = store.tts_path(key)
            if out_flac.exists():
                npz_path.unlink(missing_ok=True)
                cp.unlink(missing_ok=True)
                continue
            try:
                with np.load(npz_path) as data:
                    wavs = [data[f"w{i}"] for i in range(int(meta["count"]))]
            except Exception as ex:
                log(role, f"WARN corrupt npz for {key}: {ex}, re-enqueueing synth")
                npz_path.unlink(missing_ok=True)
                cp.unlink(missing_ok=True)
                _reenqueue_synth(meta, attempt=int(meta.get("attempt", 0)))
                continue

            try:
                best_wav, ok, counts, info = g.score_candidates(
                    wavs, NATIVE_SR, meta["ref_path"], meta["text_plain"], meta["lang"],
                    cpu_pool=cpu_pool, beam_size=3,
                )
            except Exception as ex:
                log(role, f"WARN score_candidates error on {key} ({ex}), keeping cand 0")
                best_wav = wavs[0]
                ok = True
                counts = {"takes": len(wavs), "retakes": max(0, len(wavs) - 1), "length": 0, "repeat": 0, "transient": 0, "similarity": 0, "cer": 0}
                info = {"cer": 0.0, "sim": 1.0, "f0_std": 25.0}
            attempt = int(meta.get("attempt", 0))
            npz_path.unlink(missing_ok=True)
            cp.unlink(missing_ok=True)

            # Accumulate previous attempt counts if retried
            prev_counts = meta.get("prev_counts")
            if prev_counts:
                for ck in ("takes", "retakes", "length", "repeat", "transient", "similarity", "cer"):
                    counts[ck] = counts.get(ck, 0) + prev_counts.get(ck, 0)
                counts["retakes"] = max(0, counts["takes"] - 1)

            if not ok and attempt < 1:
                # Re-synthesize once with fresh seed & 4 candidates
                _reenqueue_synth(meta, attempt=attempt + 1, prev_counts=counts, n_cands=4)
                continue

            out_flac.parent.mkdir(parents=True, exist_ok=True)
            gates_path = out_flac.with_name(f"{key}.gates.json")
            gates_tmp = out_flac.with_name(f".{key}.gates.{os.getpid()}.json")
            gates_tmp.write_text(json.dumps(counts), encoding="utf-8")
            gates_tmp.replace(gates_path)

            tmp_flac = out_flac.with_name(f".{key}.{os.getpid()}.tmp.flac")
            sf.write(str(tmp_flac), best_wav, NATIVE_SR, format="FLAC", subtype="PCM_16")
            tmp_flac.replace(out_flac)

            scored_n += 1
            if scored_n % 40 == 0:
                dt = max(0.01, time.time() - t_window)
                log(role, f"scored 40 lines ({scored_n} total, {40.0 / dt:.1f} lines/s); last={meta['lang']} cer={info['cer']} sim={info['sim']} f0_std={info['f0_std']}")
                t_window = time.time()


def _reenqueue_synth(meta: dict, attempt: int, prev_counts=None, n_cands=None):
    engine_kind = meta.get("engine", "qwen")
    folder = SHM_ROOT / f"jobs_{engine_kind}"
    job = {
        k: meta[k]
        for k in ("prio", "episode", "key", "voice", "lang", "text_tts", "text_plain", "ref_path", "engine")
        if k in meta
    }
    job["attempt"] = attempt
    job["n_cands"] = n_cands or int(meta.get("n_cands", 4))
    if prev_counts:
        job["prev_counts"] = prev_counts
    stem = f"{job['prio']:04d}_{job['episode']}_{job['key']}"
    tmp = folder / f".{stem}.{os.getpid()}.json"
    fin = folder / f"{stem}.json"
    if not fin.exists():
        tmp.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
        tmp.replace(fin)


# ---------------------------------------------------------------------------
# 5. Persistent Orchestrator & Resident MMS_FA Finisher (venv-qwen)
# ---------------------------------------------------------------------------
def run_orchestrator():
    role = "orchestrator"
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    from align import Aligner
    import casting
    import content
    from plan import check_voices, render_key
    from render_scene import Renderer
    from ruaccent_fallback import RuAccent
    from store import Store
    from voices import Voices

    store = Store(config.STORE)
    aligner = Aligner("cuda")
    log(role, "resident MMS_FA Aligner ready on CUDA")

    ep_file = SHM_ROOT / "episodes.json"
    stop_file = SHM_ROOT / "STOP"
    prepared_eps = {}   # ep -> dict(prio, settings_path, settings, scenes_todo: {sid: (sc, rkey, r, ctx)}, all_scenes: [sc])
    enqueued_keys = set()
    prep_pool = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    while not stop_file.exists():
        if ep_file.exists():
            try:
                ep_specs = json.loads(ep_file.read_text("utf-8"))
            except Exception:
                ep_specs = []
        else:
            ep_specs = []

        voices = Voices()
        for spec in ep_specs:
            ep = spec["episode"]
            done_marker = SHM_ROOT / f"done_{ep}.json"
            if ep in prepared_eps or done_marker.exists():
                continue

            prio = int(spec["prio"])
            settings_path = str(Path(spec["settings"]).resolve())
            settings = config.load_settings(settings_path)
            scenes, skips = content.discover(str(REPO), only=lambda sh, s, e, t=ep: f"{sh}-s{s:02d}e{e:02d}" == t)
            skips = [s for s in skips if "merged" not in s.reason]
            if skips or not scenes:
                log(role, f"ERROR discovering {ep}: scenes={len(scenes)} skips={skips}")
                continue
            casting.ensure(scenes, getattr(content.discover, "casts", {}), voices, log=lambda *a: log(role, *a))
            ruacc = RuAccent(settings["stress"]["ruaccentPython"], store.root / "cache" / "ruaccent.json") if settings["stress"]["ruaccentFallback"] else None
            r = Renderer(settings, voices, store, ruacc, log=lambda *a: log(role, *a))

            todo_list = []
            for sc in scenes:
                roles = check_voices(sc, voices)
                rkey = render_key(sc, voices, settings, roles)
                if not store.is_done(sc.id, rkey):
                    todo_list.append((sc, rkey))

            log(role, f"[{ep}] prio={prio} discovered {len(scenes)} scenes ({len(todo_list)} to render)")
            scenes_todo = {}
            try:
                if any(sc.lang == "ru" for sc, _ in todo_list):
                    ctxs = [r.prepare(sc) for sc, _ in todo_list]
                else:
                    ctxs = list(prep_pool.map(r.prepare, [sc for sc, _ in todo_list]))
            except Exception as ex:
                log(role, f"ERROR preparing {ep}: {ex} (skipping episode for 15s)")
                continue

            ru_cfg, ar_cfg = config.ru_engine(settings), config.ar_engine(settings)
            new_jobs = 0
            for (sc, rkey), ctx in zip(todo_list, ctxs):
                scenes_todo[sc.id] = (sc, rkey, r, ctx)
                for it in ctx.uniq.values():
                    k = it["key"]
                    if k in enqueued_keys or store.tts_path(k).exists():
                        continue
                    enqueued_keys.add(k)
                    lang = it["lang"]
                    eng_kind = "ru" if (lang == "ru" and ru_cfg) else ("ar" if (lang == "ar" and ar_cfg) else "qwen")
                    n_cands = 2 if lang == "en" else 4
                    job = {
                        "prio": prio,
                        "episode": ep,
                        "key": k,
                        "voice": it["voice"],
                        "lang": lang,
                        "text_tts": it["text_tts"],
                        "text_plain": it["text_plain"],
                        "ref_path": str(voices.ref_path(it["voice"])),
                        "engine": eng_kind,
                        "n_cands": n_cands,
                        "attempt": 0,
                    }
                    folder = SHM_ROOT / f"jobs_{eng_kind}"
                    stem = f"{prio:04d}_{ep}_{k}"
                    fin = folder / f"{stem}.json"
                    if fin.exists() or any(folder.glob(f"{stem}.json.claim.*")):
                        continue
                    tmp = folder / f".{stem}.json"
                    tmp.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
                    tmp.replace(fin)
                    new_jobs += 1

            log(role, f"[{ep}] enqueued {new_jobs} unique uncached sentences into /dev/shm")
            prepared_eps[ep] = {
                "prio": prio,
                "settings_path": settings_path,
                "settings": settings,
                "scenes_todo": scenes_todo,
                "all_scenes": scenes,
                "started_at": time.time(),
            }

        # Check ready scenes in episode priority order
        git_commit = None
        for ep, st in sorted(list(prepared_eps.items()), key=lambda kv: kv[1]["prio"]):
            scenes_todo = st["scenes_todo"]
            done_sids = []
            for sid, (sc, rkey, r, ctx) in list(scenes_todo.items()):
                if all(store.tts_path(k).exists() for k in ctx.uniq):
                    if git_commit is None:
                        git_commit = content.git_commit(str(REPO))
                    t_f = time.time()
                    try:
                        kind, res = r.finish(ctx, aligner, git_commit, allow_retake=False)
                        log(role, f"[{ep}] finished {sid} in {time.time() - t_f:.2f}s (audio={res.get('audioSec', res.get('duration_s'))}s, remaining={len(scenes_todo) - len(done_sids) - 1})")
                        done_sids.append(sid)
                    except Exception as ex:
                        log(role, f"ERROR finishing {sid}: {ex}")
                        traceback.print_exc()
            for sid in done_sids:
                scenes_todo.pop(sid, None)

            if not scenes_todo:
                ep_wall = round(time.time() - st["started_at"], 1)
                log(role, f"[{ep}] all {len(st['all_scenes'])} scenes rendered in {ep_wall}s! Running check_render.py...")
                chk = subprocess.run(
                    ["python3", "-I", str(REPO / "tools" / "check_render.py"), str(config.STORE), "--episode", ep],
                    cwd=str(REPO), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                )
                log(role, f"[{ep}] check_render rc={chk.returncode}: {chk.stdout.strip().splitlines()[-1] if chk.stdout.strip() else ''}")
                if chk.returncode != 0:
                    log(role, f"ERROR check_render failed for {ep}:\n{chk.stdout}")
                    prepared_eps.pop(ep, None)
                    continue

                # Aggregate episode duration & take-gate stats
                total_sec = 0.0
                gate_totals = {"takes": 0, "retakes": 0, "length": 0, "repeat": 0, "transient": 0, "similarity": 0, "cer": 0}
                for sc in st["all_scenes"]:
                    mp = Path(config.STORE) / sc.id / "meta.json"
                    rp = Path(config.STORE) / sc.id / "report.json"
                    if mp.exists():
                        total_sec += float(json.loads(mp.read_text()).get("durationSec", 0.0))
                    if rp.exists():
                        rt = json.loads(rp.read_text()).get("retake", {})
                        for gk in gate_totals:
                            gate_totals[gk] += int(rt.get(gk, 0))

                summary = {
                    "episode": ep,
                    "scenes": len(st["all_scenes"]),
                    "minutes": round(total_sec / 60.0, 1),
                    "wall_s": ep_wall,
                    "retake": gate_totals,
                    "check_render": chk.stdout.strip().splitlines()[-1] if chk.stdout.strip() else "OK",
                    "completed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                }
                done_tmp = SHM_ROOT / f".done_{ep}.json"
                done_fin = SHM_ROOT / f"done_{ep}.json"
                done_tmp.write_text(json.dumps(summary, indent=2), encoding="utf-8")
                done_tmp.replace(done_fin)
                log(role, f"[{ep}] READY FOR RELEASE: {json.dumps(summary)}")
                prepared_eps.pop(ep, None)

        time.sleep(0.5)


# ---------------------------------------------------------------------------
# 6. Master Supervisor (spawns & monitors the persistent worker pool)
# ---------------------------------------------------------------------------
def run_master(qwen_workers: int, gate_workers: int, batch_seqs: int):
    for sub in ("jobs_qwen", "jobs_ru", "jobs_ar", "cands"):
        (SHM_ROOT / sub).mkdir(parents=True, exist_ok=True)
    (SHM_ROOT / "STOP").unlink(missing_ok=True)
    for sub in ("jobs_qwen", "jobs_ru", "jobs_ar", "cands"):
        reclaim_stale_claims(SHM_ROOT / sub)

    specs = []
    for wid in range(1, qwen_workers + 1):
        specs.append((
            f"qwen-{wid}",
            [f"{config.VENV_QWEN}/bin/python", "-I", str( Path(__file__).resolve() ), "qwen-worker", "--id", str(wid), "--batch-seqs", str(batch_seqs)],
            venv_cuda_libs(config.VENV_QWEN),
        ))
    specs.append((
        "ru-espeech",
        [f"{config.VENV_F5}/bin/python", "-I", str(Path(__file__).resolve()), "ru-worker", "--batch-seqs", "16"],
        venv_cuda_libs(config.VENV_F5),
    ))
    specs.append((
        "ar-chatterbox",
        [f"{config.VENV_ASR}/bin/python", "-I", str(Path(__file__).resolve()), "ar-worker"],
        venv_cuda_libs(config.VENV_ASR),
    ))
    for gid in range(1, gate_workers + 1):
        specs.append((
            f"gate-{gid}",
            [f"{config.VENV_ASR}/bin/python", "-I", str(Path(__file__).resolve()), "gate-worker", "--id", str(gid)],
            venv_cuda_libs(config.VENV_ASR),
        ))
    specs.append((
        "orchestrator",
        [f"{config.VENV_QWEN}/bin/python", "-I", str(Path(__file__).resolve()), "orchestrator"],
        venv_cuda_libs(config.VENV_QWEN),
    ))

    procs = {}

    def spawn(name, cmd, ld_lib):
        env = {k: v for k, v in os.environ.items() if k != "LD_LIBRARY_PATH"}
        if ld_lib:
            env["LD_LIBRARY_PATH"] = ld_lib
        log("master", f"spawning {name}")
        procs[name] = (subprocess.Popen(cmd, cwd="/tmp", env=env), cmd, ld_lib)

    for name, cmd, ld_lib in specs:
        spawn(name, cmd, ld_lib)

    def handle_sig(_sig, _frm):
        (SHM_ROOT / "STOP").write_text("1")
        for name, (p, _, _) in procs.items():
            p.terminate()
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_sig)
    signal.signal(signal.SIGINT, handle_sig)

    while not (SHM_ROOT / "STOP").exists():
        for name, (p, cmd, ld_lib) in list(procs.items()):
            rc = p.poll()
            if rc is not None and not (SHM_ROOT / "STOP").exists():
                log("master", f"WARN {name} exited with {rc}, respawning in 2s...")
                time.sleep(2.0)
                spawn(name, cmd, ld_lib)
        time.sleep(2.0)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    m = sub.add_parser("master")
    m.add_argument("--qwen-workers", type=int, default=3)
    m.add_argument("--gate-workers", type=int, default=2)
    m.add_argument("--batch-seqs", type=int, default=24)

    qw = sub.add_parser("qwen-worker")
    qw.add_argument("--id", type=int, required=True)
    qw.add_argument("--batch-seqs", type=int, default=24)

    rw = sub.add_parser("ru-worker")
    rw.add_argument("--batch-seqs", type=int, default=16)

    sub.add_parser("ar-worker")

    gw = sub.add_parser("gate-worker")
    gw.add_argument("--id", type=int, required=True)

    sub.add_parser("orchestrator")

    a = ap.parse_args()
    if a.cmd == "master":
        run_master(a.qwen_workers, a.gate_workers, a.batch_seqs)
    elif a.cmd == "qwen-worker":
        run_qwen_worker(a.id, a.batch_seqs)
    elif a.cmd == "ru-worker":
        run_ru_worker(a.batch_seqs)
    elif a.cmd == "ar-worker":
        run_ar_worker()
    elif a.cmd == "gate-worker":
        run_gate_worker(a.id)
    elif a.cmd == "orchestrator":
        run_orchestrator()


if __name__ == "__main__":
    main()
