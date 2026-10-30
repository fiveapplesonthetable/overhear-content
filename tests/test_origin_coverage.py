import gzip
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from origin_coverage import covered, inventory, blob_document


class Coverage(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
