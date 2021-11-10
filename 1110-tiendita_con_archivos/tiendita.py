
carrito = []
carrito_cantidad = []

opcion_menu_principal = 0

nombre_archivo = "tiendita.csv"

def menu_princial():
    print("Menu principal")
    print("1. Mostrar el carrito.")
    print("2. Mostrar secciones de compra.")
    print("3. Mostrar ofertas.")
    print("9. Salir.")
    print("")


def menu_compras():
    print("Menu compras")
    print("1. Mostrar productos de botanas")
    print("2. Mostrar refrescos")
    print("3. Mostrar bebidas alcoholicas")
    print("9. Regresar al menu anterior")
    print("")


def mostrar_producto(categoria):
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
        carrito.append(productos[producto-1])
        carrito_cantidad.append(cantidad)

    print("-----------------------------------------------")
    archivo.close()


def mostrar_secciones_de_compra():
    opcion_menu_compras = 0
    while opcion_menu_compras != 9:
        menu_compras()
        opcion_menu_compras = eval(input("Ingresa la Opción: "))

        if opcion_menu_compras == 1:
            mostrar_producto("botanas")
        elif opcion_menu_compras == 2:
            mostrar_producto("refrescos")
        elif opcion_menu_compras == 3:
            mostrar_producto("bebidas alcoholicas")

def mostrar_carrito():
    archivo = open(nombre_archivo, "r")

    carrito_precios =[]
    total = 0.0

    for producto in carrito:
        # seek(0) comenzamos desde el principio del archivo
        archivo.seek(0)
        for linea in archivo:
            lista = linea.split(",")
            if producto.lower() == lista[0].strip().lower():
                carrito_precios.append(float(lista[1]))
                break
    archivo.close()

    print("{:<5s}{:<15s}{:>8s}{:>10s}{:>10s}".format("No.", "Nombre", "Cantidad", "P. Unit.", "Precio"))
    for indice in range(len(carrito)):
        print("{:<5d}{:<15s}{:>8d}{:>10.2f}{:>10.2f}".format(indice+1, carrito[indice], int(carrito_cantidad[indice]), float(carrito_precios[indice]), float(carrito_precios[indice])*float(carrito_cantidad[indice])))
        total += float(carrito_precios[indice])*float(carrito_cantidad[indice])
    print("-----------------------------------------------")
    print("{:>38s}{:>10.2f}".format("Total:", total))


while opcion_menu_principal != 9:
    menu_princial()
    opcion_menu_principal = eval(input("Ingresa la Opcion: "))

    if opcion_menu_principal == 1:
        mostrar_carrito()
    elif opcion_menu_principal == 2:
        mostrar_secciones_de_compra()
    elif opcion_menu_principal == 3:
        print("Mostrar ofertas")
