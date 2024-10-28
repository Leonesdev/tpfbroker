from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def registrar_usuario(self, nombre, email):
        self.usuario_dao.agregar_usuario(nombre, email)
        print(f"Usuario {nombre} registrado exitosamente.")

    def iniciar_sesion(self, email):
        usuario = self.usuario_dao.obtener_usuario(email)
        if usuario:
            print(f"Bienvenido {usuario[1]}!")
        else:
            print("Usuario no encontrado.")
