archivo = open("promedio.txt")

suma = 0
contador = 0
for linea in archivo:
    numero = eval(linea)
    suma += numero
    contador += 1

promedio = suma / contador
print("La suma de todos es:", suma)
print("El promedio es:", promedio)