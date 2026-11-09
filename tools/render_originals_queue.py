#!/usr/bin/env python3
"""GPU render & release queue for Overhear Originals (`originals/`), following strict 3-2-1 priority:
  1) Season 1 across all 10 languages in 3 RU -> 2 FR -> 1 each of ES, IT, PT, DE, AR, JA, KO, ZH cycles.
  2) Season 2+ in global 3 RU -> 2 FR -> 1 each cycles across available episodes per language stream.

For every episode:
  render/pipeline.py (scenes + lexicon example clips + paradigm form clips)
  -> tools/check_render.py
  -> tools/package_render.py --release

Parallel workers: render/pipeline.py allows ONE run per --store (pipeline.lock), so each worker needs its own
store (e.g. a hardlinked copy of the main store) plus --langs/--exclude-langs; workers share --state-dir and claim
episodes atomically, e.g.
  render_originals_queue.py --langs ar --store ~/overhear/render-store
  render_originals_queue.py --exclude-langs ar --store ~/overhear/render-store-b
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
    # Tier 1 (Main priority — weight 4): Russian, French, Spanish
    ("ru", "dvorik-u-mosta", "render/settings.ru-qwen-lora-en.json"),
    ("fr", "hotel-du-tilleul", "render/settings.fr-qwen-en.json"),
    ("es", "posada-del-limonero", "render/settings.es-qwen-en.json"),
    ("en", "linden-courtyard-ru", "render/settings.en-qwen.json"),
    ("en", "linden-courtyard-fr", "render/settings.en-qwen.json"),
    ("en", "linden-courtyard-es", "render/settings.en-qwen.json"),
    # Tier 2 (Weight 2): German, Italian, Korean
    ("de", "pension-sonnenhof", "render/settings.de-qwen-en.json"),
    ("it", "locanda-del-tiglio", "render/settings.it-qwen-en.json"),
    ("ko", "haessal-guesthouse", "render/settings.ko-qwen-en.json"),
    ("en", "linden-courtyard-de", "render/settings.en-qwen.json"),
    ("en", "linden-courtyard-it", "render/settings.en-qwen.json"),
    ("en", "linden-courtyard-ko", "render/settings.en-qwen.json"),
    # Tier 3 (Weight 1): Chinese, Japanese (+ Portuguese)
    ("zh", "xiaoyuan-kezhan", "render/settings.zh-qwen-en.json"),
    ("ja", "hidamari-ryokan", "render/settings.ja-qwen-en.json"),
    ("pt", "pousada-do-cajueiro", "render/settings.pt-qwen-en.json"),
    ("en", "linden-courtyard-zh", "render/settings.en-qwen.json"),
    ("en", "linden-courtyard-ja", "render/settings.en-qwen.json"),
    ("en", "linden-courtyard-pt", "render/settings.en-qwen.json"),
    # Tier 4 (Lowest priority — weight 1, last): Arabic, Hindi
    ("ar", "bayt-al-yasmin", "render/settings.ar-chatterbox-en.json"),
    ("hi", "aangan-haveli", "render/settings.hi-chatterbox-en.json"),
    ("en", "linden-courtyard-ar", "render/settings.en-ar.json"),
    ("en", "linden-courtyard-hi", "render/settings.en-hi.json"),
]
QUOTA = {
    "dvorik-u-mosta": 4,
    "hotel-du-tilleul": 4,
    "posada-del-limonero": 4,
    "linden-courtyard-ru": 4,
    "linden-courtyard-fr": 4,
    "linden-courtyard-es": 4,
    "pension-sonnenhof": 2,
    "locanda-del-tiglio": 2,
    "haessal-guesthouse": 2,
    "linden-courtyard-de": 2,
    "linden-courtyard-it": 2,
    "linden-courtyard-ko": 2,
}


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
        max_s1[show] = max(eps) if eps else 0
    nxt = {show: 1 for _, show, _ in SHOWS}
    while any(nxt[show] <= max_s1[show] for _, show, _ in SHOWS):
        for lang, show, st in SHOWS:
            for _ in range(QUOTA.get(show, QUOTA.get(lang, 1))):
                if nxt[show] <= max_s1[show]:
                    ep_dir = root / "originals" / show / f"s01e{nxt[show]:02d}"
                    if (ep_dir / "scene-01.json").is_file():
                        q.append((lang, f"{show}-s01e{nxt[show]:02d}", st))
                    nxt[show] += 1

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
        streams[show] = eps
    idx = {show: 0 for _, show, _ in SHOWS}
    while any(idx[show] < len(streams[show]) for _, show, _ in SHOWS):
        for lang, show, _st in SHOWS:
            for _ in range(QUOTA.get(show, QUOTA.get(lang, 1))):
                if idx[show] < len(streams[show]):
                    _s, _e, ep_slug, st = streams[show][idx[show]]
                    q.append((lang, ep_slug, st))
                    idx[show] += 1
    return q


def run_step(cmd, root: Path, out_dir: Path, log: Path, hold_git_lock: bool = False, lang: str = "") -> int:
    cmd_s = " ".join(cmd)
    is_ar = (lang in ("ar", "hi")) or any(x in cmd_s for x in ("chatterbox", "settings.en-ar", "settings.en-hi"))
    extra_env = {
        "OVERHEAR_HOME": os.environ.get("OVERHEAR_HOME", str(Path.home() / "overhear")),
        "GPURUN_BUDGET_MIB": os.environ.get("GPURUN_BUDGET_MIB", "35500"),
        "GPURUN_MARGIN_MIB": os.environ.get("GPURUN_MARGIN_MIB", "3500"),
        "OVERHEAR_SYNTH_WORKERS": "2" if is_ar else os.environ.get("OVERHEAR_SYNTH_WORKERS", "4"),
        "OVERHEAR_ALIGN_WORKERS": "2" if is_ar else os.environ.get("OVERHEAR_ALIGN_WORKERS", "3"),
        "OVERHEAR_SCENES_PER_SYNTH": "2" if is_ar else os.environ.get("OVERHEAR_SCENES_PER_SYNTH", "4"),
        "OVERHEAR_FORM_WORKERS": "2" if is_ar else os.environ.get("OVERHEAR_FORM_WORKERS", "3"),
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
    ap.add_argument("--langs", default="", help="Comma-separated languages this worker handles (default: all)")
    ap.add_argument("--exclude-langs", default="", help="Comma-separated languages this worker skips")
    args = ap.parse_args()
    only = {x for x in args.langs.split(",") if x}
    skip = {x for x in args.exclude_langs.split(",") if x}

    def wanted(lang):
        env_file = args.state_dir.resolve() / "env.json"
        if env_file.exists():
            try:
                if json.loads(env_file.read_text()).get("ALL_LANGS_321"):
                    return True
            except Exception:
                pass
        return (not only or lang in only) and lang not in skip

    root = args.content.resolve()
    if args.print_only:
        for lang, ep, _st in build_order(root):
            if wanted(lang):
                print(ep)
        return

    out_dir = args.state_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    sp = out_dir / "state.json"
    claims = out_dir / "claims"
    claims.mkdir(exist_ok=True)

    def load_state():
        return json.loads(sp.read_text()) if sp.exists() else {"done": [], "failed": {}}

    def update_state(fn):
        # Several workers share state.json: read-modify-write under an exclusive lock.
        with open(out_dir / "state.lock", "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            st_ = load_state()
            fn(st_)
            tmp = sp.with_suffix(".tmp")
            tmp.write_text(json.dumps(st_, indent=1))
            tmp.replace(sp)
            return st_

    state = load_state()
    while True:
        state = load_state()
        lang = ep = st = None
        prio_items = []
        prio_file = out_dir / "priority.json"
        if prio_file.exists():
            try:
                for item in json.loads(prio_file.read_text()):
                    ep_slug = item["episode"]
                    show_slug, ep_code = ep_slug.rsplit("-", 1)
                    if (root / "originals" / show_slug / ep_code / "scene-01.json").is_file() and (root / item["settings"]).is_file():
                        prio_items.append((item["lang"], ep_slug, item["settings"]))
            except Exception:
                pass
        for l_, e_, s_ in prio_items + build_order(root):
            if not wanted(l_) or e_ in state["done"] or e_ in state["failed"]:
                continue
            try:  # Atomic claim so parallel workers never render the same episode.
                os.close(os.open(claims / f"{e_}.claim", os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            except FileExistsError:
                continue
            lang, ep, st = l_, e_, s_
            break
        if ep is None:
            break
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
                root, out_dir, log, lang=lang,
            )
            busy_waits = 0
            while rc == 0 and log.read_text(errors="replace")[-400:].rstrip().endswith("another pipeline run is active; exiting") and busy_waits < 240:
                # Store is locked by another pipeline run: wait instead of burning a retry / marking the episode failed.
                busy_waits += 1
                time.sleep(60)
                rc = run_step(
                    ["python3", "-I", "render/pipeline.py", "--root", "originals", "--episode", ep, "--settings", st, "--store", str(args.store), *extra],
                    root, out_dir, log, lang=lang,
                )
            if rc == 0:
                stage = f"check(pass={attempt})"
                rc = run_step(
                    ["python3", "-I", "tools/check_render.py", str(args.store), "--root", "originals", "--episode", ep],
                    root, out_dir, log, lang=lang,
                )
            if rc == 0:
                break
            print(f"[{time.strftime('%H:%M:%S')}] RETRY {ep} after {stage} (rc={rc})", flush=True)
        if rc == 0:
            stage = "release"
            rc = run_step(
                ["python3", "-I", "tools/package_render.py", str(args.store), "--root", "originals", "--episode", ep, "--release"],
                root, out_dir, log, hold_git_lock=True, lang=lang,
            )
        mins = round((time.time() - t0) / 60, 1)
        if rc == 0:
            def ok(s_):
                if ep not in s_["done"]:
                    s_["done"].append(ep)
                s_["failed"].pop(ep, None)
            state = update_state(ok)
            print(f"[{time.strftime('%H:%M:%S')}] RELEASED original-{ep} in {mins} min ({len(state['done'])} total)", flush=True)
        else:
            def bad(s_):
                s_["failed"][ep] = f"{stage} rc={rc}"
            state = update_state(bad)
            print(f"[{time.strftime('%H:%M:%S')}] FAILED {ep} at {stage} (rc={rc}) after {mins} min; see {log}", flush=True)
        (claims / f"{ep}.claim").unlink(missing_ok=True)
    print("QUEUE COMPLETE", json.dumps(state), flush=True)


if __name__ == "__main__":
    main()
