"""Explicit retakes for an unchanged authored segment; zero preserves every existing key."""
import json
from pathlib import Path


def for_scene(scene, path=None):
    path = Path(path or Path(__file__).with_name('retakes.json'))
    data = json.loads(path.read_text()) if path.exists() else {}
    entries = data.get(scene.id, {})
    if not isinstance(entries, dict):
        raise ValueError(f'{scene.id}: retakes must map segment indices to positive counters')
    result = {}
    for index, counter in entries.items():
        if not str(index).isdigit() or not isinstance(counter, int) or isinstance(counter, bool) or counter < 0:
            raise ValueError(f'{scene.id}: invalid retake {index!r}')
        if int(index) >= len(scene.script['segments']):
            raise ValueError(f'{scene.id}: retake segment {index} no longer exists')
        if counter:
            result[str(int(index))] = counter
    return result
