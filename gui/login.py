from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

#from PyQt6 import uic 
class Login():
    def __init__(self):
        self.login = uic. loadUi("gui/login.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()

    def ingresar (self):
        if len(self.login.txtUsuario.text() ) < 2:
             self.login.lblMensaje.setText("Ingrese un mesaje valido")
        elif len(self.login.txtClave.text() ) < 3:
            self.login.lblMensaje.setText("Ingrese una contraseña valida")
        else:
            pass 

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)