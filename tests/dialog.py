"""仅控制指定测试进程的原生文件选择对话框。"""
import argparse
import ctypes
from ctypes import wintypes as wt
import time

user = ctypes.WinDLL("user32", use_last_error=True)
callback = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
user.GetDlgItem.restype = wt.HWND
user.GetDlgItem.argtypes = [wt.HWND, ctypes.c_int]
user.SendMessageW.argtypes = [wt.HWND, wt.UINT, wt.WPARAM, wt.LPARAM]
user.PostMessageW.argtypes = [wt.HWND, wt.UINT, wt.WPARAM, wt.LPARAM]


def find(parent, pid, kind):
    matches = []
    @callback
    def visit(hwnd, unused):
        owner = wt.DWORD()
        name = ctypes.create_unicode_buffer(128)
        user.GetWindowThreadProcessId(wt.HWND(hwnd), ctypes.byref(owner))
        user.GetClassNameW(wt.HWND(hwnd), name, len(name))
        if owner.value == pid and name.value.lower() == kind.lower():
            matches.append(hwnd)
        return True
    if parent:
        user.EnumChildWindows(wt.HWND(parent), visit, 0)
    else:
        user.EnumWindows(visit, 0)
    return matches[0] if matches else None


def act(pid, filename):
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline:
        dialog = find(None, pid, "#32770")
        if dialog and user.IsWindowVisible(wt.HWND(dialog)):
            if not filename:
                user.PostMessageW(dialog, 0x10, 0, 0)
                return
            combo = user.GetDlgItem(dialog, 1148)
            edit = find(combo, pid, "Edit") if combo else None
            button = user.GetDlgItem(dialog, 1)
            if edit and button and user.IsWindowVisible(wt.HWND(edit)):
                value = ctypes.create_unicode_buffer(filename)
                user.SendMessageW(edit, 0x000C, 0, ctypes.addressof(value))
                actual = ctypes.create_unicode_buffer(len(filename) + 1)
                user.SendMessageW(edit, 0x000D, len(actual), ctypes.addressof(actual))
                if actual.value == filename and user.IsWindowEnabled(wt.HWND(button)):
                    user.PostMessageW(dialog, 0x0111, 1, button)
                    return
        time.sleep(.08)
    raise RuntimeError("未找到目标进程的文件对话框或文件名控件")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("pid", type=int)
    p.add_argument("filename", nargs="?")
    args = p.parse_args()
    act(args.pid, args.filename)
