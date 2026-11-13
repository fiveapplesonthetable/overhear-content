import config
import textprep as tp
import wordcheck as wc

ACUTE = "́"
HOM = frozenset({"чека", "замок"})
TEXT = "Нет, тут только ручка и три старых чека!"


def _sentence(policy):
    words = [{"t": "ручка", "stress": "ру" + ACUTE + "чка"}, {"t": "чека", "stress": "че" + ACUTE + "ка"}]
    (s,) = tp.prepare_segment(0, "x", TEXT, "ru", words, policy, 0.5, 0.5, hom=HOM)
    return s


def test_wrong_word_fails_and_right_word_passes():
    assert wc.missing(["чека"], "Нет, тут только ручка и три старых чивка.") == ["чека"]
    assert wc.missing(["чека"], "Нет, тут только ручка и три старых чека!") == []


def test_normalisation_ignores_case_yo_marks_and_punctuation():
    assert wc.missing(["Всё", "че́ка"], "ВСЕ, ЧЕКА.") == []
    assert wc.missing(["кто-то"], "кто то пришёл") == []
    assert wc.missing(["чека"], "") == ["чека"]


def test_required_words_are_scoped_homographs_and_marked_words():
    assert wc.required_words(_sentence("onflag"), "homographs", HOM) == ["чека"]
    assert wc.required_words(_sentence("onflag"), "all", HOM) == ["ручка", "чека"]
    assert wc.required_words(_sentence("homographs"), "homographs", HOM) == ["чека"]


def test_onflag_sends_plain_text_but_keeps_the_stress_words():
    s = _sentence("onflag")
    assert s.tts == TEXT and ACUTE not in s.tts
    assert [e[1] for e in s.expected] == ["ручка", "чека"] and not s.missing
    assert ACUTE in _sentence("homographs").tts            # the old behaviour is still available


def test_retake_text_marks_only_the_flagged_word():
    s = _sentence("onflag")
    flagged = [e for e in s.expected if e[1] == "чека"]
    marked = tp.mark_words(s.plain, flagged)
    assert marked == "Нет, тут только ручка и три старых че" + ACUTE + "ка!"
    assert tp.strip_acute(marked) == TEXT


def test_policy_changes_the_render_key_and_not_the_sentence_cache_signature():
    s = config.load_settings(config.HERE / "settings.ru-qwen-lora-en.json")
    old = {**s, "ttsRu": {**s["ttsRu"], "stress": "homographs"}}
    assert s["ttsRu"]["stress"] == "onflag"
    assert config.tts_signature(s) != config.tts_signature(old)
    assert config.sentence_signature(s, "ru") == config.sentence_signature(old, "ru")
