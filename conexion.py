import sqlite3
class Conexion():
    def __init__(self):
        try:
            self.con=sqlite3.connect("banco.db")
            self.crearTabalas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sql_tabla1= """CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, usuario TEX UNIQUE, clave TEXT)"""
        cur=self.con.cursor()
        cur.execute(sql_tabla1)
con=Conexion()