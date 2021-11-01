
archivo = open("directorio.csv","a")

nombre = ""
telefono = ""
correo_e = ""

numero = eval(input("¿Cuantos registros quieres agregar? "))

for x in range(numero):
    nombre = input("Escribe el nombre: ")
    telefono = input("Escribe el telefono: ")
    correo_e = input("Escribe el correo electronico: ")
    archivo.write(nombre + "," + telefono + "," + correo_e + "\n")