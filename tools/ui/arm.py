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
        self.hand = None
        self.left_hand = None
        self.right_hand = None

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

        self.ui.setup_right_btn.clicked.connect(
            lambda x="right": self.setup_hand(x))
        self.ui.setup_mid_btn.clicked.connect(
            lambda x="": self.setup_hand(x))
        self.ui.setup_left_btn.clicked.connect(
            lambda x="left": self.setup_hand(x))

        self.ui.hand_right_btn.clicked.connect(
            lambda x="right": self.rig_hand(x))
        self.ui.hand_mid_btn.clicked.connect(
            lambda x="": self.rig_hand(x))
        self.ui.hand_left_btn.clicked.connect(
            lambda x="left": self.rig_hand(x))
        return

    def rig_hand(self, side):
        side = side if "" == side else side + "_"
        hand = getattr(self, side + "hand")

        # setup_hand() cleanup
        thumb = hand.result_chain["thumb"]

        thumb_start = thumb["base"]
        aim_setup = thumb_start.inputs(type="aimConstraint")[0]
        aim_setup = aim_setup.target.inputs()
        pm.delete(aim_setup)
        pm.makeIdentity(thumb_start, apply=1, r=1)

        palm_locators_group = self.locators[0].getParent()
        pm.parent(self.locators, w=1)
        pm.delete(palm_locators_group)

        # rig_hand()
        names = ["index", "middle", "ring", "pinky"]
        hand.finger_attributes(fingers=names)

        params = {
            "palm": self.locators,
            "fingers": names
        }
        hand.palm_attributes(**params)

        params = {}
        try:
            arm = getattr(self, side + "arm")
            params = {
                "control": arm.result_chain["hand"],
                "bind_joint": arm.twist_nodes["lower"]["end_bind"],
                "settings": arm.controls["arm_settings"],
            }
        except:
            pass
        hand.connect(**params)
        return

    def setup_hand(self, side):
        hand_joint = pm.ls(sl=1)[0]
        pm.select(cl=1)

        root = pm.joint(p=[68.17, 138.49, 2.02])

        pm.select(root)
        pinky = pm.joint(p=[72.26, 138.44, -0.63], n="pinky")
        pm.joint(p=[76.93, 138.44, -0.9])
        pm.joint(p=[79.19, 138.44, -0.9])
        pm.joint(p=[81.26, 138.44, -0.9])
        pm.joint(p=[83.04, 138.44, -0.9])

        pm.select(root)
        ring = pm.joint(p=[72.32, 138.85, 0.79], n="ring")
        pm.joint(p=[77.23, 138.85, 0.67])
        pm.joint(p=[80.56, 138.85, 0.67])
        pm.joint(p=[83.09, 138.85, 0.67])
        pm.joint(p=[85.03, 138.85, 0.67])

        pm.select(root)
        middle = pm.joint(p=[72.32, 139.11, 2.14], n="middle")
        pm.joint(p=[77.59, 139.11, 2.3])
        pm.joint(p=[81.01, 139.11, 2.3])
        pm.joint(p=[83.58, 139.11, 2.3])
        pm.joint(p=[85.66, 139.11, 2.3])

        pm.select(root)
        index = pm.joint(p=[72.23, 139.11, 3.62], n="index")
        pm.joint(p=[77.74, 139.11, 3.87])
        pm.joint(p=[80.85, 139.11, 3.87])
        pm.joint(p=[83.39, 139.11, 3.87])
        pm.joint(p=[85.33, 139.11, 3.87])

        pm.select(root)
        thumb = pm.joint(p=[71.11, 137.67, 5.15], n="thumb")
        pm.joint(p=[73.27, 136.91, 6.71])
        pm.joint(p=[74.76, 136.39, 7.78])
        pm.joint(p=[76.83, 135.66, 9.28])

        fingers = {
            "thumb": thumb,
            "index": index,
            "middle": middle,
            "ring": ring,
            "pinky": pinky
        }

        # palm locators
        middle = pm.spaceLocator(n="middle")
        middle.t.set([77.59, 139.11, 2.3])

        outer = pm.spaceLocator(n="outer")
        outer.t.set([75.37, 137.33, -1.16])

        inner = pm.spaceLocator(n="inner")
        inner.t.set([75.79, 137.55, 4.45])

        self.locators = [middle, inner, outer]

        grp = pm.group(self.locators)
        grp.setParent(root)
        pm.matchTransform(root, hand_joint, pos=1)

        if "right" == side:
            pass

        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        root_con = controls[-1]
        hand = Hand(root, side=side, root_control=root_con)
        side = side if "" == side else side + "_"
        setattr(self, side + "hand", hand)

        for k, v in fingers.items():
            hand.finger_chain(v, name=k)

        aim_loc = pm.spaceLocator(n="aim_LOC")
        up_loc = pm.spaceLocator(n="up_LOC")
        up_loc.ty.set(3)
        up_loc.setParent(aim_loc)

        thumb_finger = hand.result_chain["thumb"].values()
        thumb_end = thumb_finger[-1]
        pm.matchTransform(aim_loc, thumb_end)

        thumb_start = thumb_finger[0]
        pm.aimConstraint(aim_loc, thumb_start,
                         mo=1,
                         aimVector=[1, 0, 0],
                         upVector=[0, 1, 0],
                         worldUpType="objectRotation",
                         worldUpVector=[0, 1, 0],
                         worldUpObject=up_loc)
        pm.select(aim_loc)
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
            pm.select(shoulder.groups["attach"])
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
