import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow as main_ui
from about_window import AboutWindow
import qdarkstyle

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # loads main_ui

        # buttons
        self.rb_darkmode.toggled.connect(self.dark_mode)
        
        # menubar
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def about_qt(self):
        QApplication.aboutQt()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
