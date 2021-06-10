from youtube import YoutubeVideo
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Components import
from super_frame import *
from presentation import *
from inputUrl import *
from preview import *
from progressBar import *

#Main Window
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, mainwindow):
        mainwindow.setFixedSize(500, 600)
        mainwindow.setStyleSheet(u"background: #0cbccc")

        self.presentation = PresentationFrame(self, 15, 15, 470, 130)
        self.presentation.setupUi()

        self.input = URLInputFrame(self, 15, 160, 470, 40)
        self.input.setupUi()
        self.input.searchButton.clicked.connect(lambda:self.chargeVideoPreview(self.input.url.text()))           

        self.preview = PreviewFrame(self, 15, 215, 470, 175)
        self.preview.setupUi()
        self.preview.downloadButton.clicked.connect(self.Download)

        self.leftSquare = Frame(self, 15, 405, 227.5, 140)
        
        self.rightSquare = Frame(self, 257.5, 405, 227.5, 140)

        self.progressBar = ProgressBarFrame(self, 15, 560, 470, 25)
        self.progressBar.setupUi()
        
    def chargeVideoPreview(self, url):
        self.preview.getVideoInfo(url)

    def Download(self):
        video = self.preview.video

        video.receiveProgressBar(self.progressBar.p_bar)

        self.preview.getDirectoryPath()



import sys
#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ui_MainWindow()
    window.setupUi(window)
    window.show()

    sys.exit(app.exec_())


