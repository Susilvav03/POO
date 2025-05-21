from Cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa: float):
        super().__init__(saldo, tasa)
        self.sobregiro = 0.0

    def retirar(self, cantidad: float):
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self.sobregiro > 0:
            residuo = self.sobregiro - cantidad
            if residuo > 0:
                self.sobregiro = residuo
            else:
                self.saldo = -residuo
                self.sobregiro = 0
        else:
            super().consignar(cantidad)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        print(f"Saldo = ${self.saldo:.2f}")
        print(f"Cargo mensual = ${self.comision_mensual:.2f}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
        print(f"Valor de sobregiro = ${self.sobregiro:.2f}\n")
