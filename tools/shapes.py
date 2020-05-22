from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from pymel.util.path import path
from tools.color_shapes import ColorShapes
from tools.control_shapes import ControlShapes


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
        self.ui = self.import_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.init_ui()

    @staticmethod
    def import_ui():
        ui_file_path = \
            path(__file__.replace("tools", "tools/ui").split(".")[0] + ".ui")
        loader = QUiLoader()
        ui = loader.load(ui_file_path, None)
        return ui

    def init_ui(self):
        self._load_preset_colors()
        self._load_colors()
        self._load_shapes()
        return

    def _load_preset_colors(self):
        return

    def _load_colors(self):
        return

    def _load_shapes(self):
        return
