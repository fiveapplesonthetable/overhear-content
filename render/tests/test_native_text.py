"""Acoustic aggregation tests use explicitly synthetic CTC frames, never claimed real speech times."""
import json
from pathlib import Path
from types import SimpleNamespace

import pytest
import native_text as nt
import textprep

CASES = json.loads((Path(__file__).parent / 'fixtures/native-text.json').read_text())


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['lang'])
def test_actual_native_source_units_have_complete_traceable_mms_targets(case):
    words = nt.words_for_segment(case['text'], case['words'], case['lang'])
    plan = nt.targets(case['text'], case['lang'], words)
    assert len(plan.letters) == len(plan.owners) > 0
    assert set(plan.owners) == set(range(len(words)))
    assert all(case['text'][word.start:word.end] == word.text for word in words)
    assert all(letter in "abcdefghijklmnopqrstuvwxyz'" for letter in plan.letters)
    spans = [SimpleNamespace(start=i * 2, end=i * 2 + 1, score=.9) for i in range(len(plan.letters))]
    timed = nt.aggregate(plan, spans, .02, (len(spans) * 2 + 1) * .02)
    assert [w['span'] for w in timed] == [[word.start, word.end] for word in words]
    assert len(timed) == len(words) and all(w['ok'] for w in timed)
    # A compound receives its complete acoustic target interval, never equal character subdivisions.
    for i, word in enumerate(timed):
        owned = [s for s, owner in zip(spans, plan.owners) if owner == i]
        assert word['s'] == min(s.start for s in owned) * .02
        assert word['e'] == max(s.end for s in owned) * .02


def test_incomplete_acoustics_and_unknown_numbers_fail_instead_of_interpolating():
    words = nt.words_for_segment('학교', [{'t': '학교', 'span': [0, 2]}], 'ko')
    plan = nt.targets('학교', 'ko', words)
    with pytest.raises(nt.NativeAlignmentError, match='span count'):
        nt.aggregate(plan, [], .02, 1)
    words = nt.words_for_segment('今天3点', [{'t': '今天3点', 'span': [0, 4], 'reading': 'jin tian 3 dian'}], 'zh')
    with pytest.raises(nt.NativeAlignmentError, match='unresolved MMS target'):
        nt.targets('今天3点', 'zh', words)


def test_reviewed_japanese_context_does_not_use_chinese_kanji_readings():
    words = nt.words_for_segment('今日', [{'t': '今日', 'span': [0, 2], 'reading': 'キョウ'}], 'ja')
    assert ''.join(nt.targets('今日', 'ja', words).letters) == 'kyou'
    with pytest.raises(nt.NativeAlignmentError): nt.words_for_segment('今日', [{'t': '今日', 'span': [0, 2]}], 'ja')


def test_arabic_presentation_forms_and_marks_keep_exact_logical_source_owners():
    text = 'ﻻ كَتَبَ'
    words = nt.words_for_segment(text, [{'t': 'ﻻ', 'span': [0, 1]}, {'t': 'كَتَبَ', 'span': [2, 8]}], 'ar')
    plan = nt.targets(text, 'ar', words)
    assert ''.join(plan.letters) == 'lakataba'
    assert plan.words[0].text == 'ﻻ' and plan.words[1].text == 'كَتَبَ'


def test_native_sentence_boundaries_preserve_punctuation_quotes_and_offsets():
    for text, expected in [('「行こう。」次です。', ['「行こう。」', '次です。']), ('你好！再见。', ['你好！', '再见。']), ('كيف حالك؟ أنا بخير.', ['كيف حالك؟', 'أنا بخير.'])]:
        result = textprep.split_sentences(text)
        assert [sentence for _, _, sentence in result] == expected
        assert all(text[start:end] == sentence for start, end, sentence in result)
