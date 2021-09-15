frase1 = "Esta es una frase que no dice nada"
#         0123456789012345678901234567890123
frase2 = "Hola"
frase3 = "0123456789"

# Para saber el largo de una cadena de texto se usa "len"

print("La frase 1 tiene de largo:", len(frase1))
print("La frase 2 tiene de largo:", len(frase2))

print("1:",frase1[5]) # Letra "e"
print("2:",frase1[4]) # Espacio en blanco " "

print("3:",frase1[:5])
print("4:",frase3[:2])

print("5:",frase3[2:])
print("6:",frase1[22:])

print("7:",frase1[8:17])

print("8:",frase1[:-1])
print("9:",frase1[:-9])

print("10:",frase1[::-1])
print("11:",frase2[::-1])
print("12:",frase3[::-1])