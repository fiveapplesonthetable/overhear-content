import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import forced_score as fs  # noqa: E402


def test_variants_are_capitalised_and_marked():
    assert fs.variants("белой") == [" Белой.", " Белой!", " Белой?"]


def test_norm_drops_stress_case_and_marks():
    assert fs.norm("Бе́лой.") == "белой"
    assert fs.norm("Чём-нибудь!") == "чем-нибудь"


class FakeScorer(fs.ForcedScorer):
    def __init__(self, table):
        self.table = table

    def score(self, text):
        return self.table[text]

    def score_raw(self, text):
        return self.table[text]


def test_margin_is_reference_minus_best_competitor():
    s = FakeScorer({"белой": -2.0, "белый": -5.0, "белая": -4.0})
    assert s.margin("бе́лой", ["белый", "белая", "белой"]) == 2.0


def test_margin_includes_free_decoding_and_skips_it_when_it_is_the_reference():
    s = FakeScorer({"белой": -2.0, "белый": -5.0, "Белое.": -1.0})
    assert s.margin("белой", ["белый"], heard="Белое.") == -1.0
    assert s.margin("белой", ["белый"], heard="Белой.") == 3.0


def test_folded_cer_hyphenated_compound():
    import clip_asr
    assert clip_asr.folded_cer("кого́-то", "Кого-то.") == 0.0
