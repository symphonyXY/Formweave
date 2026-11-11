"""安装、更新、核验独立技能。仅使用 Python 标准库。"""
import argparse
import hashlib
import json
import os
import shutil
import stat
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAMES = ("formweave-plan", "formweave-preview", "formweave-build", "formweave-audit")
RECEIPT = ".formweave-install.json"


def ordinary(path):
    info = path.lstat()
    if (stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 1024
            or not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode))):
        raise ValueError(f"不接受链接或特殊文件：{path}")
    if stat.S_ISREG(info.st_mode) and info.st_nlink > 1:
        raise ValueError(f"保留多重硬链接：{path}")


def safe_path(path):
    if ".." in path.parts:
        raise ValueError(f"路径含上级跳转：{path}")
    path = path.absolute()
    for parent in [*reversed(path.parents), path]:
        if os.path.lexists(parent):
            ordinary(parent)
    return path.resolve()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root, installed=False):
    safe_path(root)
    entries = {}
    def visit(directory):
        for item in sorted(directory.iterdir()):
            ordinary(item)
            key = item.relative_to(root).as_posix()
            if installed and key == RECEIPT:
                continue
            if item.is_dir():
                entries[key + "/"] = ""
                visit(item)
            else:
                entries[key] = digest(item)
    visit(root)
    return entries


def read_receipt(target):
    receipt = target / RECEIPT
    if not receipt.is_file():
        raise ValueError(f"同名目录没有织形安装记录：{target}")
    ordinary(receipt)
    data = json.loads(receipt.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("skill") != target.name or data.get("format") != 1:
        raise ValueError(f"安装记录无效：{receipt}")
    return data.get("entries")


def install_one(name, dest, action):
    source = SKILLS / name
    expected = inventory(source)
    if RECEIPT in expected or "SKILL.md" not in expected:
        raise ValueError(f"无效源技能：{source}")
    target = dest / name
    exists = os.path.lexists(target)
    if exists:
        current = inventory(target, installed=True)
        if current != read_receipt(target):
            raise ValueError(f"目标有本地改动，已保留：{target}")
        if current == expected:
            return "一致"
        if action != "update":
            raise ValueError(f"源与已安装版本不同，请使用 update：{name}")
    elif action == "verify":
        raise ValueError(f"未安装：{target}")

    # 临时、备份和目标在同一卷。每个技能为一个事务。
    work = Path(tempfile.mkdtemp(prefix=".formweave-stage-", dir=dest))
    stage, backup = work / "new", work / "previous"
    try:
        shutil.copytree(source, stage)
        if inventory(stage) != expected:
            raise ValueError("暂存副本校验失败")
        (stage / RECEIPT).write_text(json.dumps(
            {"format": 1, "skill": name, "entries": expected}, ensure_ascii=False, indent=2
        ), encoding="utf-8")
        if exists:
            if inventory(target, installed=True) != current or read_receipt(target) != current:
                raise ValueError("准备更新时目标已变化")
            target.rename(backup)
        try:
            stage.rename(target)
        except OSError:
            if backup.exists() and not os.path.lexists(target):
                backup.rename(target)
            raise
        if backup.exists():
            shutil.rmtree(backup)
    finally:
        if backup.exists():
            print(f"保留恢复副本：{backup}", file=sys.stderr)
        else:
            shutil.rmtree(work)
    return "已更新" if exists else "已安装"


def manage(action, destination, names):
    dest = safe_path(destination)
    if dest.is_relative_to(SKILLS) or any(SKILLS.is_relative_to(dest / name) for name in names):
        raise ValueError("目标不能与技能源目录重叠")
    if action == "verify":
        for name in names:
            print(name, install_one(name, dest, action))
        return
    dest.mkdir(parents=True, exist_ok=True)
    lock = dest / ".formweave-install.lock"
    with lock.open("x", encoding="utf-8") as handle:
        handle.write(str(os.getpid()))
    try:
        for name in names:
            print(name, install_one(name, dest, action))
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("install", "update", "verify"))
    parser.add_argument("--dest", required=True, type=Path, help="技能父目录")
    parser.add_argument("--skill", choices=NAMES, action="append", help="可重复，默认四个")
    args = parser.parse_args()
    try:
        manage(args.action, args.dest, args.skill or NAMES)
    except (OSError, ValueError) as error:
        parser.exit(1, f"未完成：{error}\n")


if __name__ == "__main__":
    main()
