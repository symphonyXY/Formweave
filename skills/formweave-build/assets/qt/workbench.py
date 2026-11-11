"""本地盘点工作台。演示数据按行生成，选择多行可后台计算校验值。"""
import hashlib
import sys

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPropertyAnimation, QThread, Qt, Signal
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QAbstractItemView, QApplication, QFrame, QGraphicsOpacityEffect, QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QTableView, QVBoxLayout, QWidget,
)


from inventory_style import STYLE, SheetArt, motion_enabled


class Inventory(QAbstractTableModel):
    names = ("瓦楞纸箱", "缠绕膜", "热敏标签", "手持终端", "扫描枪", "周转箱")
    headers = ("物料编号", "库区", "数量", "物料名称")

    def __init__(self, count):
        super().__init__()
        self.count = count
        self.rows = range(count)

    def rowCount(self, parent=QModelIndex()):
        return 0 if parent.isValid() else len(self.rows)

    def columnCount(self, parent=QModelIndex()):
        return 0 if parent.isValid() else len(self.headers)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return super().headerData(section, orientation, role)

    @staticmethod
    def label(item):
        return f"FW-{item:06d}"

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            item = self.rows[index.row()]
            return (self.label(item), f"{item % 12 + 1} 区", str(item % 87), self.names[item % len(self.names)])[index.column()]

    def search(self, value):
        term = value.strip().upper()
        self.beginResetModel()
        self.rows = [i for i in range(self.count) if term in self.label(i)] if term else range(self.count)
        self.endResetModel()


class Batch(QThread):
    progress = Signal(int)

    def __init__(self, items):
        super().__init__()
        self.items = items
        self.done = 0
        self.digest = ""
        self.error = ""

    def run(self):
        digest = hashlib.sha256()
        try:
            for item in self.items:
                if self.isInterruptionRequested():
                    break
                digest.update(Inventory.label(item).encode("ascii"))
                self.done += 1
                if self.done % 128 == 0:
                    self.progress.emit(self.done)
            self.digest = digest.hexdigest()
        except Exception as exc:
            self.error = str(exc)


