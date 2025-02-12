import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui
import qdarkstyle

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # loads main_ui
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts

        # menubar
        self.actionDarkMode.toggled.connect(self.dark_mode)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAboutQt.triggered.connect(self.about_qt)

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self):  # loads the About window
        self.about_window = AboutWindow(dark_mode=self.actionDarkMode.isChecked())
        self.about_window.show()

    def closeEvent(self, event):  # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

    def about_qt(self):  # loads the About Qt window
        QApplication.aboutQt()

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.actionDarkMode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.actionDarkMode.isChecked())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv)  # needs to run first
    main_window = MainWindow()  # Instance of MainWindow
    main_window.show()
    sys.exit(app.exec())
