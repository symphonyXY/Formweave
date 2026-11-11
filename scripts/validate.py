"""检查源码技能或单独安装的包；验证名称、元数据、本地引用和资源完整性。"""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
import yaml
from manage import NAMES, ROOT, inventory

LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\s]+)\)")
UNFINISHED = re.compile(r"\[(?:TODO|INSERT HERE|REPLACE ME)\b|\bTBD\b", re.I)


class UniqueKeyLoader(yaml.SafeLoader):
    """拒绝会被普通 YAML 加载静默覆盖的重复字段。"""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str) or key in result:
            raise ValueError(f"YAML 字段重复或不是字符串：{key!r}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_mapping(text, source):
    result = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(result, dict):
        raise ValueError(f"{source}: YAML 须为字段映射")
    return result


def require_text(mapping, key, source, maximum=None):
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip() or (maximum and len(value) > maximum):
        raise ValueError(f"{source}: {key} 须为非空字符串" + (f"，最多 {maximum} 字符" if maximum else ""))
    return value


def check_text(path):
    """落实 .editorconfig 的文本约定，不自动重写文件。"""
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw:
        raise ValueError(f"{path}: 须为 UTF-8 无 BOM、LF 换行")
    content = raw.decode("utf-8")
    if not content.endswith("\n") or content.endswith("\n\n"):
        raise ValueError(f"{path}: 文件末尾须为一个换行")
    if any(line != line.rstrip(" \t") for line in content.splitlines()):
        raise ValueError(f"{path}: 存在行尾空白")


def check_links(doc, boundary):
    boundary = boundary.resolve()
    for link in LINK.findall(doc.read_text(encoding="utf-8")):
        path = link.split("#")[0]
        if not path or path.startswith(("https://", "http://", "mailto:")):
            continue
        target = (doc.parent / path).resolve()
        if Path(path).is_absolute() or not target.is_relative_to(boundary) or not target.is_file():
            raise ValueError(f"{doc}: 引用越界或不存在 {link}")


def validate_skill(folder):
    folder = folder.resolve()
    entries = inventory(folder, installed=True)
    for name in ("SKILL.md", "agents/openai.yaml", "LICENSE"):
        if name not in entries:
            raise ValueError(f"{folder}: 缺少 {name}")
    body = (folder / "SKILL.md").read_text(encoding="utf-8")
    match = re.fullmatch(r"---\n(.+?)\n---\n(.+)", body, re.S)
    if not match:
        raise ValueError(f"{folder}: 缺少技能头部或正文")
    meta = load_mapping(match[1], folder / "SKILL.md")
    supported = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    if meta.keys() - supported:
        raise ValueError(f"{folder}: 非跨客户端通用字段，请先核对兼容性：{sorted(meta.keys() - supported)}")
    if meta.get("name") != folder.name or not re.fullmatch("[a-z0-9]+(-[a-z0-9]+)*", folder.name) or len(folder.name) > 64:
        raise ValueError(f"{folder}: 技能名无效")
    require_text(meta, "description", folder, 1024)
    for key, maximum in (("license", None), ("compatibility", 500), ("allowed-tools", None)):
        if key in meta:
            require_text(meta, key, folder, maximum)
    metadata = meta.get("metadata", {})
    if not isinstance(metadata, dict) or any(not isinstance(v, str) for v in metadata.values()):
        raise ValueError(f"{folder}: metadata 须为字符串键值映射")
    if not match[2].strip():
        raise ValueError(f"{folder}: 技能正文为空")
    agent = load_mapping((folder / "agents/openai.yaml").read_text(encoding="utf-8"), folder)
    ui = agent.get("interface")
    if not isinstance(ui, dict):
        raise ValueError(f"{folder}: interface 须为字段映射")
    require_text(ui, "display_name", folder)
    short = require_text(ui, "short_description", folder, 64)
    prompt = require_text(ui, "default_prompt", folder)
    if len(short) < 25 or not re.search(r"\$" + re.escape(folder.name) + r"(?![a-z0-9-])", prompt):
        raise ValueError(f"{folder}: 界面元数据无效")
    if "policy" in agent:
        policy = agent["policy"]
        if not isinstance(policy, dict) or ("allow_implicit_invocation" in policy
                and not isinstance(policy["allow_implicit_invocation"], bool)):
            raise ValueError(f"{folder}: 调用策略无效")
    for doc in folder.rglob("*.md"):
        check_links(doc, folder)
        if UNFINISHED.search(doc.read_text(encoding="utf-8")):
            raise ValueError(f"{doc}: 残留脚手架标记")
    return meta


def validate_repo():
    for required in ("VERSION", ".editorconfig", ".gitattributes", "README.md", "AGENTS.md",
                     "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE",
                     "docs/compatibility.md", "docs/validation.md", ".github/workflows/check.yml"):
        if not (ROOT / required).is_file():
            raise ValueError(f"仓库缺少 {required}")
    skills = ROOT / "skills"
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"(?:0|[1-9]\d*)(?:\.(?:0|[1-9]\d*)){2}", version):
        raise ValueError("VERSION 须为 主.次.修订 三段数字")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    release = re.search(r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})$", changelog, re.M)
    if not release or release[1] != version:
        raise ValueError("更新日志最新定版条目与 VERSION 不一致")
    date.fromisoformat(release[2])
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if f"版本 **{version}**" not in readme or f"定版日期 **{release[2]}**" not in readme:
        raise ValueError("README 版本或日期不一致")
    if {d.name for d in skills.iterdir()} != set(NAMES):
        raise ValueError("技能目录与安装清单不符")
    copies = {}
    for name in NAMES:
        folder = skills / name
        meta = validate_skill(folder)
        if meta.get("metadata", {}).get("version") != version:
            raise ValueError(f"{name}: 技能版本与 VERSION 不一致")
        for doc in (folder / "references").glob("*.md"):
            if copies.setdefault(doc.name, doc.read_bytes()) != doc.read_bytes():
                raise ValueError(f"独立包内共享参考发生漂移：{doc.name}")
    for doc in [*ROOT.glob("*.md"), *(ROOT / "docs").rglob("*.md"), *(ROOT / "evals").glob("*.md")]:
        check_links(doc, ROOT)
    text_suffixes = {".md", ".py", ".yaml", ".yml", ".json", ".jsonl", ".html",
                     ".js", ".cjs", ".css", ".cs", ".csproj", ".xaml", ".txt"}
    sources = [p for p in ROOT.iterdir() if p.is_file()]
    for directory in ("skills", "scripts", "tests", "docs", "evals", ".github"):
        sources.extend(p for p in (ROOT / directory).rglob("*") if p.is_file())
    for path in sources:
        if path.suffix in text_suffixes or path.name in {"VERSION", "LICENSE", ".editorconfig", ".gitattributes", ".gitignore"}:
            check_text(path)
    cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
    if len({case["id"] for case in cases}) != len(cases):
        raise ValueError("行为评测 ID 重复")
    for case in cases:
        if not case["request"] or not case["observables"] or case["skill"] not in (None, *NAMES):
            raise ValueError(f"无效评测：{case}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path)
    args = parser.parse_args()
    try:
        validate_skill(args.skill) if args.skill else validate_repo()
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as error:
        parser.exit(1, f"校验失败：{error}\n")
    print("校验通过")
