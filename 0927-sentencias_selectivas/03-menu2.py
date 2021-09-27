num1 = eval(input("Escribe un número: "))
num2 = eval(input("Escribe otro número: "))

print("Menu")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("")
opcion = eval(input("Opción: "))

if opcion == 1:
    print("La suma es", num1 + num2)

if opcion == 2:
    print("La resta es", num1 - num2)

if opcion == 3:
    print("La multiplicación es", num1 * num2)

if opcion == 4:
    if num2 == 0:
        print("No se puede hacer la división.")
    else:
        print("La división es", num1 / num2)


if opcion <= 0 or opcion >= 5:
    print("opcion invalida")