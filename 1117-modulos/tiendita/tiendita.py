import menu
import productos
import carrito

opcion_menu_principal = 0

nombre_archivo = "tiendita.csv"

def mostrar_secciones_de_compra():
    opcion_menu_compras = 0
    while opcion_menu_compras != 9:
        menu.compras()
        opcion_menu_compras = eval(input("Ingresa la Opción: "))

        if opcion_menu_compras == 1:
            productos.mostrar("botanas", nombre_archivo)
        elif opcion_menu_compras == 2:
            productos.mostrar("refrescos", nombre_archivo)
        elif opcion_menu_compras == 3:
            productos.mostrar("bebidas alcoholicas", nombre_archivo)



while opcion_menu_principal != 9:
    menu.princial()
    opcion_menu_principal = eval(input("Ingresa la Opcion: "))

    if opcion_menu_principal == 1:
        carrito.mostrar(nombre_archivo)
    elif opcion_menu_principal == 2:
        mostrar_secciones_de_compra()
    elif opcion_menu_principal == 3:
        print("Mostrar ofertas")
