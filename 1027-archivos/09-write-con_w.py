archivo = open("demo2.txt","w")

archivo.write("Woops! ya se borro.\n")
archivo.close()

archivo = open("demo2.txt","r")
print(archivo.read())