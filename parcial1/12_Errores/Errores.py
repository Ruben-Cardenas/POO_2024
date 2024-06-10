# Manejo de errores es la forma en la que tienen los lenguajes de programacion
# para evitar que sucedan erroes en tiempo de ejecucion 

#Ejemplo 1 Error cuando una variable no se genra 

# try:
#  nombre = input("Dame el nombre: ")

#  if len (nombre)>1:
#     nombre_usuario = "El nombre es: "+ nombre

    
#  print (nombre_usuario)
# except:
#     print ("Es necesario introducir un nombe de un usuario")

# Ejwmplo cuando se solicita un numero y se introduce una letra 


"""
try:
     numero = int (input ("Dame un numero: "))
     if numero>0:
         print ("soy un numero entero positivo")
     else: 
         print ("Soy un numero entero negativo")
except:
     print ("no se puede convertir un caracter no numerico a numero")
else: 
    print ("Todo se ejecuto correctamente")
"""


#Ejemplo 3 cuando se generan meltuples excepciones

try:
 numero = int (input("Dame un numero: "))
 print ("el cuadrado es: " + str(numero*numero))
except ValueError:
    print("No se puede convertir un caracter que no sea numerico")
except TypeError: 
    print("No es ´posible convertir el numero a entero")
else:
    print ("Finalizo correctamente")
finally:
    print ("Listo se finalizo")
 








 















































