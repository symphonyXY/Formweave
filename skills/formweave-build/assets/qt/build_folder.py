"""从当前解释器构建工作台，隔离 PATH 上其他原生工具附带的 DLL。"""
import argparse
import os
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path.cwd() / "packaging-output")
    output = parser.parse_args().output.absolute()
    if output.exists() and any(output.iterdir()):
        parser.error("输出目录需为空，已有交付物应先保留")
    output.mkdir(parents=True, exist_ok=True)
    windows = Path(os.environ["SystemRoot"])
    paths = [Path(sys.executable).parent, Path(sys.base_prefix),
             Path(sys.base_prefix) / "DLLs", windows / "System32", windows]
    env = dict(os.environ, PATH=os.pathsep.join(map(str, paths)), PYTHONNOUSERSITE="1")
    entry = Path(__file__).with_name("workbench.py")
    subprocess.run([sys.executable, "-m", "PyInstaller", "--onedir", "--windowed",
                    "--name", "FormweaveInventory", "--specpath", str(output),
                    "--workpath", str(output / "build"), "--distpath", str(output / "dist"),
                    str(entry)], env=env, cwd=output, check=True)


if __name__ == "__main__":
    main()
