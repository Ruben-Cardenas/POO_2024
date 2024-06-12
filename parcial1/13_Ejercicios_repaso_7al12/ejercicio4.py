# 4.- Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
# y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

mi_lista = [1, 2, 3, 4, 5]
mi_cadena = "Hola Mundo"
mi_entero = 10
mi_logico = True



def imprimir_tipo(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena de texto.")
    elif isinstance(variable, int):
        print("La variable es un número entero.")
    elif isinstance(variable, bool):
        print("La variable es un valor lógico.")
    else:
        print("El tipo de la variable es desconocido.")

imprimir_tipo(mi_lista)
imprimir_tipo(mi_cadena)
imprimir_tipo(mi_entero)
imprimir_tipo(mi_logico)

















