from casa import Casa

class CasaRural(Casa):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos, distancia_cabecera, altitud):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud
        self.valor_area = 1500000

    def imprimir(self):
        super().imprimir()
        print(f"Distancia: {self.distancia_cabecera} km, Altitud: {self.altitud} m, Valor por m²: {self.valor_area}")
