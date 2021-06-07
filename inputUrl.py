from PySide2.QtWidgets import *
from super_frame import Frame

class URLInputFrame(Frame):
    
    def setupUi(self):
        self.url = QLineEdit(self)
        self.url.setGeometry(7, 7, 380, 26) 
        self.url.setPlaceholderText("Inserte la URL del video.")
        self.url.setStyleSheet(
            u'''
                background: #dbe1e1;
                border: 0px;
            '''
        )

        self.searchButton = QPushButton(self)
        self.searchButton.setGeometry(397, 7, 63, 26)
        self.searchButton.setText("Search")
        self.searchButton.setStyleSheet(
            u'''
                QPushButton
                {
                    background: #DBE1E1;
                    border: none;
                }

                QPushButton:hover
                {
                    background: #0CBCCC;
                }

                
            '''
        )

    