from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

#from PyQt6 import uic 
class MainWindow():
    def __init__(self):
        self.main = uic. loadUi("gui/main.ui")
        #self.initGUI()
        self.main.showMaximized()