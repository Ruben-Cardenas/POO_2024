# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for


for num in range(1, 61):
    cuadrado = num ** 2
    print(f"El cuadrado de {num} es {cuadrado}")

