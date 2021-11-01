

def sujeto():
    regresar = ""
    numero = 3 # Aqui va que se calcule el número aleatorio
    if numero == 1:
        regresar = "El gato"
    elif numero == 2:
        regresar = "El perro"
    elif numero == 3:
        regresar = "La señora"
    return regresar


def verbo():
    regresar = "tiene"
    return regresar


def objeto():
    regresar = "un carro"
    return regresar



print(sujeto(), verbo(), objeto())