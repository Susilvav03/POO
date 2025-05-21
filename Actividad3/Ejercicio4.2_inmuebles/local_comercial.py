from local import Local

class LocalComercial(Local):
    def __init__(self, identificador_inmobiliario, area, direccion, tipo, centro_comercial):
        super().__init__(identificador_inmobiliario, area, direccion, tipo)
        self.centro_comercial = centro_comercial
        self.valor_area = 3000000

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self.centro_comercial}, Valor por m²: {self.valor_area}")
