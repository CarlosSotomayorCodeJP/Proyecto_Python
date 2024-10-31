import conexion as con
class UsuarioDate():
    def __init__(self):
        self.db= con.Conexion().conectar()
        self.cursor=self.db.cursor()

    