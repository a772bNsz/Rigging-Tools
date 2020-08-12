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
        return

    def rig(self, side):
        if not self.ui.space_switch_lsw.count():
            pm.warning("No spaces to connect leg rig.")

        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        knee_loc = "_".join([side, "knee"])

        root = pm.PyNode(side)
        root_con = controls[-1]

        from tools import leg as mod
        reload(mod)

        leg = mod.Rig(root, side=side, root_control=root_con, knee_loc=knee_loc)
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        leg.create_groups()
        leg.space_switch(controls)
        leg.clean_up()

        locators = {
            "heel": "heel_LOC",
            "ball": "ball_LOC",
            "toe": "toe_LOC",
            "inner": "innerFoot_LOC",
            "outer": "outerFoot_LOC"
        }
        for k, v in locators.items():
            name = side + v[0].upper() + v[1:]
            loc = pm.PyNode("_".join([side, k])).rename(name)
            locators[k] = loc

        leg.locators = locators
        leg.ik_foot()

        pm.delete(knee_loc)
        pm.select(cl=1)
        return

    def match(self):
        # locators
        left_locators = pm.ls("left_*", type="transform")
        right_locators = pm.ls("right_*", type="transform")

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

        # joints
        left_chain = pm.PyNode("left")
        left_chain = [left_chain] + left_chain.getChildren(ad=1)[::-1]

        right_chain = pm.PyNode("right")
        right_chain = [right_chain] + right_chain.getChildren(ad=1)[::-1]

        for right, left in zip(right_chain, left_chain):
            pos = left.getTranslation(space="world")
            pos[0] = pos[0] * -1
            right.setTranslation(pos, space="world")

            size = left.radius.get()
            right.radius.set(size)
        return
    
    def create_guides(self):
        # left
        pm.select(cl=1)
        root = pm.joint(p=[8.93, 83.9, 0.93], n="left")  # thigh
        pm.joint(p=[8.93, 53.22, 2.37])  # shin
        pm.joint(p=[8.93, 11.02, -3.94])  # foot
        pm.joint(p=[8.93, 2.27, 7.47])  # ball
        pm.joint(p=[8.93, 1.82, 19.65])  # toe

        chain = [root] + root.getChildren(ad=1)[::-1]

        locators = []
        locators += [pm.spaceLocator(n="left_knee")]
        pm.matchTransform(locators[-1], chain[1], pos=1)

        locators += [pm.spaceLocator(n="left_heel")]
        locators[-1].t.set(9.42, -0.16, -10.07)

        locators += [pm.spaceLocator(n="left_outer")]
        locators[-1].t.set(15.11, 0.0, 13.66)

        locators += [pm.spaceLocator(n="left_inner")]
        locators[-1].t.set(3.34, 0.0, 11.72)

        locators += [pm.spaceLocator(n="left_ball")]
        pm.matchTransform(locators[-1], chain[-2], pos=1)

        locators += [pm.spaceLocator(n="left_toe")]
        pm.matchTransform(locators[-1], chain[-1], pos=1)
        locators[-1].rotateOrder.set(2)

        self.color.sel = locators
        self.color.index = 6  # blue
        self.color.by_index()

        # right
        root = pm.duplicate(root, n="right")[0]
        root.tx.set(root.tx.get() * -1)

        for i, loc in enumerate(locators):
            name = loc.replace("left", "right")
            loc = locators[i] = pm.duplicate(loc, n=name)[0]
            loc.tx.set(loc.tx.get() * -1)

        self.color.sel = locators
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
