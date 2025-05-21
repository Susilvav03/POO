from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, direccion, departamento, categoria):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def get_departamento(self):
        return self.departamento

    def set_departamento(self, departamento):
        self.departamento = departamento

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria
