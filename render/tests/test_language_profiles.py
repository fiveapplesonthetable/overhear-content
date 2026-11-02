"""Registration consumes the reviewed native pool without changing default speech settings."""
import pytest
import config, plan
from voices import Voices
import casting

@pytest.mark.parametrize('lang,show', [('de','die-discounter'), ('es','paquita-salas'), ('pt','porta-dos-fundos')])
def test_latin_pilot_profiles(lang, show):
    settings = config.load_settings(config.HERE / f'settings.{lang}-qwen-en.json')
    default = config.load_settings()
    assert not settings['lora']['enabled'] and config.en_engine(settings) is None
    assert settings['forms']['voices'] == settings['clips']['voices'] == {}
    assert settings['priority'] == [[show, 1]]
    assert lang not in default['tts']['languages']
    for code,text in [('ru','Привет!'),('fr','Bonjour.')]:
        assert plan.cache_key(settings,'voice','ref',code,text) == plan.cache_key(default,'voice','ref',code,text)


def test_no_voice_ref_is_cut_from_show_audio():
    """Public refs are synthetic (VoiceDesign / voice-lab), ElevenLabs output, or CC0 corpora; never the actors' voices (spec/voices.md)."""
    for key, ref in Voices().refs.items():
        for src in ref.get("source", []):
            assert src.get("kind") != "private-source-conditioning", key
