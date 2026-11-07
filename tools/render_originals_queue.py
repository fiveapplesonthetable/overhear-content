#!/usr/bin/env python3
"""GPU render & release queue for Overhear Originals (`originals/`), following strict 3-2-1 priority:
  1) Season 1 across all 10 languages in 3 RU -> 2 FR -> 1 each of ES, IT, PT, DE, AR, JA, KO, ZH cycles.
  2) Season 2+ in global 3 RU -> 2 FR -> 1 each cycles across available episodes per language stream.

For every episode:
  render/pipeline.py (scenes + lexicon example clips + paradigm form clips)
  -> tools/check_render.py
  -> tools/package_render.py --release
"""
import argparse
import fcntl
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

SHOWS = [
    ("ru", "dvorik-u-mosta", "render/settings.ru-qwen-lora-en.json"),
    ("fr", "hotel-du-tilleul", "render/settings.fr-qwen-en.json"),
    ("es", "posada-del-limonero", "render/settings.es-qwen-en.json"),
    ("it", "locanda-del-tiglio", "render/settings.it-qwen-en.json"),
    ("pt", "pousada-do-cajueiro", "render/settings.pt-qwen-en.json"),
    ("de", "pension-sonnenhof", "render/settings.de-qwen-en.json"),
    ("ar", "bayt-al-yasmin", "render/settings.ar-chatterbox-en.json"),
    ("ja", "hidamari-ryokan", "render/settings.ja-qwen-en.json"),
    ("ko", "haessal-guesthouse", "render/settings.ko-qwen-en.json"),
    ("zh", "xiaoyuan-kezhan", "render/settings.zh-qwen-en.json"),
]
QUOTA = {"ru": 3, "fr": 2}


def build_order(root: Path):
    q = []
    max_s1 = {}
    for lang, show, _st in SHOWS:
        sdir = root / "originals" / show
        eps = [
            int(m.group(1))
            for p in (sdir.iterdir() if sdir.is_dir() else [])
            if (m := re.match(r"^s01e(\d\d)$", p.name)) and (p / "scene-01.json").is_file()
        ]
        max_s1[lang] = max(eps) if eps else 0
    nxt = {lang: 1 for lang, _, _ in SHOWS}
    while any(nxt[lang] <= max_s1[lang] for lang, _, _ in SHOWS):
        for lang, show, st in SHOWS:
            for _ in range(QUOTA.get(lang, 1)):
                if nxt[lang] <= max_s1[lang]:
                    ep_dir = root / "originals" / show / f"s01e{nxt[lang]:02d}"
                    if (ep_dir / "scene-01.json").is_file():
                        q.append((lang, f"{show}-s01e{nxt[lang]:02d}", st))
                    nxt[lang] += 1

    streams = {}
    for lang, show, st in SHOWS:
        sdir = root / "originals" / show
        eps = []
        if sdir.is_dir():
            for p in sdir.iterdir():
                m = re.match(r"^s(\d\d)e(\d\d)$", p.name)
                if m and int(m.group(1)) >= 2 and (p / "scene-01.json").is_file():
                    eps.append((int(m.group(1)), int(m.group(2)), f"{show}-{p.name}", st))
        eps.sort()
        streams[lang] = eps
    idx = {lang: 0 for lang, _, _ in SHOWS}
    while any(idx[lang] < len(streams[lang]) for lang, _, _ in SHOWS):
        for lang, _show, _st in SHOWS:
            for _ in range(QUOTA.get(lang, 1)):
                if idx[lang] < len(streams[lang]):
                    _s, _e, ep_slug, st = streams[lang][idx[lang]]
                    q.append((lang, ep_slug, st))
                    idx[lang] += 1
    return q


