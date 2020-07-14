from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from shiboken2 import wrapInstance
from maya.OpenMayaUI import MQtUtil
from pymel.util.path import path

import pymel.core as pm
from tools.arm import Rig as Arm
from tools.shoulder import Rig as Shoulder
from tools.hand import Rig as Hand


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

        self.shoulder = None
        self.left_shoulder = None
        self.right_shoulder = None
        self.arm = None
        self.left_arm = None
        self.right_arm = None
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

        self.ui.shoulder_right_btn.clicked.connect(
            lambda x="right": self.rig_shoulder(x))
        self.ui.shoulder_mid_btn.clicked.connect(
            lambda x="": self.rig_shoulder(x))
        self.ui.shoulder_left_btn.clicked.connect(
            lambda x="left": self.rig_shoulder(x))

        self.ui.arm_right_btn.clicked.connect(
            lambda x="right": self.rig_arm(x))
        self.ui.arm_mid_btn.clicked.connect(
            lambda x="": self.rig_arm(x))
        self.ui.arm_left_btn.clicked.connect(
            lambda x="left": self.rig_arm(x))

        # self.ui.setup_right_btn.clicked.connect(
        #     lambda x="right": self.setup_hand(x))
        # self.ui.setup_mid_btn.clicked.connect(
        #     lambda x="": self.setup_hand(x))
        # self.ui.setup_left_btn.clicked.connect(
        #     lambda x="left": self.setup_hand(x))
        #
        # self.ui.hand_right_btn.clicked.connect(
        #     lambda x="right": self.rig_hand(x))
        # self.ui.hand_mid_btn.clicked.connect(
        #     lambda x="": self.rig_hand(x))
        # self.ui.hand_left_btn.clicked.connect(
        #     lambda x="left": self.rig_hand(x))
        return

    def rig_hand(self, side):
        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        root = pm.ls(sl=1)[0]
        root_con = controls[-1]
        hand = Hand(root, side=side, root_control=root_con)

        names = ["index", "middle", "ring", "pinky"]
        hand.finger_attributes(fingers=names)

        params = {
            "palm": self.locators,
            "fingers": names
        }
        hand.palm_attributes(**params)
        arm = getattr(self, side + "arm")
        params = {
            "control": arm.result_chain["hand"],
            "bind_joint": arm.twist_nodes["lower"]["end_bind"],
            "settings": arm.controls["arm_settings"],
        }
        hand.connect(**params)
        return

    def setup_hand(self):
        middle = pm.spaceLocator(n="middle")
        middle.t.set([77.59, 139.11, 2.3])

        outer = pm.spaceLocator(n="outer")
        outer.t.set([75.37, 137.33, -1.16])

        inner = pm.spaceLocator(n="inner")
        inner.t.set([75.79, 137.55, 4.45])

        self.locators = [middle, inner, outer]
        pm.select(self.locators)
        return

    def rig_shoulder(self, side):
        if not pm.ls(sl=1):
            pm.warning("No root joint selected.")
            return

        if not self.ui.space_switch_lsw.count():
            pm.warning("No spaces to connect arm rig.")

        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        root = pm.ls(sl=1)[0]
        root_con = controls[-1]
        shoulder = Shoulder(root, side=side, root_control=root_con)
        shoulder.ik()
        shoulder.connect(control="chest_CON")

        add = True
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            item = self.ui.space_switch_lsw.item(e).text()
            if "shoulder" in item.lower():
                add = False
                break

        if add:
            pm.select(shoulder.groups["shoulder"])
            self._add_list_widget_item()
            pm.select(cl=1)

        if "right" == side:
            self.right_shoulder = shoulder
        elif "left" == side:
            self.left_shoulder = shoulder
        else:
            self.shoulder = shoulder

        pm.select(cl=1)
        return

    def rig_arm(self, side):
        if not pm.ls(sl=1):
            pm.warning("No root joint selected.")
            return

        if not self.ui.space_switch_lsw.count():
            pm.warning("No spaces to connect arm rig.")

        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        root = pm.ls(sl=1)[0]
        root_con = controls[-1]
        arm = Arm(root, side=side, root_control=root_con)
        arm.twist()
        arm.ikfk_switch()
        arm.fk()
        arm.ik()
        arm.connect(controls)

        if "right" == side:
            self.right_arm = arm
        elif "left" == side:
            self.left_arm = arm
        else:
            self.arm = arm

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
                space = item.text()
                found += pm.ls(space + "*" + c)

                if "shoulder" == space:
                    found += pm.ls(space.upper() + "_GRP")

            if not found:
                self.ui.space_switch_lsw.takeItem(e)
                continue

            item.setText(str(found[0]))
        return
