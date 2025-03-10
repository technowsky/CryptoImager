from PIL import Image
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSpacerItem, QLineEdit, QTextEdit
from PyQt6.QtGui import QScreen
from PyQt6.QtCore import Qt, QRect
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

        with open('css/style.css', 'r') as f:
            self.css = f.read()

        self.setStyleSheet(self.css)

        self.encode_tab = QPushButton("Encode")
        self.encode_tab.setObjectName("en_tab")
        self.decode_tab = QPushButton("Decode")
        self.space = QSpacerItem(int(self.width/2), 50)

        self.main_layout = QVBoxLayout(self)

        self.frame = QFrame()
        self.frame.setFrameRect(QRect(0, 0, self.width, self.height-50))

        self.tab_layout = QHBoxLayout()
        self.tab_layout.setObjectName('tab_layout')
        self.tab_layout.addWidget(self.encode_tab)
        self.tab_layout.addWidget(self.decode_tab)
        self.tab_layout.addSpacerItem(self.space)


        ##Lower Layout
        self.lower_layout = QGridLayout()
        
        self.pass_input = QLineEdit()
        self.pin_input = QLineEdit()
        self.code_button = QPushButton("Code")
        self.imgs_frame = QFrame()
        self.output_text = QTextEdit()

        self.lower_layout.addWidget(self.pass_input, 0, 0, 1, 2)
        self.lower_layout.addWidget(self.pin_input, 0, 3, 1, 2)
        self.lower_layout.addWidget(self.code_button, 0, 6, 1, 2, Qt.AlignmentFlag.AlignCenter)
        self.lower_layout.addWidget(self.imgs_frame, 1, 0, 5, 5)
        self.lower_layout.addWidget(self.output_text, 1, 6, 5, 3)



        self.main_layout.addLayout(self.tab_layout)
        self.main_layout.addLayout(self.lower_layout)


        


if __name__ == "__main__":
    #main()
    app = QApplication([])
    widget = main_window()
    widget.show()

    sys.exit(app.exec())

    
    #str_fun()