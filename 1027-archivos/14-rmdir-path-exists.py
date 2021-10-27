import os

if os.path.exists("carpeta1"):
    os.rmdir("carpeta1")
    print("Ya borre la carpeta1")
else:
    print("La carpeta/directorio no existe")