from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Main Window
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, mainwindow):
        mainwindow.setFixedSize(500, 600)




import sys
#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ui_MainWindow()
    window.setupUi(window)
    window.show()

    sys.exit(app.exec_())