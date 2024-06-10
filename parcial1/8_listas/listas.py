#list (array)
#son colleciones o conjuntos de datos/valores bajo
#un mismo nombre para acceder a los valores se 
#hace con un indice numerico 


#Nota: sus valores si son modificables
#la lista es una coleccion ordenada y modificable permite miembros duplicados 


#ejemplo 1 crea una lsita con valores numericos enteros e imprimir la lista 

#numero = 23
#numero = 34 

"""

numero1 = [23,34]
print(numero1)

#Recorrer la lista con un for 

for i in numero1 :
    print (i)

#Recorrer la lista con un while

i = 0

while i<len (numero1):
    print (numero1[i]) 
    i+=1

"""

#ejemplo 2 crear una lista de palabras posteriormente ingresar una palabra para buscar la coincidencia en la lista e indicar 
#si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

"""
#palabra_buscar = input ("ingresar la palabra a buscar: ")
palabra = [ "hola", "2024" , "10.23","True"]
palabra_buscar = input ("ingresar la palabra a buscar: ")
#Recorrer la lista con un for 
"""
#Recorrer la lista con un 



# palabra = [ "hola", "2024" , "10.23","True"]
# palabra_buscar = input ("ingresar la palabra a buscar: ")


# noloencontro = True

# for o in palabra : 
#     if  palabra_buscar == o:
     
#      print (f"Encontre la palabra {palabra_buscar}, en la posicion : {palabra.index (o)}")
#      noloencontro = False 


# if noloencontro:
#  print(f"no se encontro la palabra dentro de la lista ")



# print ("\n") 

# print ("esto es con el while")

# print ("\n") 

# #Recorrer la lista con un while

# palabra = [ "hola", "2024" , "10.23","True"]
# palabra_buscar = input ("ingresar la palabra a buscar: ")

# while  o <len (palabra):
#     if palabra == palabra_buscar [o]:
#      print (f"Encontre la palabra {palabra_buscar}, en la posicion : {palabra.index (o)}")
#      noloencontro = False 
#     o+=1
        
        
# if noloencontro:
#  print(f"no se encontro la palabra dentro de la lista ")
    


#Ejemplo 3  lsitas multilineal o multidimensional (matriz) para crear una agenda

# nombres = [
#     ["Carlos" , 6181234567],
#     ["Fernando", 6182334567],
#     ["Matiaas", 6691112233],
#     ["Juan", 6182332345]
# ]
# print (nombres)

# for o in nombres:
#     print (f"{nombres.index(o)+1}.-{o}")


# ejemplo 4 crear un programa que permita gestionar (administrar) peliculas, color un menu de opciones para agregar
# , remover, consultar peliculas 

# Nota 
#1.-Utilizar funciones y mandaer lla mar desde otro archivo 
#2.- utilizar listas para almacenar los nombres de peliculas



def esperetecla():
    print("Oprima cualquier tecla para continuar")
    input()

def insertarpeliculas(peliculas):
    pelicula = input("Ingrese el nombre de la película: ")
    peliculas.append(pelicula)
    esperetecla()

def Eliminarpeliculas(peliculas):
    pelicula = input("Eliminar la película: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print("Película eliminada correctamente.")
    else:
        print("La película no existe en la lista.")
    esperetecla()

def Removerpeliculas(peliculas):
    pelicula = input("Pelicula que desea remover: ")
    if pelicula in peliculas:
        peliculas.pop(pelicula)
        print("Película removida correctamente.")
    else:
        print("La película no existe en la lista.")
    esperetecla()

def Consultarpeliculas(peliculas):
    print("Lista de películas:")
    for pelicula in peliculas:
        print(pelicula)
    esperetecla()

def Actualizarpeliculas():
    pelicula_actual = input("Ingrese el nombre de la película a actualizar: ")
    if pelicula_actual in peliculas:
        indice = peliculas.index(pelicula_actual)
        nueva_pelicula = input("Ingrese el nuevo nombre de la película: ")
        peliculas[indice] = nueva_pelicula
        print("Película actualizada correctamente.")
    else:
        print("La película no existe en la lista.")
    esperetecla()

peliculas = []

while True:
    
    print("\n\t..::: CINEMEX :::...\n1.- Agregar\n2.- Remover\n3.- Consultar\n4.- Eliminar\n5.- Actualizar\n6.- SALIR")
    opcion = input("\tElige una opción: ").upper()
    
    if opcion == "1" or opcion == "AGREGAR":
        insertarpeliculas(peliculas)
    elif opcion == "2" or opcion == "REMOVER":
        Removerpeliculas(peliculas)
    elif opcion == "3" or opcion == "CONSULTAR":
        Consultarpeliculas(peliculas)
    elif opcion == "4" or opcion == "ELIMINAR":
        Eliminarpeliculas(peliculas)
    elif opcion == "5" or opcion == "ACTUALIZAR":
        Actualizarpeliculas(peliculas)
    elif opcion == "6" or opcion == "SALIR":
        print("Salió del sistema del Cinema")
        break


    

 


