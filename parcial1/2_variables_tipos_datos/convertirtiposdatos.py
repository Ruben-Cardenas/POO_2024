

"""
comvertir de varias lineas 
notas: a la hora concatenar cadenas no es posible incluir en algunas ocaciones contenido que no sea del str
"""

# concatenar un str con str 

#texto = "soy una cadena de texto"

# numero =23

# print (texto +  "y soy otra cadena")


# concatenar un str con str 

# texto = "soy una cadena de texto"

# numero =23

# numero_str = str(numero)

# print ("El numero : " + numero_str )

# print ("El numero: "+ str (numero))

# concatenar un str con int

n1 = '23'
n2 = 33 

suma = int(n1)+n2 # int es entero 

print ("El numero es: " + str(suma))

# concatenar un float con int con str

n1 = '23'
n2 = 33.0 # es un float o un real 

suma = int (n1)+n2

print ("El numero es: " + str(int(suma)))

print(F"El numero : {suma}")

# concatenar un float y float con float

n1 = '23.34'
n2 = '33.99' # es un float o un real 

suma = float(n1)+float (n2)

print(F"El numero : {suma}")