from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout, QComboBox
from PyQt6.QtCore import Qt
from pathlib import Path
import json, os
from .. import settingManager

class setting_window(QWidget):
    def __init__(self):
        super().__init__()


        self.setFixedSize(700, 500)

        self.save_dir_label = QLabel("Saving Directory:") #Select where encoded image will be saved | empty = program folder
        self.coding_method_label = QLabel("Encoding/decoding Method:") #Select what methods text will be encoded | diagonal pixels - from first to last - random(using pincode) - from center loop
        self.save_custom_name_label = QLabel("Saving Name:") #Select if saving name | global (prefix_selected-image-name) - ask every time - same as selected image
        self.save_prefix_label = QLabel("Saving Prefix:") #User prefix for saving encoded image (only visable when global name is selected)

        self.save_dir_input = QLineEdit()
        self.save_dir_input.setReadOnly(True)
        self.save_dir_input.setText(settingManager.get_setting("save_dir"))

        self.coding_method_select = QComboBox()
        self.coding_method_select.addItems(["Diagonal", "From first to last", "Random", "Spiral from center"])
        self.coding_method_select.setCurrentIndex(settingManager.get_setting("coding_method"))

        self.save_custom_name_input = QComboBox()
        self.save_custom_name_input.addItems(["Global", "Ask every time", "Same as selected image"])
        self.save_custom_name_input.setCurrentIndex(settingManager.get_setting("save_custom_name"))
        self.save_custom_name_input.activated.connect(self.display_prefix)


        self.save_prefix_input = QLineEdit()
        self.save_prefix_input.setText(settingManager.get_setting("save_prefix"))

        self.save_button = QPushButton("Save")
        self.select_dir_button = QPushButton("Select path")

        self.save_button.clicked.connect(self.save_settings)
        self.select_dir_button.clicked.connect(self.select_saving_path)

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
        self.display_prefix()
        self.layout.addLayout(self.save_prefix_layout)
        self.layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(self.layout)

    def save_settings(self):

        settingManager.set_setting("save_dir", self.save_dir_input.text())
        settingManager.set_setting("coding_method", self.coding_method_select.currentIndex())
        settingManager.set_setting("save_custom_name", self.save_custom_name_input.currentIndex())
        settingManager.set_setting("save_prefix", self.save_prefix_input.text())
        
        settingManager.save_settings()

        self.close()


    def display_prefix(self):
        settingManager.set_setting("save_custom_name", self.save_custom_name_input.currentIndex())
        if settingManager.get_setting("save_custom_name") != 0:
            self.save_prefix_label.hide()
            self.save_prefix_input.hide()
        else:
            self.save_prefix_label.show()
            self.save_prefix_input.show()

    def select_saving_path(self):
        fd = QFileDialog()
        selected_path = fd.getExistingDirectory()
        if selected_path:
            path = str(Path(selected_path)) + os.sep
        else:
            path = settingManager.get_setting("save_dir")
            
        self.save_dir_input.setText(path)
        settingManager.set_setting("save_dir", path)




        

        