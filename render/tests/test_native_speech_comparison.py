import pytest

from audit_speech_batch import normalized


@pytest.mark.parametrize(('lang', 'expected', 'different'), [
    ('es', 'año', 'ano'), ('es', 'sí', 'si'),
    ('de', 'schön', 'schon'), ('de', 'für', 'fur'),
    ('pt', 'avô', 'avó'), ('pt', 'mãe', 'mae'), ('pt', 'pôde', 'pode'),
    ('it', 'è', 'e'), ('ja', 'が', 'か'), ('ja', 'バ', 'ハ'),
    ('zh', '问', '间'), ('ko', '발', '팔'), ('ar', 'ألم', 'الم'),
])
def test_native_spelling_distinctions_are_not_silent_asr_acceptances(lang, expected, different):
    assert normalized(expected, lang) != normalized(different, lang)


def test_arabic_optional_vowels_do_not_destroy_words_or_hamza():
    assert normalized('رَاتِب', 'ar') == normalized('راتب', 'ar')
    assert normalized('أَلَم', 'ar') != normalized('الم', 'ar')


def test_legacy_french_accent_review_policy_stays_unchanged():
    assert normalized('Noémie', 'fr') == normalized('Noemie', 'fr')
