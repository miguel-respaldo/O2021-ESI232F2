archivo = open("demo.txt","r")

print("Los primeros 5 caracteres son:")
print(archivo.read(5))
print("Los siguientes 5 caracteres son:")
print(archivo.read(5))
print("Los siguientes 10 caracteres son:")
print(archivo.read(10))