#!/usr/bin/env python3
"""Packs one rendered episode into a release tarball (spec/OUTPUT-CONTRACT.md, "Packages"). Python 3 stdlib only (+ `gh` for --release).

  python3 tools/package_render.py STORE --episode kukhnya-s01e01                 # -> dist/render-kukhnya-s01e01.tar
  python3 tools/package_render.py STORE --episode kukhnya-s01e01 --release       # and upload it as GitHub release render-kukhnya-s01e01

STORE is the render store ($OVERHEAR_HOME/render-store). The episode must pass tools/check_render.py --episode first: a package
never carries a scene the publisher would drop. The tarball holds, with paths relative to the store:
  <sceneId>/{audio.mp3, spans.json, timing.json, meta.json, report.json}   every non-merged scene of the episode
  clips/<id>.{json,mp3}                                                    the example clips of those scenes' lexicons (failed: .json only)
  forms/<id>.{json,mp3}                                                    the form clips of those lexicons' tables
  forms-plan/<episode>.json                                                the episode's rows of forms/.plan.json
  MANIFEST.json                                                            episode, content commit, per-scene contentHash, sha256 of every file
"""
import hashlib, io, json, re, subprocess, sys, tarfile, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_render as cr

ROOT = Path(__file__).resolve().parents[1]


def resolve_episode_root(content: Path, episode: str, explicit_root=None) -> str:
    m = re.match(r"^([a-z0-9-]+)-s\d\de\d\d$", episode)
    show = m.group(1) if m else episode
    in_out = (content / "out" / show).is_dir()
    in_orig = (content / "originals" / show).is_dir()
    if in_out and in_orig:
        raise ValueError(f"show slug {show!r} exists in both out/ and originals/ (slug collision)")
    if explicit_root is not None:
        if explicit_root not in ("out", "originals"):
            raise ValueError(f"--root must be 'out' or 'originals', got {explicit_root!r}")
        if explicit_root == "originals" and in_out:
            raise ValueError(f"episode {episode!r} lives in out/, not originals/")
        if explicit_root == "out" and in_orig:
            raise ValueError(f"episode {episode!r} lives in originals/, not out/")
        return explicit_root
    if in_orig:
        return "originals"
    return "out"


def episode_files(store, content, episode, root=None):
    """-> (scene ids, [relative paths], [plan rows]) of one episode."""
    scenes = [s for s in cr.scenes_of(content, episode=episode, root=root) if not s[3]]
    files, ids = [], set()
    for sid, sp, npth, _ in scenes:
        files += [f"{sid}/{f}" for f in cr.SCENE_FILES]
        pair = json.loads(sp.read_text(encoding="utf-8"))["pair"]
        for e in json.loads(npth.read_text(encoding="utf-8")).get("lexicon", {}).values():
            for ex in e.get("examples", []):
                ids.add(("clips", cr.clip_id(pair, ex["text"])))
            for t in ([e["forms"]] if e.get("forms") else []) + list(e.get("moreForms") or []):
                heads = t.get("columns") or []
                for row in t["rows"]:
                    for c, cell in enumerate(row["cells"][1:], 1):
                        if cell:
                            ids.add(("forms", cr.form_id(pair, e["lemma"], t.get("title", ""), row["cells"][0], heads[c] if c < len(heads) else "", cell)))
    for kind, i in sorted(ids):
        for ext in ("json", "mp3"):
            if (store / kind / f"{i}.{ext}").is_file():
                files.append(f"{kind}/{i}.{ext}")
    plan_file = store / "forms" / ".plan.json"
    form_ids = {i for kind, i in ids if kind == "forms"}
    plan = [r for r in json.loads(plan_file.read_text(encoding="utf-8")) if r["id"] in form_ids] if plan_file.is_file() else []
    return [s[0] for s in scenes], files, plan


