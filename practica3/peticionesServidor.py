import random
import genCadenasAleatoriasBin as gca
import manejadorArchivos as arch
import automata as att
import re

def isOn():
    respuesta = random.randint(0,1)
    return respuesta != 0

def peticion(mensajeFile):
    mensaje = arch.leerContenidoArchivo(mensajeFile);
    print("Mensaje recibido")
    
    patron = re.compile('\d+')
    mensaje = patron.findall(mensaje)
    
    print("Evaluando cadenas...")
    fileCadenasAceptadas = open('./cadenasAceptadas.txt', 'a')
    fileCadenasRechazadas = open('./cadenasRechazadas.txt', 'a')
    
    for cadena in mensaje:
        if (att.automata1s0spares(cadena)):
            fileCadenasAceptadas.write(cadena + ", ")
        else:
            fileCadenasRechazadas.write(cadena + ", ")
    
    fileCadenasAceptadas.write("\n")
    fileCadenasRechazadas.write("\n")
    
    fileCadenasAceptadas.close()
    fileCadenasRechazadas.close()
    
    print("Cadenas evaluadas")
    
    