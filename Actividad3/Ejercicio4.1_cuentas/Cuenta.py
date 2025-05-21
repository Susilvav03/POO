class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0.0

    def consignar(self, cantidad: float):
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad: float):
        nuevo_saldo = self.saldo - cantidad
        if nuevo_saldo >= 0:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        self.calcular_interes()
