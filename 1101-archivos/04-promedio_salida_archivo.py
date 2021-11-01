archivo = open("promedio.txt")
resultado = open("resultado.txt", "w")

suma = 0
contador = 0
for linea in archivo:
    numero = eval(linea)
    suma += numero
    contador += 1

archivo.close()

promedio = suma / contador

#print("La suma de todos es:", suma)
resultado.write("La suma de todo es " + str(suma) + "\n")
#print("El promedio es:", promedio)
resultado.write("El promedio es: " + str(promedio) + "\n")