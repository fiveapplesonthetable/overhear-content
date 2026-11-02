import json
from pathlib import Path
import config
import content
import plan as tts
from voices import Voices


def test_cache_key_stable_and_sensitive():
    s = config.load_settings()
    k = tts.cache_key(s, "alisa", "abcd1234", "ru", "Привет!")
    assert k == tts.cache_key(s, "alisa", "abcd1234", "ru", "Привет!")
    assert k != tts.cache_key(s, "alisa", "abcd1235", "ru", "Привет!")
    assert k != tts.cache_key(s, "anja", "abcd1234", "ru", "Привет!")
    assert k != tts.cache_key(s, "alisa", "abcd1234", "ru", "Привет.")
    s2 = json.loads(json.dumps(s))
    s2["lora"]["enabled"] = True
    assert tts.cache_key(s, "tom", "abcd1234", "fr", "Salut.") != tts.cache_key(s2, "tom", "abcd1234", "fr", "Salut.")   # French = Qwen settings
    assert tts.cache_key(s, "sky", "abcd1234", "en", "Hello.") == tts.cache_key(s2, "sky", "abcd1234", "en", "Hello.")   # English = ttsEn only
    assert k == tts.cache_key(s2, "alisa", "abcd1234", "ru", "Привет!")      # Russian keys depend on ttsRu only
    s4 = json.loads(json.dumps(s))
    s4["tts"]["model"] = "other/english-model"                                # changing the narrator engine keeps Russian audio
    assert k == tts.cache_key(s4, "alisa", "abcd1234", "ru", "Привет!")
    assert tts.cache_key(s, "tom", "abcd1234", "fr", "Salut.") != tts.cache_key(s4, "tom", "abcd1234", "fr", "Salut.")
    s5 = json.loads(json.dumps(s))
    s5["ttsRu"]["nfe"] = 32
    assert k != tts.cache_key(s5, "alisa", "abcd1234", "ru", "Привет!")
    s3 = json.loads(json.dumps(s))
    s3["audio"]["mp3Kbps"] = 64          # assembly only: sentence cache unaffected
    assert k == tts.cache_key(s3, "alisa", "abcd1234", "ru", "Привет!")


def test_stress_policy_auto():
    s = config.load_settings()
    assert config.stress_policy(s) == "homographs"
    s["lora"]["enabled"] = True
    assert config.stress_policy(s) == "all"


def test_every_voice_has_ref_and_text():
    v = Voices()
    for k, r in v.refs.items():
        assert v.ref_path(k).exists(), k
        assert r["text"].strip() and r["lang"] in set(content.LANG_OF_PAIR.values()) | {"en"}
        assert len(v.ref_version(k)) == 8
