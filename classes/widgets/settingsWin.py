from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout, QComboBox
from PyQt6.QtCore import Qt
import json


class setting_window(QWidget):
    def __init__(self):
        super().__init__()

        self.settings_path = "settings.json"

        try:
            with open(self.settings_path, "r") as f:
                self.json_settings = json.load(f)
        except:
            self.json_settings = {
                "save_dir": "./",
                "coding_method": 0,  # 0 - diagonal, 1 - From first to last, 2 - "Random", 3 - "Spiral from center"
                "save_custom_name": 1, # 0 - global, 1 - Ask every time, 2 - Same as selected image
                "save_prefix": ""
            }
            with open(self.settings_path, "w") as f:
                json.dump(self.json_settings, f)


        self.setFixedSize(700, 500)

        self.save_dir_label = QLabel("Saving Directory:") #Select where encoded image will be saved | empty = program folder
        self.coding_method_label = QLabel("Encoding/decoding Method:") #Select what methods text will be encoded | diagonal pixels - from first to last - random(using pincode) - from center loop
        self.save_custom_name_label = QLabel("Saving Name:") #Select if saving name | global (prefix_selected-image-name) - ask every time - same as selected image
        self.save_prefix_label = QLabel("Saving Prefix:") #User prefix for saving encoded image (only visable when global name is selected)

        self.save_dir_input = QLineEdit()
        self.save_dir_input.setReadOnly(True)
        self.save_dir_input.setText(self.json_settings["save_dir"])

        self.coding_method_select = QComboBox()
        self.coding_method_select.addItems(["Diagonal", "From first to last", "Random", "Spiral from center"])
        self.coding_method_select.setCurrentIndex(self.json_settings["coding_method"])

        self.save_custom_name_input = QComboBox()
        self.save_custom_name_input.addItems(["Global", "Ask every time", "Same as selected image"])
        self.save_custom_name_input.setCurrentIndex(self.json_settings["save_custom_name"])
        self.save_custom_name_input.activated.connect(self.display_prefix)


        self.save_prefix_input = QLineEdit()
        self.save_prefix_input.setText(self.json_settings["save_prefix"])

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
     self.json_settings["save_dir"] = self.save_dir_input.text()
     self.json_settings["coding_method"] = self.coding_method_select.currentIndex()
    self.json_settings["save_custom_name"] = self.save_custom_name_input.currentIndex()
     self.json_settings["save_prefix"] = self.save_prefix_input.text()
     
     try:
         with open(self.settings_path, "w") as f:
             json.dump(self.json_settings, f)
    except Exception as e:
        print(f"Error saving settings: {e}")

     self.close()


    def display_prefix(self):
        self.json_settings["save_custom_name"] = self.save_custom_name_input.currentIndex()
        if self.json_settings["save_custom_name"] != 0:
            self.save_prefix_label.hide()
            self.save_prefix_input.hide()
        else:
            self.save_prefix_label.show()
            self.save_prefix_input.show()
from pathlib import Path

 def select_saving_path(self):
     fd = QFileDialog()
    selected_path = fd.getExistingDirectory()
    if selected_path:
        path = str(Path(selected_path)) + os.sep
    else:
        path = self.json_settings["save_dir"]
        
     self.save_dir_input.setText(path)
     self.json_settings["save_dir"] = path




        

        