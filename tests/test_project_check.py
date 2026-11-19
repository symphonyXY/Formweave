"""验证目标项目盘点的边界、输出和无副作用。"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1] / "skills" / "formweave-build"


class ProjectCheckTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="formweave-project-check-")
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        self.root = base / "桌面 工程"
        self.root.mkdir()
        self.script = base / "standalone" / "project_check.py"
        self.script.parent.mkdir()
        shutil.copyfile(SKILL / "scripts/project_check.py", self.script)

    def write(self, relative, content="test\n"):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def invoke(self, *args):
        return subprocess.run([sys.executable, "-IB", "-X", "utf8", str(self.script), str(self.root),
                               "--json", *args], check=False, capture_output=True, text=True,
                              encoding="utf-8", timeout=15, cwd=self.script.parent)

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): (None if path.is_dir() else
                hashlib.sha256(path.read_bytes()).hexdigest()) for path in self.root.rglob("*")}

    def test_new_project_is_not_treated_as_ready(self):
        manifest = self.write("package.json", '{"scripts":{"start":"echo do not run"}}\n')
        before = self.snapshot()
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        checks = {check["id"]: check for check in report["checks"]}
        self.assertEqual(checks["build-entry"]["paths"], [manifest.name])
        self.assertEqual(checks["readme"]["state"], "待复核")
        self.assertEqual(checks["clean-start"]["state"], "未验证")
        self.assertNotIn("license", checks)
        self.assertEqual(report["submitted_artifacts"], [])
        self.assertEqual(self.snapshot(), before)

    def test_existing_project_only_reports_explicit_files(self):
        for relative in ("src/Inventory/Inventory.csproj", "docs/Readme.md", "LICENSE",
                         ".github/CONTRIBUTING.md", "dist/probe.txt", "dist/user-notes.txt",
                         "tests/test_required.py", "src/settings.json", ".env"):
            self.write(relative)
        before = self.snapshot()
        result = self.invoke("--profile", "open-source", "--entry", "src/Inventory/Inventory.csproj",
                             "--artifact", "dist\\probe.txt", "--artifact", "dist/probe.txt")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        checks = {check["id"]: check for check in report["checks"]}
        self.assertEqual(checks["readme"]["paths"], ["docs/Readme.md"])
        self.assertEqual(checks["license"]["paths"], ["LICENSE"])
        self.assertEqual(checks["build-entry"]["paths"], ["src/Inventory/Inventory.csproj"])
        self.assertEqual(checks["publication"]["state"], "未验证")
        self.assertEqual(report["submitted_artifacts"],
                         [{"path": "dist/probe.txt", "bytes": 5, "state": "待复核"}])
        for name in ("user-notes.txt", "test_required.py", "settings.json", ".env"):
            self.assertNotIn(name, result.stdout)
        self.assertEqual(self.snapshot(), before)

    def test_explicit_paths_cannot_escape_or_address_special_paths(self):
        for value in ("../outside.txt", str(self.root / "local.txt"), "dist/*.txt",
                      "C:file.txt", "build/file.txt:stream", ".git/config", "dist. /item.txt", "dist/nul.txt"):
            with self.subTest(value=value):
                result = self.invoke("--artifact", value)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
        self.assertEqual(self.snapshot(), {})

    def test_hardlinked_docs_are_skipped_and_explicit_link_is_rejected(self):
        original = self.root.parent / "outside.md"
        original.write_text("private\n", encoding="utf-8", newline="\n")
        os.link(original, self.root / "README.md")
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["skipped"], ["README.md"])
        self.assertNotIn("private", result.stdout)
        self.assertEqual(self.invoke("--entry", "README.md").returncode, 2)
        self.assertEqual(original.read_text(encoding="utf-8"), "private\n")

    def test_does_not_follow_linked_output_or_build_directories(self):
        outside = self.root.parent / "outside"
        outside.mkdir()
        outside_file = outside / "workbench.py"
        outside_file.write_text("unrelated\n", encoding="utf-8", newline="\n")
        if os.name == "nt":
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(self.root / "src"), str(outside)],
                                    capture_output=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            (self.root / "src").symlink_to(outside, target_is_directory=True)
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["skipped"], ["src"])
        self.assertNotIn("workbench.py", result.stdout)
        self.assertEqual(self.invoke("--artifact", "src/workbench.py").returncode, 2)
        self.assertEqual(outside_file.read_text(encoding="utf-8"), "unrelated\n")
