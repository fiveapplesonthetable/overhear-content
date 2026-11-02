"""CPU-only Portuguese routing contracts; no model load or acoustic claim."""
from types import SimpleNamespace
import json

import numpy as np

import align
import content
import native_text
import textprep
from tts import QwenEngine


def test_portuguese_scene_is_ingested_without_relaxing_unknown_pairs(tmp_path):
    folder = tmp_path / 'out/porta-dos-fundos/s01e01'
    folder.mkdir(parents=True)
    path = folder / 'scene-01.json'
    script = {'id': 'porta-dos-fundos-s01e01-scene-01', 'pair': 'pt-en',
              'segments': [{'v': 'speaker', 't': 'Olá.', 'gap': .3}]}
    path.write_text(json.dumps(script))
    path.with_name('scene-01.notes.json').write_text(json.dumps({'lines': []}))
    cast = {'speaker': {'gender': 'm', 'ru': 'Speaker'}}
    scene = content.load_scene(path, cast=cast)
    assert isinstance(scene, content.Scene) and scene.lang == 'pt'
    assert scene.script['segments'][0]['t'] == 'Olá.'
    script['pair'] = 'xx-en'
    path.write_text(json.dumps(script))
    assert isinstance(content.load_scene(path, cast=cast), content.Skip)


def test_portuguese_generic_latin_preparation_preserves_canonical_source():
    text = 'A mãe vê o avô. Olá!'
    sentences = textprep.prepare_segment(0, 'native_pt', text, 'pt', [], 'none', .4, .2)
    assert [sentence.plain for sentence in sentences] == ['A mãe vê o avô.', 'Olá!']
    assert [sentence.tts for sentence in sentences] == [sentence.plain for sentence in sentences]
    assert 'pt' not in native_text.LANGUAGES  # Latin whitespace/MMS path, no fabricated native-script spans.
    assert ''.join(align.romanize_char(ch, 'pt') for ch in 'mãe avô avó') == 'maeavoavo'


def test_configured_portuguese_label_reaches_qwen_without_any_gpu_or_model(tmp_path):
    engine = object.__new__(QwenEngine)
    engine.s = {'tts': {'languages': {'pt': 'Portuguese'}, 'batch': 1, 'sentence_retries': 0}}
    engine.torch = SimpleNamespace(cuda=SimpleNamespace(OutOfMemoryError=RuntimeError))
    engine.log = lambda *_: None
    called = []
    def generate(batch, seed):
        called.extend(batch)
        return [np.zeros(24000, dtype=np.float32)]
    engine.generate = generate
    store = SimpleNamespace(tts_path=lambda key: tmp_path / (key + '.flac'))
    item = {'key': '12345678', 'voice': 'native_pt', 'lang': 'pt', 'text_tts': 'Olá.', 'text_plain': 'Olá.'}
    result = engine.synth_many([item], store)
    assert called == [('native_pt', 'Portuguese', 'Olá.')]
    assert result['n'] == 1 and store.tts_path(item['key']).is_file()
