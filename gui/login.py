from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox
#from PyQt6 import uic 
class Login():
    def __init__(self):
        self.login = uic. loadUi("gui/login.ui")
        self.login.show()