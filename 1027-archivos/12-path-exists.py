import os

if os.path.exists("demo2.txt"):
    os.remove("demo2.txt")
else:
    print("El archivo demo2.txt no existe.")