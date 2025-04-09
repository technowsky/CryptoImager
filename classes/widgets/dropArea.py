from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from classes.image import Image

class dropArea(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("Drop image here")
        self.setStyleSheet( """
        QLabel{
            border: 5px dashed grey;
        }
        """)
        self.setAcceptDrops(True)

        self.img = None

        

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage: event.accept()
        else: event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            url = event.mimeData().urls()[0].path()
            if url[0] == "/" or url [0] == "\\": url = url[1:]
            self.img = Image(url)
            if self.img.pixmap.width() > self.img.pixmap.height(): self.img.pixmap = self.img.pixmap.scaledToWidth(self.width()-20)
            else: self.img.pixmap = self.img.pixmap.scaledToHeight(self.height()-20)
            self.setPixmap(self.img.pixmap)
            event.accept()
        else:
            print("nie zdj")
            event.ignore()