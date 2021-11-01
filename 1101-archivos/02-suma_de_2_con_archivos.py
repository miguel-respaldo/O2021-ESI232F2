def suma(n1, n2):
    return n1 + n2

archivo = open("sumade2.txt","r")

num1 = eval(archivo.readline())
num2 = eval(archivo.readline())

archivo.close()

print("La suma es:", suma(num1,num2))

