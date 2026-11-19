"""用独立从上游定义取得的 ID 集合指纹，检查离线索引的覆盖与可用性。"""
from collections import defaultdict
import hashlib
from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = {
    "https://luckymaomi.github.io/ui/animations/":
        (57, "efcd8173214507892e6f5fea24e63a2c670020c7787186e108e8211e38840b73"),
    "https://motionlab.uanx.online/lab/":
        (160, "758ca79378748f017a3aec9f1330d407c1453dab38b733680686926434335173"),
    "https://holynova.github.io/web-motion-showcase/detail.html":
        (60, "bf5fbae8fb48155943abc250df02d68e3175ee6a027144f0c78f10fc484c42d3"),
}


class MotionCatalogTests(unittest.TestCase):
    def test_packaged_ids_links_and_decisions(self):
        for skill in (ROOT / "skills").iterdir():
            with self.subTest(skill=skill.name):
                index = "\n".join((skill / "references" / name).read_text(encoding="utf-8")
                                  for name in ("motion-luckymaomi-index.md", "motion-lab-index.md",
                                               "motion-hub-index.md"))
                guide = (skill / "references/motion.md").read_text(encoding="utf-8")
                decisions = set(re.findall(r"^\| ([^|]+?) \|", guide, re.M))
                found = defaultdict(list)
                for line in index.splitlines():
                    if not line.startswith("| ["):
                        continue
                    link, identifier, settings, decision = (cell.strip() for cell in line.strip("|").split("|"))
                    url = re.fullmatch(r"\[[^\]]+\]\(([^)]+)\)", link)[1]
                    base = next(key for key in SNAPSHOTS if url.startswith(key))
                    if urlsplit(base).path.endswith(".html"):
                        parsed = urlsplit(url)
                        self.assertEqual(parsed.scheme + "://" + parsed.netloc + parsed.path, base)
                        query = parse_qs(parsed.query)
                        self.assertEqual(len(query["id"]), 1)
                        slug = query["id"][0]
                        self.assertIn(settings, {"进入", "滚动", "悬停", "反馈", "图片", "布局"})
                    else:
                        slug = url.removeprefix(base).rstrip("/")
                    self.assertEqual(identifier, f"`{slug}`")
                    self.assertTrue(settings)
                    self.assertIn(decision, decisions)
                    found[base].append(slug)
                for base, (count, fingerprint) in SNAPSHOTS.items():
                    ids = found[base]
                    self.assertEqual(len(ids), count)
                    self.assertEqual(len(set(ids)), count)
                    digest = hashlib.sha256("\n".join(sorted(ids)).encode()).hexdigest()
                    self.assertEqual(digest, fingerprint)
