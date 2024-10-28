import sqlite3

class ConexionDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def cerrar_conexion(self, conn):
        conn.close()
