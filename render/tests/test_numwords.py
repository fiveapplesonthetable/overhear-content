import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import numwords as nw  # noqa: E402


def test_spell_basic():
    assert nw.spell(0) == "ноль"
    assert nw.spell(5, "nom") == "пять"
    assert nw.spell(7, "gen") == "семи"
    assert nw.spell(21, "nom", "f") == "двадцать одна"
    assert nw.spell(22, "nom", "f") == "двадцать две"
    assert nw.spell(10) == "десять"
    assert nw.spell(80, "gen") == "восьмидесяти"
    assert nw.spell(120) == "сто двадцать"
    assert nw.spell(7000) == "семь тысяч"
    assert nw.spell(2000) == "две тысячи"
    assert nw.spell(1000) == "тысяча"
    assert nw.spell(21000) == "двадцать одна тысяча"
    assert nw.spell(15000, "gen") == "пятнадцати тысяч"
    assert nw.spell(345, "ins") == "тремястами сорока пятью"


def test_expand_uses_reference_form():
    assert nw.expand("Дай мне 5 рублей.", "Дай мне пять рублей.") == "Дай мне пять рублей."
    assert nw.expand("Через 10 минут буду.", "Через десять минут буду.") == "Через десять минут буду."
    assert nw.expand("Сейчас 7 часов.", "Сейчас семь часов.") == "Сейчас семь часов."
    assert nw.expand("Осталось 3 минуты.", "Осталось три минуты.") == "Осталось три минуты."
    assert nw.expand("120 на 80, как у космонавта.", "Сто двадцать на восемьдесят, как у космонавта!") == "сто двадцать на восемьдесят, как у космонавта."
    assert nw.expand("Там депозит на 7 000 рублей.", "Там депозит на семь тысяч рублей!").startswith("Там депозит на семь тысяч")


def test_expand_picks_case_of_reference():
    assert nw.expand("Нет 2 минут", "Нет двух минут") == "Нет двух минут"
    assert nw.expand("С 5 людьми", "С пятью людьми") == "С пятью людьми"


def test_no_digits_untouched():
    assert nw.expand("Пять рублей", "Пять рублей") == "Пять рублей"


def test_clip_asr_scores_digits_as_words():
    import clip_asr
    assert clip_asr.folded_cer("Дай мне пять рублей", nw.expand("Дай мне 5 рублей.", "Дай мне пять рублей.")) == 0.0
