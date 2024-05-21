# Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
no_aprobados = 0


for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    if calificacion >= 5.9:
        aprobados += 1
    else:
        no_aprobados += 1


print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos no aprobados: {no_aprobados}")
