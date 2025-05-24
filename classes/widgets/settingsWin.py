from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class setting_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 500)

        self.save_dir_label = QLabel("Saving Directory:") #Select where encoded image will be saved | empty = program folder
        self.coding_method_label = QLabel("Encoding/decoding Method:") #Select what methods text will be encoded | diagonal pixels - from first to last - random(using pincode) - from center loop
        self.save_custom_name_label = QLabel("Saving Name:") #Select if saving name | global (prefix_selected-image-name) - ask every time - same as selected image
        self.save_prefix_label = QLabel("Saving Prefix:") #User prefix for saving encoded image (only visable when global name is selected)

        self.save_dir_input = QLineEdit()
        self.coding_method_select = QLineEdit()
        self.save_custom_name_input = QLineEdit()
        self.save_prefix_input = QLineEdit()

        self.save_button = QPushButton("Save")
        self.select_dir_button = QPushButton("Select path")

        self.save_button.clicked.connect(self.save_settings)

        self.save_dir_layout = QHBoxLayout()
        self.coding_method_layout = QHBoxLayout()
        self.save_custom_name_layout = QHBoxLayout()
        self.save_prefix_layout = QHBoxLayout()

        self.save_dir_layout.addWidget(self.save_dir_label)
        self.save_dir_layout.addWidget(self.save_dir_input)
        self.save_dir_layout.addWidget(self.select_dir_button)

        self.coding_method_layout.addWidget(self.coding_method_label)
        self.coding_method_layout.addWidget(self.coding_method_select)
        
        self.save_custom_name_layout.addWidget(self.save_custom_name_label)
        self.save_custom_name_layout.addWidget(self.save_custom_name_input)

        self.save_prefix_layout.addWidget(self.save_prefix_label)
        self.save_prefix_layout.addWidget(self.save_prefix_input)


        self.layout = QVBoxLayout()
        #self.layout.addWidget(self.save_dir_label)
        #self.layout.addWidget(self.coding_method_label)
        #self.layout.addWidget(self.save_custom_name_label)
        #self.layout.addWidget(self.save_prefix_label)
        self.layout.addLayout(self.save_dir_layout)
        self.layout.addLayout(self.coding_method_layout)
        self.layout.addLayout(self.save_custom_name_layout)
        self.layout.addLayout(self.save_prefix_layout)
        self.layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(self.layout)

    def save_settings(self):
        ...

        