def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    pass

num1 = eval(input("Ingresa un número: "))
num2 = eval(input("Ingresa otro número: "))

# Regrese a una variable
resultado = suma(num1, num2)
print("La suma es:", resultado)

# imprimir directo
print("La suma es:", suma(num1, num2))
