import unittest
from services.inversion_service import InversionService

class TestInversionService(unittest.TestCase):
    def setUp(self):
        self.inversion_service = InversionService()

    def test_realizar_inversion(self):
        self.inversion_service.realizar_inversion(1000)
        # Aquí deberías agregar una verificación para asegurarte que la inversión se haya registrado

if __name__ == "__main__":
    unittest.main()
