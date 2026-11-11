"""对新启动的本地交付程序测量首个可见主窗和窗口稳定后的进程树快照。"""
import argparse
import ctypes
from ctypes import wintypes
import json
from pathlib import Path
import subprocess
import sys
import time

import psutil


def visible_window(pid):
    user = ctypes.windll.user32
    result = []
    callback = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    @callback
    def visit(hwnd, unused):
        owner = wintypes.DWORD()
        user.GetWindowThreadProcessId(hwnd, ctypes.byref(owner))
        if owner.value == pid and user.IsWindowVisible(hwnd) and user.GetWindowTextLengthW(hwnd):
            result.append(hwnd)
        return True
    user.EnumWindows(visit, 0)
    return result[0] if result else None


def probe(command):
    start = time.perf_counter()
    with subprocess.Popen(command) as child:
        try:
            window = None
            while not window and time.perf_counter() - start < 15:
                if child.poll() is not None:
                    raise RuntimeError(f"程序提前退出 {child.returncode}")
                window = visible_window(child.pid)
                time.sleep(.01)
            if not window:
                raise RuntimeError("15 秒内未出现可见窗口")
            startup = time.perf_counter() - start
            time.sleep(2)
            sampler = Path(__file__).resolve().parents[1] / "skills/formweave-build/scripts/sample_process.py"
            stats = json.loads(subprocess.check_output([sys.executable, "-B", str(sampler),
                                                       str(child.pid), "--count", "1"]))
            ctypes.windll.user32.PostMessageW(wintypes.HWND(window), 0x10, 0, 0)
            if child.wait(timeout=10) != 0:
                raise RuntimeError("程序关闭异常")
            print(json.dumps({"first_window_ms": round(startup * 1000, 1), **stats}))
        finally:
            if child.poll() is None:
                child.kill()


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", nargs=argparse.REMAINDER)
    args = p.parse_args()
    if not args.command:
        p.error("需要独立可执行文件路径")
    probe(args.command)
