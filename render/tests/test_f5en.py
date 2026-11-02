"""English narrator engine config: cache-key isolation, trim plan, reference text convention, stage wiring (no GPU)."""
import json

import config
import f5ref
import plan as tts


def _copy(s):
    return json.loads(json.dumps(s))


def test_default_settings_make_f5_the_narrator_engine():
    s = config.load_settings()
    en = config.en_engine(s)
    assert en and en["model"] == "F5TTS_v1_Base" and en["nfe"] == 16
    assert config.engine_label(s, "en") == "f5-tts" and config.engine_label(s, "fr") == "qwen3-tts"
    assert config.sentence_signature(s, "en") == {"en": {k: v for k, v in en.items() if not k.startswith("_")}}


def test_english_key_depends_only_on_ttsEn_voice_ref_text():
    s = config.load_settings()
    k = tts.cache_key(s, "sky", "abcd1234", "en", "Hello there.")
    for edit in (lambda x: x["tts"].update(model="other"), lambda x: x["lora"].update(enabled=True),
                 lambda x: x["ttsRu"].update(nfe=99), lambda x: x["audio"].update(mp3Kbps=64),
                 lambda x: x["tts"].update(batchEn=2), lambda x: x["stress"].update(policy="all")):
        s2 = _copy(s)
        edit(s2)
        assert tts.cache_key(s2, "sky", "abcd1234", "en", "Hello there.") == k
    for edit in (lambda x: x["ttsEn"].update(nfe=32), lambda x: x["ttsEn"].update(cfg=3.0),
                 lambda x: x["ttsEn"].update(refTrim={"sky": {"seconds": 5.0, "text": "When you watch"}})):
        s2 = _copy(s)
        edit(s2)
        assert tts.cache_key(s2, "sky", "abcd1234", "en", "Hello there.") != k
    assert tts.cache_key(s, "theo", "abcd1234", "en", "Hello there.") != k
    assert tts.cache_key(s, "sky", "abcd1235", "en", "Hello there.") != k
    assert tts.cache_key(s, "sky", "abcd1234", "en", "Hello there!") != k


def test_russian_and_french_keys_ignore_ttsEn():
    s = config.load_settings()
    s2 = _copy(s)
    s2["ttsEn"]["nfe"] = 8
    s2["ttsEn"]["model"] = "x"
    for lang in ("ru", "fr"):
        assert tts.cache_key(s, "v", "abcd1234", lang, "Texte.") == tts.cache_key(s2, "v", "abcd1234", lang, "Texte.")
    del s2["ttsEn"]       # without the block English falls back to the Qwen signature
    assert tts.cache_key(s, "sky", "abcd1234", "en", "Hi.") != tts.cache_key(s2, "sky", "abcd1234", "en", "Hi.")
    assert config.en_engine(s2) is None


def test_render_key_changes_with_ttsEn():
    s = config.load_settings()
    s2 = _copy(s)
    s2["ttsEn"]["nfe"] = 32
    assert config.tts_signature(s) != config.tts_signature(s2)


def test_trim_plan():
    cfg = {"refTrim": {"sky": {"seconds": 5.8, "text": "When you watch"}}}
    assert f5ref.trim_plan(cfg, "sky", 8.08, "full text") == (5.8, "When you watch")
    assert f5ref.trim_plan(cfg, "sky", 4.0, "full text") == (4.0, "When you watch")      # never longer than the clip
    assert f5ref.trim_plan(cfg, "theo", 8.0, "full text") == (8.0, "full text")
    assert f5ref.trim_plan({}, "sky", 8.0, "full text") == (8.0, "full text")


def test_ref_text_convention():
    assert f5ref.ref_text_for_f5("Hello there.") == "Hello there. "
    assert f5ref.ref_text_for_f5("  Hello there  ") == "Hello there. "
    assert f5ref.ref_text_for_f5("Really?") == "Really? "


def test_engine_hooks():
    import pytest
    pytest.importorskip("soundfile")
    import f5en
    from espeech import EspeechEngine
    assert (f5en.F5EnEngine.SETTINGS_KEY, f5en.F5EnEngine.LANG_NAME) == ("ttsEn", "English")
    assert (EspeechEngine.SETTINGS_KEY, EspeechEngine.LANG_NAME) == ("ttsRu", "Russian")
    e = f5en.F5EnEngine.__new__(f5en.F5EnEngine)
    assert e.text("  Hello   there. ") == "Hello there."


def test_gpu_reservation_for_english_step():
    s = config.load_settings()
    assert 0 < s["gpu"]["enMiB"] <= 4000


def test_stage_cmd_gpu_reservation_optional():
    import types
    import pipeline
    a = types.SimpleNamespace(content="/c", store="/s", settings=None)
    s = config.load_settings()
    assert pipeline.stage_cmd(a, s, "synth-en", "x", 2400, venv="/v")[:2] == [config.GPURUN, "2400"]
    cmd = pipeline.stage_cmd(a, s, "missing", "x", 0)
    assert cmd[0].endswith("/bin/python") and "missing" in cmd and config.GPURUN not in cmd
