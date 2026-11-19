import hashlib
import json
import os
from pathlib import Path
import py_compile
import sys
import subprocess
import shutil
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import clean
import manage
import validate


class FilesystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "src"
        self.dest = self.root / "installed"
        self.name = "formweave-build"
        self.skill = self.source / self.name
        (self.skill / "assets" / "nested").mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("version one")
        (self.skill / "assets" / "nested" / "sample.txt").write_text("example")
        self.dest.mkdir()
        self.target = self.dest / self.name
        self.addCleanup(patch.stopall)
        patch.object(manage, "SKILLS", self.source).start()

    def call(self, action):
        manage.manage(action, self.dest, [self.name])

    def test_nested_repeat_update_and_verify(self):
        unrelated = self.dest / "other"
        unrelated.write_text("keep")
        self.call("install")
        self.call("install")
        self.call("verify")
        self.assertEqual((self.target / "assets/nested/sample.txt").read_text(), "example")
        (self.skill / "SKILL.md").write_text("version two")
        with self.assertRaises(ValueError):
            self.call("verify")
        self.call("update")
        self.call("verify")
        self.assertEqual((self.target / "SKILL.md").read_text(), "version two")
        self.assertEqual(unrelated.read_text(), "keep")

    def test_standalone_reference_cannot_escape_or_disappear(self):
        doc = self.skill / "SKILL.md"
        for url in ("../another-skill/guide.md", "references/missing.md"):
            doc.write_text(f"[read]({url})", encoding="utf-8")
            with self.assertRaises(ValueError):
                validate.check_links(doc, self.skill)
        doc.write_text("[sample](assets/nested/sample.txt)", encoding="utf-8")
        validate.check_links(doc, self.skill)

    def test_local_edits_and_unknown_directories_survive(self):
        self.target.mkdir()
        (self.target / "notes").write_text("mine")
        with self.assertRaises(ValueError):
            self.call("install")
        self.assertEqual((self.target / "notes").read_text(), "mine")
        self.target.rename(self.dest / "renamed")
        self.call("install")
        (self.target / "notes").write_text("local")
        with self.assertRaises(ValueError):
            self.call("update")
        self.assertEqual((self.target / "notes").read_text(), "local")

    def test_failed_swap_restores_previous_tree(self):
        self.call("install")
        original = manage.inventory(self.target)
        (self.skill / "SKILL.md").write_text("changed")
        rename = Path.rename
        def fail_stage(path, target):
            if path.name == "new":
                raise OSError("simulated rename failure")
            return rename(path, target)
        with patch.object(Path, "rename", fail_stage), self.assertRaises(OSError):
            self.call("update")
        self.assertEqual(manage.inventory(self.target), original)
        self.assertEqual(list(self.dest.iterdir()), [self.target])

    def test_corrupt_receipts_are_rejected_without_mutation(self):
        self.call("install")
        receipt = self.target / manage.RECEIPT
        valid = receipt.read_text(encoding="utf-8")
        data = json.loads(valid)
        invalid = [valid.replace('"format": 1', '"format": true'),
                   valid.replace('"format": 1', '"format": 0, "format": 1'),
                   json.dumps(dict(data, entries=[]))]
        for raw in invalid:
            with self.subTest(receipt=raw[:80]):
                receipt.write_text(raw, encoding="utf-8")
                before = manage.inventory(self.target)
                with self.assertRaises(ValueError):
                    self.call("verify")
                self.assertEqual(manage.inventory(self.target), before)
        receipt.write_text(valid, encoding="utf-8")
        self.call("verify")

    def test_failed_restore_preserves_recovery_tree(self):
        self.call("install")
        original = manage.inventory(self.target)
        (self.skill / "SKILL.md").write_text("changed")
        rename = Path.rename
        def fail_swap_and_restore(path, target):
            if path.name in {"new", "previous"}:
                raise OSError("simulated restore failure")
            return rename(path, target)
        with patch.object(Path, "rename", fail_swap_and_restore), self.assertRaises(OSError):
            self.call("update")
        work, = self.dest.glob(".formweave-stage-*")
        self.assertEqual(manage.inventory(work / "previous"), original)
        self.assertTrue((work / "new/SKILL.md").is_file())
        self.assertFalse(self.target.exists())
        self.assertFalse((self.dest / ".formweave-install.lock").exists())

    def test_links_lock_and_missing_verify(self):
        with self.assertRaises(ValueError):
            self.call("verify")
        lock = self.dest / ".formweave-install.lock"
        lock.write_text("busy")
        with self.assertRaises(FileExistsError):
            self.call("install")
        self.assertTrue(lock.exists())
        lock.unlink()
        os.link(self.skill / "SKILL.md", self.skill / "linked")
        with self.assertRaises(ValueError):
            self.call("install")
        self.assertFalse(self.target.exists())

    def test_cleanup_preview_digest_and_unknown(self):
        for name in ("scripts", "tests", "skills"):
            (self.root / name).mkdir()
        src = self.root / "scripts" / "example.py"
        src.write_text("answer = 42")
        bytecode = Path(py_compile.compile(str(src), doraise=True))
        unknown = bytecode.parent / "unknown.pyc"
        unknown.write_bytes(b"keep")
        items = clean.candidates(self.root)
        self.assertEqual(list(items), [bytecode.relative_to(self.root).as_posix()])
        clean.clean(self.root, None)
        with self.assertRaises(ValueError):
            clean.clean(self.root, "old")
        self.assertTrue(bytecode.exists())
        key = hashlib.sha256(json.dumps(items, sort_keys=True).encode()).hexdigest()
        clean.clean(self.root, key)
        self.assertFalse(bytecode.exists())
        self.assertEqual(unknown.read_bytes(), b"keep")

    @unittest.skipUnless(os.name == "nt", "Windows junction")
    def test_destination_junction_is_rejected(self):
        outside = self.root / "other-user"
        outside.mkdir()
        link = self.dest / "junction"
        subprocess.run(["pwsh", "-NoProfile", "-Command",
                        "New-Item -ItemType Junction -Path $env:FW_TEST_LINK -Target $env:FW_TEST_OTHER | Out-Null"],
                       check=True, env=dict(os.environ, FW_TEST_LINK=str(link), FW_TEST_OTHER=str(outside)))
        try:
            with self.assertRaises(ValueError):
                manage.manage("install", link / "skills", [self.name])
            self.assertEqual(list(outside.iterdir()), [])
        finally:
            link.rmdir()


