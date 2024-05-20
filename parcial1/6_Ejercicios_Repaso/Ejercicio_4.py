#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

num = float (input ("Escribir el numero que desee: "))
num_2 = float (input ("Escriba nuevamente otro numero: "))
#(+)
num_suma= num + num_2
#(-)
num_restra = num - num_2
#(*)
num_multi = num * num_2
#(/)
num_divi = num / num_2 

print ("\n")
print (f"el la suma de los dos numero es: {num_suma}") 
print ("\n")
print (f"el la resta de los dos numero es: {num_restra}")
print ("\n")
print (f"el la multipliacion de los dos numero es: {num_multi}")
print ("\n")
print (f"el la divicion de los dos numero es: {num_divi}")
