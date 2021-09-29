num1 = eval(input("Escribe un número: "))
num2 = eval(input("Escribe otro número: "))

opcion = 0

while opcion < 1 or opcion > 4:
    print("Menu")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("")
    opcion = eval(input("Opción: "))
    if opcion < 1 or opcion > 4:
        print("** OPCION INVALIDA **")
        print("Ingresa de nuevo la opcion.")

if opcion == 1:
    print("La suma es", num1 + num2)
elif opcion == 2:
    print("La resta es", num1 - num2)
elif opcion == 3:
    print("La multiplicación es", num1 * num2)
elif opcion == 4:
    if num2 == 0:
        print("No se puede hacer la división.")
    else:
        print("La división es", num1 / num2)
else:
    print("Opción invalida.")

