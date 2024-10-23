import unittest
from services.usuario_service import UsuarioService

class TestUsuarioService(unittest.TestCase):
    def setUp(self):
        self.usuario_service = UsuarioService()

    def test_registrar_usuario(self):
        self.usuario_service.registrar_usuario("Juan", "juan@example.com")
        usuario = self.usuario_service.usuario_dao.obtener_usuario("juan@example.com")
        self.assertIsNotNone(usuario)

if __name__ == "__main__":
    unittest.main()