class Workbench(QMainWindow):
    def __init__(self, count=10000):
        super().__init__()
        self.setWindowTitle("织形 · 盘点工作台")
        self.resize(1010, 690)
        self.task = None
        self.closing = False
        pane = QWidget(objectName="canvas")
        self.setCentralWidget(pane)
        self.layout_main = layout = QVBoxLayout(pane)
        layout.setContentsMargins(22, 14, 22, 18)
        layout.setSpacing(12)

        brand = QHBoxLayout()
        brand.addWidget(QLabel("Formweave   /   织形", objectName="wordmark"))
        brand.addStretch()
        brand.addWidget(QLabel("本地工作区   ·   演示数据", objectName="caption"))
        layout.addLayout(brand)

        self.hero = QFrame(objectName="hero")
        banner = QHBoxLayout(self.hero)
        banner.setContentsMargins(22, 12, 20, 12)
        intro = QVBoxLayout()
        intro.setSpacing(2)
        intro.addWidget(QLabel("OPERATIONS    /    INVENTORY", objectName="kicker"))
        intro.addWidget(QLabel("库存盘点", objectName="title"))
        self.subtitle = QLabel("筛选物料、核对库存，批量校验所选记录。", objectName="subtitle")
        intro.addWidget(self.subtitle)
        banner.addLayout(intro, 1)
        self.art = SheetArt()
        banner.addWidget(self.art)
        layout.addWidget(self.hero)

        body = QHBoxLayout()
        body.setSpacing(12)
        layout.addLayout(body, 1)
        list_card = QFrame(objectName="card")
        body.addWidget(list_card, 1)
        stock = QVBoxLayout(list_card)
        stock.setContentsMargins(14, 12, 14, 10)
        stock.setSpacing(8)
        heading = QHBoxLayout()
        heading.addWidget(QLabel("物料清单", objectName="section"))
        self.counter = QLabel(objectName="tag")
        heading.addWidget(self.counter)
        heading.addStretch()
        stock.addLayout(heading)
        self.query = QLineEdit()
        self.query.setAccessibleName("按物料编号筛选")
        self.query.setPlaceholderText("搜索物料编号    Ctrl+F")
        self.query.setClearButtonEnabled(True)
        stock.addWidget(self.query)
        self.model = Inventory(count)
        self.table = QTableView()
        self.table.setAccessibleName("库存明细")
        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setShowGrid(False)
        self.table.setMouseTracking(True)
        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        header.moveSection(3, 1)
        self.table.verticalHeader().setDefaultSectionSize(31)
        self.table.verticalHeader().hide()
        stock.addWidget(self.table, 1)
        self.empty = QLabel("没有匹配的物料\n\n缩短编号，或清除筛选后重试。")
        self.empty.setAlignment(Qt.AlignCenter)
        stock.addWidget(self.empty, 1)

        self.inspector = QFrame(objectName="card")
        self.inspector.setFixedWidth(216)
        body.addWidget(self.inspector, 0, Qt.AlignTop)
        detail = QVBoxLayout(self.inspector)
        detail.setContentsMargins(16, 15, 16, 16)
        detail.setSpacing(8)
        detail.addWidget(QLabel("RECORD INSPECTOR", objectName="ref"))
        detail.addWidget(QLabel("选择详情", objectName="section"))
        self.detail_ref = QLabel(objectName="ref")
        self.detail_name = QLabel(objectName="metric")
        self.detail_info = QLabel(objectName="caption")
        detail.addSpacing(18)
        for field in (self.detail_ref, self.detail_name, self.detail_info):
            detail.addWidget(field)
        detail.addSpacing(22)
        note = QLabel("按住 Ctrl 可多选，按住 Shift 可连续选择。", objectName="caption")
        note.setWordWrap(True)
        detail.addWidget(note)
        self.fade = QGraphicsOpacityEffect(self.detail_name)
        self.detail_name.setGraphicsEffect(self.fade)
        self.fade.setOpacity(1)
        self.motion = QPropertyAnimation(self.fade, b"opacity", self)
        self.motion.setDuration(140)
        self.motion.setStartValue(.75)
        self.motion.setEndValue(1.0)

        footer = QFrame(objectName="card")
        layout.addWidget(footer)
        foot = QVBoxLayout(footer)
        foot.setContentsMargins(14, 9, 14, 9)
        actions = QHBoxLayout()
        foot.addLayout(actions)
        self.status = QLabel(objectName="receipt")
        self.status.setWordWrap(True)
        actions.addWidget(self.status, 1)
        self.start = QPushButton("校验选中项", objectName="primary")
        self.cancel = QPushButton("取消任务")
        actions.addWidget(self.cancel)
        actions.addWidget(self.start)
        self.bar = QProgressBar()
        self.bar.setAccessibleName("校验进度")
        self.bar.setTextVisible(False)
        self.bar.hide()
        foot.addWidget(self.bar)
        self.start.clicked.connect(self.begin)
        self.cancel.clicked.connect(self.stop)
        self.query.textChanged.connect(self.search)
        self.table.selectionModel().selectionChanged.connect(self.buttons)
        QShortcut(QKeySequence.Find, self, activated=self.query.setFocus)
        self.style_hints = QApplication.styleHints()
        self.accessibility = self.style_hints.accessibility()
        self.accessibility.contrastPreferenceChanged.connect(self.refresh_theme)
        self.refresh_theme()
        self.search("")

    def refresh_theme(self):
        contrast = self.accessibility.contrastPreference()
        self.setStyleSheet("" if contrast == Qt.ContrastPreference.HighContrast else STYLE)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        compact = self.width() < 760
        self.inspector.setVisible(not compact)
        self.art.setVisible(not compact)
        self.subtitle.setVisible(self.height() > 490)

    def buttons(self):
        ranges = self.table.selectionModel().selection()
        selected = sum(group.height() for group in ranges)
        if selected == 1:
            item = self.model.rows[ranges[0].top()]
            ref = self.model.label(item)
            name = self.model.names[item % len(self.model.names)]
            info = f"库区   {item % 12 + 1:02d}     /     库存   {item % 87} 件"
        elif selected:
            ref, name, info = "批量选择", f"{selected:,} 项", "校验将使用本次选中的物料编号。"
        else:
            ref, name, info = "等待选择", "尚未选择", "点击清单中的记录查看库存。"
        changed = ref != self.detail_ref.text() or name != self.detail_name.text()
        self.detail_ref.setText(ref)
        self.detail_name.setText(name)
        self.detail_info.setText(info)
        if changed and self.inspector.isVisible():
            self.motion.stop()
            self.fade.setOpacity(1)
            if motion_enabled():
                self.motion.start()
        self.start.setText(f"校验选中项（{selected}）" if selected else "校验选中项")
        self.start.setEnabled(self.task is None and selected > 0)
        self.cancel.setEnabled(self.task is not None and not self.task.isInterruptionRequested())
        self.cancel.setVisible(self.task is not None)

    def search(self, term):
        self.model.search(term)
        total = self.model.rowCount()
        self.counter.setText(f"{total:,} 项")
        self.table.setVisible(bool(total))
        self.empty.setVisible(not total)
        if self.task is None:
            self.feedback("选择物料后可开始校验" if total else "没有匹配记录，请调整筛选条件", "idle")
        self.buttons()

    def feedback(self, message, state):
        self.status.setText(message)
        if state != self.status.property("state"):
            self.status.setProperty("state", state)
            self.status.style().unpolish(self.status)
            self.status.style().polish(self.status)

    def begin(self):
        if self.task is not None:
            return
        ranges = self.table.selectionModel().selection()
        items = sorted(self.model.rows[i] for group in ranges
                       for i in range(group.top(), group.bottom() + 1))
        if not items:
            return
        self.task = Batch(items)
        self.task.progress.connect(self.bar.setValue)
        self.task.finished.connect(self.finish)
        self.bar.setRange(0, len(items))
        self.bar.setValue(0)
        self.bar.show()
        self.feedback(f"正在校验 {len(items)} 项", "busy")
        self.buttons()
        self.task.start()

    def stop(self):
        if self.task:
            self.task.requestInterruption()
            self.feedback("正在取消…", "busy")
            self.cancel.setEnabled(False)

    def finish(self):
        task = self.task
        task.wait()
        self.task = None
        if task.error:
            state = "warning"
            result = "失败：" + task.error
        elif task.done < len(task.items):
            state = "warning"
            result = f"已取消，完成 {task.done}/{len(task.items)} 项"
        else:
            state = "success"
            result = f"已完成 {task.done} 项，校验值 {task.digest[:12]}"
        self.feedback(result, state)
        self.bar.hide()
        self.buttons()
        task.deleteLater()
        if self.closing:
            self.close()

    def closeEvent(self, event):
        if self.task:
            self.closing = True
            self.stop()
            event.ignore()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Workbench()
    window.show()
    if "--smoke" in sys.argv:
        from PySide6.QtCore import QTimer
        def check_window():
            window.query.setText("000001")
            ok = window.isVisible() and window.model.rowCount() == 1
            app.exit(0 if ok else 2)
        QTimer.singleShot(100, check_window)
    sys.exit(app.exec())
