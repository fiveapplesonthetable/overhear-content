import json
from pathlib import Path
import content
import config
from store import Store


def _write(root, show, s, e, n, notes=True, pair="ru-en", cast=True, roles=("narrator", "max")):
    d = root / "out" / show / f"s{s:02d}e{e:02d}"
    d.mkdir(parents=True, exist_ok=True)
    sid = f"{show}-s{s:02d}e{e:02d}-scene-{n:02d}"
    segs = [{"v": r, "t": "Hello there." if r == "narrator" else "Привет!", "gap": 0.5} for r in roles]
    script = {"schemaVersion": 1, "id": sid, "pair": pair, "show": show, "season": s, "episode": e, "scene": n, "segments": segs}
    (d / f"scene-{n:02d}.json").write_text(json.dumps(script, ensure_ascii=False))
    if cast and not (d.parent / "cast.json").exists():
        (d.parent / "cast.json").write_text(json.dumps({"schemaVersion": 1, "show": show, "cast": [
            {"key": "max", "ru": "Макс", "en": ["Max"], "gender": "m"}, {"key": "vika", "ru": "Вика", "en": ["Vika"], "gender": "f"},
            {"key": "nastya", "ru": "Настя", "en": ["Nastya"], "gender": "f"}]}))
    if notes:
        (d / f"scene-{n:02d}.notes.json").write_text(json.dumps({"lines": [{"seg": 1, "trans": "Hi", "words": [{"t": "Привет!", "stress": "Приве\u0301т!"}]}]}))
    return sid


def test_discover_skips_instead_of_aborting(tmp_path):
    _write(tmp_path, "kukhnya", 1, 1, 1)
    _write(tmp_path, "kukhnya", 1, 1, 2, notes=False)
    _write(tmp_path, "kukhnya", 1, 1, 3, pair="xx-en")
    bad = tmp_path / "out/kukhnya/s01e01/scene-04.json"
    bad.write_text("{not json")
    scenes, skips = content.discover(tmp_path)
    assert [s.id for s in scenes] == ["kukhnya-s01e01-scene-01"]
    reasons = {s.id: s.reason for s in skips}
    assert "no notes" in reasons["kukhnya-s01e01-scene-02"]
    assert "unsupported pair" in reasons["kukhnya-s01e01-scene-03"]
    assert "unreadable" in reasons["kukhnya-s01e01-scene-04"]


def test_clips_backfill_selects_every_scene_in_a_comma_separated_scope(tmp_path, monkeypatch):
    import sys
    from types import SimpleNamespace
    import pipeline
    selected = []

    def queue(args, settings, voices, store):
        selected.extend(s.id for s in [SimpleNamespace(id=x) for x in ("one", "two", "outside")] if pipeline.select(args, s))
        return [], [], [], [], []

    monkeypatch.setattr(pipeline, "plan_queue", queue)
    monkeypatch.setattr(sys, "argv", ["pipeline.py", "--clips-only", "--dry-run", "--scene", "one,two", "--store", str(tmp_path)])
    assert pipeline.main() == 0
    assert selected == ["one", "two"]


def test_content_hash_changes_iff_script_or_notes_change(tmp_path):
    _write(tmp_path, "kukhnya", 1, 1, 1)
    a = content.discover(tmp_path)[0][0].content_hash
    assert a == content.discover(tmp_path)[0][0].content_hash
    p = tmp_path / "out/kukhnya/s01e01/scene-01.notes.json"
    p.write_text(p.read_text().replace("Hi", "Hello"))
    assert content.discover(tmp_path)[0][0].content_hash != a


def test_merged_scene_not_listed(tmp_path):
    _write(tmp_path, "kukhnya", 1, 1, 1)
    d = tmp_path / "out/kukhnya/s01e01"
    (d / "scenes.json").write_text(json.dumps({"show": "kukhnya", "season": 1, "episode": 1, "scenes": [{"scene": 1, "merge": 2}]}))
    scenes, skips = content.discover(tmp_path)
    assert not scenes and "merged" in skips[0].reason


def test_priority_order():
    class S:
        def __init__(self, show, season, ep, sc):
            self.show, self.season, self.episode, self.scene = show, season, ep, sc
    pr = config.load_settings()["priority"]
    items = [S("domashniy-arest", 1, 1, 1), S("kukhnya", 2, 1, 1), S("kukhnya", 1, 2, 1), S("kukhnya", 1, 1, 5),
             S("dix-pour-cent", 1, 1, 1), S("kukhnya", 3, 1, 1), S("dix-pour-cent", 4, 1, 1)]
    order = [(s.show, s.season, s.episode, s.scene) for s in sorted(items, key=lambda s: content.priority_key(s, pr))]
    assert order == [("kukhnya", 1, 1, 5), ("kukhnya", 1, 2, 1), ("dix-pour-cent", 1, 1, 1), ("domashniy-arest", 1, 1, 1),
                     ("kukhnya", 2, 1, 1), ("dix-pour-cent", 4, 1, 1), ("kukhnya", 3, 1, 1)]


