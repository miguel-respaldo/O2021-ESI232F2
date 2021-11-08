categoria = input("Escribe la categoria a imprimir: ")

archivo = open("tiendita.csv","r")

for linea in archivo:
    lista = linea.split(",")
    if categoria.lower() == lista[3].strip().lower():
        print(lista[0])
