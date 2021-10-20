import math

def menu():
    print("Menu")
    print("1. Calcular el área de un rectángulo.")
    print("2. Calcular el área de un triangulo.")
    print("3. Calcular el área de un cuadrado.")
    print("4. Calcular el área de un circulo.")
    print("5. Salir")

def area_circulo(radio):
    # return 3.1416 * radio * radio
    # return 3.1416 * radio**2
    return math.pi * radio**2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

opcion = 0

while opcion != 5:
    menu()
    opcion = eval(input("Escribe una opcion: "))

    if opcion == 1:  # Área de rectángulo
        base = eval(input("Escribe el valor de la base del rectangulo: "))
        altura = eval(input("Escribe el valor de la altura del rectangulo: "))
        area = area_rectangulo(base, altura)
        print("El area del rectangulo es:", area)
    elif opcion == 2: # Área de triangulo
        base = eval(input("Escribe el valor de la base del triangulo: "))
        altura = eval(input("Escribe el valor de la altura del triangulo: "))
        area = area_triangulo(base, altura)
        print("El area del triangulo es:", area)
    elif opcion == 3: # Área de cuadrado
        lado = eval(input("Escribe el valor del lado del cuadrado: "))
        area = area_rectangulo(lado, lado)
        print("El area del cuadrado es:", area)
    elif opcion == 4: # Área de circulo
        radio = eval(input("Escribe el valor del radio del circulo: "))
        area = area_circulo(radio)
        print("El area del circulo es:", area)
