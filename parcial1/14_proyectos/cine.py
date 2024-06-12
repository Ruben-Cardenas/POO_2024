
from Funciones_a_llamar import esperetecla
esperetecla()

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
        peliculas.remove(pelicula)
        print("Película removida correctamente.")
    else:
        print("La película no existe en la lista.")
esperetecla()
    
def Consultarpeliculas(peliculas):
    print("Lista de películas:")
    for pelicula in peliculas:
        print(pelicula)
    esperetecla()
    
def Actualizarpeliculas(peliculas):
    pelicula_actual = input("Ingrese el nombre de la película a actualizar: ")
    if pelicula_actual in peliculas:
        indice = peliculas.index(pelicula_actual)
        nueva_pelicula = input("Ingrese el nuevo nombre de la película: ")
        peliculas[indice] = nueva_pelicula
        print("Película actualizada correctamente.")
    else:
        print("La película no existe en la lista.")
esperetecla()

def Buscarpeliculas(peliculas):
    pelicula = input("Ingrese el nombre de la película a buscar: ")
    if pelicula in peliculas:
        print("La película está en la lista.")
    else:
        print("La película no existe en la lista.")
esperetecla()

def Vaciarpeliculas(peliculas):
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")
esperetecla()

peliculas = []

while True:
    
    print("\n\t..::: CINEMEX :::...\n1.- Agregar\n2.- Remover\n3.- Consultar\n4.- Eliminar\n5.- Actualizar\n6.- Buscar\n7.- Vaciar\n8.- SALIR")
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
    elif opcion == "6" or opcion == "BUSCAR":
        Buscarpeliculas(peliculas)
    elif opcion == "7" or opcion == "VACIAR":
        Vaciarpeliculas(peliculas)
    elif opcion == "8" or opcion == "SALIR":
        print("Salió del sistema del Cinema")
        break


















