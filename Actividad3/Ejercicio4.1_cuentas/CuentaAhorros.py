from Cuenta import Cuenta

class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa: float):
        super().__init__(saldo, tasa)
        self.activa = saldo >= 10000

    def retirar(self, cantidad: float):
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self.activa:
            super().consignar(cantidad)

    def extracto_mensual(self):
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        if self.saldo < 10000:
            self.activa = False

    def imprimir(self):
        print(f"Saldo = ${self.saldo:.2f}")
        print(f"Comisión mensual = ${self.comision_mensual:.2f}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}\n")
