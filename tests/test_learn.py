"""Learn notes (learn/<pair>/<id>.json): the real notes validate, and the checks catch what they should."""
import copy, json, shutil, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate as v

NOTE = {"schemaVersion": 1, "id": "one", "pair": "ru-en", "section": "verbs", "order": 1, "title": {"en": "One"}, "summary": {"en": "s"},
        "body": {"en": "b"}, "related": [], "examples": [{"sceneId": "kukhnya-s01e02-scene-01", "seg": 1}], "tags": ["один"]}


def run(root):
    rep = v.Report()
    v.check_learn(root, rep)
    return rep.errors


class RealNotes(unittest.TestCase):
    def test_the_published_notes_are_valid(self):
        self.assertEqual(run(ROOT), [])


class Checks(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        sc = self.root / "out" / "kukhnya" / "s01e02"
        sc.mkdir(parents=True)
        (sc / "scene-01.json").write_text(json.dumps({"segments": [{"v": "narrator", "t": "x"}, {"v": "max", "t": "Привет"}]}), "utf-8")
        self.dir = self.root / "learn" / "ru-en"
        self.dir.mkdir(parents=True)

    def tearDown(self): shutil.rmtree(self.root)

    def put(self, name, **over):
        d = {**copy.deepcopy(NOTE), **over}
        (self.dir / f"{name}.json").write_text(json.dumps(d), "utf-8")

    def test_valid(self):
        self.put("one")
        self.assertEqual(run(self.root), [])

    def test_schema_id_pair_related_and_examples(self):
        self.put("one", section="")
        self.assertTrue(any("schema" in e for e in run(self.root)))
        self.put("one", id="two")
        self.assertTrue(any("file name" in e for e in run(self.root)))
        self.put("one", pair="fr-en")
        self.assertTrue(any("folder" in e for e in run(self.root)))
        self.put("one", related=["nope"])
        self.assertTrue(any("related" in e for e in run(self.root)))
        for ex, text in (({"sceneId": "kukhnya-s01e02-scene-01", "seg": 0}, "narrator"), ({"sceneId": "kukhnya-s01e02-scene-01", "seg": 9}, "segments"),
                         ({"sceneId": "kukhnya-s01e02-scene-09", "seg": 0}, "does not exist")):
            self.put("one", examples=[ex])
            self.assertTrue(any(text in e for e in run(self.root)), text)


if __name__ == "__main__":
    unittest.main()
