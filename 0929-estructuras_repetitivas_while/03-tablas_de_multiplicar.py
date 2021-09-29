# El usuario ingrese la tabla de multiplicar que quiera ver
# Entrda:  Ingresa la tabla a imprimir: 5
# Salida:  1 x 5 = 5
#          2 x 5 = 10
#          ...
#          10 x 5 = 50

tabla = eval(input("Ingresa la tabla a imprimir: "))

i = 1
while i <= 10:
    print(i,"x",tabla,"=", i * tabla)
    i += 1

