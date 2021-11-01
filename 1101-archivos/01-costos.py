def calcular_punto_equilibrio(cf, pv, cvu):
    return cf / (pv - cvu)

def calcular_utilidad(pv, uv, cf, cvu):
    return (pv * uv) - cf - (cvu * uv)

costo_fijo = eval(input("Escribe el costo fijo: "))
precio_venta = eval(input("Escribe el precio de venta: "))
costo_variable_unitario = eval(input("Escribe el costo variable unitario: "))
unidades_vendidas = eval(input("Escribe las unidades vendidas por mes: "))

punto_equilibrio = calcular_punto_equilibrio(costo_fijo, precio_venta, costo_variable_unitario)
print("El punto de equilibrio en unidades es:", punto_equilibrio)

punto_equilibrio = calcular_punto_equilibrio(costo_fijo, precio_venta, costo_variable_unitario * 0.90)
print("El punto de equilibrio en unidades de (a) es:", punto_equilibrio)

punto_equilibrio = calcular_punto_equilibrio(costo_fijo * 0.92, precio_venta, costo_variable_unitario)
print("El punto de equilibrio en unidades de (b) es:", punto_equilibrio)

punto_equilibrio = calcular_punto_equilibrio(costo_fijo, 110, costo_variable_unitario)
print("El punto de equilibrio en unidades de (c) es:", punto_equilibrio)

utilidad = calcular_utilidad(precio_venta, unidades_vendidas, costo_fijo, costo_variable_unitario)
print("La utilidad regular es:", utilidad)

utilidad_publicidad = calcular_utilidad(precio_venta, unidades_vendidas * 1.15, costo_fijo + 3000, costo_variable_unitario)
print("La utilidad con publicidad es:", utilidad_publicidad)