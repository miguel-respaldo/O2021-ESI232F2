import operaciones

def menu():
    print(" --- Calculadora  ---")
    print("1. suma.")
    print("2. resta.")
    print("3. multiplicaicon.")
    print("4. division.")
    print("5. Salir.")
    print("")


opcion_menu = 0

while opcion_menu != 5:
    menu()
    opcion_menu = eval(input("Opcion: "))

    if opcion_menu < 5:
        n1 = eval(input("Escribe un numero: "))
        n2 = eval(input("Escribe otro numero: "))

    if opcion_menu == 1:
        resultado = operaciones.suma(n1, n2)
    elif opcion_menu == 2:
        resultado = operaciones.resta(n1,n2)
    elif opcion_menu == 3:
        resultado = operaciones.multiplicacion(n1, n2)
    elif opcion_menu == 4:
        resultado = operaciones.division(n1, n2)

    if opcion_menu < 5:
        print("El resultado es", resultado)
