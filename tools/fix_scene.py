#!/usr/bin/env python3
"""Fixes scenes of an already released Originals episode on this machine: re-renders just those scenes, re-uses every sentence
take the receiver already holds, and re-packages the episode.

  python3 tools/fix_scene.py dvorik-u-mosta-s02e01-scene-01 [SCENE ...]            # render + check + package (dist/), release nothing
  python3 tools/fix_scene.py SCENE ... --release                                    # and upload GitHub release original-<episode>
  python3 tools/fix_scene.py SCENE ... --dry-run                                    # plan only: profile, scenes, sentences still to synthesize
  options: --commit SHA   the pushed content commit this checkout must be at (default: whatever HEAD is)
           --installed DIR  the receiver's render dir (default $OVERHEAR_RENDER_DIR): installed scenes, clips, forms and its
                            sentence takes in DIR/cache/tts (shipped inside the packages, tools/fetch_renders.py)
           --work DIR     this machine's fix store (default $OVERHEAR_HOME/fix-store)
           --gpu-mib N, --batch N   scale the profile to this GPU (defaults: $GPURUN_BUDGET_MIB - 800, 3)

Commit and push the content fix first (scene text/notes, or render/retakes.json), then run this from a checkout at that commit.
Rendering is incremental per sentence: a take's cache key covers the engine settings, voice, reference, language, text and retake
counter, so a sentence the fix did not touch is a cache hit and keeps its exact audio; only the changed ones are synthesized.
The fix store holds the re-rendered scenes for real and the episode's other scenes, clips and forms as links into --installed,
so package_render sees a whole episode; only the re-rendered scenes ship their takes (--takes-of), the receiver has the rest.
The scene is rendered with its show's usual profile (tools/fix_episode.settings_for), scaled down by a derived settings copy;
batch sizes and GPU reservations are not part of any cache or render key. Rendering goes through render/pipeline.py (its
gpurun reservations share the GPU with other jobs); example clips, forms and the narrator pass are left to the main renderer.
The receiver's timer installs and publishes the release; this script waits for nothing.
"""
import argparse
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_render as cr  # noqa: E402
import fix_episode  # noqa: E402
import package_render as pr  # noqa: E402

HOME = Path(os.environ.get("OVERHEAR_HOME", Path.home() / "overhear"))
INSTALLED = Path(os.environ.get("OVERHEAR_RENDER_DIR", "/mnt/agent/s02-originals/render"))
SCENE_ID = re.compile(r"^(?P<episode>(?P<show>[a-z][a-z0-9-]*)-s\d\de\d\d)-scene-\d\d$")
BATCH_KEYS = ("batch", "batchEn")


def by_episode(scene_ids):
    """{episode: [scene ids]} in the order given."""
    episodes = {}
    for sid in scene_ids:
        m = SCENE_ID.match(sid)
        if not m:
            raise SystemExit(f"{sid!r} is not a scene id (<show>-sNNeNN-scene-NN)")
        episodes.setdefault(m["episode"], []).append(sid)
    return episodes


def scaled_settings(profile, gpu_mib, batch):
    """The profile with its GPU reservations and batch sizes capped for a smaller card. Neither enters a render or sentence
    cache key (tests/test_fix_scene.py checks that for every profile)."""
    s = json.loads(Path(profile).read_text(encoding="utf-8"))
    for k, v in s.get("gpu", {}).items():
        if k.endswith("MiB"):
            s["gpu"][k] = min(v, gpu_mib)
    for block in ("tts", "clips", "forms"):
        for k in BATCH_KEYS:
            if k in s.get(block, {}):
                s[block][k] = min(s[block][k], batch)
    return s


def link(path, target):
    """`path` becomes a symlink to `target`; an old symlink is replaced, a real file or folder is never overwritten."""
    if path.is_symlink():
        path.unlink()
    elif path.exists():
        raise SystemExit(f"{path} is a real file or folder here; refusing to replace it with a link into the installed render dir")
    path.symlink_to(target)


def assemble(work, installed, scene_ids, fixed):
    """Makes `work` hold the whole episode: the scenes being fixed stay real, the others (and clips/ forms/) link to the receiver's."""
    missing = [s for s in scene_ids if s not in fixed and not (installed / s / "meta.json").is_file()]
    if missing:
        raise SystemExit(f"not installed on the receiver ({installed}), so the episode cannot be assembled: {', '.join(missing)}")
    work.mkdir(parents=True, exist_ok=True)
    for sid in scene_ids:
        if sid in fixed:
            if (work / sid).is_symlink():
                (work / sid).unlink()               # the renderer replaces a scene folder in place, never through a link
        else:
            if (work / sid).is_dir() and not (work / sid).is_symlink():
                shutil.rmtree(work / sid)           # an earlier fix of it; the receiver's copy is the published one
            link(work / sid, installed / sid)
    for kind in ("clips", "forms"):
        if (installed / kind).is_dir():
            link(work / kind, installed / kind)


def installed_takes(installed):
    """Cache keys of the sentence takes the receiver holds."""
    return {p.name.removesuffix(".flac") for p in (installed / "cache" / "tts").glob("*.flac")}


def sentence_report(takes, held):
    """Sentences of a rendered scene ({key: text}): ([texts] taken from the receiver's takes, [texts] synthesized here)."""
    return [t for k, t in takes.items() if k in held], [t for k, t in takes.items() if k not in held]


