import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_window import AboutWindow
import qdarkstyle

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # loads main_ui
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.load_settings()

        # buttons
        self.action_darkmode.toggled.connect(self.dark_mode)
        
        # menubar
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

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

    def closeEvent(self, event):
        print("save settings")
        self.settings.setValue('window_size', self.size())
        self.settings.setValue('window_pos', self.pos())
        self.settings.setValue('dark_mode', self.action_darkmode.isChecked())
        event.accept()
#
    def load_settings(self):
        print("load settings")
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode', 'false')
        if size is not None:
            self.resize(size)
        if pos is not None:
            self.move(pos)
        if dark == 'true':
            print("the setting is true")
            self.action_darkmode.setChecked(True)
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
