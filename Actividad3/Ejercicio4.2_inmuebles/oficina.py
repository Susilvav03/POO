from local import Local

class Oficina(Local):
    def __init__(self, identificador_inmobiliario, area, direccion, tipo, es_gobierno):
        super().__init__(identificador_inmobiliario, area, direccion, tipo)
        self.es_gobierno = es_gobierno
        self.valor_area = 3500000

    def imprimir(self):
        super().imprimir()
        print(f"Es del gobierno: {self.es_gobierno}, Valor por m²: {self.valor_area}")
