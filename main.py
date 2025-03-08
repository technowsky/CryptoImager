from PIL import Image
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QScreen
from PyQt6.QtCore import Qt
import sys

def main():
    img = Image.open("test_imgs/1.jpg")
    img_size = img.size
    #img.show()
    img_bytes = img.tobytes()

    with open("img_bytes.txt", "w") as f:
        f.write(' '.join([format(b, 'b') for b in img_bytes]))

def str_fun():
    string = [b for b in bytes("testowy string", "UTF-8")]
    bits = [format(b, 'b') for b in string]
    print(len(bits), bits)
    print(len(string), string)


class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_rect = list(filter(lambda s: 
                s.geometry().x() == 0 and
                s.geometry().y() == 0
                , QApplication.screens()))

        self.width = 1000
        self.height = 570
        self.x = self.screen_rect[0].geometry().center().x()-int(self.width/2) if len(self.screen_rect) == 1 else 0
        self.y = self.screen_rect[0].geometry().center().y()-int(self.height/2) if len(self.screen_rect) == 1 else 0
        self.setGeometry(self.x,self.y,self.width,self.height)

        self.css = '''

        QHBoxLayout#tab_layout{
        border: solid black 3px;
        }

        '''

        self.setStyleSheet(css.self.css)

        self.encode_tab = QPushButton("Encode")
        self.decode_tab = QPushButton("Decode")

        self.main_layout = QVBoxLayout(self)

        self.tab_layout = QHBoxLayout()
        self.tab_layout.setObjectName('tab_layout')
        self.tab_layout.addWidget(self.encode_tab)
        self.tab_layout.addWidget(self.decode_tab)

        self.main_layout.addLayout(self.tab_layout)

        


if __name__ == "__main__":
    #main()
    app = QApplication([])
    widget = main_window()
    widget.show()

    sys.exit(app.exec())

    
    #str_fun()