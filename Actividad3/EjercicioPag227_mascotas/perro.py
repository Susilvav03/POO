from mascota import Mascota

class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, es_muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.es_muerde = es_muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")
