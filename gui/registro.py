from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox


#from PyQt6 import uic 
class RegistroWindow():
    def __init__(self):
        self.v = uic.loadUi("gui/registro.ui")
        self.initGUI()
        self.v.show()

    
