import sys 
from qtpy import QtWidgets
import backendfunctions as bf
from ui.mainwindow import Ui_MainWindow
# Bootup Routines
app = QtWidgets.QApplication(sys.argv)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokalschießen 2022 - Rönnerburg")

window = MainWindow()

window.show()

sys.exit(app.exec_())