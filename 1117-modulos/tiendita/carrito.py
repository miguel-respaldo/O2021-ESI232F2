
carrito = []
cantidad = []

def mostrar(nombre_archivo):
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
        print("{:<5d}{:<15s}{:>8d}{:>10.2f}{:>10.2f}".format(indice+1, carrito[indice], int(cantidad[indice]), float(carrito_precios[indice]), float(carrito_precios[indice])*float(cantidad[indice])))
        total += float(carrito_precios[indice])*float(cantidad[indice])
    print("-----------------------------------------------")
    print("{:>38s}{:>10.2f}".format("Total:", total))
