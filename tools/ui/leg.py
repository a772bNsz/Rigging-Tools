from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from shiboken2 import wrapInstance
from maya.OpenMayaUI import MQtUtil
from pymel.util.path import path

import pymel.core as pm
from tools.leg import Rig


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


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setParent(parent)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setObjectName("MainWindow")

        self.ui = self.import_ui()
        widget = self.findChild(QWidget, "widget")
        window_title = widget.windowTitle()
        self.setWindowTitle(window_title)
        self.init_ui()

        self.leg = None
        self.left_leg = None
        self.right_leg = None
        self.locators = {}

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
        self._load_default_spaces()
        self.ui.add_btn.clicked.connect(self._add_list_widget_item)
        self.ui.minus_btn.clicked.connect(self._minus_list_widget_item)

        self.ui.leg_right_btn.clicked.connect(
            lambda x="right": self.rig_leg(x))
        self.ui.leg_mid_btn.clicked.connect(
            lambda x="": self.rig_leg(x))
        self.ui.leg_left_btn.clicked.connect(
            lambda x="left": self.rig_leg(x))

        self.ui.setup_right_btn.clicked.connect(
            lambda x="right": self.setup_foot(x))
        self.ui.setup_mid_btn.clicked.connect(
            lambda x="": self.setup_foot(x))
        self.ui.setup_left_btn.clicked.connect(
            lambda x="left": self.setup_foot(x))

        self.ui.foot_right_btn.clicked.connect(
            lambda x="right": self.rig_foot(x))
        self.ui.foot_mid_btn.clicked.connect(
            lambda x="": self.rig_foot(x))
        self.ui.foot_left_btn.clicked.connect(
            lambda x="left": self.rig_foot(x))
        return

    def rig_foot(self, side):
        getattr(self, side + "_leg").ik_foot()
        pm.select(cl=1)
        return

    def setup_foot(self, side):
        if self.locators:
            new_locators = getattr(self, side + "_leg").ik_foot_setup()
            for old, new in zip(self.locators.values(), new_locators.values()):
                position = old.getTranslation(space="world")
                position[0] = position[0] * -1
                new.setTranslation(position, space="world")
            self.locators = new_locators

        self.locators = getattr(self, side + "_leg").ik_foot_setup()

        pm.select([self.locators[x] for x in ["heel", "inner", "outer"]])
        return

    def rig_leg(self, side):
        if not pm.ls(sl=1):
            pm.warning("No root joint selected.")
            return

        if not self.ui.space_switch_lsw.count():
            pm.warning("No spaces to connect leg rig.")

        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        root = pm.ls(sl=1)[0]
        root_con = controls[-1]
        leg = Rig(root, side=side, root_control=root_con)
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        leg.create_groups()
        leg.space_switch(controls)
        leg.clean_up()

        if "right" == side:
            self.right_leg = leg
        elif "left" == side:
            self.left_leg = leg
        else:
            self.leg = leg

        pm.select(cl=1)
        return

    def _add_list_widget_item(self):
        for sel in pm.ls(os=1):
            item = QListWidgetItem(str(sel))
            self.ui.space_switch_lsw.insertItem(0, item)
        return

    def _minus_list_widget_item(self):
        for item in self.ui.space_switch_lsw.selectedItems():
            i = self.ui.space_switch_lsw.row(item)
            self.ui.space_switch_lsw.takeItem(i)
        return

    def _load_default_spaces(self):
        i = self.ui.space_switch_lsw.count()
        for e in range(i)[::-1]:
            item = self.ui.space_switch_lsw.item(e)

            found = []
            for c in ["CON", "CTL", "CTRL"]:
                found += pm.ls(item.text() + "*" + c)

            if not found:
                self.ui.space_switch_lsw.takeItem(e)
                continue

            item.setText(str(found[0]))
        return
