# Ciclo For estructura iterativa que se ejecuta x veses 

# Sintaxis
# For variable in elemento _interable   (lista,rango,etc):
#bloque de instrucciones

# Ejemplo 1 : Crear un programa que programa que imprima en pantalla 5 veses el @


contador=1

for contador in range (1,5):
    print("@")
    

#Ejemplo 2: Crear un programa que imprima los numeros del 1 aal 5 
# y los sume y al final imprima la suma 


contador = 1
suma = 0
for contador in range (1,6):
    print(contador)
    suma+=contador

print (f"la suma es: {suma}")




#Ejemplo 3: Crear un programa que imprima la tabla de multiplicar que el usuario desee 

tabla = int (input("Ingresa un numero para calcular la tabla de multiplicar"))

i = 1
multi= 0

for i in range (1,11):
 multi= i*tabla 
 print (f"{tabla} x {i} = {multi}")


