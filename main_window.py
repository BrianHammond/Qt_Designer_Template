from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) #load the UI file

        #define our widgets
        self.text_field.returnPressed.connect(self.display_text) 
        self.push_button.clicked.connect(self.display_text)

        #menubar
        self.actionAbout.triggered.connect(self.about)

    def display_text(self):
        print(self.text_field.text())
        self.label.setText(self.text_field.text())
        self.text_field.clear()

    def about(self):
        self.window = QWidget()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

