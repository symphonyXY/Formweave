"""验证可移植清单边界、清晰失败与安装后独立读取。"""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate


class SkillContractTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name) / "sample-skill"
        (self.folder / "agents").mkdir(parents=True)
        (self.folder / "LICENSE").write_text("MIT\n", encoding="utf-8")
        self.header = "name: sample-skill\ndescription: 测试技能\n"
        self.agent = ('interface:\n  display_name: "测试"\n'
                      '  short_description: "用于验证独立技能安装后仍能读取清单并拒绝损坏的界面元数据。"\n'
                      '  default_prompt: "使用 $sample-skill。"\n')
        self.write()

    def write(self, header=None, agent=None, body="# 测试\n"):
        (self.folder / "SKILL.md").write_text(
            "---\n" + (header if header is not None else self.header) + "---\n" + body,
            encoding="utf-8", newline="\n")
        (self.folder / "agents/openai.yaml").write_text(
            agent if agent is not None else self.agent, encoding="utf-8", newline="\n")

    def test_valid_boundaries_and_installed_packages(self):
        self.write(self.header.replace("测试技能", "字" * 1024) + "compatibility: " + "字" * 500 + "\n")
        validate.validate_skill(self.folder)
        self.folder = self.folder.rename(self.folder.with_name("a" * 64))
        self.header = self.header.replace("sample-skill", "a" * 64)
        self.agent = self.agent.replace("sample-skill", "a" * 64)
        self.write()
        validate.validate_skill(self.folder)
        for source in (ROOT / "skills").iterdir():
            target = self.folder.parent / source.name
            shutil.copytree(source, target)
            validate.validate_skill(target)

    def test_invalid_manifest(self):
        invalid = ["[]\n", "name: sample-skill\n", self.header + "name: sample-skill\n",
                   self.header + "metadata:\n  version: 1\n",
                   self.header + "metadata: []\n", self.header + "compatibility: " + "字" * 501 + "\n",
                   self.header.replace("测试技能", "字" * 1025),
                   self.header + "license: false\n", self.header + "allowed-tools: []\n",
                   self.header + "disable-model-invocation: true\n"]
        for header in invalid:
            with self.subTest(header=header[:100]):
                self.write(header)
                with self.assertRaises(ValueError):
                    validate.validate_skill(self.folder)
        self.write(body=" \n")
        with self.assertRaises(ValueError):
            validate.validate_skill(self.folder)

    def test_invalid_ui_and_duplicate_nested_fields(self):
        invalid = ["[]\n", "interface: []\n", self.agent.replace('"测试"', "true"),
                   self.agent.replace("$sample-skill。", "$sample-skill-extra。"),
                   self.agent + "policy:\n  allow_implicit_invocation: 'false'\n",
                   self.agent.replace("  display_name:", "  display_name: duplicate\n  display_name:")]
        for agent in invalid:
            with self.subTest(agent=agent[:100]):
                self.write(agent=agent)
                with self.assertRaises(ValueError):
                    validate.validate_skill(self.folder)

    def test_text_format(self):
        path = self.folder / "text.md"
        for raw in (b"\xef\xbb\xbftext\n", b"text\r\n", b"text", b"text\n\n", b"text \n"):
            path.write_bytes(raw)
            with self.assertRaises(ValueError):
                validate.check_text(path)
        path.write_bytes("简体中文\n".encode("utf-8"))
        validate.check_text(path)
