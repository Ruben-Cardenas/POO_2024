# Resivo 


precio_basico = 0.987
precio_intermedio = 1.203

consumo_kwh = float(input("Ingresa la cantidad de kWh consumidos: "))

if consumo_kwh <= 150:
    costo_sin_iva_dap = consumo_kwh * precio_basico
else:
    costo_sin_iva_dap = 150 * precio_basico + (consumo_kwh - 150) * precio_intermedio

Iva =costo_sin_iva_dap * 0.16

dap = 12.56


total_a_pagar = costo_sin_iva_dap + Iva + dap


print(f"Total a pagar por el recibo de la luz: ${total_a_pagar:.2f}")



