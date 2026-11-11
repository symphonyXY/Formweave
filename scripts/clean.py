"""预览仓库中由现有 Python 源文件产生的字节码，再按清单摘要执行。"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from manage import ROOT, digest, ordinary, safe_path


def candidates(root):
    result = {}
    for category in ("scripts", "tests", "skills"):
        base = root / category
        safe_path(base)
        for directory, dirs, names in os.walk(base, followlinks=False):
            dirs[:] = [d for d in dirs if d != "__pycache__" and safe_dir(Path(directory) / d)]
            for filename in names:
                if not filename.endswith(".py"):
                    continue
                source = Path(directory) / filename
                cache = Path(importlib.util.cache_from_source(str(source)))
                try:
                    safe_path(source)
                    safe_path(cache)
                    if cache.is_file() and cache.read_bytes()[:4] == importlib.util.MAGIC_NUMBER:
                        result[cache.relative_to(root).as_posix()] = digest(cache)
                except (OSError, ValueError):
                    continue
    return dict(sorted(result.items()))


def safe_dir(path):
    try:
        ordinary(path)
        return True
    except (OSError, ValueError):
        return False


def clean(root, apply):
    root = safe_path(root)
    items = candidates(root)
    token = hashlib.sha256(json.dumps(items, sort_keys=True).encode()).hexdigest()
    for key in items:
        print(root / key)
    print(f"候选 {len(items)} 项；清单摘要 {token}")
    if apply is not None:
        if apply != token:
            raise ValueError("清单已变化或摘要不符，请重新预览")
        for key, fingerprint in items.items():
            path = safe_path(root / key)
            if not path.is_relative_to(root) or digest(path) != fingerprint:
                raise ValueError(f"候选已变动：{path}")
            path.unlink()
            print("已清理", path)
            if not any(path.parent.iterdir()):
                path.parent.rmdir()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", metavar="预览摘要")
    try:
        clean(ROOT, parser.parse_args().apply)
    except (OSError, ValueError) as error:
        parser.exit(1, f"清理停止：{error}\n")
