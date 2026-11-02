"""Light-weight planning shared by the CLI (system python, no numpy/torch) and the worker."""
import hashlib
import json

import config
from voices import Voices, VoiceError


def check_voices(scene, voices: Voices):
    """role -> voice key, or raises VoiceError. A target-language voice must speak the scene's language."""
    roles = voices.resolve(scene)
    for role, key in roles.items():
        vl = voices.lang_of(key)
        if vl not in (scene.lang, "en"):
            raise VoiceError(f"role {role!r} -> voice {key!r} speaks {vl}, scene is {scene.lang}")
        if role == "narrator" and vl != "en":
            raise VoiceError(f"narrator voice {key!r} is not English")
    return roles


def render_key(scene, voices: Voices, settings, roles=None) -> str:
    roles = roles or check_voices(scene, voices)
    native = {}
    if scene.lang in ("ja", "zh", "ko", "ar"):
        from native_text import VERSION
        native = {"nativeAlignment": VERSION}
    return config.sha({
        "contentHash": scene.content_hash,
        "tts": config.tts_signature(settings),
        "assembly": config.assembly_signature(settings),
        "voices": {r: [k, voices.ref_version(k)] for r, k in sorted(roles.items())},
        **native,
    })


def estimate_seconds(scene, cps=None):
    """Rough audio length from characters (target ~14 chars/s of speech plus the scene's gaps)."""
    cps = cps or 14.0
    chars = scene.chars()
    gaps = sum(float(g.get("gap", 0) or 0) for g in scene.script["segments"])
    return chars / cps + gaps


def cache_key(settings, voice, ref_version, lang, text):
    sig = config.sentence_signature(settings, lang)
    blob = json.dumps({"sig": sig, "voice": voice, "ref": ref_version, "lang": lang, "text": text}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def plausible(text_plain, seconds):
    """A cloned sentence that is far too long (babble/loop) or too short (dropped words) is retried."""
    n = len(text_plain.strip())
    return (0.25 + n / 32.0) <= seconds <= (0.8 + n / 4.5)


def voice_clashes(roles):
    """Voice keys used by more than one role of a scene (should not happen: casting avoids it where the pool allows)."""
    by = {}
    for r, k in roles.items():
        by.setdefault(k, []).append(r)
    return {k: rs for k, rs in by.items() if len(rs) > 1}
