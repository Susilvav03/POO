from inmueble import Inmueble

class Local(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, tipo):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.tipo = tipo

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipo}")
