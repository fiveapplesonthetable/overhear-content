"""Ingest overhear-content for rendering: walk out/<show>/sNNeNN/, build Scene objects, say why a scene is skipped.

Deliberately light: the full validator (tools/validate.py) is a publish concern. Here we only check what
rendering needs, and skip (never abort on) anything that cannot be rendered.
"""
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import config

_SCENE_RE = re.compile(r"^scene-(\d\d)\.json$")
_ID_RE = re.compile(r"^([a-z0-9-]+)-s(\d\d)e(\d\d)-scene-(\d\d)$")
LANG_OF_PAIR = {"ru-en": "ru", "fr-en": "fr", "es-en": "es", "de-en": "de", "it-en": "it",
                "ja-en": "ja", "zh-en": "zh", "ko-en": "ko", "ar-en": "ar", "pt-en": "pt"}


@dataclass
class Scene:
    id: str
    show: str
    season: int
    episode: int
    scene: int
    pair: str
    script_path: Path
    script: dict
    notes: dict
    content_hash: str
    lang: str
    cast: dict = field(default_factory=dict)      # role key -> {"gender", "ru"} from out/<show>/cast.json

    @property
    def episode_id(self):
        return f"{self.show}-s{self.season:02d}e{self.episode:02d}"

    def chars(self):
        return sum(len(s.get("t", "")) for s in self.script["segments"])


@dataclass
class Skip:
    id: str
    path: str
    reason: str


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_cast(show_dir: Path):
    """{key: {gender, ru}} from out/<show>/cast.json, or None when missing/unreadable."""
    p = Path(show_dir) / "cast.json"
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        return {c["key"]: {"gender": c["gender"], "ru": c.get("ru")} for c in d["cast"]}
    except Exception:
        return None


def load_scene(script_path: Path, require_notes=True, merged=frozenset(), cast=None):
    """Scene or Skip for one scene-NN.json."""
    m = _SCENE_RE.match(script_path.name)
    sid_guess = f"{script_path.parent.parent.name}-{script_path.parent.name}-scene-{m.group(1)}" if m else script_path.stem
    try:
        raw = script_path.read_bytes()
        script = json.loads(raw.decode("utf-8"))
    except Exception as e:
        return Skip(sid_guess, str(script_path), f"unreadable script: {e}")
    if not isinstance(script, dict):
        return Skip(sid_guess, str(script_path), "script is not an object")
    sid = script.get("id") or sid_guess
    im = _ID_RE.match(sid)
    if not im:
        return Skip(sid_guess, str(script_path), f"bad id {sid!r}")
    show, season, episode, scene = im.group(1), int(im.group(2)), int(im.group(3)), int(im.group(4))
    if sid != sid_guess:
        return Skip(sid, str(script_path), f"id {sid!r} does not match its path ({sid_guess})")
    if (show, season, episode, scene) in merged:
        return Skip(sid, str(script_path), "merged into a neighbour (scenes.json merge)")
    lang = LANG_OF_PAIR.get(script.get("pair"))
    if not lang:
        return Skip(sid, str(script_path), f"unsupported pair {script.get('pair')!r}")
    segs = script.get("segments")
    if not isinstance(segs, list) or not segs:
        return Skip(sid, str(script_path), "no segments")
    for i, g in enumerate(segs):
        if not isinstance(g, dict) or not isinstance(g.get("t"), str) or not g["t"].strip() or not isinstance(g.get("v"), str):
            return Skip(sid, str(script_path), f"segment {i} has no role/text")
        if not isinstance(g.get("gap", 0), (int, float)):
            return Skip(sid, str(script_path), f"segment {i} gap is not a number")
    if cast is None:
        cast = load_cast(script_path.parent.parent)
    if not cast:
        return Skip(sid, str(script_path), f"no cast.json for show {show}")
    for g in segs:
        if g["v"] != "narrator" and g["v"] not in cast:
            rel_cast = f"{script_path.parent.parent.parent.name}/{show}/cast.json"
            return Skip(sid, str(script_path), f"role {g['v']!r} is not in {rel_cast}")
    if "voices" in script:
        return Skip(sid, str(script_path), "script still carries a `voices` map (contract P-1: removed)")
    notes_path = script_path.with_name(script_path.stem + ".notes.json")
    notes_raw = b""
    notes = {"lines": []}
    if notes_path.exists():
        try:
            notes_raw = notes_path.read_bytes()
            notes = json.loads(notes_raw.decode("utf-8"))
        except Exception as e:
            return Skip(sid, str(script_path), f"unreadable notes: {e}")
        if not isinstance(notes, dict) or not isinstance(notes.get("lines"), list):
            return Skip(sid, str(script_path), "notes have no lines[]")
    elif require_notes:
        return Skip(sid, str(script_path), "no notes file (--require-notes)")
    import hashlib
    h = hashlib.sha256(raw + notes_raw).hexdigest()
    return Scene(sid, show, season, episode, scene, script["pair"], script_path, script, notes, h, lang, cast)


