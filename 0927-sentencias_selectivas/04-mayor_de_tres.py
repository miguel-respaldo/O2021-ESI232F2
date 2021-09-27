num1 = eval(input("Escribe el primer número: "))
num2 = eval(input("Escribe el primer número: "))
num3 = eval(input("Escribe el primer número: "))

if num1 > num2:
    if num1 > num3:
        print("El número mayor es", num1)
    else:
        print("El número mayor es", num3)
else:
    if num2 > num3:
        print("El número mayor es", num2)
    else:
        print("El número mayor es", num3)
