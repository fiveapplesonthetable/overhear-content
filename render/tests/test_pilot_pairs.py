"""All pilot pairs can enter rendering without changing voices, models or profiles."""
import json

import content
import pytest


@pytest.mark.parametrize("lang,show", [
    ("de", "die-discounter"), ("it", "boris"), ("ja", "the-naked-director"),
    ("zh", "behind-the-scenes"), ("ko", "the-producers"), ("ar", "alrawabi-school"),
])
def test_pilot_pair_scene_is_discovered_with_its_own_language(tmp_path, lang, show):
    episode = tmp_path / "out" / show / "s01e01"
    episode.mkdir(parents=True)
    sid = f"{show}-s01e01-scene-01"
    (episode / "scene-01.json").write_text(json.dumps({"id": sid, "pair": f"{lang}-en", "segments": [
        {"v": "narrator", "t": "An engineering fixture.", "gap": 0.3},
        {"v": "test", "t": "fixture", "gap": 0.3}]}))
    (episode / "scene-01.notes.json").write_text(json.dumps({"lines": []}))
    (episode.parent / "cast.json").write_text(json.dumps({"cast": [{"key": "test", "ru": "Test", "gender": "m"}]}))
    scenes, skips = content.discover(tmp_path)
    assert skips == [] and len(scenes) == 1
    assert scenes[0].pair == f"{lang}-en" and scenes[0].lang == lang
