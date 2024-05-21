# Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10


tabla = int (input("Ingresa un numero para calcular la tabla de multiplicar: "))

i = 1
multi= 0
print (f"Es la tabla del: {tabla}")

for i in range (1,11):
 multi= i*tabla 
 print (f"{tabla} x {i} = {multi}")