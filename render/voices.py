"""Voices: reference clips (voice key -> clip + ref_text + refVersion) and casting (show/role -> voice key).

voices.json: the pool (clip + transcript + language + gender). casting/<show>.json (casting.py): character -> voice,
persisted in git. Scripts have no `voices` map (content contract P-1); nothing else decides a voice.
"""
import hashlib
import json
from pathlib import Path

import casting
import config


class VoiceError(Exception):
    pass


class Voices:
    def __init__(self, path=None):
        self.path = Path(path or config.VOICES_FILE)
        d = json.loads(self.path.read_text(encoding="utf-8"))
        self.refs = d["refs"]
        self.base = self.path.parent

    def ref_path(self, key) -> Path:
        return self.base / self.refs[key]["file"]

    def ref_version(self, key) -> str:
        r = self.refs[key]
        h = hashlib.sha256()
        h.update(self.ref_path(key).read_bytes())
        h.update(r["text"].encode("utf-8"))
        return h.hexdigest()[:8]

    def voices_version(self) -> str:
        return hashlib.sha256(json.dumps({k: self.ref_version(k) for k in sorted(self.refs)}).encode()).hexdigest()[:8]

    def resolve(self, scene) -> dict:
        """role -> voice key for every role used in the scene, from casting/<show>.json (narrator: its `narrator`).
        Raises VoiceError for an uncast character. Scripts carry no voices map any more."""
        doc = casting.load(scene.show)
        if not doc:
            raise VoiceError(f"no casting/{scene.show}.json")
        out = {}
        for seg in scene.script["segments"]:
            role = seg["v"]
            if role in out:
                continue
            if role == "narrator":
                key = doc["narrator"]
            else:
                ch = doc["characters"].get(role)
                if not ch:
                    raise VoiceError(f"character {role!r} is not cast in casting/{scene.show}.json")
                key = ch["voice"]
            if key not in self.refs:
                raise VoiceError(f"role {role!r} -> voice {key!r} has no reference clip in voices.json")
            out[role] = key
        return out

    def lang_of(self, key) -> str:
        return self.refs[key]["lang"]
