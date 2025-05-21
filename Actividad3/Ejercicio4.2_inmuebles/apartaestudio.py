from apartamento import Apartamento

class Apartaestudio(Apartamento):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, piso):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, piso)
        self.valor_area = 1500000

    def imprimir(self):
        super().imprimir()
        print(f"Valor por m²: {self.valor_area}")
