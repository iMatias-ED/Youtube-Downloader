from PySide2.QtWidgets import *
from PySide2.QtCore import *
from super_frame import Frame

class PreviewFrame(Frame):
    
    def setupUi(self):
        #thumbnail
        #pixmap = QPixmap("source/thumbnail.png")
        thumbnail = QLabel(self)
        #thumbnail.setPixmap(pixmap)
        thumbnail.setGeometry(157.5, 10, 155, 87)
        thumbnail.setStyleSheet(
            '''
                background: #0CBCCC;
            '''
        )

        #Video Title
        title = QLabel(self)
        title.setGeometry(10, 107, 450, 15)
        title.setText("Your Video ppTitle Here")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            '''
                color: #DBE1E1;
                font-family: BellMT;
                font-size: 14px;
                background: transparent;
                border: none;
            '''
        )

        #Video Quality selector
        quality = QComboBox(self)
        quality.setGeometry(197.5, 127, 75, 18)

        items = ["1080p", "720p", "480p", "360p", "240p", "144p"]

        quality.insertItems(0, items)

        quality.setStyleSheet(
            '''
                color: #DBE1E1;
                font-family: BellMT;
                font-size: 14px;
                border: none;
            '''
        )

        #Download Button
        downloadButton = QPushButton(self)
        downloadButton.setText("Download")
        downloadButton.setGeometry(185, 147, 100, 23)
        downloadButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background: #DBE1E1;
                }

                QPushButton:hover{
                    background: #0CBCCC;
                }
            '''
        )

        
    