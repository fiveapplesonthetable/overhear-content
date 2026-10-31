"""Explicit bounded excerpts must not weaken whole-episode or source-integrity gates."""
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import validate as v


class TasterContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.ep = self.root / 'out/kukhnya/s01e01'
        self.ep.mkdir(parents=True)
        self.source = self.root / 'sources/kukhnya/s01/e01.ru.srt'
        self.source.parent.mkdir(parents=True)
        self.source.write_text('\n\n'.join(f'{n}\n00:00:{n*2-1:02d},000 --> 00:00:{n*2:02d},000\nПривет {n}.' for n in range(1, 6)))
        self.cue = v.parse_srt(self.source)
        self.doc = {'schemaVersion': 1, 'show': 'kukhnya', 'season': 1, 'episode': 1,
                    'title': None, 'scenes': [{'scene': 1, 'start': '00:00:03,000', 'end': '00:00:08,000',
                    'title': 'Opening taster', 'summary': 'A colleague greets a visitor.', 'characters': [],
                    'location': 'Kitchen', 'merge': None}], 'coverage': {'type': 'excerpt', 'start': '00:00:03,000',
                    'end': '00:00:08,000', 'sourceSha256': hashlib.sha256(self.source.read_bytes()).hexdigest(),
                    'reason': 'One bounded taster; remaining episode is not published.'}}
        self.script = {'source': {'file': 'sources/kukhnya/s01/e01.ru.srt', 'lines': [{'cue': 2}]}}
        (self.ep / 'scene-01.json').write_text('{}')
        (self.ep / 'scene-01.png').write_bytes(b'fixture')

    def tearDown(self):
        self.tmp.cleanup()

    def errors(self):
        (self.ep / 'scenes.json').write_text(json.dumps(self.doc))
        rep = v.Report()
        with patch.object(v, 'ROOT', self.root), patch.object(v, 'check_script', return_value=self.script), patch.object(v, 'load_cast', return_value={}):
            v.check_scenes(self.ep, 'kukhnya', rep)
        return rep.errors

    def test_excerpt_passes_with_original_outside_cues_retained(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(len(v.parse_srt(self.source)), 5)

    def test_missing_declaration_keeps_full_episode_gate(self):
        del self.doc['coverage']
        errors = self.errors()
        self.assertTrue(any('whole episode' in e for e in errors))
        self.assertTrue(any('episode subtitles run to' in e for e in errors))

    def test_hash_binds_exact_source_bytes(self):
        self.source.write_text(self.source.read_text() + '\n')
        self.assertTrue(any('sourceSha256' in e for e in self.errors()))

    def test_missing_hash_cannot_bypass_gate(self):
        del self.doc['coverage']['sourceSha256']
        self.assertTrue(any('sourceSha256' in e for e in self.errors()))

    def test_bad_or_empty_scope_fails(self):
        for start, end in [('00:00:08,000', '00:00:03,000'), ('00:00:11,000', '00:00:12,000'), ('00:99:03,000', '00:99:08,000')]:
            with self.subTest(start=start, end=end):
                self.doc['coverage'].update(start=start, end=end)
                self.assertTrue(self.errors())

    def test_scope_cannot_cut_through_a_cue(self):
        self.doc['coverage']['start'] = '00:00:03,500'
        self.doc['scenes'][0]['start'] = '00:00:03,500'
        self.assertTrue(any('cut through' in e for e in self.errors()))

    def test_scenes_and_citations_cannot_escape_declared_scope(self):
        self.doc['scenes'][0]['start'] = '00:00:01,000'
        self.assertTrue(any('extends outside' in e for e in self.errors()))
        self.doc['scenes'][0]['start'] = '00:00:03,000'
        self.script['source']['lines'][0]['cue'] = 1
        self.assertTrue(any('outside the declared excerpt' in e for e in self.errors()))

    def test_same_cue_number_in_another_file_cannot_substitute_for_hashed_source(self):
        self.script['source']['file'] = 'sources/kukhnya/s01/other.ru.srt'
        self.assertTrue(any('hashed coverage subtitle file' in e for e in self.errors()))

    def test_uncovered_internal_cue_and_early_scene_end_still_fail(self):
        self.doc['scenes'][0]['end'] = '00:00:04,000'
        errors = self.errors()
        self.assertTrue(any('outside every scene' in e for e in errors))
        self.assertTrue(any('last scene ends' in e for e in errors))

    def test_art_and_script_checks_remain_required(self):
        (self.ep / 'scene-01.png').unlink()
        self.assertTrue(any('missing art' in e for e in self.errors()))
        (self.ep / 'scene-01.json').unlink()
        self.assertTrue(any('missing scene-01.json' in e for e in self.errors()))

    def test_unknown_coverage_kind_and_fields_rejected(self):
        self.doc['coverage']['type'] = 'complete'
        self.assertTrue(any('coverage' in e for e in self.errors()))
        self.doc['coverage']['type'] = 'excerpt'
        self.doc['coverage']['ignoreErrors'] = True
        self.assertTrue(any('ignoreErrors' in e for e in self.errors()))

    def test_seven_show_and_pair_registration_does_not_accept_unknown_show(self):
        expected = {'die-discounter':'de', 'paquita-salas':'es', 'boris':'it', 'the-producers':'ko',
                    'the-naked-director':'ja', 'behind-the-scenes':'zh', 'al-maktab':'ar'}
        for show, lang in expected.items():
            with self.subTest(show=show):
                self.assertEqual(v.SHOWS[show], lang)
                self.assertEqual(v.PAIR[lang], lang + '-en')
                sch = v.load_schema('script')
                for key, value in [('id', show+'-s01e01-scene-01'), ('pair', lang+'-en'), ('show', show)]:
                    self.assertEqual(v.schema_errors(value, sch['properties'][key], sch), [])
        self.assertTrue(v.schema_errors('invented-s01e01-scene-01', sch['properties']['id'], sch))

    def test_new_native_scripts_must_actually_contain_native_text(self):
        for lang, text in [('ja', 'またね。'), ('zh', '再见。'), ('ko', '또 봐요.'), ('ar', 'مع السلامة.')]:
            with self.subTest(lang=lang):
                rep = v.Report(); v.target_ok(lang, text, 'native', rep)
                self.assertEqual(rep.errors, [])
                rep = v.Report(); v.target_ok(lang, 'Translated English only.', 'native', rep)
                self.assertTrue(any('native-script' in e for e in rep.errors))
