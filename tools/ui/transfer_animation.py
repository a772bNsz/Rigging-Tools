from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from shiboken2 import wrapInstance
from maya.OpenMayaUI import MQtUtil
from pymel.util.path import path

import pymel.core as pm
from collections import OrderedDict


def get_window():
    try:
        maya_main_window_pointer = MQtUtil.mainWindow()
        maya_main_window = \
            wrapInstance(long(maya_main_window_pointer), QWidget)
    except:
        maya_main_window = None

    global mw
    try:
        mw.close()
    except:
        pass

    mw = MyWindow(parent=maya_main_window)
    mw.show()
    return mw


class TransferAnimation(object):
    def __init__(self):
        atom_loaded = pm.pluginInfo("atomImportExport", q=1, loaded=1)
        if not atom_loaded:
            pm.loadPlugin("atomImportExport")
        return

    @staticmethod
    def get_frame_range(file_path):
        frame_range = []
        with open(file_path) as atom_file:
            data = atom_file.readlines()
            for i, line in enumerate(data):
                search = "startTime"
                if line.startswith(search):
                    i = len(search) + 1
                    frame_range += [float(line[i:-2])]

                search = "endTime"
                if line.startswith(search):
                    i = len(search) + 1
                    frame_range += [float(line[i:-2])]
                    break
        return frame_range

    def load(self, file_path, selection=None, **kwargs):
        if selection is None and not pm.ls(sl=1):
            pm.warning("Nothing selected.")

        if selection:
            pm.select(selection)

        fr = self.get_frame_range(file_path)
        frame_range = ":".join(list(map(lambda x: str(x), fr)))

        params = OrderedDict()
        params["targetTime"] = "1"
        params["srcTime"] = frame_range
        params["dstTime"] = frame_range
        params["option"] = "scaleInsert"
        params["match"] = "hierarchy"
        params["selected"] = "selectedOnly"
        params["mapFile"] = ""

        keys = params.keys()
        for k, v in kwargs.items():
            if k in keys:
                params[k] = v

        options = ""
        for item in params.items():
            options += "=".join(list(item)) + ";"

        filename = path(file_path).name.split(".")[0]

        pm.importFile(file_path, type="atomImport", f=1, ra=1,
                      namespace=filename, options=options)
        return file_path

    @staticmethod
    def save(file_path, selection=None, **kwargs):
        if selection is None and not pm.ls(sl=1):
            pm.warning("Nothing selected.")

        if selection:
            pm.select(selection)
        else:
            selection = pm.ls(sl=1)

        params = OrderedDict()
        params["precision"] = "8"
        params["statics"] = "0"
        params["baked"] = "1"
        params["sdk"] = "0"
        params["constraint"] = "0"
        params["animLayers"] = "0"
        params["selected"] = "selectedOnly"
        params["whichRange"] = "1"
        params["range"] = "1:10"
        params["hierarchy"] = "none"
        params["controlPoints"] = "0"
        params["useChannelBox"] = "1"
        params["options"] = "keys"

        keys = params.keys()
        for k, v in kwargs.items():
            if k in keys:
                params[k] = v

        options = ""
        for item in params.items():
            options += "=".join(list(item)) + ";"
        pm.exportAnim(file_path, type="atomExport", f=1, options=options)

        # correct endTime line in atom file
        start_time = end_time = None
        for sel in selection:
            anim_nodes = sel.inputs(type="animCurve")
            first_frame = pm.findKeyframe(anim_nodes, which="first")

            if start_time < first_frame:
                start_time = str(first_frame)

            last_frame = pm.findKeyframe(anim_nodes, which="last")
            if end_time < last_frame:
                end_time = str(last_frame)

        data = []
        with open(file_path) as atom_file:
            lines = atom_file.readlines()

        for line in lines:
            search = "startTime"
            if line.startswith(search):
                data += [" ".join([search, start_time]) + ";\n"]
                continue

            search = "startUnitless"
            if line.startswith(search):
                continue

            search = "endTime"
            if line.startswith(search):
                data += [" ".join([search, end_time]) + ";\n"]
                continue

            search = "endUnitless"
            if line.startswith(search):
                continue

            data += [line]

        with open(file_path, "w") as atom_file:
            atom_file.writelines(data)
        return file_path

    def from_selection(self, source=None, target=None, attributes="tr",
                       axes="xyz"):
        if source is None and target is None:
            try:
                source, target = pm.ls(sl=1)
            except:
                return

        for at in attributes:
            for ax in axes:
                attr = at + ax
                self.match_curve(source, target, attribute=attr)
        return True

    @staticmethod
    def match_curve(source=None, target=None, attribute=None):
        source_attr, source_anim_node = \
            source.attr(attribute).inputs(c=1, type="animCurve")[0]

        key_values = pm.keyframe(source_attr, q=1, tc=1, vc=1)

        # key target with source values
        for k, v in key_values:
            pm.setKeyframe(target.attr(attribute), time=k, value=v)
        target_attr, target_anim_node = \
            target.attr(attribute).inputs(c=1, type="animCurve")[0]

        # match global weight
        weighted = source_anim_node.isWeighted()
        if weighted:
            target_anim_node.setWeighted(1)

        in_tangents = pm.keyTangent(source_attr, q=1, itt=1)
        out_tangents = pm.keyTangent(source_attr, q=1, ott=1)

        # match key angle and weight - unified / broken
        for i, (itt, ott) in enumerate(zip(in_tangents, out_tangents)):
            target_anim_node.setInTangentType(i, itt)
            target_anim_node.setOutTangentType(i, ott)

            locked = pm.keyTangent(source_attr, q=1, index=[i], lock=1)[0]
            if not locked:
                pm.keyTangent(target_attr, e=1, index=[i], lock=locked)

            if itt == "fixed":
                ia = pm.keyTangent(source_attr, q=1, index=[i], ia=1)[0]
                pm.keyTangent(target_attr, e=1, index=[i], ia=ia)

                iw = pm.keyTangent(source_attr, q=1, index=[i], iw=1)[0]
                pm.keyTangent(target_attr, e=1, index=[i], iw=iw)

            if ott == "fixed" and not locked:
                oa = pm.keyTangent(source_attr, q=1, index=[i], oa=1)[0]
                pm.keyTangent(target_attr, e=1, index=[i], oa=oa)

                ow = pm.keyTangent(source_attr, q=1, index=[i], ow=1)[0]
                pm.keyTangent(target_attr, e=1, index=[i], ow=ow)
        return target_anim_node


