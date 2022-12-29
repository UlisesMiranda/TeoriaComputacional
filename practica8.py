import random

def construir_palindromo(longitud):
    f.write("Regla seleccionada: P -> ")
    if longitud == 0:
        f.write("e\n")
        return ""
    elif longitud == 1:
        c = random.choice(["0", "1"])
        if c == "0" : 
            f.write("0\n")
        else:
            f.write("1\n")
        return c
    elif longitud == 2:
        c1 = random.choice(["0", "1"])
        if c1 == "0" : 
            f.write("0\n")
        else:
            f.write("1\n")
            
        c2 = random.choice(["0", "1"])
        f.write("Regla seleccionada: P -> ")
        if c2 == "0" : 
            f.write("0\n")
        else:
            f.write("1\n")
            
        return c1 + c2
    else:
        mitad = longitud // 2
        caracter = random.choice(["0", "1"])
        if caracter == "0" : 
            f.write("0P0\n")
        else:
            f.write("1P1\n")
        return caracter + construir_palindromo(mitad) + caracter

# Solicitamos al usuario que seleccione una opción
opcion = input("Seleccione una opción\n1. para definir la longitud manualmente\n2. para generarla automáticamente\nElija su opcion: ")

if opcion == "1":
    # El usuario define la longitud del palíndromo
    longitud = int(input("Ingrese la longitud del palíndromo: "))
elif opcion == "2":
    # Generamos una longitud aleatoria entre 1 y 100,000
    longitud = random.randint(1, 100000)
    
f = open("palindromo.txt", "w")

# Construimos el palíndromo
palindromo = construir_palindromo(longitud)

f.write("Cadena resultante: " + palindromo + "\n")

# Cerramos el archivo
f.close()
