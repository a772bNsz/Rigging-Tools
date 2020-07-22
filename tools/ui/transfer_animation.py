"""
import sys
pth = r"PATH/rockstar_test"
if pth not in sys.path:
    sys.path.append(pth)
    print ">> Added:", pth

from tools.ui import transfer_animation as rt

reload(rt)
rt.get_window()
"""

from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance
from maya.OpenMayaUI import MQtUtil

from os import path

from tools.transfer_animation import TransferAnimation


def get_window():
    global mw
    try:
        mw.close()
    except:
        pass

    main_window_ptr = MQtUtil.mainWindow()
    maya_window = wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

    mw = MyWindow(parent=maya_window)
    mw.show()
    return mw


class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        """
        transfer animation UI parented to Maya main window
        uses either UI file or coded method
        :param parent: Maya main window
        """

        self.transferAnimation = TransferAnimation()

        root_dir = __file__.split("tools")[0]
        self.default_path = path.join(root_dir, "results")

        # build UI
        super(MyWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Transfer Animation Tool")
        # self.resize(250, 150)
        # self.setMaximumSize(250, 150)

        vertical_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(vertical_layout)

        save_button = QtWidgets.QPushButton("Save")
        save_button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addWidget(save_button)

        load_button = QtWidgets.QPushButton("Load")
        load_button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        vertical_layout.addWidget(load_button)

        group_box = QtWidgets.QGroupBox("Load Options")
        vertical_layout.addWidget(group_box)

        form_layout = QtWidgets.QFormLayout(parent=group_box)
        start_frame = QtWidgets.QLineEdit()
        start_frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        form_layout.addRow("Start Frame", start_frame)

        self.start_frame = start_frame

        # connect signals and slots
        save_button.clicked.connect(self.save_file)
        load_button.clicked.connect(self.load_file)

    def save_file(self):
        save_filename = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save file as...", self.default_path, "*.json")[0]

        if save_filename == "":
            return

        # save rotate and translate only
        attributes = []
        for at in "rt":
            for ax in "xyz":
                attributes += [at + ax]

        self.transferAnimation.save_data(save_filename, attributes)

    def load_file(self):
        load_filename = QtWidgets.QFileDialog.getOpenFileName(
            None, "Choose an Existing File.", self.default_path, "*.json")[0]

        if load_filename == "":
            return

        start_frame = self.start_frame.text()
        start_frame = None if "" == start_frame else float(start_frame)

        self.transferAnimation.load_data(load_filename, start_frame)
