# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario


numero_inicial = int(input("Ingresa el primer número: "))
numero_final = int(input("Ingresa el segundo número: "))


if numero_inicial > numero_final:
    print("El primer número debe ser menor o igual al segundo número.")
else:
    for numero in range(numero_inicial, numero_final + 1):
        if numero % 2 != 0:
            print(numero)
