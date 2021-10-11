vector1 = [1, 2, 3, 4, 2]
vector2 = [2, 2, 2, 1, 2]

# Producto punto
#  v1 = [a, b, c]
#  v2 = [x, y, z]
#  v1.v2 = a*x + b*y + c*z

producto_punto = 0

for x in range(len(vector1)):
    producto_punto += vector1[x]*vector2[x]

print("El producto punto de", vector1, "con", vector2, "es", producto_punto)
