from CuentaAhorros import CuentaAhorros

if __name__ == "__main__":
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial = $"))
    tasa = float(input("Ingrese tasa de interés = "))
    cuenta = CuentaAhorros(saldo_inicial, tasa)

    cantidad_consignar = float(input("Ingresar cantidad a consignar: $"))
    cuenta.consignar(cantidad_consignar)

    cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
    cuenta.retirar(cantidad_retirar)

    cuenta.extracto_mensual()
    cuenta.imprimir()