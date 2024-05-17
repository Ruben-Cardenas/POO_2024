# Ciclo While es una estructura iterativa que se ejecuta x veses siempre y cuando la condicion se cumpla y se seguira ejecutando tantas veses como sea  

# Sintaxis
# WHILE condicion:
#bloque de instrucciones

# Ejemplo 1 : Crear un programa que programa que imprima en pantalla 5 veses el @
contador= 1
 
while contador<=5:
  print ("@")
  contador += 1
 
    
#Ejemplo 2: Crear un programa que imprima los numeros del 1 aal 5 
# y los sume y al final imprima la suma 

contador = 1
suma = 0

while contador <= 5:
    print(contador)
    suma+=contador 
    contador+=1

print (f"la suma es: {suma}")


#Ejemplo 3: Crear un programa que imprima la tabla de multiplicar que el usuario desee 

tabla = int (input("Ingresa un numero para calcular la tabla de multiplicar: "))

i=1
multi= 0

while i<=10:
  multi= i*tabla 
  print (f"{tabla} x {i} = {multi}")
  i+=1

