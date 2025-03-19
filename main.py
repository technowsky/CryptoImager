from PIL import Image
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSpacerItem, QLineEdit, QTextEdit, QStackedWidget
from PyQt6.QtGui import QScreen, QPixmap
from PyQt6.QtCore import Qt, QRect
import sys
from classes.encoder import *


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

        self.width = 1600
        self.height = 900
        self.x = self.screen_rect[0].geometry().center().x()-int(self.width/2) if len(self.screen_rect) == 1 else 0
        self.y = self.screen_rect[0].geometry().center().y()-int(self.height/2) if len(self.screen_rect) == 1 else 0
        self.setGeometry(self.x,self.y,self.width,self.height)

        self.active_tab_css = "QPushButton{ height:50px;  width:100%; background-color:white;}"
        self.inactive_tab_css = "QPushButton{ height:50px;  width:100%; background-color: rgb(94, 94, 94);}"
        #self.setStyleSheet("QWidget{border: thick double #32a1ce;}")


        self.encode_tab_butt = QPushButton("Encode")
        self.decode_tab_butt = QPushButton("Decode")
        self.decode_tab_butt.setStyleSheet(self.inactive_tab_css)
        self.encode_tab_butt.setStyleSheet(self.active_tab_css)
        self.space = QSpacerItem(int(self.width/2), 50)

        self.encode_tab_butt.clicked.connect(self.encode_tab)
        self.decode_tab_butt.clicked.connect(self.decode_tab)

        self.main_layout = QVBoxLayout(self)

        self.tab_layout = QHBoxLayout()
        self.tab_layout.addWidget(self.encode_tab_butt)
        self.tab_layout.addWidget(self.decode_tab_butt)
        self.tab_layout.addSpacerItem(self.space)


        self.lower_layout = QStackedWidget()
        decodeWidget = QWidget()
        decodeWidget.setLayout(self.generate_decode_low_layout())
        encodeWidget = QWidget()
        encodeWidget.setLayout(self.generate_encode_low_layout())

        self.lower_layout.addWidget(decodeWidget)
        self.lower_layout.addWidget(encodeWidget)

        self.main_layout.addLayout(self.tab_layout)
        self.main_layout.addWidget(self.lower_layout)
        


    def generate_decode_low_layout(self):
        layout = QGridLayout()
        pass_input = QLineEdit()
        pin_input = QLineEdit()
        code_button = QPushButton("Code")
        imgs_frame = QFrame()
        output_text = QTextEdit()

        layout.addWidget(pass_input, 0, 0, 1, 2)
        layout.addWidget(pin_input, 0, 3, 1, 2)
        layout.addWidget(code_button, 0, 6, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(imgs_frame, 1, 0, 5, 5)
        layout.addWidget(output_text, 1, 6, 5, 3)
        return layout

    def generate_encode_low_layout(self):
        layout = QGridLayout()

        #pass_input
        pass_input = QLineEdit()
        pass_label = QLabel("Password:")

        #image_input
        img_display = QLabel()
        #img_display.clicked.connect(select_image)
        pixmap = QPixmap("test_imgs/add_image_icon.png")
        img_display.setPixmap(pixmap.scaledToHeight(250))
        img_display.resize(25, 25)

        #string_input
        str_input = QTextEdit()
       
        #pin_output
        pin_output = QLineEdit()
        pin_output.setReadOnly(True)

        code_butt = QPushButton("Code")
        code_butt.clicked.connect(lambda: self.encode_password(pass_input, str_input))    #output_label

        output_label = QLabel("Output data:")

        child_layout_1 = QHBoxLayout()
        child_layout_1.addWidget(pass_label)
        child_layout_1.addWidget(pass_input)

        child_layout_2 = QHBoxLayout()
        child_layout_2.addWidget(str_input)
        child_layout_2.addWidget(img_display)
        
        output_layout = QVBoxLayout()
        output_layout.addWidget(output_label, alignment=Qt.AlignmentFlag.AlignTop)
        output_layout.addWidget(pin_output, alignment=Qt.AlignmentFlag.AlignTop)

        child_layout_2.addLayout(output_layout)

        layout.addLayout(child_layout_1, 0, 0)
        layout.addLayout(child_layout_2, 1, 0)
        layout.addWidget(code_butt, 2, 0, 1, 3)

        return layout

    def decode_tab(self):
        self.decode_tab_butt.setStyleSheet(self.active_tab_css)
        self.encode_tab_butt.setStyleSheet(self.inactive_tab_css)
        self.lower_layout.setCurrentIndex(0)

    def encode_tab(self):
        self.encode_tab_butt.setStyleSheet(self.active_tab_css)
        self.decode_tab_butt.setStyleSheet(self.inactive_tab_css)
        self.lower_layout.setCurrentIndex(1)

    def encode_password(self, pass_wig, text_wig):
        text = text_wig.toPlainText()
        password = pass_wig.text()
        hashed_p = Encoder._pass_to_hash(password)
        hashed_vi = Encoder._get_VI(password)
        print(Encoder._aes_encode(hashed_p.encode(), hashed_vi.encode(), text.encode()))
    
            

        


if __name__ == "__main__":
    #main()
    app = QApplication([])
    widget = main_window()
    widget.show()

    sys.exit(app.exec())

    
    #str_fun()