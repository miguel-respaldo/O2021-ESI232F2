import random

longitud = eval(input("Longitud de la cadena: "))

cadena = ""

for x in range(longitud):
    num_letra = random.randint(ord("A"), ord("Z"))
    cadena = cadena + chr(num_letra)

print("La cadena es:", cadena)