numero = eval(input("Escribe un número: "))

if numero > 10:
    print("Es mayor a 10")
    if numero > 20:
        print("Es mayor a 20")
    else:
        print("Es menor a 20")
else:
    print("Es menor a 10")