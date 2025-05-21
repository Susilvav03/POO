class Profesor:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def get_nombre(self):
        return self.nombre

    def get_salario(self):
        return self.salario

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_salario(self, salario):
        self.salario = salario

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
