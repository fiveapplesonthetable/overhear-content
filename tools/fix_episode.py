#!/usr/bin/env python3
"""Fix already-released Originals episodes cheaply: re-voice ONLY the changed sentences, reassemble, re-check, re-release.

Why this is cheap and glitch-free
---------------------------------
Every sentence's audio is cached under `<store>/cache/tts/<key>.flac`, where key = hash(engine settings, voice, reference
version, language, exact text, retake counter). A scene's audio.mp3 is always re-assembled from those per-sentence takes
(with the authored gaps and loudness normalisation) and re-aligned, never spliced into an old mp3. So after a text fix:
  * unchanged sentences -> cache hit, byte-identical audio, no GPU synthesis;
  * changed sentences   -> new key -> synthesized once;
  * the scene mp3/timings are rebuilt cleanly from the takes (no clicks or seams at the edit point).
Same for intonation: bump a segment's counter in render/retakes.json (spec/feedback.md) and only that sentence (or the
inline narrator carrier containing it) gets a new take.

Usage
-----
  # 1. Edit the scene's authoring/scene-NN.py, regenerate JSON (tools/compose.py), validate, commit and push.
  # 2. Re-render + re-release every released episode whose scenes changed since a git revision:
  python3 tools/fix_episode.py --changed-since 70953f4ff
  # or explicit episodes, optionally asking for a new take of specific segments (bad intonation / mispronunciation):
  python3 tools/fix_episode.py --episode dvorik-u-mosta-s01e01 --retake dvorik-u-mosta-s01e01-scene-01:29
  # --dry-run prints the plan; --no-release renders and checks only.

The fix store (default ~/overhear/render-store-fix) is separate from the queue workers' stores so a fix never waits on
their pipeline.lock; `--seed-from` hard-links the content-addressed caches (tts, clips, forms) of the stores that made
the original release so nothing already voiced is synthesized again.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from render_originals_queue import SHOWS, run_step  # noqa: E402

HOME = Path(os.environ.get("OVERHEAR_HOME", Path.home() / "overhear"))
EXTRA_SETTINGS = {
    "aangan-haveli": "render/settings.hi-chatterbox-en.json",
    "linden-courtyard-ar": "render/settings.en-ar.json",
    "linden-courtyard-hi": "render/settings.en-hi.json",
}
_HEX = re.compile(r"^[0-9a-f]{16,64}\.(flac|mp3|json)$")


def settings_for(show: str) -> str:
    if show in EXTRA_SETTINGS:
        return EXTRA_SETTINGS[show]
    for _lang, s, st in SHOWS:
        if s == show:
            return st
    if show.startswith("linden-courtyard-"):
        return "render/settings.en-qwen.json"
    raise SystemExit(f"no render settings known for show {show!r}; add it to EXTRA_SETTINGS")


def lang_for(show: str) -> str:
    for lang, s, _st in SHOWS:
        if s == show:
            return lang
    return "hi" if show == "aangan-haveli" else "en"


def released_tags() -> set:
    out = subprocess.run(["gh", "release", "list", "--limit", "1000", "--json", "tagName"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return {r["tagName"] for r in json.loads(out)}


def changed_episodes(rev: str) -> list:
    out = subprocess.run(["git", "diff", "--name-only", f"{rev}..HEAD", "--", "originals"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    eps = set()
    for line in out.splitlines():
        m = re.match(r"^originals/([a-z0-9-]+)/(s\d\de\d\d)/scene-\d\d(\.notes)?\.json$", line)
        if m:
            eps.add(f"{m.group(1)}-{m.group(2)}")
    return sorted(eps)


def seed_cache(src: Path, dst: Path) -> int:
    """Hard-link content-addressed files (never temp/plan/lock files); .mp3 before .json so a clip record never
    appears before its audio."""
    n = 0
    for rel in ("cache/tts", "clips", "forms"):
        s, d = src / rel, dst / rel
        if not s.is_dir():
            continue
        d.mkdir(parents=True, exist_ok=True)
        have = {e.name for e in os.scandir(d)}
        names = sorted((e.name for e in os.scandir(s) if e.is_file() and _HEX.match(e.name) and e.name not in have),
                       key=lambda x: x.endswith(".json"))
        for name in names:
            try:
                os.link(s / name, d / name)
                n += 1
            except (FileExistsError, OSError):
                pass
    return n


def bump_retakes(specs: list) -> None:
    path = ROOT / "render" / "retakes.json"
    data = json.loads(path.read_text()) if path.exists() else {}
    for spec in specs:
        sid, _, seg = spec.rpartition(":")
        if not sid or not seg.isdigit():
            raise SystemExit(f"--retake wants <scene-id>:<segment-index>, got {spec!r}")
        cur = data.setdefault(sid, {})
        cur[str(int(seg))] = int(cur.get(str(int(seg)), 0)) + 1
        print(f"retake {sid} segment {seg} -> counter {cur[str(int(seg))]}")
    path.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--episode", action="append", default=[])
    ap.add_argument("--changed-since", help="git revision: fix every episode whose scene JSON changed since it")
    ap.add_argument("--retake", action="append", default=[], help="<scene-id>:<segment> new take of an unchanged segment")
    ap.add_argument("--store", type=Path, default=HOME / "render-store-fix")
    ap.add_argument("--seed-from", type=Path, action="append", default=[],
                    help="store(s) whose caches to hard-link first (default: every ~/overhear/render-store*)")
    ap.add_argument("--state-dir", type=Path, default=HOME / "render-fix-logs")
    ap.add_argument("--include-unreleased", action="store_true", help="also render episodes that were never released")
    ap.add_argument("--no-release", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    eps = list(args.episode)
    if args.changed_since:
        eps += changed_episodes(args.changed_since)
    eps += [s.rpartition(":")[0].rsplit("-scene-", 1)[0] for s in args.retake]
    eps = sorted(set(eps))
    if not eps:
        raise SystemExit("nothing to fix (give --episode, --changed-since or --retake)")
    tags = released_tags()
    if not args.include_unreleased:
        skipped = [e for e in eps if f"original-{e}" not in tags]
        eps = [e for e in eps if f"original-{e}" in tags]
        if skipped:
            print(f"not released yet (the queue will render the fixed text): {', '.join(skipped)}")
    plan = [(e, settings_for(e.rsplit("-s", 1)[0])) for e in eps]
    for e, st in plan:
        print(f"PLAN {e}  settings={st}")
    if args.dry_run or not plan:
        return
    if args.retake:
        bump_retakes(args.retake)
        print("render/retakes.json changed: commit and push it before releasing (package_render requires a pushed HEAD)")

    args.store.mkdir(parents=True, exist_ok=True)
    args.state_dir.mkdir(parents=True, exist_ok=True)
    seeds = args.seed_from or sorted(p for p in HOME.glob("render-store*") if p.is_dir() and p.resolve() != args.store.resolve())
    for s in seeds:
        print(f"seeded {seed_cache(s, args.store)} cached files from {s}")

    failed = []
    for ep, st in plan:
        show = ep.rsplit("-s", 1)[0]
        log = args.state_dir / f"{ep}.log"
        lang = lang_for(show)
        rc = run_step(["python3", "-I", "render/pipeline.py", "--root", "originals", "--episode", ep, "--settings", st,
                       "--store", str(args.store)], ROOT, args.state_dir, log, lang=lang)
        if rc == 0:
            rc = run_step(["python3", "-I", "tools/check_render.py", str(args.store), "--root", "originals", "--episode", ep],
                          ROOT, args.state_dir, log, lang=lang)
        if rc == 0 and not args.no_release:
            rc = run_step(["python3", "-I", "tools/package_render.py", str(args.store), "--root", "originals", "--episode", ep,
                           "--release"], ROOT, args.state_dir, log, hold_git_lock=True, lang=lang)
        print(f"{'OK  ' if rc == 0 else 'FAIL'} {ep} (log {log})", flush=True)
        if rc:
            failed.append(ep)
    if failed:
        raise SystemExit(f"failed: {' '.join(failed)}")


if __name__ == "__main__":
    main()
