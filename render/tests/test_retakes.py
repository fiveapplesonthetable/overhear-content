import hashlib
import json
from types import SimpleNamespace

import pytest
import config
import plan
import retakes


def test_zero_preserves_exact_legacy_cache_key_and_positive_retakes_only_change_target():
    settings = config.load_settings()
    sig = config.sentence_signature(settings, 'en')
    original = hashlib.sha256(json.dumps({'sig': sig, 'voice': 'test', 'ref': 'ref1', 'lang': 'en', 'text': 'A new invented sentence.'}, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    assert plan.cache_key(settings, 'test', 'ref1', 'en', 'A new invented sentence.') == original
    assert plan.cache_key(settings, 'test', 'ref1', 'en', 'A new invented sentence.', retake=0) == original
    assert plan.cache_key(settings, 'test', 'ref1', 'en', 'A new invented sentence.', retake=1) != original
    assert plan.cache_key(settings, 'test', 'ref1', 'en', 'A new invented sentence.', retake=1) != plan.cache_key(settings, 'test', 'ref1', 'en', 'A new invented sentence.', retake=2)
    with pytest.raises(ValueError): plan.cache_key(settings, 'test', 'ref1', 'en', 'invented', retake=-1)


def test_retake_scope_and_validation(tmp_path):
    scene = SimpleNamespace(id='invented-s01e01-scene-01', script={'segments': [{}, {}]})
    path = tmp_path / 'retakes.json'
    path.write_text(json.dumps({scene.id: {'0': 0, '1': 2}, 'another': {'0': 5}}))
    assert retakes.for_scene(scene, path) == {'1': 2}
    for values in ({'2': 1}, {'0': -1}, {'0': True}, {'bad': 2}):
        path.write_text(json.dumps({scene.id: values}))
        with pytest.raises(ValueError): retakes.for_scene(scene, path)


def test_render_key_changes_only_for_a_scene_with_a_positive_retake(monkeypatch):
    scene = SimpleNamespace(id='invented', lang='en', content_hash='abc')
    voices = SimpleNamespace(ref_version=lambda key: 'ref')
    settings = config.load_settings()
    monkeypatch.setattr(retakes, 'for_scene', lambda scene: {})
    original = plan.render_key(scene, voices, settings, {'narrator': 'test'})
    monkeypatch.setattr(retakes, 'for_scene', lambda scene: {'1': 2})
    assert plan.render_key(scene, voices, settings, {'narrator': 'test'}) != original
