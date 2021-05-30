from PySide2.QtWidgets import *

class Frame(QFrame):

    def __init__(self, mainwindow, width, height, xPosition, Yposition):
        super().__init__(mainwindow)
        self.setGeometry(width, height, xPosition, Yposition)

        self.setStyles()
    
    def setStyles(self):
        self.setStyleSheet(
            u'''
                background: black;
            '''
        )

