"""Tests for Overhear Originals (originals/<show>/) vs TV adaptations (out/<show>/)."""
import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_render as cr
import compose
import fetch_renders as fr
import package_render as pr
import validate as v

EX = ROOT / "examples" / "kukhnya-s01e02-knife"


class OriginalsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "out" / "kukhnya").mkdir(parents=True)
        self.show = "hotel-neva"
        self.show_dir = self.tmp / "originals" / self.show
        self.ep_dir = self.show_dir / "s01e01"
        (self.show_dir / "art").mkdir(parents=True)
        self.ep_dir.mkdir(parents=True)
        shutil.copy(EX / "art.webp", self.show_dir / "art" / "cover.webp")
        shutil.copy(EX / "art.webp", self.ep_dir / "scene-01.webp")
        (self.show_dir / "bible.md").write_text("# Hotel Neva\n\nOriginal Season 1 bible.\n", encoding="utf-8")
        (self.show_dir / "characters.md").write_text("# Characters\n\n- **Dasha**: receptionist.\n", encoding="utf-8")
        (self.show_dir / "show.json").write_text(json.dumps({
            "schemaVersion": 1,
            "slug": self.show,
            "pair": "ru-en",
            "title": {"ru": "Отель Нева", "en": "Hotel Neva"},
            "summary": {"en": "A small guesthouse in St Petersburg."},
            "type": "series",
            "categories": ["comedy"],
            "cover": "art/cover.webp",
            "seasons": [{"n": 1, "title": {"en": "Season 1", "ru": "Сезон 1"}}],
        }, ensure_ascii=False), encoding="utf-8")
        (self.show_dir / "cast.json").write_text(json.dumps({
            "schemaVersion": 1,
            "show": self.show,
            "other_names": ["Neva"],
            "cast": [
                {"key": "dasha", "ru": "Даша", "en": ["Dasha"], "gender": "f"},
                {"key": "pavel", "ru": "Павел", "en": ["Pavel"], "gender": "m"},
            ],
        }, ensure_ascii=False), encoding="utf-8")
        self.scenes = {
            "schemaVersion": 1,
            "show": self.show,
            "season": 1,
            "episode": 1,
            "title": "The Spare Key",
            "scenes": [{
                "scene": 1,
                "title": "First Morning",
                "summary": "Dasha opens the front desk while Pavel hunts for the coffee jar.",
                "characters": ["dasha", "pavel"],
                "location": "front desk",
            }],
        }
        raw = (EX / "scene.json").read_text(encoding="utf-8").replace('"anya"', '"dasha"').replace('"chef"', '"pavel"').replace("Anya", "Dasha").replace("Chef", "Pavel").replace("Шеф", "Павел")
        self.script = json.loads(raw)
        self.script.pop("voices", None)
        self.script.pop("source", None)
        self.script.update({
            "schemaVersion": 1,
            "id": f"{self.show}-s01e01-scene-01",
            "pair": "ru-en",
            "show": self.show,
            "season": 1,
            "episode": 1,
            "scene": 1,
            "title": "Первое утро  (First Morning)",
            "level": "A1 — beginner",
            "labels": {"dasha": "Даша", "pavel": "Павел"},
        })
        self.write()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self):
        v.SHOWS.clear()
        v._CAST.clear()
        v.ART_SEEN.clear()
        (self.ep_dir / "scenes.json").write_text(json.dumps(self.scenes, ensure_ascii=False), encoding="utf-8")
        (self.ep_dir / "scene-01.json").write_text(json.dumps(self.script, ensure_ascii=False), encoding="utf-8")

    def validate_ep(self):
        self.write()
        rep = v.Report()
        v.REQ[0] = False
        v.check_scenes(self.ep_dir, self.show, rep)
        return rep

    def test_original_episode_passes_without_sources_or_cue_times(self):
        rep = self.validate_ep()
        self.assertEqual(rep.errors, [])

    def test_original_rejects_source_block_while_out_still_requires_it(self):
        self.script["source"] = {"show": "x", "file": "sources/kukhnya/s01/e02.ru.dual.srt", "lines": []}
        rep = self.validate_ep()
        self.assertTrue(any("must not carry a 'source' block" in e for e in rep.errors), rep.errors)

        # Conversely, a script under out/ without `source` is still rejected.
        out_ep = self.tmp / "out" / "kukhnya" / "s01e02"
        out_ep.mkdir(parents=True)
        no_src = copy.deepcopy(self.script)
        no_src.pop("source", None)
        sp = out_ep / "scene-01.json"
        sp.write_text(json.dumps(no_src, ensure_ascii=False), encoding="utf-8")
        rep_out = v.Report()
        v.check_script(sp, "ru", rep_out, is_original=False)
        self.assertTrue(any("missing field 'source'" in e for e in rep_out.errors), rep_out.errors)

    def test_original_rejects_start_and_end_timestamps(self):
        self.scenes["scenes"][0]["start"] = "00:00:00,000"
        self.scenes["scenes"][0]["end"] = "00:01:00,000"
        rep = self.validate_ep()
        self.assertTrue(any("must not carry time/cue field" in e for e in rep.errors), rep.errors)

    def test_original_slug_collision_with_out_is_rejected(self):
        (self.tmp / "out" / self.show).mkdir(parents=True)
        rep = self.validate_ep()
        self.assertTrue(any("collides with out/" in e for e in rep.errors), rep.errors)

    def test_validate_cli_root_originals_and_learn_links(self):
        learn_dir = self.tmp / "learn" / "ru-en"
        learn_dir.mkdir(parents=True)
        (learn_dir / "desk-greeting.json").write_text(json.dumps({
            "schemaVersion": 1,
            "id": "desk-greeting",
            "pair": "ru-en",
            "section": "phrases",
            "order": 1,
            "title": {"en": "Greeting at the desk"},
            "summary": {"en": "Polite morning hello."},
            "body": {"en": "Listen for the greeting."},
            "related": [],
            "examples": [{"sceneId": f"{self.show}-s01e01-scene-01", "seg": 1}],
            "tags": ["привет"],
        }, ensure_ascii=False), encoding="utf-8")
        rc = v.main(["--root", "originals", str(self.tmp / "originals")])
        self.assertEqual(rc, 0)

    def test_compose_original_omits_source_block(self):
        auth = self.ep_dir / "authoring"
        auth.mkdir()
        draft = auth / "scene-01.py"
        draft.write_text(
            f'ID = "{self.show}-s01e01-scene-01"\n'
            'PAIR = "ru-en"\n'
            'TITLE = "Первое утро  (First Morning)"\n'
            'LEVEL = "A1 — beginner"\n'
            'LABELS = {"dasha": "Даша", "pavel": "Павел"}\n'
            'INTRO = "Dasha opens the front desk."\n'
            'STORY = [\n'
            '    ("dasha", "Доброе утро, Павел!", "Good morning, Pavel!"),\n'
            '    ("pavel", "Привет, Даша! Где ключ?", "Hi, Dasha! Where is the key?"),\n'
            '] * 5\n'
            'OPENER = "Let us go through that."\n'
            'WALK = [(0, None, "\'Good morning, Pavel!\' The Russian morning greeting literally wishes a kind morning.")]\n'
            'TRANSITION = "Now let\'s hear the whole scene again."\n'
            'OUTRO = "See you next time."\n'
            'CLOSING = ("dasha", "Пока!")\n',
            encoding="utf-8",
        )
        out_json = self.ep_dir / "scene-01.json"
        self.assertEqual(compose.main(["--root", "originals", str(draft), "--out", str(out_json)]), 0)
        built = json.loads(out_json.read_text(encoding="utf-8"))
        self.assertNotIn("source", built)
        self.assertEqual(built["show"], self.show)

    def test_package_and_fetch_use_original_tag_prefix(self):
        # Create minimal valid notes + store artifacts so check_render and package_render pass end-to-end.
        segs = [{"v": "narrator", "t": "Intro."}, {"v": "dasha", "t": "Привет!"}]
        for i in range(18):
            segs.append({"v": "narrator", "t": f"Line {i}."})
        segs.append({"v": "dasha", "t": "Пока!"})
        for s in segs:
            s["gap"] = 0.4
        self.script["segments"] = segs
        notes = {
            "schemaVersion": 1,
            "id": f"{self.show}-s01e01-scene-01",
            "lines": [
                {"seg": 1, "trans": "Hi!", "words": [{"t": "Привет!", "lemma": "привет", "pos": "interj", "stress": "приве\u0301т!", "gloss": "hi", "gram": "interj"}]},
                {"seg": 20, "trans": "Bye!", "words": [{"t": "Пока!", "lemma": "пока", "pos": "interj", "stress": "пока\u0301!", "gloss": "bye", "gram": "interj"}]},
            ],
            "lexicon": {
                "привет": {"lemma": "привет", "stress": "приве\u0301т", "pos": "interj", "gloss": "hi",
                           "meanings": [{"en": "hi", "note": ""}], "forms": None, "moreForms": [],
                           "examples": [{"text": "Привет!", "trans": "Hi!"}, {"text": "Привет, Павел!", "trans": "Hi, Pavel!"}], "related": []},
                "пока": {"lemma": "пока", "stress": "пока\u0301", "pos": "interj", "gloss": "bye",
                         "meanings": [{"en": "bye", "note": ""}], "forms": None, "moreForms": [],
                         "examples": [{"text": "Пока!", "trans": "Bye!"}, {"text": "Пока, Даша!", "trans": "Bye, Dasha!"}], "related": []},
            },
        }
        (self.ep_dir / "scene-01.notes.json").write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")
        self.write()

        store = self.tmp / "store"
        sid = f"{self.show}-s01e01-scene-01"
        sdir = store / sid
        sdir.mkdir(parents=True)
        mp3_bytes = b"\xff\xfb\x90\x64" + b"\x00" * 4096
        (sdir / "audio.mp3").write_bytes(mp3_bytes)
        chash = cr.content_hash(self.ep_dir / "scene-01.json", self.ep_dir / "scene-01.notes.json")
        spans_segs = []
        timing_doc = {}
        t = 0.0
        for idx, g in enumerate(segs):
            lang = "en" if g["v"] == "narrator" else "ru"
            toks = [x for x in g["t"].split() if any(ch.isalnum() for ch in x)]
            spans_segs.append({"seg": idx, "v": g["v"], "lang": lang, "start": round(t, 3), "end": round(t + 0.4, 3),
                               "sentences": [{"text": g["t"], "start": round(t, 3), "end": round(t + 0.4, 3)}]})
            timing_doc[str(idx)] = [{"t": tok, "s": round(t + j * 0.1, 3), "e": round(t + (j + 1) * 0.1, 3)} for j, tok in enumerate(toks)]
            t = round(t + 0.45, 3)
        dur = round(t, 3)
        spans_bytes = json.dumps({"durationSec": dur, "segs": spans_segs}).encode("utf-8")
        timing_bytes = json.dumps(timing_doc).encode("utf-8")
        (sdir / "spans.json").write_bytes(spans_bytes)
        (sdir / "timing.json").write_bytes(timing_bytes)
        (sdir / "meta.json").write_text(json.dumps({
            "sceneId": sid,
            "contentHash": chash,
            "contentCommit": "deadbeef1234",
            "tts": "espeech-test",
            "voicesVersion": "v1",
            "align": "mms_fa",
            "pipelineVersion": "1",
            "renderVersion": "1",
            "renderKey": "rk1",
            "renderedAt": "2026-11-06T00:00:00Z",
            "durationSec": dur,
            "sampleRate": 24000,
            "bitrateKbps": 96,
            "audioSha256": hashlib.sha256(mp3_bytes).hexdigest(),
            "audioBytes": len(mp3_bytes),
            "spansSha256": hashlib.sha256(spans_bytes).hexdigest(),
            "timingSha256": hashlib.sha256(timing_bytes).hexdigest(),
            "voices": {"narrator": "sky", "dasha": "ru-f1"},
        }), encoding="utf-8")
        (sdir / "report.json").write_text(json.dumps({"retake": {"takes": 2, "retakes": 0}}), encoding="utf-8")

        calls = []

        def fake_run(cmd, *a, **kw):
            calls.append(cmd)
            if cmd[:2] == ["git", "-C"]:
                return mock.Mock(returncode=0, stdout="deadbeef1234\n")
            if cmd[:3] == ["gh", "release", "view"]:
                return mock.Mock(returncode=1, stdout="")
            return mock.Mock(returncode=0, stdout="")

        with mock.patch.object(pr.subprocess, "run", side_effect=fake_run):
            rc = pr.main([str(store), "--root", "originals", "--episode", f"{self.show}-s01e01", "--content", str(self.tmp), "--release"])
        self.assertEqual(rc, 0)
        tar_path = self.tmp / "dist" / f"original-{self.show}-s01e01.tar"
        self.assertTrue(tar_path.is_file())
        self.assertFalse((self.tmp / "dist" / f"render-{self.show}-s01e01.tar").exists())
        create_calls = [c for c in calls if c[:3] == ["gh", "release", "create"]]
        self.assertEqual(len(create_calls), 1)
        self.assertEqual(create_calls[0][3], f"original-{self.show}-s01e01")

        dest = self.tmp / "installed"
        self.assertEqual(fr.main([str(dest), "--tar", str(tar_path), "--content", str(self.tmp)]), 0)
        self.assertTrue((dest / sid / "audio.mp3").is_file())

    def test_originals_require_ko_ar_readings_and_all_language_word_tables(self):
        # Korean Originals must include explicit span + reading + verb/adj/noun tables.
        ko_script = {"id": "haessal-s01e01-scene-01", "segments": [{"v": "mina", "t": "안녕하세요!"}]}
        ko_notes = {
            "schemaVersion": 1,
            "id": "haessal-s01e01-scene-01",
            "lines": [{"seg": 0, "trans": "Hello!", "words": [
                {"t": "안녕하세요!", "lemma": "안녕하다", "pos": "adj", "stress": None, "gloss": "hello", "gram": "polite"}
            ]}],
            "lexicon": {
                "안녕하다": {"lemma": "안녕하다", "stress": None, "pos": "adj", "gloss": "peaceful; hello",
                             "meanings": [{"en": "well; hello", "note": ""}], "forms": None, "moreForms": [],
                             "examples": [{"text": "안녕하세요!", "trans": "Hello!"}, {"text": "안녕히 가세요.", "trans": "Goodbye."}], "related": []}
            },
        }
        np = self.ep_dir / "ko-notes.json"
        np.write_text(json.dumps(ko_notes, ensure_ascii=False), encoding="utf-8")
        rep = v.Report()
        v.check_notes(np, ko_script, "ko", True, rep, is_original=True)
        self.assertTrue(any("explicit code-point span" in e for e in rep.errors), rep.errors)
        self.assertTrue(any("needs a reviewed spoken reading" in e for e in rep.errors), rep.errors)
        self.assertTrue(any("ko noun/adj/verb needs a forms table" in e for e in rep.errors), rep.errors)

        ko_notes["lines"][0]["words"][0].update({"span": [0, 6], "reading": "annyeonghaseyo"})
        ko_notes["lexicon"]["안녕하다"]["forms"] = {
            "title": "Forms", "columns": ["", "form"],
            "rows": [{"cells": ["dictionary", "안녕하다"]}, {"cells": ["polite", "안녕하세요"]}],
        }
        np.write_text(json.dumps(ko_notes, ensure_ascii=False), encoding="utf-8")
        rep_ok = v.Report()
        v.check_notes(np, ko_script, "ko", True, rep_ok, is_original=True)
        self.assertEqual(rep_ok.errors, [])


if __name__ == "__main__":
    unittest.main()
