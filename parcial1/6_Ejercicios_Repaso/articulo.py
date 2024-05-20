


# Solicitar nombre y precio del producto al usuario
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))

# Calcular el valor del IVA correspondiente al 16%
iva = precio_producto * 0.16

# Calcular el costo total del producto sumando el precio y el IVA
total_a_pagar = precio_producto + iva 

# Imprimir el resultado
print(f"El precio a pagar por {nombre_producto} con IVA es: ${total_a_pagar:.2f}")

  