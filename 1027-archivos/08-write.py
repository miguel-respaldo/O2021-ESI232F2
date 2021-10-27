archivo = open("demo2.txt","a")

archivo.write("Contenido del archivo.")
archivo.close()

archivo = open("demo2.txt","r")
print(archivo.read())