def main(argv):
    store_arg, episode, content, explicit_root, do_release = None, None, ROOT, None, False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--episode":
            episode = argv[i + 1]; i += 2; continue
        if a == "--content":
            content = Path(argv[i + 1]).resolve(); i += 2; continue
        if a == "--root":
            explicit_root = argv[i + 1]; i += 2; continue
        if a.startswith("--root="):
            explicit_root = a.split("=", 1)[1]; i += 1; continue
        if a == "--release":
            do_release = True; i += 1; continue
        if not a.startswith("--") and store_arg is None:
            store_arg = a
        i += 1
    if not episode or store_arg is None:
        print(__doc__); return 2
    store = Path(store_arg).resolve()
    try:
        root = resolve_episode_root(content, episode, explicit_root)
    except ValueError as e:
        print(f"ERROR {e}"); return 1
    if cr.main([str(store), "--root", root, "--episode", episode, "--content", str(content)]) != 0:
        print(f"{episode}: tools/check_render.py fails; not packaged"); return 1
    scenes, files, plan = episode_files(store, content, episode, root=root)
    commit = subprocess.run(["git", "-C", str(content), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    manifest = {"schemaVersion": 1, "episode": episode, "root": root, "contentCommit": commit,
                "packagedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "scenes": [{"sceneId": s, **{k: json.loads((store / s / "meta.json").read_text(encoding="utf-8"))[k]
                                             for k in ("contentHash", "audioSha256", "durationSec")}} for s in scenes],
                "files": {f: cr.sha256_file(store / f) for f in files}}
    plan_b = json.dumps(plan, ensure_ascii=False).encode("utf-8")
    manifest["files"][f"forms-plan/{episode}.json"] = hashlib.sha256(plan_b).hexdigest()
    prefix = "original" if root == "originals" else "render"
    out = content / "dist" / f"{prefix}-{episode}.tar"
    out.parent.mkdir(exist_ok=True)
    with tarfile.open(out, "w") as tar:
        for f in files:
            tar.add(store / f, arcname=f)
        for name, data in ((f"forms-plan/{episode}.json", plan_b),
                           ("MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=1).encode("utf-8"))):
            info = tarfile.TarInfo(name); info.size = len(data); info.mtime = int(time.time())
            tar.addfile(info, io.BytesIO(data))
    print(f"{out}: {len(scenes)} scenes, {len(files)} files, {out.stat().st_size / 1e6:.1f} MB")
    if do_release:
        m_ep = re.match(r"^([a-z0-9-]+)-(s\d\de\d\d)$", episode)
        if m_ep:
            ep_dir = content / root / m_ep.group(1) / m_ep.group(2)
            dirty = subprocess.run(["git", "-C", str(content), "status", "--porcelain", "--", str(ep_dir)],
                                   capture_output=True, text=True).stdout.strip()
            if dirty:
                print(f"ERROR {episode}: uncommitted/untracked content in {ep_dir}; commit and push before --release"); return 1
            tracked = subprocess.run(["git", "-C", str(content), "ls-tree", "HEAD", "--", str(ep_dir)],
                                     capture_output=True, text=True).stdout.strip()
            if not tracked:
                print(f"ERROR {episode}: {ep_dir} is not tracked in HEAD ({commit[:12]}); commit and push before --release"); return 1
        pushed = subprocess.run(["git", "-C", str(content), "branch", "-r", "--contains", commit],
                                capture_output=True, text=True).stdout.strip()
        if not pushed:
            print(f"ERROR {episode}: HEAD {commit[:12]} is not pushed to remote; git push before --release"); return 1
        tag = f"{prefix}-{episode}"
        notes = f"Rendered audio of {episode} (content {commit[:12]}). Verify and install with tools/fetch_renders.py."
        if subprocess.run(["gh", "release", "view", tag], capture_output=True).returncode == 0:
            subprocess.run(["gh", "release", "upload", tag, str(out), "--clobber"], check=True)
        else:
            subprocess.run(["gh", "release", "create", tag, str(out), "--title", tag, "--notes", notes], check=True)
        print(f"released {tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
