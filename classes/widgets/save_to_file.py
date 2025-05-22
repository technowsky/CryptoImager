from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout

class file_dialog(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedWidth(500)

        self.label = QLabel("Select saving path")
        self.select_button = QPushButton("Select")
        self.saving_path = QLineEdit()

        self.select_button.clicked.connect(self.select_path)


        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.saving_path)
        self.layout.addWidget(self.select_button)

        self.v_layout.addLayout(self.layout)

        self.setLayout(self.v_layout)

        self.show()

    def select_path(self):
        fd = QFileDialog()
        self.saving_path.setText(fd.getExistingDirectory()+"/")
    