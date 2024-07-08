from clases_restaurante import *
print("\n")
# Desayuno 1
desayuno1 = Desayuno("Desayuno Americano", 30, ["Huevos", "Tocino", "Pan"], "Frutas frescas", "Aperitivo")
desayuno1.mostrar_informacion()
costo = desayuno1.calcular_costo()
print(f"Costo: ${costo}")
print("\n")
# Desayuno 2
desayuno2 = Desayuno("Tostada Francesa", 25, ["Pan", "Huevos", "Leche", "Canela", "Jarabe de arce"], "Fruta del bosque", "Ligero")
desayuno2.mostrar_informacion()
costo = desayuno2.calcular_costo()
print(f"Costo: ${costo}")
print("\n")
# Desayuno 3
desayuno3 = Desayuno("Huevos Benedict", 35, ["Huevos", "Pan tostado", "Jamón canadiense", "Salsa holandesa"], "Uvas", "Completo")
desayuno3.mostrar_informacion()
costo = desayuno3.calcular_costo()
print(f"Costo: ${costo}")
print("\n")
# Comida 1
comida1 = Comida("Enchiladas", 40, ["Tortillas", "Pollo", "Salsa roja", "Queso", "Crema"], "Mexicana", True, ["Arroz", "Frijoles"])
comida1.mostrar_informacion()
total = comida1.calcular_total()
print(f"Total: ${total}")
print("\n")
# Comida 2
comida2 = Comida("Lasagna", 35, ["Pasta", "Carne molida", "Salsa de tomate", "Queso ricotta", "Queso mozzarella"], "Italiana", False, ["Ensalada verde", "Pan de ajo"])
comida2.mostrar_informacion()
total = comida2.calcular_total()
print(f"Total: ${total}")
print("\n")
# Comida 3
comida3 = Comida("Sushi", 50, ["Arroz", "Algas", "Pescado", "Verduras"], "Japonesa", True, ["Sopa miso", "Ensalada de pepino"])
comida3.mostrar_informacion()
total = comida3.calcular_total()
print(f"Total: ${total}")
print("\n")
# Cena 1
cena1 = Cena("Pasta Alfredo", 38, ["Pasta", "Crema", "Queso parmesano", "Pimienta negra"], "Italiana", False, "Ensalada Caprese")
cena1.mostrar_informacion()
total = cena1.calcular_total()
print(f"Total: ${total}")
print("\n")
# Cena 2
cena2 = Cena("Bistec a la plancha", 55, ["Carne de res", "Aceite de oliva", "Sal", "Pimienta"], "Americana", True, "Papas al horno")
cena2.mostrar_informacion()
total = cena2.calcular_total()
print(f"Total: ${total}")
print("\n")
# Cena 3
cena3 = Cena("Pollo al curry", 42, ["Pollo", "Leche de coco", "Curry", "Arroz"], "India", False, "Naan")
cena3.mostrar_informacion()
total = cena3.calcular_total()
print(f"Total: ${total}")








