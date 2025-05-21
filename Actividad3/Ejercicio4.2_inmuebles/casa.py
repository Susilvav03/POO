from inmueble_vivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.num_pisos = num_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos: {self.num_pisos}")
