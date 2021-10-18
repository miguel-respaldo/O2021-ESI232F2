def suma(*numeros):
    print("La suma es:", numeros[0] + numeros[1])

def resta(*numeros):
    print("La resta es:", numeros[0] - numeros[1])

num1 = eval(input("Escribe un número: "))
num2 = eval(input("Escribe otro número: "))

suma(num1, num2)
resta(num1, num2)