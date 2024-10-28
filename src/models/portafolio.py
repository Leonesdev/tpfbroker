class Portafolio:
    def __init__(self, id_portafolio, usuario_id):
        self.id_portafolio = id_portafolio
        self.usuario_id = usuario_id
        self.inversiones = []

    def agregar_inversion(self, inversion):
        self.inversiones.append(inversion)
