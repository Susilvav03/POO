from planeta import Planeta, TipoPlaneta

def main():
    p1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150000000, TipoPlaneta.TERRESTRE, True)
    p1.imprimir()
    print("Densidad del planeta =", p1.calcular_densidad())
    print("Es planeta exterior =", p1.es_planeta_exterior())
    print()

    p2 = Planeta("Jupiter", 79, 1.899e27, 1.4313e15, 139820, 750000000, TipoPlaneta.GASEOSO, True)
    p2.imprimir()
    print("Densidad del planeta =", p2.calcular_densidad())
    print("Es planeta exterior =", p2.es_planeta_exterior())

if __name__ == "__main__":
    main()
