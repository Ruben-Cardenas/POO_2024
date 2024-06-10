#una funcion es un conjunti de instruccines agrupadas nbajo un nombre en particular como un programa mas pequeño
#que cumpla una funcion especifica la funcion se puede reutilizar con simple hecho es decir mandarla llamar 

#sintasis

"""
def  nombredemifuncion(parametros)
 bloque o conjunto de instrucciones

nombremifuncion (parametros)

las funciones que pueden ser 4 tipos

1.-funciones que no reciben parametros y no regresa valor 

2.-Funciones que no recibe parametros y regresa valor 

3.-Funciones que recibe parametros y no regresa valor 

4.- Funciones que recibe parametros regresa valor 

"""

# 1.-Funciones que no recibe parametros y no regresa valor

"""
def sumaNumeros ():
    n1 = int (input ("Numero #1: "))
    n2 = int (input ("Numero #2: "))
    suma = n1 + n2 
    print (f"{n1} + {n2} = {suma} ")

sumaNumeros ()
"""
"""

# 2.-Funciones que no recibe parametros y no regresa valor

def sumaNumeros2 ():
    n1 = int (input ("Numero #1: "))
    n2 = int (input ("Numero #2: "))
    suma = n1 + n2 
    return f"{n1} + {n2} = {suma} "

print(sumaNumeros2())

#cadena = sumaNumeros2 ()

#print (cadena)

"""
"""

# 3.-Funciones que recibe parametros y no regresa valor

def sumaNumeros3 (n1,n2):
    suma = n1 + n2 
    print (f"{n1} + {n2} = {suma} ")


n1 = int (input ("Numero #1: "))
n2 = int (input ("Numero #2: "))

sumaNumeros3(n1,n2)
 

"""

# 4.- Funciones que recibe parametros regresa valor 

def sumaNumeros3 (n1,n2):
    suma = n1 + n2 
    return f"{n1} + {n2} = {suma} "


n1 = int (input ("Numero #1: "))
n2 = int (input ("Numero #2: "))

print (sumaNumeros3(n1,n2))


# Crea un programa que solicite a traves de una funcion la siguiente informacion 
# nombre del paciente, edad, estatura, tipo de sangre, utilizando los 
# 4 tipos de funciones 















