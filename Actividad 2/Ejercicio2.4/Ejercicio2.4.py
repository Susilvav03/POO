duracion = int(input("Ingrese la duración de la llamada en minutos: "))

total = 200  # Costo inicial

if duracion > 3:
    minutos_adicionales = duracion - 3
    total += minutos_adicionales * 100

print("El total a pagar por la llamada es: $", total)