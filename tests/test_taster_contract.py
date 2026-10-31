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
        self.script = {'segments': [{'v': 'narrator', 't': 'Intro.'}, {'v': 'guest', 't': 'Привет 2.'}, {'v': 'narrator', 't': 'Explanation.'}], 'source': {'file': 'sources/kukhnya/s01/e01.ru.srt', 'lines': [{'line': 0, 'cue': 2, 'fragment': 'Привет 2'}]}}
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

    def test_script_punctuation_and_extenders_are_not_native_letters(self):
        for lang, text in [('ja', 'English only・'), ('ja', 'English onlyー'), ('ar', 'English onlyـ')]:
            with self.subTest(lang=lang, text=text):
                rep = v.Report(); v.target_ok(lang, text, 'native', rep)
                self.assertTrue(any('native-script' in e for e in rep.errors))

    def test_excerpt_requires_citations_for_every_original_story_line(self):
        self.script['source']['lines'] = []
        self.assertTrue(any('bind every story line' in e for e in self.errors()))
        self.script['source']['lines'] = [{'line': 0, 'cue': 2, 'fragment': 'Привет 2'}]
        self.script['segments'].insert(2, {'v': 'guest', 't': 'Привет 3.'})
        self.assertTrue(any('without source citations' in e for e in self.errors()))

    def test_excerpt_citation_must_reference_the_actual_story_not_only_a_source_cue(self):
        for line, fragment in [(2, 'Привет 2'), (True, 'Привет 2'), (0, 'Unrelated'), (0, '!!!')]:
            with self.subTest(line=line, fragment=fragment):
                self.script['source']['lines'] = [{'line': line, 'cue': 2, 'fragment': fragment}]
                self.assertTrue(any('excerpt citation' in e for e in self.errors()))

    def short_script(self):
        story = [{'v': 'guest', 't': 'Привет 2.', 'gap': .5}, {'v': 'guest', 't': 'Привет 3.', 'gap': .5}]
        return {'schemaVersion': 1, 'format': 'taster', 'id': 'kukhnya-s01e01-scene-01', 'pair': 'ru-en',
                'show': 'kukhnya', 'season': 1, 'episode': 1, 'scene': 1, 'title': 'Привет  (Hello taster)',
                'level': 'A1 — beginner', 'labels': {'guest': 'Гость'},
                'segments': [{'v': 'narrator', 't': 'A visitor greets a colleague. Listen to the short conversation.', 'gap': .8}]
                    + copy.deepcopy(story)
                    + [{'v': 'narrator', 't': 'Let us go through the exchange.', 'gap': .4},
                       copy.deepcopy(story[0]), {'v': 'narrator', 't': "'Hello.' This is a greeting.", 'gap': .4},
                       copy.deepcopy(story[1]), {'v': 'narrator', 't': "'Hello.' The colleague greets the visitor too. Now listen again.", 'gap': .8}]
                    + copy.deepcopy(story)
                    + [{'v': 'narrator', 't': 'You heard two people greeting each other. See you next time.', 'gap': .5}],
                'source': {'show': 'Kukhnya', 'file': 'sources/kukhnya/s01/e01.ru.srt',
                           'lines': [{'line': 0, 'cue': 2, 'fragment': 'Привет 2'}, {'line': 1, 'cue': 3, 'fragment': 'Привет 3'}]}}

    def short_errors(self, script, excerpt=True):
        p = self.ep / 'short.json'; p.write_text(json.dumps(script))
        rep = v.Report()
        with patch.object(v, 'ROOT', self.root):
            v.check_script(p, 'ru', rep, excerpt=excerpt)
        return rep.errors

    def test_short_taster_can_end_with_natural_english_outro(self):
        self.assertEqual(self.short_errors(self.short_script()), [])

    def test_marker_and_bounded_context_are_both_required_for_short_taster(self):
        script = self.short_script()
        self.assertTrue(any('explicit source-bound excerpt' in e for e in self.short_errors(script, excerpt=False)))
        del script['format']
        self.assertTrue(any('too short' in e for e in self.short_errors(script)))
        sch = v.load_schema('script')
        self.assertTrue(v.schema_errors(script, sch, sch))

    def test_taster_recap_must_repeat_whole_story(self):
        script = self.short_script(); script['segments'][-2]['t'] = 'Другая фраза.'
        self.assertTrue(any('whole story is not repeated' in e for e in self.short_errors(script)))

    def test_taster_may_close_with_exact_source_replay_but_not_unrelated_nonfarewell(self):
        script = self.short_script()
        script['segments'].append(copy.deepcopy(script['segments'][1]))
        self.assertEqual(self.short_errors(script), [])
        script['segments'][-1]['t'] = 'Случайная фраза.'
        self.assertTrue(any('short farewell' in e for e in self.short_errors(script)))

    def test_compose_does_not_add_a_fake_farewell_or_pad_short_taster(self):
        import compose
        from types import SimpleNamespace
        mod = SimpleNamespace(ID='kukhnya-s01e01-scene-01', TITLE='Привет  (Hello taster)',
            LEVEL='A1 — beginner', PAIR='ru-en', LABELS={'guest':'Гость'}, SOURCE_NAME='Kukhnya',
            SOURCE_FILE='unused', INTRO='Listen to a greeting.', OPENER='Here is the first line.',
            STORY=[('guest', 'Привет.', 'Hello.', [(1, 'Привет')], '')],
            WALK=[(0, None, "'Hello.' A greeting.")], TRANSITION='Listen again.', OUTRO='See you next time.',
            CLOSING=None, FORMAT='taster')
        script, _, problems = compose.build(mod, check_source=False)
        self.assertEqual(problems, [])
        self.assertEqual(script['format'], 'taster')
        self.assertEqual(len(script['segments']), 7)
        self.assertEqual(script['segments'][-1]['v'], 'narrator')
        del mod.FORMAT
        self.assertTrue(compose.build(mod, check_source=False)[2])

    def test_missing_or_discontinuous_recap_cannot_reuse_walkthrough_or_original_story(self):
        script = self.short_script()
        del script['segments'][-3:-1]
        self.assertTrue(any('separate contiguous recap' in e for e in self.short_errors(script)))
        script = self.short_script()
        script['segments'].insert(-2, {'v': 'narrator', 't': 'An unrelated comment.', 'gap': .4})
        self.assertTrue(any('separate contiguous recap' in e for e in self.short_errors(script)))
        script = self.short_script()
        script['segments'][-2]['v'] = 'another_speaker'
        script['labels']['another_speaker'] = 'Другой'
        self.assertTrue(any('separate contiguous recap' in e for e in self.short_errors(script)))
