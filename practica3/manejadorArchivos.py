def leerContenidoArchivo(nombreArchivo):
    with open(nombreArchivo, 'r', encoding="utf-8") as archivo:
        return archivo.read()
    
def leerLineasArchivo(nombreArchivo):
    with open(nombreArchivo, 'r', encoding="utf-8") as archivo:
        return archivo.readlines();

def sobreescribirArchivo(nombreArchivo, textoSobreescribir):
    with open(nombreArchivo, 'w', encoding="utf-8") as archivo:
        archivo.write(textoSobreescribir);
        
def agregegarTextoArchivo(nombreArchivo, textoAgregar):
    with open(nombreArchivo, 'a', encoding="utf-8") as archivo:
        archivo.write(textoAgregar)
