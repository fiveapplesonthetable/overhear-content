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
        self.cast = {"schemaVersion": 1, "show": "kukhnya", "other_names": ["Claude Monet"], "cast": [
            {"key": "barinov", "ru": "Шеф", "en": ["Barinov", "Viktor", "Chef"], "gender": "m"},
            {"key": "nastya", "ru": "Настя", "en": ["Nastya"], "gender": "f"},
            {"key": "max", "ru": "Макс", "en": ["Max", "Maksim", "Lavrov"], "gender": "m"}]}
        self.write_cast()
        # examples/ predates cast.json: map its slot keys onto the character keys and drop `voices`
        raw = (EX / "scene.json").read_text(encoding="utf-8").replace('"anya"', '"nastya"').replace('"chef"', '"barinov"').replace("Anya", "Nastya")
        self.script = json.loads(raw)
        del self.script["voices"]
        self.script["labels"] = {"barinov": "Шеф", "nastya": "Настя"}
        self.script.update({"id": "kukhnya-s01e02-scene-01", "schemaVersion": 1, "show": "kukhnya", "season": 1,
                            "episode": 2, "scene": 1})
        self.script["source"]["show"] = "Кухня (Kukhnya) S1.02"
        self.script["title"] = "Где мой нож?  (Where's My Knife?)"
        self.scenes = {"schemaVersion": 1, "show": "kukhnya", "season": 1, "episode": 2, "title": None, "scenes": [
            {"scene": 1, "start": "00:00:00,000", "end": "00:24:11,000", "title": "t", "summary": "s",
             "characters": ["a"], "location": "kitchen", "merge": None}]}
        self.write()

    def tearDown(self): shutil.rmtree(self.tmp)

    def write_cast(self):
        (self.tmp / "kukhnya" / "cast.json").write_text(json.dumps(self.cast, ensure_ascii=False))
        v._CAST.clear()

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

    def test_merged_transition_cues_belong_to_lesson(self):
        # The example story uses cues 76 onwards. Split that source stretch
        # across an explicitly merged neighbour, then verify both directions.
        for direction in ("prev", "next"):
            with self.subTest(direction=direction):
                first = copy.deepcopy(self.scenes["scenes"][0])
                first.update(end="00:10:00,000", merge="next" if direction == "next" else None)
                second = dict(first, scene=2, start="00:10:00,000", end="00:24:11,000",
                              merge="prev" if direction == "prev" else None)
                self.scenes["scenes"] = [first, second]
                self.write()
                if direction == "next":
                    script = copy.deepcopy(self.script)
                    script.update(id="kukhnya-s01e02-scene-02", scene=2)
                    (self.ep / "scene-02.json").write_text(json.dumps(script, ensure_ascii=False))
                    shutil.copy(EX / "art.webp", self.ep / "scene-02.webp")
                self.assertEqual(run(self.ep).errors, [])
        # Removing the merge relationship must still reject those same cues.
        self.scenes["scenes"][0]["merge"] = None
        self.write()
        self.assertTrue(any("source cues lie outside" in e for e in run(self.ep).errors))

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

    # ---- P-1: one character = one role key, taken from cast.json; names in the narration match the speaker
    def test_cast_missing(self):
        (self.tmp / "kukhnya" / "cast.json").unlink(); v._CAST.clear()
        self.assertTrue(any("missing cast.json" in e for e in self.errs()))

    def test_cast_slot_key_is_rejected(self):
        self.cast["cast"].append({"key": "anya", "ru": "Аня", "en": ["Anya"], "gender": "f"}); self.write_cast()
        self.assertTrue(any("viewpoint/protagonist slot" in e for e in self.errs()))

    def test_cast_schema_and_duplicates(self):
        self.cast["cast"][1]["gender"] = "x"; self.write_cast()
        self.assertTrue(any("cast.json" in e and "gender" in e for e in self.errs()))
        self.cast["cast"][1]["gender"] = "f"
        self.cast["cast"].append({"key": "boss", "ru": "Шеф", "en": ["Boss"], "gender": "m"}); self.write_cast()   # same person, second key
        self.assertTrue(any("same display name" in e for e in self.errs()))

    def test_role_key_must_be_in_cast(self):
        for seg in self.script["segments"]:
            if seg["v"] == "nastya": seg["v"] = "vika"
        self.script["labels"] = {"barinov": "Шеф", "vika": "Вика"}
        errs = self.errs()
        self.assertTrue(any("role key `vika` is not in cast.json" in e for e in errs))

    def test_slot_key_in_script_is_rejected(self):
        for seg in self.script["segments"]:
            if seg["v"] == "nastya": seg["v"] = "anya"
        self.script["labels"] = {"barinov": "Шеф", "anya": "Настя"}
        self.assertTrue(any("`anya` is not in cast.json (viewpoint slot" in e for e in self.errs()))

    def test_voices_field_is_gone(self):
        self.script["voices"] = {"narrator": "sky", "nastya": "angelina", "barinov": "anja"}
        self.assertTrue(any("unknown field 'voices'" in e for e in self.errs()))

    def test_label_must_equal_cast_ru(self):
        self.script["labels"]["barinov"] = "Баринов"
        self.assertTrue(any("label for `barinov` is 'Баринов', cast.json says 'Шеф'" in e for e in self.errs()))

    def narr(self, i, text):
        self.script["segments"][i]["t"] = text

    def first_gloss_index(self):
        return next(i for i, s in enumerate(self.script["segments"]) if i and s["v"] == "narrator" and self.script["segments"][i - 1]["v"] != "narrator" and v.split_gloss(s["t"]))

    def test_narrator_name_must_be_in_cast(self):
        self.narr(0, "Vasily walks into the kitchen. " + self.script["segments"][0]["t"])
        self.assertTrue(any("narration names 'Vasily'" in e for e in self.errs()))
        self.narr(0, "Max and Viktor Barinov meet at Claude Monet. Maksim's day starts badly. Nobody expects the Russian chef.")
        self.assertFalse(any("narration names" in e for e in self.errs()))

    def test_narrator_names_the_actual_speaker(self):
        i = self.first_gloss_index(); who = self.script["segments"][i - 1]["v"]
        other, ok = ("Nastya", "Barinov") if who == "barinov" else ("Barinov", "Nastya")
        self.narr(i, "'He says it.' " + other + " says it with a smile.")
        self.assertTrue(any(f"narration says {other!r} did this" in e for e in self.errs()))
        for good in (ok + " says it with a smile.", "He says it with a smile.", "The speaker says it with a smile."):
            self.narr(i, "'He says it.' " + good)
            self.assertFalse(any("did this but" in e for e in self.errs()), good)

    def test_gender_heuristic_is_a_warning(self):
        seg = next(s for s in self.script["segments"] if s["v"] == "barinov")
        seg["t"] = "Я вчера пошла домой."
        self.write(); rep = run(self.ep)
        self.assertTrue(any("is male but says 'пошла'" in e for e in rep.warnings))
        self.assertFalse(any("пошла" in e for e in rep.errors))
        seg["t"] = "Я вчера пошёл домой. Это была ошибка."
        self.write(); self.assertFalse(any("is male" in e for e in run(self.ep).warnings))

    # ---- P-1 problem 2: explanations that sound like a person
    def segs_with(self, explanations, speaker="barinov"):
        segs = [{"v": "narrator", "t": "Intro.", "gap": 0.5}]
        for k, e in enumerate(explanations):
            segs.append({"v": speaker, "t": "Привет.", "gap": 0.5})
            segs.append({"v": "narrator", "t": "'Hello, number %d.' %s" % (k, e), "gap": 0.5})
        return {"id": "x-s01e01-scene-01", "show": "kukhnya", "segments": segs}

    def explain(self, explanations, cast=True):
        v.TEMPLATE_SEEN.clear(); rep = v.Report()
        v.check_explanations("w", self.segs_with(explanations), "kukhnya", v.load_cast(self.tmp / "kukhnya", v.Report()) if cast else None, rep)
        v.check_templates(rep)
        return rep.errors

    def test_template_detector(self):
        template = ["Notice how naturally this everyday Russian phrase expresses the point number %d." % k for k in range(v.TEMPLATE_MAX + 1)]
        errs = self.explain(template)
        self.assertEqual(len([e for e in errs if "reused template" in e]), v.TEMPLATE_MAX + 1)       # an error on every line
        self.assertEqual([e for e in self.explain(template[:v.TEMPLATE_MAX]) if "reused template" in e], [])   # exactly the limit is fine
        # same skeleton although the quoted words and the names differ
        named = ["Here Max puts 'cat %d' before 'dog' for emphasis." % k for k in range(v.TEMPLATE_MAX)] + ["Here Nastya puts 'sun' before 'moon' for emphasis."]
        self.assertTrue(any("reused template" in e for e in self.explain(named)))

    def test_natural_repeats_do_not_trip_the_detector(self):
        openers = ["He means that the shift is over for today.", "He means it kindly, whatever it sounds like.", "This is the first time Max hears it.",
                   "It sounds rude in English, but it is only a joke.", "Barinov says it with a smile.", "You will hear this one all the time."]
        errs = self.explain(openers * 2)       # each opening appears twice
        self.assertEqual([e for e in errs if "reused template" in e], [])

    def test_skeleton_normalisation(self):
        a, _ = v.skeleton("Max puts 'cat' before 'dog' to stress it.", {"Max"})
        b, _ = v.skeleton("Barinov puts 'sun' before 'moon' to stress it.", {"Barinov"})
        self.assertEqual(a, b)
        self.assertEqual(a, "N puts Q before Q to")

    def test_grammar_label_ending(self):
        for bad in ("The chef confronts Max with a past tense verb and duration phrase.", "Barinov barks his insult using command form verbs.",
                    "She explains it via the dative case.", "Max protests politely with past and future verbs."):
            self.assertTrue(any("grammar label" in e for e in self.explain([bad])), bad)
        for good in ("Barinov doesn't say 'Max'. He uses the surname, the way a stern boss puts you in your place.",
                     "It's what you'd shout at a group who all owe you money.", "Max protests politely, with a sigh."):
            self.assertEqual([e for e in self.explain([good]) if "grammar label" in e], [], good)

    def test_grammar_density(self):
        jargon = "The verb is in the past tense and the noun is in the accusative case."
        plain = "He is gloating because he had money on Max being late."
        self.assertTrue(any("use grammar terms" in e for e in self.explain([jargon] * 3 + [plain] * 3)))
        self.assertEqual([e for e in self.explain([jargon] + [plain] * 7) if "use grammar terms" in e], [])         # 1 of 8
        self.assertEqual([e for e in self.explain([jargon] * 3) if "use grammar terms" in e], [])                    # too few lines to judge

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
        self.assertTrue(any("outside this lesson's scene and merged source ranges" in e for e in self.errs()))

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


    # ---- P-2: teaching share and show-wide repeated phrases
    PLOT = ["Max tries to greet his tense friend.", "Kostya aggressively warns his friend to back off.", "Vika finds the waitress crying in the corridor.",
            "Nastya admits how painful the sudden rejection feels.", "Barinov loudly summons his team for a crucial tasting."]
    TEACHING = ["The Russian word for 'reigns' is built from the word for tsar, so chaos is literally on the throne.",
                "Kostya's little word \"zato\" means \"but on the plus side\".", "Russian happily doubles the no here, and that's correct.",
                "Where English says \"get ready for\", Russian says something closer to \"get ready to a new workday\".",
                "It's a handy sentence for any job you find tough, so swap in your own work."]

    def teach_run(self, explanations, strict=False):
        v.TEACH_SEEN.clear(); v.STRICT_TEACH[0] = strict; rep = v.Report()
        try: v.check_teaching("w", v.explanations(self.segs_with(explanations)["segments"]), "kukhnya", rep)
        finally: v.STRICT_TEACH[0] = False
        return rep

    def test_teaching_heuristic(self):
        for t in self.TEACHING: self.assertTrue(v.teaches(t), t)
        for t in self.PLOT: self.assertFalse(v.teaches(t), t)

    def test_teaching_share_warns_or_errors(self):
        rep = self.teach_run(self.PLOT)
        self.assertEqual(rep.errors, []); self.assertEqual(len(rep.warnings), 1)
        self.assertIn("0 of 5", rep.warnings[0])
        rep = self.teach_run(self.PLOT, strict=True)
        self.assertEqual(len(rep.errors), 1); self.assertEqual(rep.warnings, [])
        for strict in (False, True):                      # 4 of 5 teach: fine
            rep = self.teach_run(self.TEACHING[:4] + self.PLOT[:1], strict)
            self.assertEqual((rep.errors, rep.warnings), ([], []))
        rep = self.teach_run(self.TEACHING[:3] + self.PLOT[:3])      # 3 of 6: below 60%
        self.assertEqual(len(rep.warnings), 1)
        rep = self.teach_run(self.TEACHING[:3] + self.PLOT[:0], strict=True)      # too few lines to judge
        self.assertEqual((rep.errors, rep.warnings), ([], []))
        rep = self.teach_run(self.TEACHING[:3] + self.PLOT[:1], strict=True)      # 3 of 4 = 75% but fewer than 4 teaching
        self.assertEqual(len(rep.errors), 1)

    def test_gold_scenes_score_high_and_draft_low(self):
        gold = [ROOT / "examples" / "kukhnya-s01e02-knife" / "scene.json", ROOT / "examples" / "kukhnya-s01e05-orders" / "scene.json"]
        gold += [ROOT / "out" / "kukhnya" / "s01e02" / f"scene-0{k}.json" for k in (1, 2, 3)]
        for g in gold:
            if not g.is_file(): continue
            ex = v.explanations(json.loads(g.read_text(encoding="utf-8"))["segments"])
            self.assertGreaterEqual(sum(v.teaches(e) for _, _, e in ex) / len(ex), v.TEACH_MIN_SHARE, g.name)
        draft = ROOT / "tests" / "fixtures" / "draft-kukhnya-s01e07-scene-05.json"    # frozen copy of the plot-only draft (origin/main before the rewrite)
        ex = v.explanations(json.loads(draft.read_text(encoding="utf-8"))["segments"])
        self.assertLess(sum(v.teaches(e) for _, _, e in ex) / len(ex), 0.3)

    def phrase_run(self, texts, show="kukhnya"):
        v.PHRASE_SEEN.clear(); rep = v.Report()
        for t in texts: v.count_phrases({"segments": [{"v": "narrator", "t": "Intro."}, {"v": "x", "t": "Привет."}, {"v": "narrator", "t": "'Hi.' " + t}]}, show, None)
        v.check_phrases(rep)
        return rep

    def test_repeated_phrase_check(self):
        texts = ["Max %s reaches for the Russian word for %d." % (n, k) for k, n in enumerate(["a", "b"] * (v.PHRASE_MAX // 2 + 1))]
        rep = self.phrase_run(texts)            # PHRASE_MAX + 2 uses, names and quoted spans do not matter
        self.assertTrue(any("reaches for the" in e for e in rep.errors), rep.errors)
        self.assertEqual(self.phrase_run(texts[:v.PHRASE_MAX]).errors, [])             # exactly the limit is fine
        mixed = ['Kostya reaches for the Russian word "x".', 'Nastya reaches for the Russian word "y".'] * v.PHRASE_MAX
        self.assertTrue(self.phrase_run(mixed).errors)
        self.assertEqual(self.phrase_run(["Pattern %d: %s %s %s." % (k, *("alpha beta gamma delta epsilon zeta eta theta".split()[(k * m) % 8] for m in (1, 3, 5))) for k in range(80)]).errors, [])

    def test_phrase_counts_each_text_once_and_per_show(self):
        v.PHRASE_SEEN.clear()
        seg = lambda t: {"segments": [{"v": "x", "t": "Привет."}, {"v": "narrator", "t": "'Hi.' " + t}]}
        v.count_phrases(seg("Some long phrase here. Some long phrase here."), "a", None)
        self.assertEqual(v.PHRASE_SEEN["a"]["some long phrase here"], 1)
        v.count_phrases(seg("Some long phrase here."), "b", None)
        self.assertEqual(v.PHRASE_SEEN["b"]["some long phrase here"], 1)

    def test_show_summary_line(self):
        self.teach_run(self.TEACHING[:2] + self.PLOT[:2])
        v.PHRASE_SEEN.clear(); v.PHRASE_SEEN["kukhnya"] = {"brings in Q to": 7}
        line = v.show_summary()[0]
        self.assertIn("kukhnya", line); self.assertIn("word-teaching: 50%", line); self.assertIn("'brings in Q to' x7", line)


if __name__ == "__main__":
    unittest.main()
