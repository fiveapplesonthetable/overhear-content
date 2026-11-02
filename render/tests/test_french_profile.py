"""The French production profile changes only its English synthesis engine."""
import config
import plan


def test_french_profile_keeps_default_configuration_and_native_keys():
    default = config.load_settings()
    french = config.load_settings(config.HERE / "settings.fr-qwen-en.json")
    assert config.en_engine(default)["engine"] == "f5"
    assert config.en_engine(french) is None
    assert french["lora"]["enabled"] is False
    assert {k: v for k, v in french.items() if k != "_note"} == {
        k: v for k, v in default.items() if k not in ("_note", "ttsEn")
    }
    for lang, text in [("fr", "Je peux vous donner mes papiers ?"), ("ru", "Привет, как дела?")]:
        assert plan.cache_key(default, "voice", "ref", lang, text) == plan.cache_key(
            french, "voice", "ref", lang, text)
    assert plan.cache_key(default, "sky", "ref", "en", "Tell the truth.") != plan.cache_key(
        french, "sky", "ref", "en", "Tell the truth.")
    assert config.assembly_signature(default) == config.assembly_signature(french)
