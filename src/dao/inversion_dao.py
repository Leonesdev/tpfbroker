from dao.conexion_bd import ConexionDB

class InversionDAO:
    def __init__(self):
        self.conexion_db = ConexionDB('inversiones.db')

    def agregar_inversion(self, usuario_id, monto):
        conn = self.conexion_db.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inversiones (usuario_id, monto) VALUES (?, ?)", (usuario_id, monto))
        conn.commit()
        self.conexion_db.cerrar_conexion(conn)

    def obtener_inversiones(self, usuario_id):
        conn = self.conexion_db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inversiones WHERE usuario_id = ?", (usuario_id,))
        inversiones = cursor.fetchall()
        self.conexion_db.cerrar_conexion(conn)
        return inversiones
