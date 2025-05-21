from apartamento import Apartamento

class ApartamentoFamiliar(Apartamento):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, piso, valor_administracion):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, piso)
        self.valor_area = 2000000
        self.valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: {self.valor_administracion}, Valor por m²: {self.valor_area}")
