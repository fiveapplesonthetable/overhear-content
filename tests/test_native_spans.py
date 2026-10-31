"""Native lexical boundaries are authored code-point spans, never fabricated acoustic times."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from word_spans import annotation_spans, source_audio_metadata
import validate as v


class NativeSpans(unittest.TestCase):
    def test_real_mandarin_phrase_preserves_unspaced_compounds(self):
        text = '那你怎么不先进去啊？'
        edges = [(0, 1), (1, 2), (2, 4), (4, 5), (5, 6), (6, 8), (8, 9)]
        words = [{'t': text[a:b], 'span': [a, b]} for a, b in edges]
        self.assertEqual(annotation_spans(text, words, required=True), edges)
        self.assertEqual(text, '那你怎么不先进去啊？')

    def test_legacy_latin_annotation_keeps_whitespace_behavior(self):
        self.assertIsNone(annotation_spans("J'ai l'addition, merci.", [{'t': s} for s in "J'ai l'addition, merci.".split()]))

    def test_code_points_are_not_utf16_units(self):
        self.assertEqual(annotation_spans('𠀀学校。', [{'t': '𠀀', 'span': [0, 1]}, {'t': '学校', 'span': [1, 3]}], True), [(0, 1), (1, 3)])
        with self.assertRaises(ValueError): annotation_spans('𠀀学校。', [{'t': '𠀀', 'span': [0, 2]}], True)

    def test_arabic_marks_stay_with_their_written_word(self):
        text = 'كَتَبَ، نعم.'
        self.assertEqual(annotation_spans(text, [{'t': 'كَتَبَ', 'span': [0, 6]}, {'t': 'نعم.', 'span': [8, 12]}]), [(0, 6), (8, 12)])
        with self.assertRaises(ValueError): annotation_spans('كَ', [{'t': 'ك', 'span': [0, 1]}])

    def test_gaps_partial_annotations_overlaps_and_wrong_text_are_rejected(self):
        for words in [[{'t': '学校', 'span': [2, 4]}], [{'t': '今日', 'span': [0, 2]}, {'t': '学校'}],
                      [{'t': '今日学', 'span': [0, 3]}, {'t': '学校', 'span': [2, 4]}], [{'t': '今日', 'span': [0, 4]}]]:
            with self.subTest(words=words), self.assertRaises(ValueError): annotation_spans('今日学校', words, True)

    def test_native_readings_required_and_stress_not_invented(self):
        word = {'t': '银行', 'span': [0, 2], 'reading': 'yín háng', 'lemma': '银行', 'pos': 'name', 'stress': None, 'gloss': 'bank', 'gram': 'noun'}
        doc = {'schemaVersion': 1, 'id': 'behind-the-scenes-s01e01-scene-01', 'lines': [{'seg': 0, 'trans': 'A bank.', 'words': [word]}], 'lexicon': {}}
        script = {'id': doc['id'], 'segments': [{'v': 'person', 't': '银行。'}]}
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'notes.json'
            path.write_text(json.dumps(doc, ensure_ascii=False))
            rep = v.Report(); v.check_notes(path, script, 'zh', True, rep)
            self.assertEqual(rep.errors, [])
            doc['lines'][0]['words'][0].pop('reading')
            path.write_text(json.dumps(doc, ensure_ascii=False))
            rep = v.Report(); v.check_notes(path, script, 'zh', True, rep)
            self.assertTrue(any('reviewed spoken reading' in str(e) for e in rep.errors))
        rep = v.Report(); v.check_stress('ja', '学校', 'がっこう', 'fixture', rep)
        self.assertTrue(any('stress must be null' in str(e) for e in rep.errors))

    def test_private_source_metadata_is_portable_and_bounded(self):
        value = {'file': 'sources/al-maktab/s01/e01.mp4', 'sha256': 'a' * 64, 'start': 12.5, 'end': 14.2}
        self.assertEqual(source_audio_metadata(value), value)
        for patch in [{'file': '/mnt/private/source.mp4'}, {'file': 'sources/../../private.mp4'}, {'file': 'sources/a/./x.mp4'},
                      {'file': 'sources/a//x.mp4'}, {'sha256': 'wrong'}, {'end': 12.5}, {'start': -1}, {'end': float('inf')}]:
            with self.subTest(patch=patch), self.assertRaises(ValueError): source_audio_metadata({**value, **patch})


if __name__ == '__main__': unittest.main()
