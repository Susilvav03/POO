from inmueble_vivienda import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, piso):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.piso = piso

    def imprimir(self):
        super().imprimir()
        print(f"Piso: {self.piso}")
