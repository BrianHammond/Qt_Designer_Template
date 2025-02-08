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

        # buttons
        self.action_darkmode.toggled.connect(self.dark_mode)
        
        # menubar
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

        self.load_settings()

    def dark_mode(self, checked):
        if checked:
            print(checked)
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def about_qt(self):
        QApplication.aboutQt()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def closeEvent(self, event):
        # Save window settings with QSettings to an INI file
        settings = QSettings('settings.ini', QSettings.IniFormat)
        settings.setValue('window_size', self.size())
        settings.setValue('window_pos', self.pos())
        settings.setValue('dark_mode', self.action_darkmode.isChecked())
        event.accept()

    def load_settings(self):
        # Load window settings with QSettings from an INI file
        settings = QSettings('settings.ini', QSettings.IniFormat)
        size = settings.value('window_size', None)
        pos = settings.value('window_pos', None)
        dark = settings.value('dark_mode')
        if size is not None:
            self.resize(size)
        if pos is not None:
            self.move(pos)
        if dark == 'true':
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
