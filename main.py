import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui
import qdarkstyle

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # loads main_ui
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.loadSettings()

        # menubar
        self.actionDarkMode.toggled.connect(self.dark_mode)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAboutQt.triggered.connect(self.about_qt)

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

    def closeEvent(self, event): #settings will save when closing the app
        self.settings.setValue('window_size', self.size())
        self.settings.setValue('window_pos', self.pos())
        self.settings.setValue('dark_mode', self.actionDarkMode.isChecked())
        event.accept()

    def loadSettings(self): #settings will load when opening the app
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        if size is not None:
            self.resize(size)
        if pos is not None:
            self.move(pos)
        if dark == 'true':
            self.actionDarkMode.setChecked(True)
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

class AboutWindow(QWidget, about_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