class MyWindow(QWidget, TransferAnimation):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        # self.setParent(parent)
        # self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        # self.setObjectName("MainWindow")

        # self.ui = self.import_ui()
        # widget = self.findChild(QWidget, "widget")
        # window_title = widget.windowTitle()
        # self.setWindowTitle(window_title)
        # self.init_ui()

        TransferAnimation.__init__(self)

    def coded_ui(self):
        # initialize
        self.setWindowTitle("Transfer Animation Tool")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setMinimumSize(250, 75)
        self.setMaximumSize(250, 75)

        horizontal_layout = QHBoxLayout()
        self.setLayout(horizontal_layout)

        save_btn = QPushButton("Save")
        load_btn = QPushButton("Load")

        horizontal_layout.addWidget(save_btn)
        horizontal_layout.addWidget(load_btn)

        # connect signals and slots
        load_btn.clicked.connect(self.load_file_dialog)
        save_btn.clicked.connect(self.save_file_dialog)
        return

    def import_ui(self):
        """
        Imports the designer ui file from disk (eliminating the step of
        converting it to Python classes first). The UI file shares the same
        name as the python file.
        :return: the complete ingested ui (QMainWindow)
        """
        ui_file_path = path(__file__.split(".")[0] + ".ui")

        loader = QUiLoader()
        ui = loader.load(ui_file_path, parentWidget=self)
        return ui

    def init_ui(self):
        """
        Initializes the UI by populating and setting up functional
        connections between widgets.
        """
        self.ui.load_btn.clicked.connect(self.load_file_dialog)
        self.ui.save_btn.clicked.connect(self.save_file_dialog)
        return

    def load_file_dialog(self):
        selection = pm.ls(sl=1)
        if not selection:
            pm.warning("Nothing selected.")
            return

        options_ui = __file__.split(".")[0] + ".mel"
        pm.mel.source(options_ui, language="mel")

        atom_file = None
        try:
            location = path(__file__).dirname()
            atom_file = pm.fileDialog2(
                caption="Load",
                fileFilter="Atom (*.atom);;All Files (*.*)",
                dir=location,
                optionsUICreate="OptionsUI",
                optionsUICommit="OptionsUIData",
                fileMode=1,  # a single existing file
                dialogStyle=2)[0]
        except TypeError:
            return

        load_choice = pm.optionVar(q="load_choice")
        start_frame = pm.optionVar(q="start_frame")

        if load_choice == "Default":
            super(MyWindow, self).load(atom_file)
        elif load_choice == "Start Frame":
            start_at = start_frame
            frame_range = super(MyWindow, self).get_frame_range(atom_file)
            offset_value = start_at - frame_range[0]
            new_frame_range = \
                ":".join(map(lambda x: str(x + offset_value), frame_range))

            super(MyWindow, self).load(atom_file, dstTime=new_frame_range)
        elif load_choice == "Current Frame":
            start_at = pm.currentTime()
            frame_range = super(MyWindow, self).get_frame_range(atom_file)
            offset_value = start_at - frame_range[0]
            new_frame_range = \
                ":".join(map(lambda x: str(x + offset_value), frame_range))

            super(MyWindow, self).load(atom_file, dstTime=new_frame_range)

        pm.optionVar(remove="load_choice")
        pm.optionVar(remove="start_frame")
        return True

    def save_file_dialog(self):
        selection = pm.ls(sl=1)
        if not selection:
            pm.warning("Nothing selected.")
            return

        atom_file = None
        try:
            location = path(__file__).dirname()
            atom_file = pm.fileDialog2(
                caption="Save",
                dir=location,
                fileFilter="Atom (*.atom);;All Files (*.*)",
                dialogStyle=2)[0]
        except TypeError:
            return

        super(MyWindow, self).save(atom_file)
        return True
