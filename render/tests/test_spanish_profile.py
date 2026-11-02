"""Spanish renderer registration/profile checks without synthesis or model imports."""
import json

import casting
import config
import content
import plan
import pytest
from voices import VoiceError, Voices


def test_spanish_profile_uses_base_qwen_and_requires_honest_native_references():
    default = config.load_settings()
    spanish = config.load_settings(config.HERE / "settings.es-qwen-en.json")
    assert spanish["lora"]["enabled"] is False
    assert config.en_engine(spanish) is None
    assert spanish["tts"]["languages"]["es"] == "Spanish"
    assert spanish["audio"]["interSentenceGap"]["es"] == 0.5
    assert spanish["clips"]["voices"] == spanish["forms"]["voices"] == {}
    assert spanish["priority"] == [["paquita-salas", 1]]
    assert "es" not in default["tts"]["languages"]
    assert "es" not in default["audio"]["interSentenceGap"]
    for lang, text in [("ru", "Привет!"), ("fr", "Bonjour.")]:
        assert plan.cache_key(spanish, "voice", "ref", lang, text) == plan.cache_key(default, "voice", "ref", lang, text)


def test_spanish_scene_is_discovered_but_never_uses_a_french_or_russian_voice(tmp_path, monkeypatch):
    monkeypatch.setattr(casting, "DIR", tmp_path / "casting")
    ep = tmp_path / "out/paquita-salas/s01e01"
    ep.mkdir(parents=True)
    sid = "paquita-salas-s01e01-scene-01"
    (ep / "scene-01.json").write_text(json.dumps({"id": sid, "pair": "es-en", "segments": [
        {"v": "narrator", "t": "Listen for the word for year.", "gap": 0.3},
        {"v": "test", "t": "Año.", "gap": 0.3}]}))
    (ep / "scene-01.notes.json").write_text(json.dumps({"lines": []}))
    (ep.parent / "cast.json").write_text(json.dumps({"cast": [{"key": "test", "ru": "Test", "en": ["Test"], "gender": "f"}]}))
    scenes, skips = content.discover(tmp_path)
    assert skips == [] and len(scenes) == 1 and scenes[0].lang == "es"
    voices = Voices()
    voices.refs = {k: r for k, r in voices.refs.items() if r["lang"] != "es"}
    doc, new = casting.extend("paquita-salas", scenes[0].cast, scenes, voices, "es")
    assert doc["characters"] == {} and new == []
    casting.save(doc)
    with pytest.raises(VoiceError):
        plan.check_voices(scenes[0], voices)
