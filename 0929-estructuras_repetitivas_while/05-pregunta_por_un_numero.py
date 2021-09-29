# Hacer un programa que me pida un numero del 1 al 10
# y me diga cual número fue en ciclo
# Entrada: Ingresa un número: 4
# Salida: ingresaste el numero 4

numero = eval(input("Ingresa un número: "))
i = 1
while i <= 10:
    if i == numero:
        print("ingresaste el numero:", numero)
        break

