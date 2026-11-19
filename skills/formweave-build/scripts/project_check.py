"""只读检查 Windows 桌面工程的交付入口；不构建、不删除、不访问网络。"""
import argparse
import json
import ntpath
from pathlib import Path
import stat


READMES = {"readme", "readme.md", "readme.rst"}
LICENSES = {"license", "license.md", "license.txt", "license.rst", "copying"}
CONTRIBUTING = {"contributing.md", "contributing.txt", "contributing.rst"}
CHANGELOGS = {"changelog.md", "changelog.rst", "changes.md", "history.md"}
DEPENDENCIES = {"pyproject.toml", "package.json", "package-lock.json", "pnpm-lock.yaml",
                "yarn.lock", "uv.lock", "poetry.lock", "packages.lock.json", "directory.packages.props"}
PYTHON_ENTRIES = {"__main__.py", "main.py", "app.py", "workbench.py"}
BUILD_SUFFIXES = {".sln", ".slnx", ".csproj", ".vcxproj", ".fsproj", ".pro", ".spec"}
BUILD_NAMES = {"cmakelists.txt", "cargo.toml", "makefile", "setup.py", "build_folder.py",
               "package.json", "pyproject.toml"}
ARTIFACT_DIRS = {"build", "dist", "bin", "obj", "out", "publish", "packaging-output", ".formweave-work"}


def ordinary(path, want_directory):
    info = path.lstat()
    if (stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
            or (stat.S_ISREG(info.st_mode) and info.st_nlink != 1)):
        raise ValueError(f"跳过链接、重解析点或多重硬链接：{path}")
    expected = stat.S_ISDIR if want_directory else stat.S_ISREG
    if not expected(info.st_mode):
        raise ValueError(f"不是预期的普通文件或目录：{path}")
    return info


def project_root(path):
    root = path.absolute()
    if ".." in root.parts:
        raise ValueError("工程根目录不能含上级跳转")
    for directory in (*reversed(root.parents), root):
        ordinary(directory, want_directory=True)
    return root


def specified_file(root, raw):
    names = raw.replace("\\", "/").split("/")
    if (any(not name or name in {".", ".."} or name.casefold() == ".git"
            or ntpath.isreserved(name) for name in names) or "[" in raw or "]" in raw):
        raise ValueError(f"需要工程内明确的相对文件路径（无通配符）：{raw!r}")
    relative = Path(*names)
    return relative.as_posix(), file_info(root, relative)


def file_info(root, relative):
    for directory in reversed(relative.parents):
        ordinary(root / directory, want_directory=True)
    return ordinary(root / relative, want_directory=False)


def is_build(name):
    return name in BUILD_NAMES or name in PYTHON_ENTRIES or Path(name).suffix in BUILD_SUFFIXES


def is_dependency(name):
    return name in DEPENDENCIES or (name.startswith("requirements") and name.endswith(".txt"))


def inspect_project(path, profile="local", entries=(), artifacts=()):
    root = project_root(path)
    checks, skipped = [], []

    def directory_items(relative):
        directory = root / relative
        try:
            ordinary(directory, want_directory=True)
            return sorted(directory.iterdir(), key=lambda item: (item.name.casefold(), item.name))
        except FileNotFoundError:
            return []
        except (OSError, ValueError):
            skipped.append(relative.as_posix())
            return []

    def matches(items, predicate, directories=False):
        paths = []
        for item in items:
            if not predicate(item.name.casefold()):
                continue
            relative = item.relative_to(root).as_posix()
            try:
                ordinary(item, want_directory=directories)
                paths.append(relative)
            except (OSError, ValueError):
                skipped.append(relative)
        return paths

    def record(key, paths, detail, missing="待复核"):
        checks.append({"id": key, "state": "发现" if paths else missing,
                       "paths": list(dict.fromkeys(paths)), "detail": detail})

    top = directory_items(Path("."))
    community = directory_items(Path(".github")) + top + directory_items(Path("docs"))
    shallow = top + directory_items(Path("src")) + directory_items(Path("app"))
    build = matches(shallow, is_build) + [specified_file(root, item)[0] for item in entries]
    record("build-entry", build, "仅识别候选入口；按实际框架核对构建命令，深层入口可用 --entry 显式指定。")
    record("dependencies", matches(shallow, is_dependency), "确认真实依赖声明、版本和适用的锁文件；不从文件名推断依赖完整。")
    record("readme", matches(community, READMES.__contains__), "核对安装、首次操作与预期结果；从干净副本复跑适用命令。")
    record("changelog", matches(top, CHANGELOGS.__contains__), "实际交付变更应有与用户相关的记录；保留已有命名与版本习惯。")
    if profile == "open-source":
        record("license", matches(top, LICENSES.__contains__), "核对批准的许可、许可证原文及第三方分发条件。")
        record("contributing", matches(community, CONTRIBUTING.__contains__), "开放贡献时核对开发、验证与反馈入口。")
    record("output-boundary", matches(top, ARTIFACT_DIRS.__contains__, directories=True),
           "这些目录名不证明其中内容可删除；核对源码、产物、用户数据和证据的边界。", "未发现")
    record("clean-start", [], "本工具不运行构建或应用；在独立验证目录核对 README、入口与主任务。", "未验证")
    if profile == "open-source":
        record("publication", [], "本工具没有检查 Git 差异、凭据、许可内容、远端、分支或授权。", "未验证")

    submitted = {}
    for raw in artifacts:
        relative, info = specified_file(root, raw)
        submitted[relative] = {"path": relative, "bytes": info.st_size, "state": "待复核"}
    return {"root": str(root), "profile": profile, "checks": checks,
            "skipped": sorted(set(skipped)), "submitted_artifacts": list(submitted.values())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="目标工程根目录")
    parser.add_argument("--profile", choices=("local", "open-source"), default="local")
    parser.add_argument("--entry", action="append", default=[], help="确切的项目相对入口，可重复")
    parser.add_argument("--artifact", action="append", default=[], help="仅列出确切的待复核产物文件，可重复")
    parser.add_argument("--json", action="store_true", help="将报告以 JSON 写到标准输出")
    args = parser.parse_args()
    try:
        report = inspect_project(args.project, args.profile, args.entry, args.artifact)
    except (OSError, ValueError) as error:
        parser.exit(2, f"无法盘点：{error}\n")
    if args.json:
        print(json.dumps(report, indent=2))
        return
    print(f"工程：{report['root']} | 模式：{args.profile}")
    for check in report["checks"]:
        print(f"[{check['state']}] {check['id']}：{check['detail']}")
        if check["paths"]:
            print("  " + ", ".join(check["paths"]))
    for name in report["skipped"]:
        print(f"[未检查] {name}：无法读取或不是预期的普通文件/目录。")
    for item in report["submitted_artifacts"]:
        print(f"[待复核] {item['path']}（{item['bytes']} 字节）；没有判断是否可删。")
    print("只读盘点；退出码 0 仅表示报告生成，不表示验证通过。")


if __name__ == "__main__":
    main()
