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
             self.login.labelMensaje.setText("Ingrese un mesaje valido")
             self.login.txtUsuario.setFocus()
        elif len(self.login.txtClave.text() ) < 3:
            self.login.labelMensaje.setText("Ingrese una contraseña valida")
            self.login.txtClave.setFocus()
        else:
            self.login.labelMensaje.setText("")
            pass 

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)