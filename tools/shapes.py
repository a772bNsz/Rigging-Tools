from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from pymel.util.path import path
import pymel.core as pm

from tools import color_shapes, control_shapes
reload(color_shapes)
reload(control_shapes)


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
        super(MyWindow, self).__init__(None)

        self.color_shapes = color_shapes.ColorShapes()
        self.control_shapes = control_shapes.ControlShapes()

        self.ui = self.import_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.preset_buttons = self.color_buttons = self.shape_buttons = []
        self.init_ui()

        self.json_file = None
        return

    @staticmethod
    def import_ui():
        ui_file_path = path(__file__.split(".")[0] + ".ui")
        loader = QUiLoader()
        ui = loader.load(ui_file_path, None)
        return ui

    def init_ui(self):
        self.preset_buttons = self._load_preset_colors()
        self.color_buttons = self._load_colors()
        self.shape_buttons = self._load_shapes()

        self._connect_preset_buttons()
        self._connect_color_buttons()
        self._connect_shape_buttons()

        self.ui.save_btn.clicked.connect(self.save_file)
        self.ui.load_btn.clicked.connect(self.load_file)
        return True

    def _load_preset_colors(self):
        presets = ["ik", "fk", "left", "middle", "right"]
        data = self.color_shapes.get

        preset_buttons = []
        for p in presets:
            rgb = data[p]
            pbn = self.ui.findChild(QtWidgets.QPushButton, p+"_btn")
            pbn.setStyleSheet("background-color: rgb({}, {}, {})".format(*rgb))
            preset_buttons += [pbn]
        return preset_buttons

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
                rgb = map(lambda x: int(x*255), pm.colorIndex(i, q=1))
                buttons[-1].setStyleSheet(
                    "background-color: rgb({}, {}, {})".format(*rgb))
                buttons[-1].setToolTip(str(pm.colorIndex(i, q=1)))
                self.ui.color_grd.addWidget(buttons[-1], r, c)
        return buttons

    def _load_shapes(self):
        buttons = []
        rows = 6
        columns = 5
        for r in range(rows):
            for c in range(columns):
                buttons += [QtWidgets.QPushButton("")]
                self.ui.shape_grd.addWidget(buttons[-1], r, c)

        thumbnails = path(
            path(__file__).dirname() + "/shape_thumbnails").files("*.tiff")
        for f, pbn in zip(thumbnails, buttons):
            name = f.name.split(".")[0]
            pbn.setToolTip(name)
            pbn.setMinimumHeight(60)
            pbn.setStyleSheet("background-color: black")

            ico = QtGui.QIcon()
            ico.addFile(f)

            pbn.setIcon(ico)
            pbn.setIconSize(QtCore.QSize(60, 60))
        return buttons

    def _change_color_on_selection(self, arg):
        self.color_shapes.sel = pm.ls(sl=1)
        self.color_shapes.set(arg)
        return True

    def _connect_preset_buttons(self):
        presets = ["ik", "fk", "left", "middle", "right"]

        for p in presets:
            pbn = self.ui.findChild(QtWidgets.QPushButton, p+"_btn")
            pbn.clicked.connect(lambda x=p: self._change_color_on_selection(x))
        return True

    def _connect_color_buttons(self):
        for pbn in self.color_buttons:
            rgb = map(lambda x: float(x), pbn.toolTip()[1:-1].split(", "))
            pbn.clicked.connect(
                lambda x=rgb: self._change_color_on_selection(x))
        return True

    def _connect_shape_buttons(self):
        for pbn in self.shape_buttons:
            pbn.clicked.connect(getattr(self.control_shapes, pbn.toolTip()))
        return True

    def save_file(self):
        controls = pm.ls(sl=1)

        location = path(__file__).dirname().replace("tools", "results")
        save_window = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", location, "JSON files (*.json)")
        json_file = path(save_window[0])

        if json_file:
            if not json_file.endswith(".json"):
                json_file = path(json_file + ".json")
            self.control_shapes.save(json_file=json_file, controls=controls)
        return json_file

    def load_file(self):
        return
