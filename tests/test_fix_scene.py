"""Sentence takes travel with packages, and tools/fix_scene.py plans a one-scene fix around them (no GPU, no network)."""
import hashlib
import io
import json
import os
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(REPO / "render"))
import check_render as cr
import fetch_renders as fr
import fix_scene
import package_render as pr

EPISODE = "demo-s01e01"
SCENES = [f"{EPISODE}-scene-0{n}" for n in (1, 2)]
KEYS = ["a" * 64, "b" * 64]


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data if isinstance(data, bytes) else json.dumps(data).encode())


def make_content(root):
    ep = root / "originals" / "demo" / "s01e01"
    write(ep / "scenes.json", {"show": "demo", "season": 1, "episode": 1, "scenes": [{"scene": 1}, {"scene": 2}]})
    for n in (1, 2):
        write(ep / f"scene-0{n}.json", {"pair": "es-en"})
        write(ep / f"scene-0{n}.notes.json", {"lexicon": {}})


def make_store(store, content, takes=True):
    """A store whose scene 1 lists two takes (both on disk) and whose scene 2 lists none."""
    for sid in SCENES:
        n = sid[-1]
        ep = content / "originals" / "demo" / "s01e01"
        meta = {"sceneId": sid, "contentHash": cr.content_hash(ep / f"scene-0{n}.json", ep / f"scene-0{n}.notes.json"),
                "audioSha256": "0" * 64, "durationSec": 1.0}
        if takes and sid == SCENES[0]:
            meta["sentenceTakes"] = {k: f"sentence {i}" for i, k in enumerate(KEYS)}
        write(store / sid / "meta.json", meta)
        for f in ("audio.mp3", "spans.json", "timing.json", "report.json"):
            write(store / sid / f, b"x")
    if takes:
        for k in KEYS:
            write(store / "cache" / "tts" / f"{k}.flac", b"flac " + k.encode())
        write(store / "cache" / "tts" / f"{KEYS[0]}.gates.json", {"takes": 1})


def build_tar(path, store, content, takes_of=None):
    """What package_render.main writes, minus the check_render run and the GitHub release."""
    scenes, files, plan = pr.episode_files(store, content, EPISODE, root="originals", takes_of=takes_of)
    plan_b = b"[]"
    manifest = {"schemaVersion": 1, "episode": EPISODE, "root": "originals", "contentCommit": "c" * 40,
                "scenes": [{"sceneId": s, **{k: json.loads((store / s / "meta.json").read_text())[k] for k in ("contentHash", "audioSha256", "durationSec")}} for s in scenes],
                "files": {f: cr.sha256_file(store / f) for f in files}}
    manifest["files"][f"forms-plan/{EPISODE}.json"] = hashlib.sha256(plan_b).hexdigest()
    with tarfile.open(path, "w") as tar:
        pr.add_files(tar, store, files)
        for name, data in ((f"forms-plan/{EPISODE}.json", plan_b), ("MANIFEST.json", json.dumps(manifest).encode())):
            info = tarfile.TarInfo(name); info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    return files


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.content, self.store = self.dir / "content", self.dir / "store"
        make_content(self.content)

    def tearDown(self):
        self.tmp.cleanup()


class PackageTakes(Base):
    def test_takes_of_the_scenes_meta_ship_with_their_gates_record(self):
        make_store(self.store, self.content)
        _, files, _ = pr.episode_files(self.store, self.content, EPISODE, root="originals")
        takes = {f for f in files if f.startswith("cache/")}
        self.assertEqual(takes, {f"cache/tts/{KEYS[0]}.flac", f"cache/tts/{KEYS[0]}.gates.json", f"cache/tts/{KEYS[1]}.flac"})

    def test_takes_of_limits_which_scenes_ship_theirs(self):
        make_store(self.store, self.content)
        _, files, _ = pr.episode_files(self.store, self.content, EPISODE, root="originals", takes_of={SCENES[1]})
        self.assertFalse([f for f in files if f.startswith("cache/")])
        self.assertIn(f"{SCENES[0]}/audio.mp3", files)

    def test_a_scene_rendered_before_the_takes_were_recorded_ships_none(self):
        make_store(self.store, self.content, takes=False)
        _, files, _ = pr.episode_files(self.store, self.content, EPISODE, root="originals")
        self.assertFalse([f for f in files if f.startswith("cache/")])

    def test_a_listed_take_missing_from_the_store_is_skipped(self):
        make_store(self.store, self.content)
        (self.store / "cache" / "tts" / f"{KEYS[1]}.flac").unlink()
        self.assertEqual(pr.take_files(self.store, SCENES[0]), [f"cache/tts/{KEYS[0]}.flac", f"cache/tts/{KEYS[0]}.gates.json"])

    def test_linked_files_are_packed_as_regular_members(self):
        make_store(self.store, self.content)
        other = self.dir / "other" / "x.flac"
        write(other, b"bytes")
        (self.store / "cache" / "tts" / "linked.flac").symlink_to(other)
        with tarfile.open(self.dir / "t.tar", "w") as tar:
            pr.add_files(tar, self.store, ["cache/tts/linked.flac"])
        with tarfile.open(self.dir / "t.tar") as tar:
            (m,) = tar.getmembers()
            self.assertTrue(m.isfile())
            self.assertEqual(tar.extractfile(m).read(), b"bytes")


