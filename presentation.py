from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
from super_frame import Frame

class PresentationFrame(Frame):

    def setupUi(self):

        #logo
        image = QLabel(self)
        pixmapLogo = QPixmap("caiman.png")
        image.setPixmap(pixmapLogo)
        image.setGeometry(10,10,110,110)

                #big title
        title = QLabel(self)
        title.setText("YouTube Downloader")
        title.setGeometry(130,20, 330, 35)
        title.setStyleSheet(
            u'''
            border: 0px;
            border-radius: 0px;

            color: white;        
            font-family: Bookman old style;            
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            '''
        )

        #slogan
        slogan = QLabel(self)
        slogan.setText("Download Videos for Free")
        slogan.setGeometry(130,55,330,20)
        slogan.setStyleSheet(
            u'''
            border: 0px;
            border-radius: 0px;

            color: #0cbccc;        
            font-family: BellMT;            
            font-size: 10;
            font-weight: italic;
            '''
        )

        #SocialNetworks

        #Instagram
        instagramLogo = QLabel(self)
        pixmapIg = QPixmap("ig.png")
        instagramLogo.setPixmap(pixmapIg)
        instagramLogo.setGeometry(130,90,30,30)
        instagramLogo.setStyleSheet(u"border: 0px;")

        igLabel = QLabel(self)
        igLabel.setText("@imatias_ed")
        igLabel.setGeometry(161, 100, 100, 20)
        igLabel.setStyleSheet(
            u'''
                border: 0px;
                font-family: BellMT;
                font-size: 12px;
                color: white;
            '''
        )


        #Linkedin
        githubLogo = QLabel(self)
        pixmapGitHub = QPixmap("github.png")
        githubLogo.setPixmap(pixmapGitHub)
        githubLogo.setGeometry(295,93,30,30)
        githubLogo.setStyleSheet(u"border: 0px;")

        githubLabel = QLabel(self)
        githubLabel.setText("iMatias-ED")
        githubLabel.setGeometry(326, 100, 100, 20)
        githubLabel.setStyleSheet(
            u'''
                border: 0px;
                font-family: BellMT;
                font-size: 12px;
                color: white;
            '''
        )






