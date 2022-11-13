import numpy as np
import matplotlib.pyplot as plt
import re
import cmath
import os
import random
import sys

def rellenarCadenaBinaria(numCeros):
    cadenaCeros = '';
    
    for i in range(numCeros):
        cadenaCeros = cadenaCeros + '0'
        
    return cadenaCeros
    
def potenciaAlfabeto (n):
            
    for i in range(2**n):
        number = str(format(i, "b"))          
        
        if(len(number) < n):
            diferencia = n - len(number)
            cadenaCeros = rellenarCadenaBinaria(diferencia)
            file.write(cadenaCeros + number + ", ")
            fileCadUnida.write(cadenaCeros + number)  
        else:
            file.write(number + ", ")
            fileCadUnida.write(number)
        
    
def leerResultadoArchivo(file):
    result = ""   
    with open (file, 'r') as archivo:
        result = archivo.read()
    return result

def contarUnos(alfabetoUniverso):
    noDeUnos = []
    
    for element in alfabetoUniverso:
        noDeUnos.append(element.count('1'))
    
    return noDeUnos

def segmentarCadena(cadenaUnida):
    fileSeg = open('./cadenasSegmentadas.txt', 'a')
    
    for i in range(0, len(cadenaUnida), 64) :
        fileSeg.write(cadenaUnida[i: i + 64] + ", ")
        
    
def graficarUnos(result):
    #alfabetoUniverso=[]
    noDeUnos=[]
    iterador = re.finditer('\d+',result)
    
    for match in iterador:
        if sys.getsizeof(noDeUnos) < sys.maxsize:
            noDeUnos.append(match.group().count('1'))
        else:
            break;
        
    #noDeUnos = contarUnos(alfabetoUniverso)
    limite = int(len(noDeUnos)/2)
    print(len(noDeUnos))
        
    print("1ra parte") 
    x = np.array(range(0, limite))
    y = np.array(noDeUnos[0: limite])
    plt.figure(figsize=(10,4))
    plt.title("Conteo de unos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("No. de unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()
    
    print("2da parte")
    x = np.array(range(limite, len(noDeUnos)))
    y = np.array(noDeUnos[limite:])
    plt.figure(figsize=(10,4))
    plt.title("Conteo de unos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("No. de unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()

def graficarLogaritmoDeUnos(result):
    #alfabetoUniverso=[]
    log10Unos = []
    iterador = re.finditer('\d+',result)
    
    for match in iterador:
        if sys.getsizeof(log10Unos) < sys.maxsize:
            log10Unos.append(cmath.log10(match.group().count('1')))
        else:
            break;
        
    #noDeUnos = contarUnos(alfabetoUniverso)
        
    ''' for elemento in noDeUnos:
        log10Unos.append(cmath.log10(elemento))
      '''   
    limite = int(len(log10Unos)/2 ) 
    
    print("1ra parte")
    x = np.array(range(0, limite))
    y = np.array(log10Unos[0: limite])
    plt.figure(figsize=(10,4))
    plt.title("Conteo de unos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("log10 del No. de unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()
    
    print("2da parte")
    x = np.array(range(limite, len(log10Unos)))
    y = np.array(log10Unos[limite:])
    plt.figure(figsize=(10,4))
    plt.title("Conteo de unos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("log10 del No. de unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()

opc = 's'
while(opc == 's' or opc == 's'):
    
    if 'datos.txt' in os.listdir('.'):
        os.remove('./datos.txt')
    if 'cadenasSegmentadas.txt' in os.listdir('.'):
        os.remove('./cadenasSegmentadas.txt')
    if 'cadenaUnida.txt' in os.listdir('.'):
        os.remove('./cadenaUnida.txt')
        
    opcAutomatico = input("Desea un numero aleatorio de k? (s/n) ")
    k = 0
    if (opcAutomatico == 's' or opcAutomatico == 'S'):
        k = random.randint(0, 15) #Con el fin de no desbordar reduci el rango de k
        print("Se ingreso k: ",k)
    else:  
        k = int(input("Ingrese k: "))
    
    file = open ('./datos.txt', 'a')
    fileCadUnida = open ('./cadenaUnida.txt', 'a')
    file.write('{ e }, ')

    for i in range(1, k + 1):
        file.write('{ ')
        potenciaAlfabeto(i)
        file.write('}, ')

    file.close()
    fileCadUnida.close()

    result = leerResultadoArchivo('./datos.txt'); 
    print("Graficas de los universos") 
    graficarUnos(result)
    result = ""
    
    cadenaUnida = leerResultadoArchivo('./cadenaUnida.txt');  
    
    segmentarCadena(cadenaUnida)
    cadenaUnida = ""
    
    resultCadenaSeg = leerResultadoArchivo('./cadenasSegmentadas.txt')
    
    print("Graficas de la cadena segmentadd")
    graficarUnos(resultCadenaSeg)
    
    print("Graficas del logaritmo de las cadenas segmentadas")
    graficarLogaritmoDeUnos(resultCadenaSeg)
    resultCadenaSeg = ""

    opc = input("Desea realizar otra operacion? (s/n) ")
        
    
    
        
    
            
    



    