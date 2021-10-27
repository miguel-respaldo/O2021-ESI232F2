archivo = open("demo2.txt","a")

archivo.write("Contenido del archivo.\n")
archivo.close()

archivo = open("demo2.txt","r")
print(archivo.read())