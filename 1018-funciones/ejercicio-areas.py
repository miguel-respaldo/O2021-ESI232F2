def menu():
    print("Menu")
    print("1. Calcular el área de un rectángulo.")
    print("2. Calcular el área de un triangulo.")
    print("3. Calcular el área de un cuadrado.")
    print("4. Calcular el área de un circulo.")
    print("5. Salir")

def area_circulo(radio):
    return radio

opcion = 0

while opcion != 5:
    menu()
    opcion = eval(input("Escribe una opcion: "))

    if opcion == 1:  # Área de rectángulo
        pass
    elif opcion == 2: # Área de triangulo
        pass
    elif opcion == 3: # Área de cuadrado
        pass
    elif opcion == 4: # Área de circulo
        radio = eval(input("Escribe el valor del radio del circulo: "))
        area = area_circulo(radio)
        print("El area del circulo es:", area)
