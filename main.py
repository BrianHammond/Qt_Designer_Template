import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_MainWindow as about_ui

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #define our widgets
        self.text_field.returnPressed.connect(self.display_text) 
        self.push_button.clicked.connect(self.display_text)

        #menubar
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

    def display_text(self):
        print(self.text_field.text())
        self.label.setText(self.text_field.text())
        self.text_field.clear()
        
    def about_qt(self):
        QApplication.aboutQt()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

class AboutWindow(QMainWindow, about_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
