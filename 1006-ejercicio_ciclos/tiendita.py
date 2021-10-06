

opcion_menu_principal = 0

while opcion_menu_principal != 9:
    print("Menu principal")
    print("1. Mostrar el carrito.")
    print("2. Mostrar secciones de compra.")
    print("3. Mostrar ofertas.")
    print("9. Salir.")
    print("")
    opcion_menu_principal = eval(input("Ingresa la Opcion: "))

    if opcion_menu_principal == 1:
        print("Mostrar Carrito")
    elif opcion_menu_principal == 2:
        opcion_menu_compras = 0
        while opcion_menu_compras != 9:
            print("Menu compras")
            print("1. Mostrar productos de botanas")
            print("2. Mostrar refrescos")
            print("3. Mostrar bebidas alcoholicas")
            print("9. Regresar al menu anterior")
            print("")
            opcion_menu_compras = eval(input("Ingresa la Opción: "))
    elif opcion_menu_principal == 3:
        print("Mostrar ofertas")


