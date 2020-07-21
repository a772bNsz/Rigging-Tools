from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from shiboken2 import wrapInstance
from maya.OpenMayaUI import MQtUtil
from pymel.util.path import path

import pymel.core as pm
from tools import color_shapes
reload(color_shapes)


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

        self.color = color_shapes.ColorShapes()

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

        self.ui.guides_btn.clicked.connect(self.create_guides)
        self.ui.match_left_to_right_btn.clicked.connect(self.match)

        self.ui.rig_left_btn.clicked.connect(lambda x="left": self.rig(x))
        self.ui.rig_right_btn.clicked.connect(lambda x="right": self.rig(x))

        self.ui.minus_90_btn.clicked.connect(lambda x="minus": self.rotate(x))
        self.ui.add_90_btn.clicked.connect(lambda x="add": self.rotate(x))
        return

    def rig(self, side):
        shoulder, arm, hand = \
            ["_".join([side, n]) for n in ["shoulder", "arm", "hand"]]
        
        if pm.objExists(shoulder):
            self.rebuild_shoulder(side)
            # self.rig_shoulder()

        if pm.objExists(arm):
            self.rebuild_arm(side)
            # self.rig_arm()

        if pm.objExists(hand):
            self.rebuild_hand(side)
            # self.rig_hand()

        #TODO: delete locators
        return

    @staticmethod
    def rebuild_hand(side):
        guide_start = pm.PyNode("_".join([side, "hand"]))
        finger_guide_roots = guide_start.getChildren()

        for root in finger_guide_roots:
            pm.select(cl=1)

            chain = []
            guides = [root] + root.getChildren(ad=1)[::-1]
            for guide in guides:
                pos = guide.getTranslation(ws=1)
                chain += [pm.joint(p=pos)]

            pm.joint(chain, e=1, oj="xyz", sao="ydown", ch=1, zso=1)
            chain[-1].jointOrient.set(0, 0, 0)
        return

    @staticmethod
    def rebuild_arm(side):
        guide_start = pm.PyNode("_".join([side, "arm"]))
        guide_end = pm.PyNode("_".join([side, "hand"]))

        guides = [guide_start] + guide_start.getChildren(ad=1)[::-1]
        i = guides.index(guide_end) + 2
        guides = guides[:i]  # arm to hand end

        chain = []
        pm.select(cl=1)
        for guide in guides:
            pos = guide.getTranslation(ws=1)
            chain += [pm.joint(p=pos)]
        chain[-1].ty.set(0)
        chain[-1].tz.set(0)

        pm.joint(chain, e=1, oj="xyz", sao="ydown", ch=1, zso=1)
        return chain

    @staticmethod
    def rebuild_shoulder(side):
        guide_start = pm.PyNode("_".join([side, "shoulder"]))
        guide_end = guide_start.getChildren()[0]

        chain = []
        pm.select(cl=1)
        for guide in [guide_start, guide_end]:
            pos = guide.getTranslation(ws=1)
            chain += [pm.joint(p=pos)]

        pm.joint(chain, e=1, oj="xyz", sao="yup", ch=1, zso=1)
        return chain

    def match(self):
        # locators
        left_locators = \
            [loc.getParent() for loc in pm.ls("left_*", type="locator")]
        right_locators = \
            [loc.getParent() for loc in pm.ls("right_*", type="locator")]

        for right, left in zip(right_locators, left_locators):
            match = right.replace("right", "left") == left
            if not match:
                right = pm.spaceLocator(n=left.replace("left", "right"))

                self.color.sel = right
                self.color.index = 12  # red right
                self.color.by_index()

            pos = left.getTranslation(space="world")
            pos[0] = pos[0] * -1
            right.setTranslation(pos, space="world")

            size = left.localScale.get()
            right.localScale.set(size)

            if "aim" not in str(left):
                left.rotate.set(0, 0, 0)
                right.rotate.set(0, 0, 0)

        # joints
        left_chain, = filter(
            lambda x: pm.nodeType(x) == "joint", pm.ls("left*", assemblies=1))
        left_chain = [left_chain] + \
                     left_chain.getChildren(ad=1, type="joint")[::-1]

        right_chain, = filter(
            lambda x: pm.nodeType(x) == "joint", pm.ls("right*", assemblies=1))
        right_chain = [right_chain] + \
                      right_chain.getChildren(ad=1, type="joint")[::-1]

        for right, left in zip(right_chain, left_chain):
            pos = left.getTranslation(space="world")
            pos[0] = pos[0] * -1
            right.setTranslation(pos, space="world")

            size = left.radius.get()
            right.radius.set(size)
        return

    @staticmethod
    def orbit_guide(side, thumb):
        aim_loc = pm.spaceLocator(n="_".join([side, "aim"]))
        up_loc = pm.spaceLocator(n="_".join([side, "up"]))
        up_loc.setParent(aim_loc)

        thumb_end = thumb.getChildren(ad=1)[0]
        pm.matchTransform(aim_loc, thumb_end)

        aim_const = pm.aimConstraint(aim_loc, thumb,
                                     mo=1,
                                     aimVector=[1, 0, 0],
                                     upVector=[0, 1, 0],
                                     worldUpType="objectRotation",
                                     worldUpVector=[0, 1, 0],
                                     worldUpObject=up_loc)
        return [aim_loc, up_loc], aim_const

    def create_guides(self):
        # left
        arm = pm.joint(p=[8.91, 142.2, 0.97], n="left_shoulder")  # shoulder
        pm.joint(p=[17.19, 138.49, 0.94], n="left_arm")  # upper arm
        pm.joint(p=[40.69, 138.49, 1.44])  # lower arm
        root = pm.joint(p=[68.17, 138.49, 2.02], n="left_hand")  # hand
        # pm.joint(p=[75.66, 138.49, 2.18])

        pm.select(root)
        pinky = pm.joint(p=[72.26, 138.44, -0.63], n="left_pinky")
        pm.joint(p=[76.93, 138.44, -0.9])
        pm.joint(p=[79.19, 138.44, -0.9])
        pm.joint(p=[81.26, 138.44, -0.9])
        pm.joint(p=[83.04, 138.44, -0.9])

        pm.select(root)
        ring = pm.joint(p=[72.32, 138.85, 0.79], n="left_ring")
        pm.joint(p=[77.23, 138.85, 0.67])
        pm.joint(p=[80.56, 138.85, 0.67])
        pm.joint(p=[83.09, 138.85, 0.67])
        pm.joint(p=[85.03, 138.85, 0.67])

        pm.select(root)
        middle = pm.joint(p=[72.32, 139.11, 2.14], n="left_middle")
        pm.joint(p=[77.59, 139.11, 2.3])
        pm.joint(p=[81.01, 139.11, 2.3])
        pm.joint(p=[83.58, 139.11, 2.3])
        pm.joint(p=[85.66, 139.11, 2.3])

        pm.select(root)
        index = pm.joint(p=[72.23, 139.11, 3.62], n="left_index")
        pm.joint(p=[77.74, 139.11, 3.87])
        pm.joint(p=[80.85, 139.11, 3.87])
        pm.joint(p=[83.39, 139.11, 3.87])
        pm.joint(p=[85.33, 139.11, 3.87])

        pm.select(root)
        thumb = pm.joint(p=[71.11, 137.67, 5.15], n="left_thumb")
        pm.joint(p=[73.27, 136.91, 6.71])
        pm.joint(p=[74.76, 136.39, 7.78])
        pm.joint(p=[76.83, 135.66, 9.28])

        chain = [arm] + arm.getChildren(ad=1)[::-1]
        pm.joint(chain, e=1, oj="xyz", sao="ydown", ch=1, zso=1)
        for finger_root in [thumb, index, middle, ring, pinky]:
            tip_joint = finger_root.getChildren(ad=1)[0]
            tip_joint.jointOrient.set(0, 0, 0)

        aim_locators, aim_const = self.orbit_guide("left", thumb)

        locators = [pm.spaceLocator(n="left_elbow")]
        pm.matchTransform(locators[-1], chain[2], pos=1)
        pm.select(cl=1)

        locators += [pm.spaceLocator(n="left_middle")]
        locators[-1].t.set(77.59, 139.11, 2.3)

        locators += [pm.spaceLocator(n="left_outer")]
        locators[-1].t.set(75.37, 137.33, -1.16)

        locators += [pm.spaceLocator(n="left_inner")]
        locators[-1].t.set(75.79, 137.55, 4.45)

        self.color.sel = locators + aim_locators
        self.color.index = 6  # blue
        self.color.by_index()

        # right
        for i, loc in enumerate(locators):
            name = loc.replace("left", "right")
            loc = locators[i] = pm.duplicate(loc, n=name)[0]
            loc.tx.set(loc.tx.get() * -1)

        pm.PyNode(pm.mirrorJoint(arm, mirrorYZ=1, mirrorBehavior=1,
                                 searchReplace=["left", "right"])[0])

        thumb = pm.PyNode("right_thumb")
        aim_locators, aim_const = self.orbit_guide("right", thumb)

        self.color.sel = locators + aim_locators
        self.color.index = 12  # red right
        self.color.by_index()

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

    def rotate(self, direction):
        selection = pm.ls(sl=1)
        rotate_axis = str(self.ui.rotate_axis_cbx.currentText())
        value = -90 if direction == "minus" else 90

        for sel in selection:
            params = {
                rotate_axis: 1,
                "r": 1,
                "eu": 1,
                "fo": 1
            }
            pm.rotate(sel, value, **params)
        return
