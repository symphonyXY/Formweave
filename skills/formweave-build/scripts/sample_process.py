"""采样指定 Windows 进程树，输出逐次 JSON Lines。需要 psutil。"""
import argparse
import json
import sys
import time


def sample(pid, count, interval):
    if sys.platform != "win32":
        raise ValueError("此口径仅用于 Windows")
    import psutil
    root = psutil.Process(pid)
    for index in range(count):
        if not root.is_running():
            raise ValueError("根进程已结束")
        private = working = measured = 0
        skipped = []
        for process in [root, *root.children(recursive=True)]:
            try:
                memory = process.memory_info()
                private += memory.private
                working += memory.rss
                measured += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                skipped.append(process.pid)
        print(json.dumps(dict(index=index, unix_time=time.time(), root_pid=pid,
                              measured=measured, skipped=skipped,
                              private_bytes=private, working_set_sum_bytes=working)), flush=True)
        if index + 1 < count:
            time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pid", type=int)
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--interval", type=float, default=1)
    args = parser.parse_args()
    if args.pid < 1 or args.count < 1 or args.interval < 0:
        parser.error("PID、次数须为正整数，间隔须非负")
    try:
        sample(args.pid, args.count, args.interval)
    except Exception as error:
        parser.exit(1, f"采样失败：{error}\n")
