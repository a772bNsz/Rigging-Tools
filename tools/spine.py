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
        self.ui.joints_sld.valueChanged.connect(self._joints)
        self.ui.joints_sld.sliderReleased.connect(self._select_root)
        self.ui.ikspline_btn.clicked.connect(self._ikspline)
        self.ui.ribbon_btn.clicked.connect(self._ribbon)
        return

    def _select_root(self):
        pm.select(self.root)
        self.root = None
        return

    def _joints(self):
        if pm.ls(sl=1) and isinstance(pm.ls(sl=1)[0], pm.nodetypes.NurbsCurve):
            pm.warning("No curve selected.")
            return

        curve = pm.ls(sl=1)[0]
        if self.root:
            pm.delete(self.root)
            self.root = None
        val = self.ui.joints_sld.value()
        chain_name = self.ui.name_lne.text()
        self.root = joint_chain(curve, number=val, name=chain_name)
        pm.select(curve)
        return

    def _ikspline(self):
        return

    def _ribbon(self):
        return
