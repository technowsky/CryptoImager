from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout

class setting_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 500)

        self.save_dir_label = QLabel("Saving Directory:") #Select where encoded image will be saved | empty = program folder
        self.coding_method_label = QLabel("Encoding/decoding Method:") #Select what methods text will be encoded | diagonal pixels - from first to last - random(using pincode) - from center loop
        self.save_custom_name_label = QLabel("Saving Name:") #Select if saving name | global (prefix_selected-image-name) - ask every time - same as selected image
        self.save_prefix_label = QLabel("Saving Prefix:") #User prefix for saving encoded image (only visable when global name is selected)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.save_dir_label)
        self.layout.addWidget(self.coding_method_label)
        self.layout.addWidget(self.save_custom_name_label)
        self.layout.addWidget(self.save_prefix_label)

        self.show()
        