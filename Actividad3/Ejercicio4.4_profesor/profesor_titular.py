from profesor import Profesor

class ProfesorTitular(Profesor):
    def __init__(self, nombre, salario, categoria):
        super().__init__(nombre, salario)
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def imprimir(self):
        super().imprimir()
        print(f"Categoría: {self.categoria}")
