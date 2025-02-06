from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import uic
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) #load the UI file

        #define our widgets
        self.text_field.returnPressed.connect(self.display_text) 
        self.push_button.clicked.connect(self.display_text)

        #menubar
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

    def display_text(self):
        print(self.text_field.text())
        self.label.setText(self.text_field.text())
        self.text_field.clear()

    def about(self):
        self.window = QDialog()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

    def about_qt(self):
        QApplication.aboutQt()

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
