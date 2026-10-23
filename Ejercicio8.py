nombre =input("¿Cual es tu nombre? ")
print("Hola", nombre)

edad = int(input("¿Cual es tu edad? "))
print("Tu edad es", edad)

ciudad = input("¿Cual es tu ciudad? ")
print("Tu ciudad es", ciudad)

calificacion1  = float(input("Ingresa tu calificacion: "))
calificacion2 = float(input("Ingresa tu calificacion: "))
calificacion3 = float(input("Ingresa tu calificacion: "))

promedio= (calificacion1 + calificacion2 + calificacion3) / 3


if promedio >= 71:
    print("Aprobaste")

else:
    print("Reprobaste")
