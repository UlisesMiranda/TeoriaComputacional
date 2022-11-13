from random import random
import random;
import manejadorArchivos as arch
    
def genCadenasAleatoriasBin(tamaño, cantidad, archivoMensaje): 
    file = open(archivoMensaje, 'w')
    fileAcum = open("cadenasGeneradasAcumuladas.txt", 'a')
    
    for i in range(cantidad):
        for j in range (tamaño):
            bit = str(random.randint(0, 1))
            file.write(bit)
            fileAcum.write(bit)
            
        file.write(", ")
        fileAcum.write(", ")
     
    fileAcum.write('\n') 
        
    file.close()
    fileAcum.close()
    


        
