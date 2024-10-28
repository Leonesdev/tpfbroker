from dao.conexion_bd import ConexionDB

class UsuarioDAO:
    def __init__(self):
        self.conexion_db = ConexionDB('inversiones.db')

    def agregar_usuario(self, nombre, email):
        conn = self.conexion_db.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        self.conexion_db.cerrar_conexion(conn)

    def obtener_usuario(self, email):
        conn = self.conexion_db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()
        self.conexion_db.cerrar_conexion(conn)
        return usuario
