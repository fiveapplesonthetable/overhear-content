import importlib.util
import json
import os
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location("fix_episode", Path(__file__).resolve().parents[2] / "tools" / "fix_episode.py")
fix_episode = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fix_episode)


def test_settings_for_every_show_family():
    assert fix_episode.settings_for("dvorik-u-mosta") == "render/settings.ru-qwen-lora-en.json"
    assert fix_episode.settings_for("linden-courtyard-fr") == "render/settings.en-qwen.json"
    assert fix_episode.settings_for("linden-courtyard-ar") == "render/settings.en-ar.json"
    assert fix_episode.settings_for("linden-courtyard-hi") == "render/settings.en-hi.json"
    assert fix_episode.settings_for("aangan-haveli") == "render/settings.hi-chatterbox-en.json"


def test_seed_cache_links_only_content_addressed_files_audio_first(tmp_path):
    src, dst = tmp_path / "a", tmp_path / "b"
    for rel in ("cache/tts", "clips", "forms"):
        (src / rel).mkdir(parents=True)
    (src / "cache/tts/" / ("ab" * 16 + ".flac")).write_bytes(b"x")
    (src / "clips/0123456789abcdef.mp3").write_bytes(b"m")
    (src / "clips/0123456789abcdef.json").write_text("{}")
    (src / "clips/.0123456789abcdef.tmp.json").write_text("{}")
    (src / "forms/.plan.json").write_text("[]")
    (src / "forms/review.jsonl").write_text("")
    assert fix_episode.seed_cache(src, dst) == 3
    assert (dst / "clips/0123456789abcdef.mp3").stat().st_ino == (src / "clips/0123456789abcdef.mp3").stat().st_ino
    assert not (dst / "clips/.0123456789abcdef.tmp.json").exists()
    assert not (dst / "forms/.plan.json").exists() and not (dst / "forms/review.jsonl").exists()
    assert fix_episode.seed_cache(src, dst) == 0


def test_bump_retakes_increments_existing_counter(tmp_path, monkeypatch):
    (tmp_path / "render").mkdir()
    (tmp_path / "render/retakes.json").write_text(json.dumps({"x-s01e01-scene-01": {"9": 1}}))
    monkeypatch.setattr(fix_episode, "ROOT", tmp_path)
    fix_episode.bump_retakes(["x-s01e01-scene-01:9", "x-s01e01-scene-02:3"])
    data = json.loads((tmp_path / "render/retakes.json").read_text())
    assert data == {"x-s01e01-scene-01": {"9": 2}, "x-s01e01-scene-02": {"3": 1}}
