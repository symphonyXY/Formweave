"""盘点工作台的表面、排版和动效设置。"""
import ctypes
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication


def motion_enabled():
    if sys.platform == "win32":
        enabled = ctypes.c_int()
        if ctypes.windll.user32.SystemParametersInfoW(0x1042, 0, ctypes.byref(enabled), 0):
            return bool(enabled.value)
    return QApplication.isEffectEnabled(Qt.UI_AnimateCombo)


STYLE = """
QWidget {font-family:"Microsoft YaHei UI","Segoe UI"; font-size:10pt;}
QWidget#canvas {background:#f1f5f2;}
QLabel {color:#272538; background:transparent;}
QLabel#caption {color:#526964; font-size:9pt;}
QLabel#title {color:#19332f; font-size:17pt; font-weight:700;}
QFrame#card {background:#fff; border:1px solid #d5e0dc; border-radius:8px;}
QLabel#section {font-size:12pt; font-weight:700;}
QLabel#tag {background:#e2f1eb; color:#185c4f; border-radius:8px; padding:3px 9px; font:600 9pt 'Segoe UI';}
QLabel#ref {color:#526964; font:600 9pt 'Segoe UI';}
QLabel#metric {color:#19332f; font-size:17pt; font-weight:600;}
QLineEdit {background:#faf9fc; border:1px solid #d8d3e2; border-radius:7px; padding:6px 10px; color:#302b40; selection-background-color:#62478a; selection-color:white;}
QLineEdit:hover {border-color:#a89abb;} QLineEdit:focus {border:2px solid #79629a; padding:5px 9px;}
QTableView {background:#fff; border:0; color:#333041; selection-background-color:#ede8f8; selection-color:#382a52; outline:0;}
QTableView::item {border:none; border-bottom:1px solid #eeeaf2; padding-left:7px;}
QTableView::item:hover {background:#f4f2f9;}
QTableView::item:selected {background:#dcefe6; color:#173e34;}
QTableView::item:focus {border:1px solid #126556;}
QHeaderView::section {background:#eaf0ed; color:#526964; padding:5px 8px; border:0; font-weight:600;}
QPushButton {background:#faf9fc; color:#494155; border:1px solid #d5cfdf; border-radius:7px; padding:7px 14px; font-weight:600;}
QPushButton:hover {background:#f0edf5;} QPushButton:pressed {background:#e1dbe9;}
QPushButton:focus {border:2px solid #795e9d; padding:6px 13px;}
QPushButton#primary {background:#126556; color:white; border-color:#126556;}
QPushButton#primary:hover {background:#105748;} QPushButton#primary:pressed {background:#10483c;}
QPushButton#primary:focus {border-color:#281835;}
QPushButton:disabled, QPushButton#primary:disabled {background:#f2f0f5; color:#76717d; border-color:#e4dfe9;}
QProgressBar {background:#eeeaf4; border:0; border-radius:3px; max-height:6px;}
QProgressBar::chunk {background:#126556; border-radius:3px;}
QLabel#receipt {color:#625d70; background:#f5f3f8; border-radius:6px; padding:6px 9px;}
QLabel#receipt[state="busy"] {color:#523778; background:#eee8f7;}
QLabel#receipt[state="success"] {color:#305e4b; background:#e8f2eb;}
QLabel#receipt[state="warning"] {color:#765026; background:#fbefdb;}
"""
