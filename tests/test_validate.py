import copy, json, shutil, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate as v

EX = ROOT / "examples" / "kukhnya-s01e02-knife"


def run(path, script=False, require=False, lang="ru"):
    v.REQ[0] = require
    rep = v.Report()
    if script:
        v.LENIENT_VERSION[0] = True     # like `validate.py --script`: examples/ predate the schema
        try: v.check_script(path, lang, rep)
        finally: v.LENIENT_VERSION[0] = False
    else:
        v.check_scenes(Path(path), "kukhnya", rep)
    return rep


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.ep = self.tmp / "kukhnya" / "s01e02"
        self.ep.mkdir(parents=True)
        (self.tmp / "kukhnya" / "characters.md").write_text("Story role key / voice: `chef` -> anja")
        self.script = json.loads((EX / "scene.json").read_text(encoding="utf-8"))
        self.script.update({"id": "kukhnya-s01e02-scene-01", "schemaVersion": 1, "show": "kukhnya", "season": 1,
                            "episode": 2, "scene": 1})
        self.script["source"]["show"] = "Кухня (Kukhnya) S1.02"
        self.script["title"] = "Где мой нож?  (Where's My Knife?)"
        self.scenes = {"schemaVersion": 1, "show": "kukhnya", "season": 1, "episode": 2, "title": None, "scenes": [
            {"scene": 1, "start": "00:00:00,000", "end": "00:24:11,000", "title": "t", "summary": "s",
             "characters": ["a"], "location": "kitchen", "merge": None}]}
        self.write()

    def tearDown(self): shutil.rmtree(self.tmp)

    def write(self):
        (self.ep / "scenes.json").write_text(json.dumps(self.scenes, ensure_ascii=False))
        (self.ep / "scene-01.json").write_text(json.dumps(self.script, ensure_ascii=False))
        shutil.copy(EX / "art.webp", self.ep / "scene-01.webp")

    def errs(self, **kw):
        self.write()
        return run(self.ep, **kw).errors

    def test_examples_pass(self):
        for d in (ROOT / "examples").iterdir():
            self.assertEqual(run(d / "scene.json", script=True, lang="fr" if d.name.startswith("dix") else "ru").errors, [], d.name)

    def test_notes_example_pass(self):
        rep = v.Report()
        v.LENIENT_VERSION[0] = True     # the example predates the schema and cannot be edited
        try: v.check_notes(EX / "scene.notes.json", self.script, "ru", False, rep)
        finally: v.LENIENT_VERSION[0] = False
        self.assertEqual(rep.errors, [])

    def test_clean_episode(self):
        self.assertEqual(self.errs(), [])

    def test_missing_art(self):
        self.write(); (self.ep / "scene-01.webp").unlink()
        self.assertTrue(any("missing art" in e for e in run(self.ep).errors))

    def test_uncovered_cues(self):
        self.scenes["scenes"][0]["end"] = "00:10:00,000"
        self.assertTrue(any("outside every scene" in e for e in self.errs()))

    def test_scene_numbering(self):
        self.scenes["scenes"][0]["scene"] = 2
        self.assertTrue(any("without gaps" in e for e in self.errs()))

    def test_stress_mark_in_text(self):
        self.script["segments"][2]["t"] = "Шеф, я не брала́."
        self.assertTrue(any("stress mark" in e for e in self.errs()))

    def test_narrator_cyrillic(self):
        self.script["segments"][0]["t"] = "Say Шеф now."
        self.assertTrue(any("English only" in e for e in self.errs()))

    def test_latin_in_russian(self):
        self.script["segments"][2]["t"] = "Chef, я не брала."
        self.assertTrue(any("Latin" in e for e in self.errs()))

    def test_bad_source_fragment(self):
        self.script["source"]["lines"][0]["fragment"] = "совсем другое"
        self.assertTrue(any("fragment" in e for e in self.errs()))

    def test_merge_scene_needs_no_script(self):
        self.scenes["scenes"][0]["end"] = "00:24:00,000"
        self.scenes["scenes"].append({"scene": 2, "start": "00:24:00,000", "end": "00:24:11,000", "title": "t",
                                      "summary": "s", "characters": [], "location": "x", "merge": "prev"})
        self.assertEqual(self.errs(), [])

    def test_notes_stray_acute(self):
        n = json.loads((EX / "scene.notes.json").read_text(encoding="utf-8"))
        n["lines"][0]["trans"] = "Chef́"
        p = self.tmp / "n.json"; p.write_text(json.dumps(n, ensure_ascii=False))
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep)
        self.assertTrue(any("U+0301" in e for e in rep.errors))

    # ---- schema (spec/schema/*.json) and the rules that come with it
    def test_schema_version_required(self):
        del self.scenes["schemaVersion"]
        self.assertTrue(any("schemaVersion" in e for e in self.errs()))
        self.scenes["schemaVersion"] = 1
        del self.script["schemaVersion"]
        self.assertTrue(any("schemaVersion" in e for e in self.errs()))

    def test_schema_unknown_field(self):
        self.scenes["scenes"][0]["cue_start"] = 1
        self.assertTrue(any("unknown field 'cue_start'" in e for e in self.errs()))

    def test_schema_title_format(self):
        for bad in ("Где мой нож? (Where's My Knife?)", "Где мой нож?  (Where's  My Knife?)", "Где мой нож?  (Knife?) "):
            self.script["title"] = bad
            self.assertTrue(any("title" in e for e in self.errs()), bad)

    def test_schema_level_and_id(self):
        self.script["level"] = "beginner"
        self.assertTrue(any("$.level" in e for e in self.errs()))
        self.script["level"] = "A1 — Duolingo Section 2"
        self.script["id"] = "kukhnya-s01e02-scene-1"
        self.assertTrue(any("$.id" in e for e in self.errs()))

    def test_schema_ru_only_source_accepted(self):
        # Russian-only transcripts (eNN.ru.srt) are valid sources for scenes.json coverage and source.file
        self.assertEqual(v.schema_errors("sources/kukhnya/s02/e04.ru.srt", {"type": "string", "pattern": v.load_schema("script")["properties"]["source"]["properties"]["file"]["pattern"]}, {}), [])

    def good_notes(self):
        L = {"lemma": "шеф", "stress": "ше́ф", "pos": "noun", "gloss": "boss", "gender": "m",
             "meanings": [{"en": "boss", "note": ""}],
             "forms": {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [{"cells": ["nominative", "шеф", "шефы"]}]},
             "moreForms": [], "examples": [{"text": "Шеф здесь.", "trans": "The boss is here."}, {"text": "Где шеф?", "trans": "Where is the boss?"}],
             "related": []}
        return {"schemaVersion": 1, "id": self.script["id"], "lexicon": {"шеф": L}, "lines": [
            {"seg": 2, "trans": "Chef!", "words": [{"t": "Шеф!", "lemma": "шеф", "pos": "noun", "stress": "ше́ф", "gloss": "chef", "gram": "vocative"}]}]}

    def test_schema_notes_fields(self):
        n = self.good_notes(); sch = v.load_schema("notes")
        self.assertEqual(v.schema_errors(n, sch, sch), [])
        n["lines"][0]["words"][0]["grammar"] = "x"                      # old name for gram
        n["lexicon"]["шеф"]["aspect"] = "perfective"
        errs = v.schema_errors(n, sch, sch)
        self.assertTrue(any("unknown field 'grammar'" in e for e in errs))
        self.assertTrue(any("aspect" in e for e in errs))
        n = self.good_notes(); del n["lines"][0]["words"][0]["stress"]; n["lexicon"]["шеф"]["gender"] = "pl"
        errs = v.schema_errors(n, sch, sch)
        self.assertTrue(any("'stress'" in e for e in errs) and any("gender" in e for e in errs))

    def test_schema_checker_basics(self):
        sch = {"type": "object", "required": ["a"], "additionalProperties": False,
               "properties": {"a": {"type": ["integer", "null"], "minimum": 1}, "b": {"enum": ["x"]}}}
        self.assertEqual(v.schema_errors({"a": None, "b": "x"}, sch, sch), [])
        self.assertTrue(v.schema_errors({"a": True}, sch, sch))          # bool is not an integer
        self.assertTrue(v.schema_errors({"a": 0}, sch, sch))
        self.assertTrue(v.schema_errors({}, sch, sch))
        self.assertTrue(v.schema_errors({"a": 1, "c": 1}, sch, sch))

    def test_role_key_must_be_in_characters_md(self):
        (self.tmp / "kukhnya" / "characters.md").write_text("nothing here")
        v._KEYS.clear()
        self.assertTrue(any("`chef` is not in kukhnya/characters.md" in e for e in self.errs()))
        v._KEYS.clear()

    def test_one_voice_per_character(self):
        v.CHAR_VOICES.clear()
        for sid, voice in (("a", "anja"), ("b", "angelina")):
            self.script["voices"]["chef"] = voice
            f = self.tmp / f"{sid}.json"; f.write_text(json.dumps(self.script, ensure_ascii=False))
            v.check_script(f, "ru", v.Report())
        rep = v.Report(); v.check_voices(rep); v.CHAR_VOICES.clear()
        self.assertTrue(any("more than one voice" in e for e in rep.errors))

    def test_one_role_key_per_character(self):
        v.CHAR_KEYS.clear()
        for key in ("chef", "boss"):
            self.script["voices"] = {"narrator": "sky", "anya": "alisa", key: "anja"}
            self.script["labels"] = {key: "Шеф"}
            f = self.tmp / f"{key}.json"; f.write_text(json.dumps(self.script, ensure_ascii=False))
            v.check_script(f, "ru", v.Report())
        rep = v.Report(); v.check_voices(rep); v.CHAR_KEYS.clear()
        self.assertTrue(any("more than one role key" in e for e in rep.errors))

    def test_words_must_be_whitespace_tokens(self):
        n = self.good_notes()
        self.script["segments"][2]["t"] = "Шеф! — Да."
        n["lines"][0]["words"][0]["t"] = "Шеф!"            # "Да." missing
        p = self.tmp / "n.json"; p.write_text(json.dumps(n, ensure_ascii=False))
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep)
        self.assertTrue(any("whitespace-separated tokens" in e for e in rep.errors))
        self.script["segments"][2]["t"] = "Шеф! —"          # a bare dash needs no entry
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep)
        self.assertFalse(any("whitespace-separated tokens" in e for e in rep.errors))

    def test_multisyllable_word_needs_stress(self):
        n = self.good_notes(); n["lines"][0]["words"][0].update({"t": "Здравствуйте!", "stress": None})
        self.script["segments"][2]["t"] = "Здравствуйте!"
        p = self.tmp / "n.json"; p.write_text(json.dumps(n, ensure_ascii=False))
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep)
        self.assertTrue(any("needs a stress value" in e for e in rep.errors))

    def test_closing_line_is_a_farewell(self):
        story_line = next(x["t"] for x in self.script["segments"][2:] if x["v"] != "narrator")
        self.script["segments"][-1]["t"] = story_line
        self.assertTrue(any("must be a short farewell" in e for e in self.errs()))
        self.script["segments"][-1]["t"] = "До свидания!"
        self.assertFalse(any("farewell" in e for e in self.errs()))

    def test_source_cue_must_be_inside_scene(self):
        self.scenes["scenes"][0].update({"end": "00:24:11,000", "start": "00:00:00,000"})
        self.assertEqual(self.errs(), [])
        cue = self.script["source"]["lines"][0]["cue"]
        start = v.parse_srt(ROOT / self.script["source"]["file"])[cue][0]
        self.scenes["scenes"][0]["start"] = v.fmt(start + 60)      # scene now begins after the cue it cites
        self.assertTrue(any("outside this scene's time range" in e for e in self.errs()))

    def test_lexicon_must_agree_across_scenes(self):
        v.LEX_SEEN.clear()
        for aspect in ("pf", "impf"):
            n = self.good_notes(); n["lexicon"]["шеф"]["aspect"] = aspect
            p = self.tmp / f"{aspect}.json"; p.write_text(json.dumps(n, ensure_ascii=False))
            v.check_notes(p, self.script, "ru", False, v.Report())
        rep = v.Report(); v.check_lexicon(rep); v.LEX_SEEN.clear()
        self.assertTrue(any("conflicting aspect" in e for e in rep.errors))

    def test_identical_art_in_two_scenes(self):
        v.ART_SEEN.clear()
        self.errs()
        v.ART_SEEN.setdefault(next(iter(v.ART_SEEN)), []).append("kukhnya/s01e03/scene-04")   # a second scene with the same picture
        rep = v.Report(); v.check_art(rep); v.ART_SEEN.clear()
        self.assertTrue(any("more than one scene" in e for e in rep.errors))

    def test_lexicon_stress_mark(self):
        n = self.good_notes(); n["lexicon"]["шеф"].update({"lemma": "красивый", "stress": "красивый"})
        n["lexicon"]["красивый"] = n["lexicon"].pop("шеф")
        p = self.tmp / "n.json"; p.write_text(json.dumps(n, ensure_ascii=False))
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep); v.LEX_SEEN.clear()
        self.assertTrue(any("lacks the U+0301" in e for e in rep.errors))

    def test_placeholder_in_narration(self):
        self.script["segments"][0]["t"] = "In this scene, The characters discuss their situation. -, x."
        self.assertTrue(any("placeholder text leaked" in e for e in self.errs()))

    def test_placeholder_summary(self):
        self.scenes["scenes"][0]["summary"] = "The characters discuss their situation. -, x"
        self.assertTrue(any("placeholder summary" in e for e in self.errs()))

    def test_scenes_title_is_english_only(self):
        self.scenes["scenes"][0]["title"] = "Где нож  (Knife)"
        self.assertTrue(any("scenes[0].title" in e for e in self.errs()))

    def test_art_must_be_1024_square(self):
        self.write(); (self.ep / "scene-01.webp").write_bytes(b"RIFF\x00\x00\x00\x00WEBPVP8 " + b"\x00" * 30)
        self.assertTrue(any("1024x1024" in e for e in run(self.ep).errors))

    def test_notes_id_must_match_script(self):
        n = self.good_notes(); n["id"] = "kukhnya-s01e02-scene-09"
        p = self.tmp / "n.json"; p.write_text(json.dumps(n, ensure_ascii=False))
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep)
        self.assertTrue(any("must equal the script id" in e for e in rep.errors))

    def test_russian_only_source_for_coverage(self):
        # no dual sidecar for this episode, only eNN.ru.srt: scenes.json is checked against it
        ep = self.tmp / "kukhnya" / "s02e04"; ep.mkdir()
        self.scenes.update({"season": 2, "episode": 4})
        (ep / "scenes.json").write_text(json.dumps(self.scenes, ensure_ascii=False))
        rep = v.Report(); v.REQ[0] = False; v.check_scenes(ep, "kukhnya", rep)
        self.assertFalse(any("source subtitles missing" in e for e in rep.errors), rep.errors)


if __name__ == "__main__":
    unittest.main()
