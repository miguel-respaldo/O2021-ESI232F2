import carrito

def mostrar(categoria, nombre_archivo):
    archivo = open(nombre_archivo, "r")
    productos=[]
    numero = 1

    print("{:<5s}{:<15s}{:>8s}{:>8s}".format("No.", "Nombre", "Cantidad", "Precio"))
    for linea in archivo:
        lista = linea.split(",")
        if categoria.lower() == lista[3].strip().lower():
            productos.append(lista[0])
            print("{:<5d}{:<15s}{:>8d}{:>8.2f}".format(numero,lista[0],int(lista[2]),float(lista[1])))
            numero += 1

    print("-----------------------------------------------")
    print("¿Cúal producto desear agregar al carrito?")
    print("Nota: puedes ponder 0 para salir")
    producto = eval(input("Producto: "))

    if producto != 0:
        cantidad = eval(input("¿Cuantos articulos?: "))
        carrito.carrito.append(productos[producto-1])
        carrito.cantidad.append(cantidad)

    print("-----------------------------------------------")
    archivo.close()
