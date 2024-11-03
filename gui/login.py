from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

from data.user import UsuarioDate
from gui.main import MainWindow
from model.usuario import Usuario

#from PyQt6 import uic 
class Login():
    def __init__(self):
        self.login = uic. loadUi("gui/login.ui")
        self.initGUI()
        self.login.Mensaje.setText("")
        self.login.show()

    def ingresar (self):
        if len(self.login.Usuario.text() ) < 2:
             self.login.Mensaje.setText("Ingrese Nombre valido")
             self.login.Usuario.setFocus()
        elif len(self.login.Clave.text() ) < 3:
            self.login.Mensaje.setText("Ingrese una contraseña valida")
            self.login.Clave.setFocus()
        else:
            self.login.Mensaje.setText("")
            usu=Usuario(usuario=self.login.Usuario.text(), clave=self.login.Clave.text())
            usuDate=UsuarioDate()
            res=usuDate.login(usu)
            if res:
                 self.main= MainWindow()
                 self.login.hide()
            else:
                 self.login.Mensaje.setText("Datos de acceso incorrecto")


    def initGUI(self):
        self.login.Acceder.clicked.connect(self.ingresar)