def test_state_diff_and_atomic_commit(tmp_path):
    st = Store(tmp_path)
    assert not st.is_done("x-s01e01-scene-01", "k1")
    files = {"audio.mp3": b"a", "spans.json": b"{}", "timing.json": b"{}", "report.json": b"{}",
             "meta.json": json.dumps({"renderKey": "k1"}).encode()}
    st.commit_scene("x-s01e01-scene-01", files)
    assert st.is_done("x-s01e01-scene-01", "k1")
    assert not st.is_done("x-s01e01-scene-01", "k2")      # changed inputs => stale
    files["meta.json"] = json.dumps({"renderKey": "k2"}).encode()
    st.commit_scene("x-s01e01-scene-01", files)           # replace
    assert st.is_done("x-s01e01-scene-01", "k2")
    assert not [p for p in tmp_path.iterdir() if p.name.startswith(".")]


def test_render_key_changes_with_voice_ref_and_content(tmp_path, monkeypatch):
    import casting
    import plan
    from voices import Voices
    monkeypatch.setattr(casting, "DIR", tmp_path / "casting")
    _write(tmp_path, "kukhnya", 1, 1, 1)
    scenes = content.discover(tmp_path)[0]
    v = Voices()
    casting.ensure(scenes, content.discover.casts, v, log=lambda *a: None)
    sc = scenes[0]
    s = config.load_settings()
    k = plan.render_key(sc, v, s)
    assert k == plan.render_key(sc, v, s)
    doc = casting.load("kukhnya")
    doc["characters"]["max"]["voice"] = "ru-m3"          # re-cast by hand
    casting.save(doc)
    assert plan.render_key(sc, v, s) != k
    s2 = json.loads(json.dumps(s)); s2["renderVersion"] = "r-test"
    assert plan.render_key(sc, Voices(), s2) != plan.render_key(sc, v, s)
    s3 = json.loads(json.dumps(s)); s3["stressRetry"]["attempts"] = 9
    assert plan.render_key(sc, Voices(), s3) == plan.render_key(sc, v, s)      # retry budget never forces a re-render


def test_casting_gender_distinct_and_append_only(tmp_path, monkeypatch):
    import casting
    from voices import Voices
    monkeypatch.setattr(casting, "DIR", tmp_path / "casting")
    _write(tmp_path, "kukhnya", 1, 1, 1, roles=("narrator", "max", "vika", "nastya"))
    scenes = content.discover(tmp_path)[0]
    v = Voices()
    casting.ensure(scenes, content.discover.casts, v, log=lambda *a: None)
    doc = casting.load("kukhnya")
    ch = doc["characters"]
    assert doc["narrator"] == "sky"
    assert v.refs[ch["max"]["voice"]]["gender"] == "m" and ch["max"]["voice"] == "ru-m1"      # designed for max
    assert v.refs[ch["vika"]["voice"]]["gender"] == "f" and v.refs[ch["nastya"]["voice"]]["gender"] == "f"
    assert len({ch[k]["voice"] for k in ch}) == 3                                       # distinct in a shared scene
    before = json.dumps(doc, sort_keys=True)
    casting.ensure(scenes, content.discover.casts, v, log=lambda *a: None)
    assert json.dumps(casting.load("kukhnya"), sort_keys=True) == before                # idempotent
    # a new scene with a new character: existing entries untouched
    (tmp_path / "out/kukhnya/cast.json").write_text(json.dumps({"schemaVersion": 1, "show": "kukhnya", "cast": [
        {"key": k, "ru": k, "en": [k], "gender": g} for k, g in [("max", "m"), ("vika", "f"), ("nastya", "f"), ("kostya", "m")]]}))
    _write(tmp_path, "kukhnya", 1, 1, 2, roles=("narrator", "max", "kostya"))
    scenes = content.discover(tmp_path)[0]
    casting.ensure(scenes, content.discover.casts, v, log=lambda *a: None)
    d2 = casting.load("kukhnya")["characters"]
    assert all(d2[k] == ch[k] for k in ch) and d2["kostya"]["voice"] == "ru-m3"


def test_voice_errors_are_skips(tmp_path, monkeypatch):
    import casting
    import plan
    from voices import Voices, VoiceError
    import pytest
    monkeypatch.setattr(casting, "DIR", tmp_path / "casting")
    _write(tmp_path, "kukhnya", 1, 1, 1)
    sc = content.discover(tmp_path)[0][0]
    with pytest.raises(VoiceError):                      # nobody cast yet
        plan.check_voices(sc, Voices())
    _write(tmp_path, "kukhnya", 1, 1, 2, roles=("narrator", "ghost"))        # role not in cast.json
    skips = content.discover(tmp_path)[1]
    assert any("not in out/kukhnya/cast.json" in s.reason for s in skips)
    _write(tmp_path, "dix-pour-cent", 1, 1, 1, cast=False, pair="fr-en")
    assert any("no cast.json" in s.reason for s in content.discover(tmp_path)[1])