class CompletePackageTests(unittest.TestCase):
    def test_install_update_and_recovery_for_all_real_packages(self):
        with tempfile.TemporaryDirectory(prefix="formweave-packages-") as temporary:
            boundary = Path(temporary).resolve()
            self.assertEqual(boundary.parent, Path(tempfile.gettempdir()).resolve())
            source, dest = boundary / "source", boundary / "installed"
            shutil.copytree(ROOT / "skills", source)
            dest.mkdir()
            unrelated = dest / "user-notes.txt"
            unrelated.write_text("keep", encoding="utf-8")
            with patch.object(manage, "SKILLS", source):
                manage.manage("install", dest, manage.NAMES)
                manage.manage("verify", dest, manage.NAMES)
                for name in manage.NAMES:
                    doc = source / name / "references/motion.md"
                    doc.write_text(doc.read_text(encoding="utf-8") + "\n隔离更新标记。\n",
                                   encoding="utf-8", newline="\n")
                manage.manage("update", dest, manage.NAMES)
                manage.manage("verify", dest, manage.NAMES)
                for name in manage.NAMES:
                    target = dest / name
                    validate.validate_skill(target)
                    original = manage.inventory(target)
                    doc = source / name / "SKILL.md"
                    doc.write_text(doc.read_text(encoding="utf-8") + "\n隔离失败恢复标记。\n",
                                   encoding="utf-8", newline="\n")
                    rename = Path.rename
                    def fail_stage(path, destination):
                        self.assertTrue(path.resolve().is_relative_to(boundary))
                        self.assertTrue(destination.resolve().is_relative_to(boundary))
                        if path.name == "new":
                            raise OSError("injected swap failure")
                        return rename(path, destination)
                    with patch.object(Path, "rename", fail_stage), self.assertRaises(OSError):
                        manage.manage("update", dest, [name])
                    self.assertEqual(manage.inventory(target), original)
                    validate.validate_skill(target)
                    manage.manage("update", dest, [name])
                    manage.manage("verify", dest, [name])
                self.assertEqual(unrelated.read_text(encoding="utf-8"), "keep")
                self.assertEqual({path.name for path in dest.iterdir()}, {*manage.NAMES, unrelated.name})
