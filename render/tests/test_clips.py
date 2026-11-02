import json
import shutil
from types import SimpleNamespace

import clips
import config
from voices import Voices


def scene(texts, lang="ru", pair="ru-en"):
    lex = {f"w{i}": {"examples": [{"text": t, "trans": "x"}]} for i, t in enumerate(texts)}
    return SimpleNamespace(lang=lang, pair=pair, notes={"lexicon": lex})


def test_clip_id_pinned_and_shared_with_the_publisher():
    assert clips.clip_id("ru-en", "Я режу хлеб.") == "75d68611617d8042"
    assert clips.clip_id("fr-en", "Я режу хлеб.") != clips.clip_id("ru-en", "Я режу хлеб.")


def test_plan_dedupes_and_keys_follow_voice_text_and_settings():
    s, v = config.load_settings(), Voices()
    items = clips.plan_scene(scene(["Я режу хлеб.", "Я режу хлеб.", "Где нож?"]), s, v)
    assert [i.text for i in items] == ["Я режу хлеб.", "Где нож?"]
    assert all(i.voice == s["clips"]["voices"]["ru"] and i.sents and i.sents[0].key for i in items)
    again = clips.plan_scene(scene(["Я режу хлеб."]), s, v)[0]
    assert again.ckey == items[0].ckey
    s2 = json.loads(json.dumps(s))
    s2["clips"]["voices"]["ru"] = "ru-f2"
    assert clips.plan_scene(scene(["Я режу хлеб."]), s2, v)[0].ckey != again.ckey
    s3 = json.loads(json.dumps(s))
    s3["clips"]["programLufs"] = -18.0
    other = clips.plan_scene(scene(["Я режу хлеб."]), s3, v)[0]
    assert other.ckey != again.ckey and other.sents[0].key == again.sents[0].key      # loudness: re-assemble, no new synthesis
    s4 = json.loads(json.dumps(s))
    s4["clips"]["batch"] = 1
    assert clips.plan_scene(scene(["Я режу хлеб."]), s4, v)[0].ckey == again.ckey     # batch size is not part of the audio


def test_no_voice_for_a_language_means_no_clips():
    s, v = config.load_settings(), Voices()
    s["clips"]["voices"] = {}
    assert clips.plan_scene(scene(["Привет."]), s, v) == []


def test_clip_keys_follow_the_qwen_engine_that_renders_them():
    s, v = config.load_settings(), Voices()
    sc = scene(["Я режу хлеб."])
    before = clips.plan_scene(sc, s, v)[0]
    changed_scene_engines = {k: val for k, val in s.items() if k not in ("ttsRu", "ttsEn")}
    assert clips.plan_scene(sc, changed_scene_engines, v)[0].ckey == before.ckey
    changed_qwen = json.loads(json.dumps(s))
    changed_qwen["lora"]["enabled"] = not s["lora"]["enabled"]
    assert clips.plan_scene(sc, changed_qwen, v)[0].sents[0].key != before.sents[0].key


def test_a_multi_sentence_example_is_split_and_gapped():
    s, v = config.load_settings(), Voices()
    it = clips.plan_scene(scene(["Привет. Как дела?"]), s, v)[0]
    assert [x.plain for x in it.sents] == ["Привет.", "Как дела?"]


def test_commit_and_fail_final_leave_a_record_and_clean_the_work_dir(tmp_path):
    s, v = config.load_settings(), Voices()
    it = clips.plan_scene(scene(["Я режу хлеб.", "Где нож?"]), s, v)
    cs = clips.ClipStore(tmp_path)
    for i in it:
        (cs.work / f"{i.id}.mp3").write_bytes(b"mp3-" + i.id.encode())
        cs.write_work(i.id, {"id": i.id, "pair": i.pair, "text": i.text, "lang": i.lang, "voice": i.voice, "ckey": i.ckey,
                             "tries": 0, "durationSec": 1.5})
    assert len(cs.pending(it)) == 2
    clips.commit(tmp_path, it[0].id, 0.02, "я режу хлеб", None)
    clips.fail_final(tmp_path, it[1].id, 0.9, "что-то другое")
    rec = cs.record(it[0].id)
    assert rec["status"] == "ok" and rec["text"] == "Я режу хлеб." and rec["cer"] == 0.02 and (cs.dir / f"{it[0].id}.mp3").exists()
    bad = cs.record(it[1].id)
    assert bad["status"] == "failed" and not (cs.dir / f"{it[1].id}.mp3").exists()
    assert not list(cs.work.iterdir())
    assert cs.pending(it) == []                                    # failed clips are not retried until their inputs change
    s2 = json.loads(json.dumps(s))
    s2["clips"]["voices"]["ru"] = "ru-f2"
    assert len(cs.pending(clips.plan_scene(scene(["Я режу хлеб.", "Где нож?"]), s2, v))) == 2


def test_a_record_without_its_mp3_is_not_done(tmp_path):
    s, v = config.load_settings(), Voices()
    it = clips.plan_scene(scene(["Где нож?"]), s, v)[0]
    cs = clips.ClipStore(tmp_path)
    (cs.dir / f"{it.id}.json").write_text(json.dumps({"ckey": it.ckey, "status": "ok"}))
    assert not cs.is_done(it)


def test_retake_selection_picks_only_current_failed_checks(tmp_path):
    s, v = config.load_settings(), Voices()
    sc = scene(["Я режу хлеб.", "Где нож?"])
    a, b = clips.plan_scene(sc, s, v)
    cs = clips.ClipStore(tmp_path)
    cs.write_work(a.id, {"ckey": a.ckey, "tries": 0, "failedCheck": True})
    cs.write_work(b.id, {"ckey": "stale", "tries": 0, "failedCheck": True})
    got = clips.items_for_retake([sc], s, v, tmp_path, 1)
    assert [i.id for i in got] == [a.id]
    assert clips.items_for_retake([sc], s, v, tmp_path, 2) == []
