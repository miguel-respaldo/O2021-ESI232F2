lista = []

fruta = "algo"

while fruta != "":
    fruta = input("Ingresa un nombre de una fruta: ")
    if fruta != "":
        lista.append(fruta)

print("La lista original es:", lista)

# Ordenamos la lista con sort
lista.sort()

print("La lista ordenada es:", lista)