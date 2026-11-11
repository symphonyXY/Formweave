"""在桌面会话运行 Qt 样例的交互探针，可选保存完整窗口截图。"""
import argparse
import json
from pathlib import Path
import statistics
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/formweave-build/assets/qt"))
from workbench import Workbench
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication


def wait_for(app, condition, seconds=5):
    limit = time.monotonic() + seconds
    while not condition():
        app.processEvents()
        if time.monotonic() > limit:
            raise AssertionError("事件循环等待超时")


def main(screenshot):
    app = QApplication([])
    win = Workbench(80000)
    win.show()
    win.activateWindow()
    app.setActiveWindow(win)
    wait_for(app, win.isActiveWindow)
    win.table.setFocus()
    app.processEvents()
    QTest.keyClick(win.table, Qt.Key_F, Qt.ControlModifier)
    wait_for(app, win.query.hasFocus)
    assert win.model.rowCount() == 80000
    timings = []
    for _ in range(5):
        start = time.perf_counter()
        win.query.setText("000001")
        assert win.model.rowCount() == 1
        timings.append((time.perf_counter() - start) * 1000)
        win.query.clear()
    win.query.setText("不存在")
    assert not win.model.rowCount() and "没有匹配" in win.status.text()
    win.query.setText("00000")
    win.table.selectAll()
    win.start.click()
    wait_for(app, lambda: win.task is None)
    assert "已完成" in win.status.text()
    win.query.clear()
    win.table.selectAll()
    win.start.click()
    win.cancel.click()
    wait_for(app, lambda: win.task is None)
    cancel_status = win.status.text()
    assert "已取消" in cancel_status or "已完成" in cancel_status
    win.table.clearSelection()
    win.table.selectRow(2)
    assert "（1）" in win.start.text()
    win.resize(610, 420)
    app.processEvents()
    assert not win.inspector.isVisible() and win.start.isVisible()
    win.resize(1010, 690)
    app.processEvents()
    assert win.inspector.isVisible()
    for row in (1, 0, 4, 2):
        point = win.table.visualRect(win.model.index(row, 0)).center()
        QTest.mouseClick(win.table.viewport(), Qt.LeftButton, Qt.NoModifier, point)
    assert win.detail_ref.text() == "FW-000002"
    assert win.detail_name.text() == "热敏标签"
    win.start.click()
    win.start.click()
    wait_for(app, lambda: win.task is None)
    assert "已完成 1 项" in win.status.text()
    QTest.qWait(170)
    if screenshot:
        assert win.grab().save(str(screenshot))
    win.start.click()
    win.close()
    wait_for(app, lambda: not win.isVisible() and win.task is None)
    print(json.dumps(dict(rows=80000, filter_ms=timings,
                          median_ms=statistics.median(timings), cancel=cancel_status),
                     ensure_ascii=False))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--screenshot", type=Path)
    main(p.parse_args().screenshot)
