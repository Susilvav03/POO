from casa_urbana import CasaUrbana

class CasaIndependiente(CasaUrbana):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_area = 3000000

    def imprimir(self):
        super().imprimir()
        print(f"Valor por m²: {self.valor_area}")
