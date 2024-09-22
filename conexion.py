import sqlite3
class Conexion():
    def __init__(self):
        try:
            self.con=sqlite3.connect("banco.db")
            self.crearTabalas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sqlite3
