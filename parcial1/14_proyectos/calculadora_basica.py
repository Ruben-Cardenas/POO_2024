# Calculadora

"""
print ("Menu de opciones") 
print ("1.-suma") 
print ("2.-resta") 
print ("3.-multiplicacion") 
print ("4.-divicion") 
print ("5.-SALIR") 

opciones =  input ("\t Elige una opcion: ").upper()

if opciones == "1" or opciones == "+" or opciones == "SUMA":  
 n1 = int (input ("Numero #1: "))
 n2 = int (input ("Numero #2: "))
 suma = n1 + n2 
 print (f"{n1} + {n2} = {suma} ")
elif opciones == "2" or opciones == "-" or opciones == "RESTA":
    n1 = int (input ("Numero #1: "))
    n2 = int (input ("Numero #2: "))
    suma = n1 - n2 
    print (f"{n1} - {n2} = {suma} ")  
elif opciones == "3" or opciones == "*" or opciones == "MULTIPLICACION":
    n1 = int (input ("Numero #1: "))
    n2 = int (input ("Numero #2: "))
    suma = n1 * n2 
    print (f"{n1} * {n2} = {suma} ")    
elif opciones == "4" or opciones == "/" or opciones == "DIVICION":
    n1 = int (input ("Numero #1: "))
    n2 = int (input ("Numero #2: "))
    suma = n1  / n2 
    print (f"{n1} / {n2} = {suma} ")
else opciones == "5" or opciones == "SALIR"
"""
"""
opcion=True
while opcion:
    
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()


    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}+{n2}={n1+n2}")
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}-{n2}={n1-n2}")
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}*{n2}={n1*n2}")
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}*{n2}={n1/n2}")
    else:
        opcion=False
        print("Gracias por utilizar el sistema ...")
        
"""
"""
def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}*{n2}={n1/n2}"
    else:
        opcion=False
        return "Gracias por utilizar el sistema ..."

"""
        
"""
def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":

        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}/{n2}={n1/n2}"



opcion=True 
while opcion:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    if opcion != "5" :  
     solicitarNumeros()
     print(calculadora(n1,n2,opcion))
    else:
     opcion = False
     print  ("Gracias por utilizar el sistema ...")

"""
from Funciones_a_llamar import esperetecla
esperetecla()

import os
import math 

def solicitarNumeros():
    global n1, n2
    n1 = int(input("Número #1: "))
    n2 = int(input("Número #2: "))

def calculadora(n1, n2, opcion):
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "**" or opcion == "POTENCIA":
        return f"{n1} ** {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ": 
        return f"Raíz cuadrada de {n1} = {math.sqrt(n1)} "  

opcion = True
while opcion:
    os.system('cls')
    print("\n\t..::: CALCULADORA BÁSICA :::...\n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n5.- Potencia\n6.- Raíz cuadrada\n7.- SALIR")  # Agrega una opción para la raíz cuadrada en el menú
    opcion = input("\tElige una opción: ").upper()
    if opcion != "7":
        solicitarNumeros()
        print(calculadora(n1, n2, opcion))
        esperetecla()
    else:
        opcion = False
        print("Gracias por utilizar el sistema...")




























