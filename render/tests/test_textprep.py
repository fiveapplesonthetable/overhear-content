import re
import textprep as tp

ACUTE = "́"


def test_split_matches_compose_regex():
    # content repo compose.py regex: (?<=[.!?…])\s+
    rx = re.compile(r"(?<=[.!?…])[\s]+")
    for t in ["Привет! Как дела? Хорошо.", "Один.", "Вот… и всё. Да!", "  Пока!  ", "Где мой нож? Не знаю!  Ищи."]:
        want = [p.strip() for p in rx.split(t.strip()) if p.strip()] or [t]
        assert [s.strip() for _, _, s in tp.split_sentences(t)] == want


def test_split_offsets():
    t = "Привет! Как дела?"
    for a, b, s in tp.split_sentences(t):
        assert t[a:b] == s


def _words(text, stresses):
    return [{"t": tok, "stress": st} for tok, st in zip(text.split(), stresses)]


def test_stress_injection_all():
    text = "Девушка, с вами всё в порядке?"
    words = _words(text, ["Де" + ACUTE + "вушка", None, "ва" + ACUTE + "ми", None, None, "поря" + ACUTE + "дке"])
    (s,) = tp.prepare_segment(0, "anya", text, "ru", words, "all", 0.5, 0.5)
    assert s.plain == text
    assert s.tts == "Де" + ACUTE + "вушка, с ва" + ACUTE + "ми всё в поря" + ACUTE + "дке?"
    assert tp.strip_acute(s.tts) == text


def test_acute_only_from_stress_field():
    text = "Он сказал слово замок."
    words = _words(text, [None, None, None, "за" + ACUTE + "мок"])
    (s,) = tp.prepare_segment(0, "x", text, "ru", words, "all", 0.5, 0.5)
    assert s.tts.count(ACUTE) == 1
    (s0,) = tp.prepare_segment(0, "x", text, "ru", words, "none", 0.5, 0.5)
    assert ACUTE not in s0.tts
    # French and English are never marked
    (f,) = tp.prepare_segment(0, "x", "Bonjour", "fr", [{"t": "Bonjour", "stress": "bɔ̃ʒuʁ"}], "all", 0.5, 0.5)
    assert f.tts == "Bonjour"


def test_homograph_policy_marks_only_homographs():
    tp._HOMOGRAPHS = frozenset({"замок"})
    text = "Девушка, повесила замок."
    words = _words(text, ["Де" + ACUTE + "вушка", "пове" + ACUTE + "сила", "за" + ACUTE + "мок"])
    (s,) = tp.prepare_segment(0, "x", text, "ru", words, "homographs", 0.5, 0.5, hom=tp._HOMOGRAPHS)
    assert s.tts == "Девушка, повесила за" + ACUTE + "мок."
    tp._HOMOGRAPHS = None


def test_mark_with_punctuation_and_capital():
    off = tp.acute_offsets("«Де́вушка,»".replace(ACUTE, ""), "Де" + ACUTE + "вушка")
    assert off == [3]


def test_sentence_marks_follow_split():
    text = "Привет! Как дела?"
    words = _words(text, ["Приве" + ACUTE + "т!", "Как", "дела" + ACUTE + "?"])
    ss = tp.prepare_segment(3, "x", text, "ru", words, "all", 0.7, 0.5)
    assert [s.tts for s in ss] == ["Приве" + ACUTE + "т!", "Как дела" + ACUTE + "?"]
    assert [s.gap for s in ss] == [0.5, 0.7]


def test_missing_marks_reported_and_ruaccent_fallback_only_for_missing():
    text = "Лёва любит Андрея."
    words = _words(text, [None, "лю" + ACUTE + "бит", None])
    calls = []

    def fake(sents):
        calls.append(sents)
        return ["Лёва лю" + ACUTE + "бит Андре" + ACUTE + "я."]

    (s,) = tp.prepare_segment(0, "x", text, "ru", words, "all", 0.5, 0.5, ruaccent=fake)
    assert calls and s.missing == []
    assert s.tts == "Лёва лю" + ACUTE + "бит Андре" + ACUTE + "я."   # Лёва (ё) never marked, notes mark kept once


def test_standalone_poka_carries_its_stress_mark_so_the_cache_key_follows_the_respelling():
    for text, marked in (("Пока!", "Пока" + ACUTE + "!"), ("Пока.", "Пока" + ACUTE + "."), ("Пока", "Пока" + ACUTE)):
        (s,) = tp.prepare_segment(0, "max", text, "ru", [], "homographs", 0.3, 0.5)
        assert (s.plain, s.tts) == (text, marked)
    for text in ("Ну пока, Даня!", "Привет!"):                      # only a sentence that is the word alone
        (s,) = tp.prepare_segment(0, "max", text, "ru", [], "homographs", 0.3, 0.5)
        assert s.tts == text
