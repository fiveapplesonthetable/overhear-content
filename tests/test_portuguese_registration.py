"""Brazilian Portuguese authoring gates; synthetic metadata is not speech QA."""
import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import validate as v


def notes():
    return {'schemaVersion': 1, 'id': 'porta-dos-fundos-s01e01-scene-01', 'lines': [
        {'seg': 0, 'trans': 'Mother.', 'words': [{'t': 'Mãe.', 'lemma': 'mãe', 'pos': 'noun',
         'stress': 'ˈmɐ̃j̃', 'gloss': 'mother', 'gram': 'feminine singular'}]}], 'lexicon': {'mãe': {
        'lemma': 'mãe', 'stress': 'ˈmɐ̃j̃', 'pos': 'noun', 'gloss': 'mother', 'gender': 'f',
        'meanings': [{'en': 'mother', 'note': ''}], 'forms': {'title': 'Number', 'columns': ['', 'singular', 'plural'],
        'rows': [{'cells': ['form', 'mãe', 'mães']}]}, 'moreForms': [],
        'examples': [{'text': 'A mãe.', 'trans': 'The mother.'}, {'text': 'As mães.', 'trans': 'The mothers.'}], 'related': []}}}


def check(tmp_path, doc):
    path = tmp_path / 'scene-01.notes.json'
    path.write_text(json.dumps(doc, ensure_ascii=False))
    rep = v.Report()
    v.check_notes(path, {'id': doc['id'], 'segments': [{'v': 'speaker', 't': 'Mãe.'}]}, 'pt', True, rep)
    return rep.errors


def test_brazilian_portuguese_identity_source_path_and_nasal_ipa_are_supported(tmp_path):
    assert v.SHOWS['porta-dos-fundos'] == 'pt' and v.PAIR['pt'] == 'pt-en'
    assert check(tmp_path, notes()) == []
    schema = v.load_schema('script')
    for key, value in [('id', notes()['id']), ('pair', 'pt-en'), ('show', 'porta-dos-fundos')]:
        assert v.schema_errors(value, schema['properties'][key], schema) == []
    assert v.schema_errors('sources/porta-dos-fundos/s01/e01.pt.srt', schema['properties']['source']['properties']['file'], schema) == []
    assert v.schema_errors('unknown-show-s01e01-scene-01', schema['properties']['id'], schema)
    for farewell in ['Tchau!', 'Até logo.', 'Até amanhã.']:
        assert v.FAREWELL['pt'].search(farewell)


@pytest.mark.parametrize('bad', [None, '[ˈmɐ̃j̃]', 'Mɐ̃j̃', 'avó', 'avô', 'mɐ̃j̃́'])
def test_portuguese_words_require_bare_ipa_without_spelling_accents(tmp_path, bad):
    doc = notes()
    doc['lines'][0]['words'][0]['stress'] = bad
    assert check(tmp_path, doc)


def test_ordinary_portuguese_lexicon_cannot_omit_pronunciation_or_written_forms(tmp_path):
    doc = notes()
    doc['lexicon']['mãe']['stress'] = None
    assert check(tmp_path, doc)
    doc = notes()
    doc['lexicon']['mãe']['forms'] = None
    assert any('pt noun/adj/verb needs a forms table' in error for error in check(tmp_path, doc))


def test_portuguese_target_does_not_accept_cyrillic():
    rep = v.Report()
    v.target_ok('pt', 'Привет.', 'fixture', rep)
    assert any('Cyrillic in Brazilian Portuguese' in error for error in rep.errors)


@pytest.mark.parametrize('kind', ['learn', 'dictionary', 'origins'])
def test_portuguese_optional_metadata_pair_is_registered(kind):
    schema = v.load_schema(kind)
    assert v.schema_errors('pt-en', schema['properties']['pair'], schema) == []
