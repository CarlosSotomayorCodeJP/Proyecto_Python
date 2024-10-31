import sqlite3
class Conexion():
    def __init__(self):
        try:
            self.con=sqlite3.connect("banco.db")
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sql_tabla1= """CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, usuario TEX UNIQUE, clave TEXT)"""
        cur=self.con.cursor()
        cur.execute(sql_tabla1)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:
            sql_insert= """INSERT INTO usuarios values(null, '{}', '{}', '{}')""".format("Administrador", "admin", "admin2050.")
            cur=self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit()
        except Exception as ex:
            print("Usuario existente",ex) 
    def conectar(self):
        return self.con.commit()
       