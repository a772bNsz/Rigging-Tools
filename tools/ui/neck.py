from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from pymel.util.path import path
import pymel.core as pm

from tools.joint_chain import joint_chain


def get_window():
    """Loads one UI only; removes previous UI if it's there."""
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
        """
        Initializes the class.
        """
        self.ui = self.import_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.init_ui()
        self.root = None

    @staticmethod
    def import_ui():
        """
        Imports the designer ui file from disk (eliminating the step of
        converting it to Python classes first). The UI file shares the same
        name as the python file.
        :return: the complete ingested ui (QMainWindow)
        """
        ui_file_path = path(__file__.split(".")[0] + ".ui")

        loader = QUiLoader()
        ui = loader.load(ui_file_path, None)
        return ui

    def init_ui(self):
        """
        Initializes the UI by populating and setting up functional
        connections between widgets.
        """
        self.ui.joints_sld.valueChanged.connect(self.joints_sld_changed)
        self.ui.joints_sld.sliderReleased.connect(self._select_root)

        self.ui.numjoints_lne.returnPressed.connect(self.numjoint_lne_returned)

        self._load_default_spaces()
        self.ui.add_btn.clicked.connect(self._add_listwidgetitem)
        self.ui.minus_btn.clicked.connect(self._minus_listwidgetitem)

        self.ui.ikspline_btn.clicked.connect(self._ikspline)
        self.ui.ribbon_btn.clicked.connect(self._ribbon)

        # REMOVE RIBBON FOR NOW
        self.ui.ribbon_btn.deleteLater()
        return

    def _add_listwidgetitem(self):
        for sel in pm.ls(sl=1):
            item = QtWidgets.QListWidgetItem(str(sel))
            self.ui.space_switch_lsw.addItem(item)
        return

    def _minus_listwidgetitem(self):
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

    def _select_root(self):
        pm.select(self.root)
        self.root = None
        return

    def joints_sld_changed(self):
        number = self.ui.joints_sld.value()
        self._joints(number)

        self.ui.numjoints_lne.setText("")
        self.ui.numjoints_lne.setPlaceholderText(str(number))
        return

    def numjoint_lne_returned(self):
        number = int(self.ui.numjoints_lne.text())
        self._joints(number)
        self._select_root()

        self.ui.joints_sld.valueChanged.disconnect(self.joints_sld_changed)
        self.ui.joints_sld.setSliderPosition(number)
        self.ui.joints_sld.valueChanged.connect(self.joints_sld_changed)
        return

    def _joints(self, number):
        if pm.ls(sl=1) and isinstance(pm.ls(sl=1)[0], pm.nodetypes.NurbsCurve):
            pm.warning("No curve selected.")
            return

        curve = pm.ls(sl=1)[0]
        if self.root:
            pm.delete(self.root)
            self.root = None

        chain_name = self.ui.name_lne.text()
        self.root = joint_chain(curve, number=number, name=chain_name)
        pm.select(curve)
        return

    def _ikspline(self):
        if pm.ls(sl=1) and not isinstance(pm.ls(sl=1)[0], pm.nodetypes.Joint):
            pm.warning("No root joint selected.")
            return

        controls = []
        i = self.ui.space_switch_lsw.count()
        for e in range(i):
            controls += [pm.PyNode(self.ui.space_switch_lsw.item(e).text())]

        root = pm.ls(sl=1)[0]

        from tools import head_neck
        reload(head_neck)
        neck = head_neck.Rig(root)
        neck.ik_spline()
        neck.setup_controls()

        #TODO: add neck_CON to space switch
        print ">>", pm.ls(sl=1)
        # self._add_listwidgetitem()

        neck.guts()
        neck.connect("chest_CON")
        neck.space_switch(controls)
        neck.clean_up()
        return

    def _ribbon(self):
        return
