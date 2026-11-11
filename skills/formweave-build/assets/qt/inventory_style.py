"""盘点工作台的表面、排版和动效设置。"""
import ctypes
import sys

from PySide6.QtCore import QByteArray, QRectF, Qt
from PySide6.QtGui import QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication, QWidget

ART = b'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 136" fill="none">
<defs><linearGradient id="sheet" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox"><stop stop-color="#f5edff"/><stop offset="1" stop-color="#bab1f5"/></linearGradient></defs>
<g stroke="#a49bd7" opacity=".32" stroke-width=".8"><path d="m6 93 125-65 182 72M50 125l143-80 125 52M74 132l139-74M1 63l172 72M64 25l219 91"/><circle cx="42" cy="79" r="2"/><circle cx="276" cy="86" r="2"/></g>
<g stroke-linejoin="round"><path d="m72 88 89-48 96 37-91 52z" fill="#534b88" stroke="#9c92c8"/><path d="m72 76 89-48 96 37-91 52z" fill="#8174b7" stroke="#b1a8de"/><path d="m72 61 89-48 96 37-91 52z" fill="url(#sheet)" stroke="#ece7ff"/>
<path d="m90 61 40-21 7 3-40 22z" fill="#625291"/><path d="m105 67 29-15m-22 18 18-9" stroke="#8e80b7" stroke-width="2.5"/>
<path d="m162 29 19 8m-24-5 18 8m-22-6 17 7" stroke="#8675ab" stroke-width="1.8"/>
<path d="m180 66 30-16 22 8-30 17z" fill="#9182be"/><path d="m188 66 20-10m-15 12 19-10" stroke="#f0e9fa" stroke-width="1.5"/>
</g></svg>'''


class SheetArt(QWidget):
    def __init__(self):
        super().__init__()
        self.renderer = QSvgRenderer(QByteArray(ART), self)
        self.setFixedWidth(244)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w = min(self.width(), self.height() * 320 / 136)
        h = w * 136 / 320
        self.renderer.render(painter, QRectF((self.width() - w) / 2, (self.height() - h) / 2, w, h))


def motion_enabled():
    if sys.platform == "win32":
        enabled = ctypes.c_int()
        if ctypes.windll.user32.SystemParametersInfoW(0x1042, 0, ctypes.byref(enabled), 0):
            return bool(enabled.value)
    return QApplication.isEffectEnabled(Qt.UI_AnimateCombo)


STYLE = """
QWidget {font-family:"Microsoft YaHei UI","Segoe UI"; font-size:10pt;}
QWidget#canvas {background:#f4f3f8;}
QLabel {color:#272538; background:transparent;}
QLabel#wordmark {color:#413759; font:600 11pt 'Segoe UI';}
QLabel#caption {color:#635e72; font-size:9pt;}
QFrame#hero {background:#383152; border-radius:14px;}
QLabel#kicker {color:#d8cfef; font:600 9pt 'Segoe UI';}
QLabel#title {color:white; font-size:20pt; font-weight:700;}
QLabel#subtitle {color:#e2ddee; font-size:10pt;}
QFrame#card {background:#fff; border:1px solid #dfdbe8; border-radius:12px;}
QLabel#section {font-size:12pt; font-weight:700;}
QLabel#tag {background:#eeeaf8; color:#594482; border-radius:8px; padding:3px 9px; font:600 9pt 'Segoe UI';}
QLabel#ref {color:#67568b; font:600 9pt 'Segoe UI';}
QLabel#metric {color:#342b4d; font-size:17pt; font-weight:600;}
QLineEdit {background:#faf9fc; border:1px solid #d8d3e2; border-radius:7px; padding:6px 10px; color:#302b40; selection-background-color:#62478a; selection-color:white;}
QLineEdit:hover {border-color:#a89abb;} QLineEdit:focus {border:2px solid #79629a; padding:5px 9px;}
QTableView {background:#fff; border:0; color:#333041; selection-background-color:#ede8f8; selection-color:#382a52; outline:0;}
QTableView::item {border:none; border-bottom:1px solid #eeeaf2; padding-left:7px;}
QTableView::item:hover {background:#f4f2f9;}
QTableView::item:selected {background:#eae4f5; color:#38294f;}
QTableView::item:focus {border:1px solid #846daa;}
QHeaderView::section {background:#f6f5f9; color:#645d71; padding:5px 8px; border:0; font-weight:600;}
QPushButton {background:#faf9fc; color:#494155; border:1px solid #d5cfdf; border-radius:7px; padding:7px 14px; font-weight:600;}
QPushButton:hover {background:#f0edf5;} QPushButton:pressed {background:#e1dbe9;}
QPushButton:focus {border:2px solid #795e9d; padding:6px 13px;}
QPushButton#primary {background:#654d89; color:white; border-color:#654d89;}
QPushButton#primary:hover {background:#554074;} QPushButton#primary:pressed {background:#46355f;}
QPushButton#primary:focus {border-color:#281835;}
QPushButton:disabled, QPushButton#primary:disabled {background:#f2f0f5; color:#76717d; border-color:#e4dfe9;}
QProgressBar {background:#eeeaf4; border:0; border-radius:3px; max-height:6px;}
QProgressBar::chunk {background:#8166aa; border-radius:3px;}
QLabel#receipt {color:#625d70; background:#f5f3f8; border-radius:6px; padding:6px 9px;}
QLabel#receipt[state="busy"] {color:#523778; background:#eee8f7;}
QLabel#receipt[state="success"] {color:#305e4b; background:#e8f2eb;}
QLabel#receipt[state="warning"] {color:#765026; background:#fbefdb;}
"""
