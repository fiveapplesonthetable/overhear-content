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
import hashlib, io, json, subprocess, sys, tarfile, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_render as cr

ROOT = Path(__file__).resolve().parents[1]


def episode_files(store, content, episode):
    """-> (scene ids, [relative paths], [plan rows]) of one episode."""
    scenes = [s for s in cr.scenes_of(content, episode=episode) if not s[3]]
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
    args = [a for a in argv if not a.startswith("--")]
    if "--episode" not in argv or len(args) < 2:
        print(__doc__); return 2
    store = Path(args[0]).resolve()
    episode = argv[argv.index("--episode") + 1]
    content = Path(argv[argv.index("--content") + 1]).resolve() if "--content" in argv else ROOT
    if cr.main([str(store), "--episode", episode, "--content", str(content)]) != 0:
        print(f"{episode}: tools/check_render.py fails; not packaged"); return 1
    scenes, files, plan = episode_files(store, content, episode)
    commit = subprocess.run(["git", "-C", str(content), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    manifest = {"schemaVersion": 1, "episode": episode, "contentCommit": commit,
                "packagedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "scenes": [{"sceneId": s, **{k: json.loads((store / s / "meta.json").read_text(encoding="utf-8"))[k]
                                             for k in ("contentHash", "audioSha256", "durationSec")}} for s in scenes],
                "files": {f: cr.sha256_file(store / f) for f in files}}
    plan_b = json.dumps(plan, ensure_ascii=False).encode("utf-8")
    manifest["files"][f"forms-plan/{episode}.json"] = hashlib.sha256(plan_b).hexdigest()
    out = ROOT / "dist" / f"render-{episode}.tar"
    out.parent.mkdir(exist_ok=True)
    with tarfile.open(out, "w") as tar:
        for f in files:
            tar.add(store / f, arcname=f)
        for name, data in ((f"forms-plan/{episode}.json", plan_b),
                           ("MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=1).encode("utf-8"))):
            info = tarfile.TarInfo(name); info.size = len(data); info.mtime = int(time.time())
            tar.addfile(info, io.BytesIO(data))
    print(f"{out}: {len(scenes)} scenes, {len(files)} files, {out.stat().st_size / 1e6:.1f} MB")
    if "--release" in argv:
        tag = f"render-{episode}"
        notes = f"Rendered audio of {episode} (content {commit[:12]}). Verify and install with tools/fetch_renders.py."
        if subprocess.run(["gh", "release", "view", tag], capture_output=True).returncode == 0:
            subprocess.run(["gh", "release", "upload", tag, str(out), "--clobber"], check=True)
        else:
            subprocess.run(["gh", "release", "create", tag, str(out), "--title", tag, "--notes", notes], check=True)
        print(f"released {tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
