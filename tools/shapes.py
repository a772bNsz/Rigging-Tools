from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from pymel.util.path import path
from tools.color_shapes import ColorShapes
from tools.control_shapes import ControlShapes
import pymel.core as pm


def get_window():
    global mw
    try:
        mw.ui.close()
    except:
        pass

    mw = MyWindow()
    mw.ui.show()
    return mw


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        self.color_shapes = ColorShapes()
        self.control_shapes = ControlShapes()

        self.ui = self.import_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.init_ui()

    @staticmethod
    def import_ui():
        ui_file_path = path(__file__.split(".")[0] + ".ui")
        loader = QUiLoader()
        ui = loader.load(ui_file_path, None)
        return ui

    def init_ui(self):
        self._load_preset_colors()
        self._load_colors()
        self._load_shapes()
        return

    def _load_preset_colors(self):
        presets = ["ik", "fk", "left", "middle", "right"]
        data = self.color_shapes.get

        for p in presets:
            rgb = data[p]
            pbn = self.ui.findChild(QtWidgets.QPushButton, p+"_btn")
            pbn.setStyleSheet("background-color: rgb({}, {}, {})".format(*rgb))
        return

    def _load_colors(self):
        buttons = []
        rows = 4
        columns = 8
        for r in range(rows):
            for c in range(columns):
                i = (r*columns) + c + 1
                if i >= 32:
                    break

                buttons += [QtWidgets.QPushButton("")]
                rgb = map(lambda x: round(x*255, 2), pm.colorIndex(i, q=1))
                buttons[-1].setStyleSheet(
                    "background-color: rgb({}, {}, {})".format(*rgb))
                self.ui.color_grd.addWidget(buttons[-1], r, c)
        return

    def _load_shapes(self):
        # add hint
        # add thumbnail image
        # get number of icons
        return
