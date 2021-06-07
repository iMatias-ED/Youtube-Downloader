from PySide2.QtWidgets import *
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import *
from PySide2.QtNetwork import *

from super_frame import Frame
from youtube import *


class PreviewFrame(Frame):
    
    def setupUi(self):
        #thumbnail
        self.thumbnail = QLabel(self)
        self.thumbnail.setGeometry(157.5, 10, 155, 87)
        self.thumbnail.setStyleSheet(
            '''
                border: none;
                border-radius: 0px;
                background: #0CBCCC;
            '''
        )

        #Video Title
        self.title = QLabel(self)
        self.title.setGeometry(10, 107, 450, 15)
        self.title.setText("Your Video Title Here")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            '''
                color: #DBE1E1;
                font-family: BellMT;
                font-size: 14px;
                background: transparent;
                border: none;
            '''
        )

        #Video Quality selector
        self.quality = QComboBox(self)
        self.quality.setGeometry(197.5, 127, 75, 18)

        #self.quality.insertItems(0, self.items)

        self.quality.setStyleSheet(
            '''
                color: #DBE1E1;
                font-family: BellMT;
                font-size: 14px;
                border: none;
            '''
        )

        #Download Button
        self.downloadButton = QPushButton(self)
        self.downloadButton.setText("Download")
        self.downloadButton.setGeometry(185, 147, 100, 23)
        self.downloadButton.setStyleSheet(
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
    
    def videoData(self, url):
        print("funcion video data llamada")
        video = YoutubeVideo(url)

        self.title.setText(video.title)

        #charge video thumbnail
        url_image = video.thumbnail_url
        manager = QNetworkAccessManager(self)
        manager.finished.connect(self.onFinished)
        manager.get(QNetworkRequest(QUrl(url_image)))

        resolutions = video.streams.filter(file_extension="mp4")
        items = []

        for i in resolutions:
            items.append(i.resolution)

        self.quality.insertItems(0, items)

        #mp4 = video.streams.get_by_itag(itag)
        #mp4.download()




        
    def onFinished(self, reply):
        print("En teoria cargando la imagen")
        qimage = QImage.fromData(reply.readAll())

        image = QPixmap.fromImage(qimage)
        image = image.scaledToWidth(155)
        image = image.scaledToHeight(87)

        self.thumbnail.setPixmap(image)
        

        
    