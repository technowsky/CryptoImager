from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

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

        

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage: event.accept()
        else: event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            print(event.mimeData().urls())
            event.accept()
        else:
            print("nie zdj")
            event.ignore()