def run_step(cmd, root: Path, out_dir: Path, log: Path, hold_git_lock: bool = False) -> int:
    extra_env = {
        "OVERHEAR_HOME": os.environ.get("OVERHEAR_HOME", str(Path.home() / "overhear")),
        "GPURUN_BUDGET_MIB": os.environ.get("GPURUN_BUDGET_MIB", "33500"),
        "OVERHEAR_SYNTH_WORKERS": os.environ.get("OVERHEAR_SYNTH_WORKERS", "3"),
        "OVERHEAR_ALIGN_WORKERS": os.environ.get("OVERHEAR_ALIGN_WORKERS", "3"),
        "OVERHEAR_SCENES_PER_SYNTH": os.environ.get("OVERHEAR_SCENES_PER_SYNTH", "4"),
        "OVERHEAR_FORM_WORKERS": os.environ.get("OVERHEAR_FORM_WORKERS", "3"),
        "OVERHEAR_FORMS_BATCH": os.environ.get("OVERHEAR_FORMS_BATCH", "32"),
        "OVERHEAR_TTS_BATCH": os.environ.get("OVERHEAR_TTS_BATCH", "16"),
    }
    env_file = out_dir / "env.json"
    if env_file.exists():
        try:
            extra_env.update({k: str(v) for k, v in json.loads(env_file.read_text()).items()})
        except Exception:
            pass
    lock_fh = None
    if hold_git_lock:
        lock_fh = open(out_dir / "git_release.lock", "w")
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
    try:
        with open(log, "a") as fh:
            fh.write(f"\n$ {' '.join(cmd)}\n")
            fh.flush()
            return subprocess.run(
                cmd, cwd=root, stdout=fh, stderr=subprocess.STDOUT, env={**os.environ, **extra_env}
            ).returncode
    finally:
        if lock_fh is not None:
            fcntl.flock(lock_fh, fcntl.LOCK_UN)
            lock_fh.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--store", type=Path, default=Path.home() / "overhear" / "render-store")
    ap.add_argument("--state-dir", type=Path, default=Path.home() / "overhear" / "render-queue")
    ap.add_argument("--print", dest="print_only", action="store_true", help="Print planned episode order and exit")
    args = ap.parse_args()

    root = args.content.resolve()
    if args.print_only:
        for _lang, ep, _st in build_order(root):
            print(ep)
        return

    out_dir = args.state_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    sp = out_dir / "state.json"

    while True:
        state = json.loads(sp.read_text()) if sp.exists() else {"done": [], "failed": {}}
        pending = [
            (lang, ep, st)
            for lang, ep, st in build_order(root)
            if ep not in state["done"] and ep not in state["failed"]
        ]
        if not pending:
            break
        lang, ep, st = pending[0]
        log = out_dir / f"{ep}.log"
        t0 = time.time()
        print(f"[{time.strftime('%H:%M:%S')}] START {ep} ({lang})", flush=True)
        rc = 1
        stage = "init"
        for attempt in range(1, 4):
            stage = f"render(pass={attempt})"
            extra = ["--retry-failed"] if attempt > 1 else []
            rc = run_step(
                ["python3", "-I", "render/pipeline.py", "--root", "originals", "--episode", ep, "--settings", st, "--store", str(args.store), *extra],
                root, out_dir, log,
            )
            if rc == 0:
                stage = f"check(pass={attempt})"
                rc = run_step(
                    ["python3", "-I", "tools/check_render.py", str(args.store), "--root", "originals", "--episode", ep],
                    root, out_dir, log,
                )
            if rc == 0:
                break
            print(f"[{time.strftime('%H:%M:%S')}] RETRY {ep} after {stage} (rc={rc})", flush=True)
        if rc == 0:
            stage = "release"
            rc = run_step(
                ["python3", "-I", "tools/package_render.py", str(args.store), "--root", "originals", "--episode", ep, "--release"],
                root, out_dir, log, hold_git_lock=True,
            )
        mins = round((time.time() - t0) / 60, 1)
        if rc == 0:
            state["done"].append(ep)
            state["failed"].pop(ep, None)
            print(f"[{time.strftime('%H:%M:%S')}] RELEASED original-{ep} in {mins} min ({len(state['done'])} total)", flush=True)
        else:
            state["failed"][ep] = f"{stage} rc={rc}"
            print(f"[{time.strftime('%H:%M:%S')}] FAILED {ep} at {stage} (rc={rc}) after {mins} min; see {log}", flush=True)
        sp.write_text(json.dumps(state, indent=1))
    print("QUEUE COMPLETE", json.dumps(state), flush=True)


if __name__ == "__main__":
    main()
