from PyQt6.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

class askWin(QDialog):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 100)

        self.name_input_text = None

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit("")

        self.save_button = QPushButton("Ok")
        self.save_button.clicked.connect(self._save_name)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.name_label)
        self.horizontal_layout.addWidget(self.name_input)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.horizontal_layout)
        self.main_layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.main_layout)

    def _save_name(self):
        self.name_input_text = self.name_input.text()
        self.close()