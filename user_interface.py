from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic

class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) #load the UI file

        #define our widgets
        self.text_field.returnPressed.connect(self.display_text) 
        self.push_button.clicked.connect(self.display_text)

        #menubar
        self.actionAbout.triggered.connect(self.about)

        #fields
        self.text = self.text_field
      
    def display_text(self):
        print(self.text.text())
        self.label.setText(self.text.text())
        self.text.clear()

    def about(self):
        self.window = QWidget()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

