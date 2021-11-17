def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    resultado = 0
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("No se puede dividir entre cero.")
    return resultado