def merged_scenes(ep_dir: Path):
    """{(show, season, episode, scene)} marked merge in scenes.json."""
    sj = ep_dir / "scenes.json"
    out = set()
    if not sj.exists():
        return out
    try:
        d = _load(sj)
        for s in d.get("scenes", []):
            if s.get("merge"):
                out.add((d["show"], int(d["season"]), int(d["episode"]), int(s["scene"])))
    except Exception:
        pass
    return out


def _resolve_roots(content_dir=None, root=None):
    import os
    base = Path(content_dir or config.CONTENT_DIR)
    if base.name in ("out", "originals") and not (base / "out").is_dir() and not (base / "originals").is_dir():
        return [base]
    r = root or os.environ.get("OVERHEAR_CONTENT_ROOT") or "out"
    if r == "all":
        return [base / x for x in ("originals", "out") if (base / x).is_dir()]
    return [base / r]


def discover(content_dir=None, require_notes=True, only=None, root=None):
    """(scenes, skips). `only`: optional predicate on (show, season, episode)."""
    roots = _resolve_roots(content_dir, root)
    scenes, skips, casts = [], [], {}
    for rdir in roots:
        if not rdir.is_dir():
            continue
        for show_dir in sorted(p for p in rdir.iterdir() if p.is_dir() and not p.name.startswith("_")):
            for ep_dir in sorted(p for p in show_dir.iterdir() if p.is_dir() and re.match(r"^s\d\de\d\d$", p.name)):
                if only and not only(show_dir.name, int(ep_dir.name[1:3]), int(ep_dir.name[4:6])):
                    continue
                merged = merged_scenes(ep_dir)
                cast = casts.setdefault(show_dir.name, load_cast(show_dir))
                for f in sorted(ep_dir.glob("scene-*.json")):
                    if not _SCENE_RE.match(f.name):
                        continue
                    r = load_scene(f, require_notes, merged, cast or {})
                    (scenes if isinstance(r, Scene) else skips).append(r)
    discover.casts = casts
    return scenes, skips


def priority_key(scene, priority):
    """Sort key: configured (show, season) groups first, in order, then the rest by show/season/episode/scene."""
    try:
        rank = priority.index([scene.show, scene.season])
    except ValueError:
        rank = len(priority)
    return (rank, scene.show if rank == len(priority) else "", scene.season, scene.episode, scene.scene)


def git_commit(content_dir=None):
    import subprocess
    r = subprocess.run(["git", "-C", str(content_dir or config.CONTENT_DIR), "rev-parse", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() or None


def show_dir(content_dir, show, root=None):
    import os
    base = Path(content_dir or config.CONTENT_DIR)
    if base.name in ("out", "originals") and not (base / "out").is_dir() and not (base / "originals").is_dir():
        return base / show
    r = root or os.environ.get("OVERHEAR_CONTENT_ROOT")
    if r and r != "all":
        return base / r / show
    for cand in ("originals", "out"):
        p = base / cand / show
        if p.is_dir():
            return p
    return base / "out" / show


def scene_path(content_dir, sid, root=None):
    m = re.match(r"^([a-z0-9-]+)-s(\d\d)e(\d\d)-scene-(\d\d)$", sid)
    if not m:
        raise ValueError(f"bad scene id {sid!r}")
    return show_dir(content_dir, m.group(1), root=root) / f"s{m.group(2)}e{m.group(3)}" / f"scene-{m.group(4)}.json"
