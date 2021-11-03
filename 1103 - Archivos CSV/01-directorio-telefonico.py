import os

def menu():
    print("  ---  Menu Principal  ---")
    print("1. Listar todo el directorio.")
    print("2. Agregar al directorio.")
    print("3. Borrar del directorio.")
    print("4. Modificar del directrio.")
    print("5. Salir")
    print("")


def crear_directorio(nombre):
    if os.path.exists(nombre):
        archivo = open(nombre, "r")
    else:
        archivo = open(nombre, "w")
        archivo.write("Nombre, Telefono, E-mail\n")
        archivo.close()
        archivo = open(nombre, "r")
    return archivo

def listar_directorio(archivo):
    # El metodo seek(0) nos pone al principio del archivo
    archivo.seek(0)
    for linea in archivo:
        # split sirve para crear una lista separada por comas
        lista = linea.split(",")
        print("{:<20s}{:>15s}{:>30s}".format(lista[0], lista[1], lista[2]))

def agregar_al_directorio(nombre_archivo):
    nombre = input("Escribe el nombre: ")
    telefono = input("Escribe el telefono: ")
    correo_e = input("Escribe el correo electronico: ")
    archivo = open(nombre_archivo, "a")
    archivo.write(nombre + ", " + telefono + ", "+ correo_e + "\n")
    archivo.close()
    archivo = open(nombre_archivo, "r")
    return archivo


opcion = 1
archivo = crear_directorio("directorio.csv")


while opcion != 5:
    menu()
    opcion = eval(input("Opcion: "))

    if opcion == 1:
        listar_directorio(archivo)
    elif opcion == 2:
        archivo.close()
        archivo = agregar_al_directorio("directorio.csv")
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print("Opcion Invalida")