class InstallTakes(Base):
    def test_install_puts_takes_in_the_sentence_cache(self):
        make_store(self.store, self.content)
        build_tar(self.dir / "p.tar", self.store, self.content)
        render = self.dir / "render"
        fr.install(self.dir / "p.tar", render, self.content, root="originals")
        self.assertEqual((render / "cache" / "tts" / f"{KEYS[1]}.flac").read_bytes(), b"flac " + KEYS[1].encode())
        self.assertTrue((render / SCENES[0] / "meta.json").is_file())

    def test_cache_dir_option_redirects_the_takes(self):
        make_store(self.store, self.content)
        build_tar(self.dir / "p.tar", self.store, self.content)
        fr.install(self.dir / "p.tar", self.dir / "render", self.content, root="originals", cache=self.dir / "takes")
        self.assertTrue((self.dir / "takes" / f"{KEYS[0]}.flac").is_file())
        self.assertFalse((self.dir / "render" / "cache").exists())

    def test_a_package_without_takes_still_installs(self):
        make_store(self.store, self.content, takes=False)
        build_tar(self.dir / "p.tar", self.store, self.content)
        render = self.dir / "render"
        fr.install(self.dir / "p.tar", render, self.content, root="originals")
        self.assertTrue((render / SCENES[1] / "meta.json").is_file())
        self.assertFalse((render / "cache").exists())

    def test_a_take_with_a_wrong_checksum_is_refused(self):
        make_store(self.store, self.content)
        build_tar(self.dir / "p.tar", self.store, self.content)
        (self.store / "cache" / "tts" / f"{KEYS[0]}.flac").write_bytes(b"tampered")
        build = self.dir / "q.tar"
        with tarfile.open(self.dir / "p.tar") as src, tarfile.open(build, "w") as dst:
            for m in src.getmembers():
                data = src.extractfile(m).read()
                if m.name.endswith(f"{KEYS[0]}.flac"):
                    data = b"tampered"
                m.size = len(data)
                dst.addfile(m, io.BytesIO(data))
        with self.assertRaises(SystemExit):
            fr.install(build, self.dir / "render", self.content, root="originals")

    def test_a_take_name_outside_the_layout_is_refused(self):
        with tarfile.open(self.dir / "bad.tar", "w") as tar:
            info = tarfile.TarInfo("cache/tts/../../evil.flac"); info.size = 1
            tar.addfile(info, io.BytesIO(b"x"))
        with self.assertRaises(SystemExit):
            fr.read_package(self.dir / "bad.tar")


