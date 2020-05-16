"""
# Loads /Rigging-Tools into current Maya session
import sys
pth = r"/Users/kathyhuinali/Documents/maya/projects/default/scripts/Rigging-Tools"
for p in sys.path[::-1]:
    if pth == p:
        sys.path.remove(p)
sys.path.append(pth)

# Loads script and updates in case edits were made
import ui_template
reload(ui_template)
ui_template.get_window()
"""
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from os import path


# UI
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

# end get_window


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        """
        Initializes the class.
        """
        self.ui = self.import_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.init_ui()

    # end __init__

    @staticmethod
    def import_ui():
        """
        Imports the designer ui file from disk (eliminating the step of
        converting it to Python classes first). The UI file shares the same
        name as the python file.
        :return: the complete ingested ui (QMainWindow)
        """
        basename = path.basename(__file__).split(".")[0] + ".ui"
        ui_file_path = path.join(path.dirname(__file__), "ui", basename)

        loader = QUiLoader()
        ui = loader.load(ui_file_path, None)

        return ui

    # end import_ui

    def init_ui(self):
        """
        Initializes the UI by populating and setting up functional
        connections between widgets.
        """
        self.ui.pushButton.clicked.connect(self.setup_ui)

    # end init_ui

    def setup_ui(self):
        """
        Sets up the UI with validators, slots and filters.
        """
        print ">> Button clicked."
        self.ui.pushButton.clicked.disconnect()  # won't print next time
        print ">> Button disconnected."
    # end setup_ui
# end class MyWindow
