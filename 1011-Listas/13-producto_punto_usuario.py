vector1 = []
vector2 = []

dimension = eval(input("Escribe la dimensión del vector: "))

for x in range(dimension):
    numero = eval(input("Escribe un número del vector 1: "))
    vector1.append(numero)

for x in range(dimension):
    numero = eval(input("Escribe un número del vector 2: "))
    vector2.append(numero)

producto_punto = 0

for x in range(len(vector1)):
    producto_punto += vector1[x]*vector2[x]

print("El producto punto de", vector1, "con", vector2, "es", producto_punto)
