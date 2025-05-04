a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

if a > b and a > c:
    print("El mayor número es:", a)
elif b > c:
    print("El mayor número es:", b)
else:
    print("El mayor número es:", c)
