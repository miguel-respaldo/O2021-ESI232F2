def suma(*numeros):
    print("La suma es:", numeros[0] + numeros[1])

def resta(*numeros):
    print("La resta es:", numeros[0] - numeros[1])

def multiplicacion(num1, num2):
    print("La resta es:", num1 * num2)


num1 = eval(input("Escribe un número: "))
num2 = eval(input("Escribe otro número: "))

suma(num1, num2, 3, 4, 5, 6)
resta(num1, num2, 3, 4, 5)
multiplicacion(num1, num2)