numero = eval(input("Ingresa un numero: "))

i=0
while i <= numero:
    i += 1
    if i % 2 != 0: # el numero i es impar
        continue
    print(i)

print("Termine.")