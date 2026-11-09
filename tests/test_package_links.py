"""Packages never contain hardlinks, and the installer still reads the ones older packages do."""
import io
import os
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import fetch_renders as fr

A, B = "forms/" + "a" * 16 + ".mp3", "forms/" + "b" * 16 + ".mp3"


def write_tar(path, members):
    with tarfile.open(path, "w") as tar:
        for name, data, link in members:
            info = tarfile.TarInfo(name)
            if link:
                info.type, info.linkname = tarfile.LNKTYPE, link
            else:
                info.size = len(data)
            tar.addfile(info, None if link else io.BytesIO(data))


class PackageLinks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tar = Path(self.tmp.name) / "p.tar"

    def tearDown(self):
        self.tmp.cleanup()

    def test_hardlink_member_gets_its_targets_bytes(self):
        write_tar(self.tar, [(A, b"clip", None), (B, b"", A)])
        self.assertEqual(fr.read_package(self.tar), {A: b"clip", B: b"clip"})

    def test_hardlink_to_unsafe_or_missing_target_is_refused(self):
        for target in ("../../etc/passwd", "forms/" + "c" * 16 + ".mp3"):
            write_tar(self.tar, [(A, b"clip", None), (B, b"", target)])
            with self.assertRaises(SystemExit):
                fr.read_package(self.tar)

    def test_hardlink_with_unsafe_name_is_refused(self):
        write_tar(self.tar, [(A, b"clip", None), ("evil.mp3", b"", A)])
        with self.assertRaises(SystemExit):
            fr.read_package(self.tar)

    def test_symlink_is_refused(self):
        with tarfile.open(self.tar, "w") as tar:
            info = tarfile.TarInfo(A); info.type, info.linkname = tarfile.SYMTYPE, "x"
            tar.addfile(info)
        with self.assertRaises(SystemExit):
            fr.read_package(self.tar)

    def test_packager_writes_same_inode_files_as_regular_members(self):
        store = Path(self.tmp.name) / "store"
        (store / "forms").mkdir(parents=True)
        (store / A).write_bytes(b"clip")
        os.link(store / A, store / B)
        with tarfile.open(self.tar, "w") as tar:                  # the loop package_render.main uses
            import package_render as pr
            pr.add_files(tar, store, [A, B])
        with tarfile.open(self.tar) as tar:
            self.assertTrue(all(m.isfile() for m in tar.getmembers()))
        self.assertEqual(fr.read_package(self.tar), {A: b"clip", B: b"clip"})


if __name__ == "__main__":
    unittest.main()
