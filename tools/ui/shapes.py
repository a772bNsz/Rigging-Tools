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
        self._load_colors()
        self._load_shapes()

        self.ui.save_btn.clicked.connect(self.save_file)
        self.ui.load_btn.clicked.connect(self.load_file)
        return

    def _load_colors(self):
        buttons = {}
        rows = 4
        columns = 8
        default_btn = None
        for r in range(rows):
            for c in range(columns):
                i = (r*columns) + c + 1
                if i >= 32:
                    default_btn = QtWidgets.QPushButton("")
                    default_btn.setStyleSheet("""
                        background-color: Transparent;
                        """)
                    self.ui.color_grd.addWidget(default_btn, r, c)
                    break

                buttons[i] = QtWidgets.QPushButton("")

                rgb = map(lambda x: int(x*255), pm.colorIndex(i, q=1))
                buttons[i].setStyleSheet(
                    "background-color: rgb({}, {}, {})".format(*rgb))

                self.ui.color_grd.addWidget(buttons[i], r, c)

        for i, pbn in buttons.items():
            pbn.clicked.connect(lambda x=i: self._connect_color_buttons(x))

        default_btn.clicked.connect(self._no_color)
        return buttons

    def _no_color(self):
        self.color_shapes.sel = pm.ls(sl=1)
        self.color_shapes.default()
        return

    def _load_shapes(self):
        buttons = []
        rows = 6
        columns = 5
        for r in range(rows):
            for c in range(columns):
                buttons += [QtWidgets.QPushButton("")]
                self.ui.shape_grd.addWidget(buttons[-1], r, c)

        thumbnails = path(
            __file__.split("/ui")[0] + "/shape_thumbnails").files("*.tiff")
        for f, pbn in zip(thumbnails, buttons):
            pbn.setMinimumHeight(60)
            pbn.setStyleSheet("background-color: black")

            ico = QtGui.QIcon()
            ico.addFile(f)

            pbn.setIcon(ico)
            pbn.setIconSize(QtCore.QSize(60, 60))

            name = f.name.split(".")[0]
            pbn.clicked.connect(lambda x=name: self._connect_shape_buttons(x))
        return buttons

    def _connect_color_buttons(self, index):
        self.color_shapes.sel = pm.ls(sl=1)
        self.color_shapes.index = index
        self.color_shapes.by_index()
        return

    def _connect_shape_buttons(self, name):
        selected = pm.ls(sl=1)

        if selected:
            shape_and_colors = {}
            for sel in selected:
                sel_shape = sel.getShapes()[0]
                if sel_shape.overrideEnabled.get():
                    shape_and_colors[sel] = sel_shape.overrideColor.get()

            for sel in selected:
                pm.select(sel)
                getattr(self.control_shapes, name)()
                try:
                    self.color_shapes.sel = sel
                    self.color_shapes.index = shape_and_colors[sel]
                    self.color_shapes.by_index()
                except:
                    pass
        else:
            selected = getattr(self.control_shapes, name)()
        pm.select(selected)
        return

    def save_file(self):
        controls = pm.ls(sl=1)

        location = path(__file__).dirname().replace("tools", "results")
        json_file = path(QtWidgets.QFileDialog.getSaveFileName(
            self, "Save JSON", location, "JSON files (*.json)")[0])

        if json_file:
            if not json_file.endswith(".json"):
                json_file = path(json_file + ".json")
            self.control_shapes.save(json_file=json_file, controls=controls)
        return json_file

    def load_file(self):
        location = path(__file__).dirname().replace("tools", "results")
        json_file, _filter = QtWidgets.QFileDialog.getOpenFileName(
            self, "Load JSON", location, "JSON files (*.json)")

        if json_file:
            self.control_shapes.load(json_file=path(json_file))

            import json
            with open(json_file) as f:
                data = json.load(f)
        return data
