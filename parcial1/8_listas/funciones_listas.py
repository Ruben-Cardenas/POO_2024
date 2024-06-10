
paises=["Mexico","USA","Brasil","Chile"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

print (paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort() 
print(numeros)


# agregar elemento
print()
print(numeros)
numeros.insert(len(numeros),200)
print (numeros)


#Remover elementos 
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)



#Darle la vuelta a los elementos de una lista

print(varios)
varios.reverse()
print(varios)

#buscar un valor dentro de una lista

encontro = "Brasil" in paises 
print (encontro)

# vasiar una lista 

print (paises)
paises.clear()
print(paises)

# Unir listas 
print(varios)
varios.extend(numeros)
print(varios)
















