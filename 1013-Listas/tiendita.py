
botanas = ["cacahuates", "chocolates", "papas", "gomitas"]
botanas_precio = [10, 20.5, 15.5, 13]
botanas_stock = [7, 10, 20, 14]

refrescos = ["coca", "sprite", "fanta", "manzanita"]
refrescos_precio = [16.25, 17, 15.5, 17]
refrescos_stock = [10, 15, 12, 16]

#Bebidas Alcoholicas
be_alco = ["cervesa", "tequila", "vino", "mezcal"]
be_alco_precio = [40, 120, 150, 200]
be_alco_stock = [30, 40, 50, 70]

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

            if opcion_menu_compras == 1:
                print("No.   Nombre  Cantidad   Precio ")
                for numero in range(len(botanas)):
                    print(numero,"  ",botanas[numero],"  ",
                            botanas_stock[numero], "  ", botanas_precio[numero])

            elif opcion_menu_compras == 2:
                print("mostrar refrescos")
            elif opcion_menu_compras == 3:
                print("mostrar bebidas alcoholicas")


    elif opcion_menu_principal == 3:
        print("Mostrar ofertas")


