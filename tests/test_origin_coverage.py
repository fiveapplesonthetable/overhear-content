import gzip
import hashlib
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from origin_coverage import covered, inventory, blob_document, completeness


class Coverage(unittest.TestCase):
    def fixture(self, root, pair, entries, histories, scenes=(), articles=None):
        (root / 'meta').mkdir(); (root / f'pairs/{pair}/scenes').mkdir(parents=True)
        (root / 'word-origins').mkdir(); (root / 'gcs/index').mkdir(parents=True)
        def put(name, doc):
            data = gzip.compress(json.dumps(doc).encode())
            (root / 'gcs/index' / name).write_bytes(data)
            return {'url': 'https://example.test/o/index%2F' + name, 'sha256': hashlib.sha256(data).hexdigest()}
        shard = put('words.gz', {'entries': entries})
        manifest = put('manifest.gz', {'lexicon': {'shards': {'00': {'blob': shard}}}, 'learn': articles or {}})
        (root / f'pairs/{pair}/pair.json').write_text(json.dumps({'index': {'manifest': manifest}}))
        (root / 'meta/app.json').write_text(json.dumps({'pairs': [{'id': pair, 'learn': pair[:2], 'from': 'en', 'published': True}]}))
        (root / f'word-origins/{pair}.json').write_text(json.dumps({'entries': histories}))
        for sid, words, published in scenes:
            line = {'lang': pair[:2], **words} if isinstance(words, dict) else {'lang': pair[:2], 'words': words}
            blob = put(sid + '.gz', {'transcript': {'lines': [line]}})
            (root / f'pairs/{pair}/scenes/{sid}.json').write_text(json.dumps({'id': sid, 'published': published, 'content': blob}))

    def source(self):
        return {'etymology': 'A reviewed history.', 'sources': [{'title': 'Specific entry', 'url': 'https://example.test/entry'}]}

    def test_empty_or_unsourced_histories_are_not_counted_as_coverage(self):
        self.assertFalse(covered({'etymology': 'A claim.'}))
        self.assertFalse(covered({'etymology': ' ', 'sources': [{'title': 'x', 'url': 'https://example.test'}]}))
        self.assertTrue(covered({'etymology': 'Origin disputed.', 'certainty': 'uncertain',
                                 'sources': [{'title': 'Specific entry', 'url': 'https://example.test/entry'}]}))

    def test_only_current_manifest_words_enter_the_queue_including_learning_only_pairs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'meta').mkdir(); (root / 'pairs/fr-en').mkdir(parents=True)
            (root / 'word-origins').mkdir(); (root / 'gcs/index').mkdir(parents=True)
            def put(name, doc):
                data = gzip.compress(json.dumps(doc).encode())
                (root / 'gcs/index' / name).write_bytes(data)
                return {'url': 'https://example.test/o/index%2F' + name,
                        'sha256': hashlib.sha256(data).hexdigest()}
            shard = put('current.gz', {'entries': {'je': {'gloss': 'I'}, 'tu': {'gloss': 'you'}}})
            put('obsolete.gz', {'entries': {'old': {'gloss': 'obsolete'}}})
            manifest = put('manifest.gz', {'lexicon': {'shards': {'00': {'blob': shard}}}})
            (root / 'pairs/fr-en/pair.json').write_text(json.dumps({'index': {'manifest': manifest}}))
            (root / 'meta/app.json').write_text(json.dumps({'pairs': [{'id': 'fr-en', 'learn': 'fr', 'published': True}]}))
            (root / 'word-origins/fr-en.json').write_text(json.dumps({'entries': {'je': {'etymology': 'From Latin.',
                'sources': [{'title': 'Entry', 'url': 'https://example.test/je'}]}, 'elsewhere': {}}}))
            report = inventory(root, root)['fr-en']
            self.assertEqual((2, 1, 1), (report['words'], report['covered'], report['missing']))
            self.assertEqual(['tu'], [w['lemma'] for w in report['queue']])
            self.assertEqual(['elsewhere'], report['outsideDictionary'])
            (root / 'gcs/index/current.gz').write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError, 'digest mismatch'):
                blob_document(root, shard)

    def test_every_published_season_is_checked_and_gaps_cannot_pass_strict_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root, 'ru-en', {'я': {'gloss': 'I'}, 'ты': {'gloss': 'you'}}, {'я': self.source()}, scenes=[
                ('show-s01e01-scene-01', [{'t': 'Я', 'lex': 'я'}], True),
                ('show-s02e01-scene-01', [{'t': 'ты', 'lex': 'ты'}, {'t': 'Неизвестное'}], True),
                ('show-s99e01-scene-01', [{'t': 'Draft'}], False),
            ])
            report = inventory(root, root)
            self.assertEqual({'show/s01', 'show/s02'}, set(report['ru-en']['seasons']))
            self.assertEqual(1, report['ru-en']['seasons']['show/s01']['audioScenes'])
            self.assertTrue(completeness(report, 'show/s01'))
            self.assertFalse(completeness(report, 'show/s02'))
            self.assertFalse(completeness(report))
            self.assertEqual(['Неизвестное'], report['ru-en']['seasons']['show/s02']['unresolved'])
            with self.assertRaisesRegex(ValueError, 'Season not found'):
                completeness(report, 'typo/s01')
            cmd = [sys.executable, str(Path(__file__).resolve().parents[1] / 'tools/origin_coverage.py'),
                   '--serving-out', str(root), '--content-dir', str(root), '--require-complete', '--season']
            self.assertEqual(0, subprocess.run(cmd + ['show/s01'], capture_output=True).returncode)
            self.assertEqual(1, subprocess.run(cmd + ['show/s02'], capture_output=True).returncode)

    def test_only_published_learning_notes_enter_their_season_and_elisions_resolve_to_base_words(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entries = {'avoir': {'gloss': 'have', 'surface': ['ai']}, 'nous': {'gloss': 'we'}}
            self.fixture(root, 'fr-en', entries, {w: self.source() for w in entries}, articles={'published': {}})
            (root / 'learn/fr-en').mkdir(parents=True)
            article = {'examples': [{'sceneId': 'french-show-s02e03-scene-01'}],
                       'body': {'en': 'English “you”. French *j’ai* and *nous*.'}}
            (root / 'learn/fr-en/published.json').write_text(json.dumps(article))
            (root / 'learn/fr-en/draft.json').write_text(json.dumps({'examples': [{'sceneId': 'other-s99e01-scene-01'}], 'body': {'en': '*missing*'}}))
            report = inventory(root, root)
            self.assertEqual({'french-show/s02'}, set(report['fr-en']['seasons']))
            self.assertEqual(2, report['fr-en']['seasons']['french-show/s02']['covered'])
            self.assertEqual(0, report['fr-en']['seasons']['french-show/s02']['audioScenes'])
            self.assertEqual(1, report['fr-en']['seasons']['french-show/s02']['learningNotes'])
            self.assertTrue(completeness(report))


if __name__ == '__main__':
    unittest.main()


class NativeLearnCoverage(unittest.TestCase):
    fixture = Coverage.fixture
    source = Coverage.source

    def native_report(self, run, words, entries=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entries = entries or {'你们': {'gloss':'you plural'}, '一起':{'gloss':'together'}, '进去':{'gloss':'go in'}}
            sid = 'behind-the-scenes-s01e01-scene-01'
            self.fixture(root, 'zh-en', entries, {w:self.source() for w in entries},
                scenes=[(sid, {'seg':3,'text':'你们一起进去。','words':words}, True)], articles={'published':{}})
            (root/'learn/zh-en').mkdir(parents=True)
            (root/'learn/zh-en/published.json').write_text(json.dumps({'examples':[{'sceneId':sid,'seg':3}], 'body':{'en':'A reviewed example: *'+run+'*.'}}))
            return inventory(root, root)

    def words(self):
        return [{'t':'你们','lex':'你们','charStart':0,'charEnd':2},
                {'t':'一起','lex':'一起','charStart':2,'charEnd':4},
                {'t':'进去','lex':'进去','charStart':4,'charEnd':6}]

    def test_unspaced_example_resolves_to_actual_published_lexical_owners(self):
        report = self.native_report('你们一起进去', self.words())
        scope = report['zh-en']['seasons']['behind-the-scenes/s01']
        self.assertEqual(scope['unresolved'], [])
        self.assertEqual(scope['words'], 3)
        self.assertTrue(completeness(report))

    def test_no_dictionary_segmentation_is_guessed_without_source_spans(self):
        words = self.words()
        for word in words: del word['charStart']; del word['charEnd']
        report = self.native_report('你们一起进去', words)
        self.assertIn('你们一起进去', report['zh-en']['seasons']['behind-the-scenes/s01']['unresolved'])
        self.assertFalse(completeness(report))

    def test_partial_compound_cannot_be_claimed_as_a_whole_reviewed_word(self):
        report = self.native_report('们一起', self.words())
        self.assertIn('们一起', report['zh-en']['seasons']['behind-the-scenes/s01']['unresolved'])

    def test_wrong_span_and_unmatched_example_remain_unresolved(self):
        words = self.words(); words[0]['charEnd'] = 1
        report = self.native_report('你们一起进去', words)
        self.assertIn('你们一起进去', report['zh-en']['seasons']['behind-the-scenes/s01']['unresolved'])
        report = self.native_report('你们不知道', self.words())
        self.assertIn('你们不知道', report['zh-en']['seasons']['behind-the-scenes/s01']['unresolved'])

    def test_missing_dictionary_owner_is_not_hidden_by_an_example_match(self):
        report = self.native_report('你们一起进去', self.words(), {'你们':{'gloss':'you'},'进去':{'gloss':'go in'}})
        self.assertIn('一起', report['zh-en']['seasons']['behind-the-scenes/s01']['unresolved'])
        self.assertFalse(completeness(report))
