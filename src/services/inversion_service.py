from dao.inversion_dao import InversionDAO

class InversionService:
    def __init__(self):
        self.inversion_dao = InversionDAO()

    def realizar_inversion(self, monto):
        # Aquí deberías obtener el ID del usuario desde algún contexto (ej., sesión)
        usuario_id = 1  # Este es un ejemplo, debes obtenerlo dinámicamente
        self.inversion_dao.agregar_inversion(usuario_id, monto)
        print(f"Inversión de {monto} registrada exitosamente.")
