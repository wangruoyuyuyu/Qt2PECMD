from uis import ui_mainWindow
from PySide6 import QtWidgets, QtGui
from PySide6_AceEditor import constants
import asyncio
import pyperclip
import os
import sys

import convert

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class MainWindow(ui_mainWindow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.widget_from.setMode(constants.BuiltinModes.XML)
        self.widget_to.setMode(constants.BuiltinModes.PLAIN_TEXT)
        self.converter = convert.UiToPecmdConverter()

        self.pushButton_open.clicked.connect(self.openfrom)
        self.pushButton_trans.clicked.connect(self.convert)
        self.pushButton_save.clicked.connect(self.saveto)
        self.pushButton_copy.clicked.connect(self.copy)

        os.chdir(os.path.dirname(sys.argv[0]))
        if os.path.exists("./icon.png"):
            self.setWindowIcon(QtGui.QPixmap("./icon.png"))

    def copy(self):
        pyperclip.copy(self.widget_to.text())

    def saveto(self):
        if not self.widget_to.text():
            self.convert()
        with open(
            QtWidgets.QFileDialog.getSaveFileName(
                self, "保存PECMD文件", filter="PECMD文件(*.wcs)"
            )[0],
            "w+",
        ) as f:
            f.write(self.widget_to.text())

    def openfrom(self):
        with open(
            QtWidgets.QFileDialog.getOpenFileName(
                self, "打开UI文件", filter="UI文件(*.ui)"
            )[0],
            "r+",
            encoding="utf-8",
        ) as f:
            self.widget_from.setText(f.read())

    def convert(self):
        if not self.widget_from.text():
            self.openfrom()
        self.widget_to.setText(self.converter.convert_string(self.widget_from.text()))


if __name__ == "__main__":
    qa = QtWidgets.QApplication(list())
    mw = MainWindow()
    mw.show()
    qa.exec()