def check_rendered(work, scene_id, content, root):
    """Problems that make a re-rendered scene unfit to ship; check_render covers the contract itself."""
    meta_path = work / scene_id / "meta.json"
    if not meta_path.is_file():
        return ["not rendered"]
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    scene = next(s for s in cr.scenes_of(content, scene=scene_id, root=root))
    problems = []
    if meta["contentHash"] != cr.content_hash(scene[1], scene[2]):
        problems.append("rendered from other content than this checkout")
    report = json.loads((work / scene_id / "report.json").read_text(encoding="utf-8"))
    if report["stress"]["stillFlagged"]:
        problems.append(f"{report['stress']['stillFlagged']} sentences still flagged by the stress check")
    if report["timing"]["notOk"]:
        problems.append(f"{report['timing']['notOk']} words without a measured time")
    return problems


def run_pipeline(args, settings_file, root, ids, extra=()):
    cmd = [sys.executable, "-I", str(ROOT / "render" / "pipeline.py"), "--root", root, "--scene", ",".join(ids),
           "--content", str(ROOT), "--store", str(args.work), "--settings", str(settings_file),
           "--no-clips", "--no-forms", "--no-narrator", "--retry-failed", *extra]
    env = {**os.environ, "OVERHEAR_CONTENT": str(ROOT)}
    return subprocess.run(cmd, env=env, cwd="/tmp").returncode


def stage_missing(args, settings_file, root, sid):
    """Sentences of one scene that no take exists for yet (stage.py missing; no GPU)."""
    venv = os.environ.get("OVERHEAR_VENV_QWEN", str(HOME / "venv-qwen"))
    p = subprocess.run([f"{venv}/bin/python", "-I", str(ROOT / "render" / "stage.py"), "missing", "--scene", sid, "--root", root,
                        "--content", str(ROOT), "--store", str(args.work), "--settings", str(settings_file)],
                       capture_output=True, text=True, cwd="/tmp", env={**os.environ, "OVERHEAR_CONTENT": str(ROOT)})
    for line in reversed(p.stdout.splitlines()):
        if line.startswith("OK "):
            return {k: v for k, v in json.loads(line[3:]).items() if k != "stage"}
    return None


def asset_stamp(tag):
    """updated_at of a release's episode tarball, the stamp the receiver's state records for it."""
    p = subprocess.run(["gh", "api", f"repos/{{owner}}/{{repo}}/releases/tags/{tag}", "--jq", ".assets[] | select(.name == \"" + tag + ".tar\") | .updated_at"],
                       capture_output=True, text=True, cwd=ROOT)
    return p.stdout.strip()


def fix_episode_scenes(args, episode, ids):
    root = pr.resolve_episode_root(ROOT, episode, None)
    profile = ROOT / fix_episode.settings_for(SCENE_ID.match(ids[0])["show"])
    scaled = args.work / "settings" / profile.name
    scaled.parent.mkdir(parents=True, exist_ok=True)
    scaled.write_text(json.dumps(scaled_settings(profile, args.gpu_mib, args.batch), indent=1), encoding="utf-8")
    scene_ids = [s[0] for s in cr.scenes_of(ROOT, episode=episode, root=root) if not s[3]]
    unknown = [i for i in ids if i not in scene_ids]
    if unknown:
        raise SystemExit(f"not scenes of {episode} in this checkout: {', '.join(unknown)}")
    assemble(args.work, args.installed, scene_ids, set(ids))
    linked = fix_episode.seed_cache(args.installed, args.work, rels=("cache/tts",))
    print(f"{episode}: profile {profile.name}, fixing {len(ids)} of {len(scene_ids)} scenes, {linked} takes linked from the receiver")
    held = installed_takes(args.installed)
    if args.dry_run:
        for sid in ids:
            print(f"  {sid}: still to synthesize {stage_missing(args, scaled, root, sid)}")
        return 0
    rc = run_pipeline(args, scaled, root, ids)
    for sid in ids:
        problems = check_rendered(args.work, sid, ROOT, root) if rc == 0 else ["pipeline failed"]
        if problems:
            print(f"ERROR {sid}: {'; '.join(problems)}")
            return 1
        takes = json.loads((args.work / sid / "meta.json").read_text(encoding="utf-8")).get("sentenceTakes", {})
        reused, new = sentence_report(takes, held)
        print(f"{sid}: {len(reused)} sentences reused, {len(new)} re-synthesized")
        for text in new:
            print(f"    new: {text}")
    pack = [str(args.work), "--episode", episode, "--root", root, "--content", str(ROOT), "--takes-of", ",".join(ids)]
    rc = pr.main(pack + (["--release"] if args.release else []))
    if rc == 0 and args.release:
        tag = f"{'original' if root == 'originals' else 'render'}-{episode}"
        print(f"RELEASED {tag} {asset_stamp(tag)}")
    return rc


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scenes", nargs="+")
    ap.add_argument("--commit")
    ap.add_argument("--installed", type=Path, default=INSTALLED)
    ap.add_argument("--work", type=Path, default=HOME / "fix-store")
    ap.add_argument("--gpu-mib", type=int, default=int(os.environ.get("GPURUN_BUDGET_MIB", "7800")) - 800)
    ap.add_argument("--batch", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--release", action="store_true")
    args = ap.parse_args(argv)
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if args.commit and not head.startswith(args.commit):
        raise SystemExit(f"this checkout is at {head[:12]}, not {args.commit[:12]}")
    episodes = by_episode(args.scenes)
    args.work.mkdir(parents=True, exist_ok=True)
    with open(args.work / "fix.lock", "w") as lock:           # one fix at a time; the GPU share itself is gpurun's business
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("another fix_scene run is active; exiting")
            return 75
        rc = 0
        for episode, ids in episodes.items():
            rc |= fix_episode_scenes(args, episode, ids)
        return rc


if __name__ == "__main__":
    sys.exit(main())