class FixPlanning(Base):
    def test_scenes_group_by_episode_and_bad_ids_are_refused(self):
        self.assertEqual(fix_scene.by_episode(["a-b-s01e02-scene-03", "a-b-s01e02-scene-01", "c-s03e01-scene-01"]),
                         {"a-b-s01e02": ["a-b-s01e02-scene-03", "a-b-s01e02-scene-01"], "c-s03e01": ["c-s03e01-scene-01"]})
        with self.assertRaises(SystemExit):
            fix_scene.by_episode(["a-b-s01e02"])

    def test_scaling_never_changes_a_render_or_sentence_key(self):
        import config
        profiles = sorted((REPO / "render").glob("settings*.json"))
        self.assertGreater(len(profiles), 10)
        for profile in profiles:
            scaled_file = self.dir / profile.name
            scaled_file.write_text(json.dumps(fix_scene.scaled_settings(profile, 7000, 3)))
            before, after = config.load_settings(profile), config.load_settings(scaled_file)
            self.assertEqual(config.tts_signature(before), config.tts_signature(after), profile.name)
            self.assertEqual(config.assembly_signature(before), config.assembly_signature(after), profile.name)
            for lang in before["tts"]["languages"]:
                self.assertEqual(config.sentence_signature(before, lang), config.sentence_signature(after, lang), (profile.name, lang))

    def test_scaling_caps_reservations_and_batches_only(self):
        s = fix_scene.scaled_settings(REPO / "render" / "settings.es-qwen-en.json", 7000, 3)
        self.assertLessEqual(max(v for k, v in s["gpu"].items() if k.endswith("MiB")), 7000)
        self.assertEqual((s["tts"]["batch"], s["tts"]["batchEn"]), (3, 3))
        self.assertEqual(s["gpu"]["alignMiB"], 1500)

    def test_every_originals_show_has_a_profile_that_scales(self):
        import fix_episode
        for show in sorted(p.name for p in (REPO / "originals").iterdir() if p.is_dir() and not p.name.startswith("_")):
            self.assertTrue((REPO / fix_episode.settings_for(show)).is_file(), show)

    def test_assemble_links_the_installed_scenes_and_keeps_the_fixed_one_real(self):
        installed, work = self.dir / "installed", self.dir / "work"
        make_store(installed, self.content)
        (installed / "clips").mkdir()
        write(work / SCENES[0] / "meta.json", {})                      # an earlier render of the scene being fixed
        (work / SCENES[1]).mkdir(parents=True)                         # and a stale one of a scene that is not
        fix_scene.assemble(work, installed, SCENES, {SCENES[0]})
        self.assertFalse((work / SCENES[0]).is_symlink())
        self.assertEqual(os.readlink(work / SCENES[1]), str(installed / SCENES[1]))
        self.assertEqual(os.readlink(work / "clips"), str(installed / "clips"))
        fix_scene.assemble(work, installed, SCENES, {SCENES[0]})        # idempotent

    def test_assemble_names_an_episode_scene_the_receiver_lacks(self):
        installed = self.dir / "installed"
        make_store(installed, self.content)
        (installed / SCENES[1] / "meta.json").unlink()
        with self.assertRaises(SystemExit) as e:
            fix_scene.assemble(self.dir / "work", installed, SCENES, {SCENES[0]})
        self.assertIn(SCENES[1], str(e.exception))

    def test_a_real_folder_is_never_replaced_by_a_link(self):
        installed, work = self.dir / "installed", self.dir / "work"
        make_store(installed, self.content)
        (work / "clips").mkdir(parents=True)
        (installed / "clips").mkdir()
        with self.assertRaises(SystemExit):
            fix_scene.assemble(work, installed, SCENES, {SCENES[0]})

    def test_sentence_report_splits_reused_from_new_takes(self):
        takes = {"k1": "kept sentence", "k2": "edited sentence"}
        self.assertEqual(fix_scene.sentence_report(takes, {"k1", "other"}), (["kept sentence"], ["edited sentence"]))

    def test_installed_takes_lists_cache_keys(self):
        make_store(self.store, self.content)
        self.assertEqual(fix_scene.installed_takes(self.store), set(KEYS))

    def test_seeding_links_takes_with_their_gates_records(self):
        import fix_episode
        make_store(self.store, self.content)
        work = self.dir / "work"
        self.assertEqual(fix_episode.seed_cache(self.store, work, rels=("cache/tts",)), 3)
        self.assertTrue((work / "cache" / "tts" / f"{KEYS[0]}.gates.json").is_file())
        self.assertFalse((work / SCENES[0]).exists())

    def test_check_rendered_flags_stale_and_unresolved_scenes(self):
        make_store(self.store, self.content)
        write(self.store / SCENES[0] / "report.json", {"stress": {"stillFlagged": 2}, "timing": {"notOk": 0}})
        problems = fix_scene.check_rendered(self.store, SCENES[0], self.content, "originals")
        self.assertEqual(problems, ["2 sentences still flagged by the stress check"])
        write(self.store / SCENES[1] / "report.json", {"stress": {"stillFlagged": 0}, "timing": {"notOk": 0}})
        write(self.content / "originals/demo/s01e01/scene-02.json", {"pair": "es-en", "edited": True})
        self.assertEqual(fix_scene.check_rendered(self.store, SCENES[1], self.content, "originals"),
                         ["rendered from other content than this checkout"])


if __name__ == "__main__":
    unittest.main()
