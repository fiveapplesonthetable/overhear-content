#!/usr/bin/env python3
"""Installs episode packages (tools/package_render.py) into a render directory, verifying everything first. Python 3 stdlib only (+ `gh`).

  python3 tools/fetch_renders.py RENDER_DIR --tar dist/render-kukhnya-s01e01.tar     # a local package
  python3 tools/fetch_renders.py RENDER_DIR --episode kukhnya-s01e01                 # download GitHub release render-<episode>
  python3 tools/fetch_renders.py RENDER_DIR --all                                    # every render-* release
  options: --content DIR  content checkout to verify against (default: this repo; check it out at the commit the packages name)

A package is installed only when every file matches MANIFEST.json, every scene's contentHash equals sha256(script + notes) of the
content checkout, and the tarball has no path outside the layout. The episode's form-plan rows are merged into
RENDER_DIR/forms/.plan.json (same id: the package wins). Then tools/check_render.py --episode runs on the installed result.
"""
import hashlib, json, re, subprocess, sys, tarfile, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_render as cr

ROOT = Path(__file__).resolve().parents[1]
SAFE = re.compile(r"^(?:[a-z][a-z0-9-]*-s\d\de\d\d-scene-\d\d/(?:audio\.mp3|spans\.json|timing\.json|meta\.json|report\.json)"
                  r"|(?:clips|forms)/[0-9a-f]{16}\.(?:json|mp3)|forms-plan/[a-z][a-z0-9-]*-s\d\de\d\d\.json|MANIFEST\.json)$")


def read_package(tar_path):
    """{name: bytes} of a package. Regular files, plus hardlinks (older packages store byte-identical clips that way) whose
    target is a regular file of the package; names and link targets must both fit the layout."""
    with tarfile.open(tar_path) as tar:
        members = tar.getmembers()
        regular = {m.name for m in members if m.isfile()}
        for m in members:
            if not SAFE.match(m.name):
                raise SystemExit(f"{tar_path}: unexpected member {m.name!r}")
            if m.islnk():
                if not SAFE.match(m.linkname) or m.linkname not in regular:
                    raise SystemExit(f"{tar_path}: unexpected link {m.name!r} -> {m.linkname!r}")
            elif not m.isfile():
                raise SystemExit(f"{tar_path}: unexpected member {m.name!r}")
        by_name = {m.name: m for m in members}
        return {name: tar.extractfile(m.linkname if m.islnk() else name).read() for name, m in by_name.items()}


def install(tar_path, render, content, root=None):
    data = read_package(tar_path)
    man = json.loads(data.pop("MANIFEST.json"))
    ep = man["episode"]
    eff_root = root or man.get("root")
    if set(data) != set(man["files"]):
        raise SystemExit(f"{tar_path}: files differ from MANIFEST.json")
    for name, b in data.items():
        if hashlib.sha256(b).hexdigest() != man["files"][name]:
            raise SystemExit(f"{tar_path}: {name} sha256 mismatch")
    scripts = {s[0]: s for s in cr.scenes_of(content, episode=ep, root=eff_root)}
    for s in man["scenes"]:
        sid = s["sceneId"]
        if sid not in scripts:
            raise SystemExit(f"{tar_path}: {sid} is not a scene of the content checkout")
        _, sp, npth, _ = scripts[sid]
        if cr.content_hash(sp, npth) != s["contentHash"]:
            raise SystemExit(f"{tar_path}: {sid} was rendered from other content (commit {man['contentCommit'][:12]}); check that commit out")
    plan_rows = json.loads(data.pop(f"forms-plan/{ep}.json"))
    for name, b in data.items():
        p = render / name
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(p.name + ".tmp")
        tmp.write_bytes(b)
        tmp.replace(p)
    pf = render / "forms" / ".plan.json"
    pf.parent.mkdir(parents=True, exist_ok=True)
    rows = json.loads(pf.read_text(encoding="utf-8")) if pf.is_file() else []
    merged = {r["id"]: r for r in rows}
    merged.update({r["id"]: r for r in plan_rows})
    tmp = pf.with_name(".plan.json.tmp")
    tmp.write_text(json.dumps(list(merged.values()), ensure_ascii=False), encoding="utf-8")
    tmp.replace(pf)
    print(f"{ep}: installed {len(man['scenes'])} scenes, {len(data)} files")
    return ep


def main(argv):
    render_arg, content, root, tar_arg, episode, do_all = None, ROOT, None, None, None, False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--content": content = Path(argv[i + 1]).resolve(); i += 2; continue
        if a == "--root": root = argv[i + 1]; i += 2; continue
        if a.startswith("--root="): root = a.split("=", 1)[1]; i += 1; continue
        if a == "--tar": tar_arg = Path(argv[i + 1]); i += 2; continue
        if a == "--episode": episode = argv[i + 1]; i += 2; continue
        if a == "--all": do_all = True; i += 1; continue
        if not a.startswith("--") and render_arg is None: render_arg = a
        i += 1
    if render_arg is None:
        print(__doc__); return 2
    render = Path(render_arg).resolve()
    prefix = "original-" if root == "originals" else "render-"
    tars = []
    with tempfile.TemporaryDirectory() as tmp:
        if tar_arg:
            tars = [tar_arg]
        else:
            if do_all:
                listing = subprocess.run(["gh", "release", "list", "--limit", "1000", "--json", "tagName"], capture_output=True, text=True, check=True)
                tags = [r["tagName"] for r in json.loads(listing.stdout) if r["tagName"].startswith(prefix)]
            else:
                m = re.match(r"^([a-z0-9-]+)-s\d\de\d\d$", episode or "")
                ep_prefix = "original-" if (root == "originals" or (root is None and m and (content / "originals" / m.group(1)).is_dir())) else "render-"
                tags = [f"{ep_prefix}{episode}"]
            for tag in tags:
                subprocess.run(["gh", "release", "download", tag, "--dir", tmp, "--pattern", f"{tag}.tar", "--clobber"], check=True)
                tars.append(Path(tmp) / f"{tag}.tar")
        bad = 0
        for t in tars:
            ep = install(t, render, content, root=root)
            chk_args = [str(render), "--episode", ep, "--content", str(content)]
            if root:
                chk_args += ["--root", root]
            bad |= cr.main(chk_args)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
