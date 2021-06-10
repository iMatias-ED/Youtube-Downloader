from PySide2.QtWidgets import *
from PySide2.QtCore import *
from super_frame import Frame

class ProgressBarFrame(Frame):
    def setupUi(self):
        self.p_bar = QProgressBar(self)
        self.p_bar.setGeometry(7, 5, 456, 15)
        self.p_bar.setAlignment(Qt.AlignCenter)
        self.p_bar.setStyleSheet(u'''
        background: #DBE1E1;
        border: none;
        border-radius: 3px;
        ''')

    def updateProgressBar(self, percent):
        print("Actualizando valor de progress bar")
        self.p_bar.setValue(percent)
    