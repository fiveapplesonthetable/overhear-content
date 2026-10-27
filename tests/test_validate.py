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
        v.check_script(path, lang, rep)
    else:
        v.check_scenes(Path(path), "kukhnya", rep)
    return rep


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.ep = self.tmp / "kukhnya" / "s01e02"
        self.ep.mkdir(parents=True)
        (self.tmp / "kukhnya" / "characters.md").write_text("x")
        self.script = json.loads((EX / "scene.json").read_text(encoding="utf-8"))
        self.script["id"] = "kukhnya-s01e02-scene-01"
        self.scenes = {"show": "kukhnya", "season": 1, "episode": 2, "title": None, "scenes": [
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
        v.check_notes(EX / "scene.notes.json", self.script, "ru", False, rep)
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
        self.scenes["scenes"][0]["end"] = "00:20:00,000"
        self.scenes["scenes"].append({"scene": 2, "start": "00:20:00,000", "end": "00:24:11,000", "title": "t",
                                      "summary": "s", "characters": [], "location": "x", "merge": "prev"})
        self.assertEqual(self.errs(), [])

    def test_notes_stray_acute(self):
        n = json.loads((EX / "scene.notes.json").read_text(encoding="utf-8"))
        n["lines"][0]["trans"] = "Chef́"
        p = self.tmp / "n.json"; p.write_text(json.dumps(n, ensure_ascii=False))
        rep = v.Report(); v.check_notes(p, self.script, "ru", False, rep)
        self.assertTrue(any("U+0301" in e for e in rep.errors))


if __name__ == "__main__":
    unittest.main()
