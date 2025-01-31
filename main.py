# checks to see if the 'PyQT6' module is installed
try: 
    from PyQt6.QtWidgets import QApplication, QMainWindow
    from PyQt6 import uic
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("PyQT6 module is not installed")
    import subprocess
    required_packages = ['PyQT6']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class UI(QMainWindow):
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
        self.window = QMainWindow()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

# Show/Run app
if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec())