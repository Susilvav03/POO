from inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self.num_habitaciones}, Baños: {self.num_banos}")
