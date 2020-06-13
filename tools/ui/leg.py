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

        self.ui.right_btn.clicked.connect(lambda x="right": self.rig_leg(x))
        self.ui.mid_btn.clicked.connect(lambda x="": self.rig_leg(x))
        self.ui.left_btn.clicked.connect(lambda x="left": self.rig_leg(x))
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
        return

    def _add_list_widget_item(self):
        for sel in pm.ls(os=1):
            item = QListWidgetItem(str(sel))
            # self.ui.space_switch_lsw.addItem(item)
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
