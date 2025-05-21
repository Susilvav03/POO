from casa_urbana import CasaUrbana

class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos, valor_administracion, tiene_campo_deportivo, tiene_piscina):
        super().__init__(identificador_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_area = 2500000
        self.valor_administracion = valor_administracion
        self.tiene_campo_deportivo = tiene_campo_deportivo
        self.tiene_piscina = tiene_piscina

    def imprimir(self):
        super().imprimir()
        print(f"Administración: {self.valor_administracion}, Campo deportivo: {self.tiene_campo_deportivo}, Piscina: {self.tiene_piscina}, Valor por m²: {self.valor_area}")
