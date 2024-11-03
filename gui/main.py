from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

from gui.registro import RegistroWindow

#from PyQt6 import uic 
class MainWindow():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    def iniGUI(self):
        self.main.btnRegistrarTransferencias.triggered.connect(lambda: RegistroWindow())