#Numeros primos

from sympy import isprime
import matplotlib.pyplot as plt
import numpy as np
import re
import math
import os
import random

opc = 's'
while (opc == 's' or opc == 'S'):
    
    if 'primosBinario.txt' in os.listdir('.'):
        os.remove('./primosBinario.txt')
    if 'primosDecimal.txt' in os.listdir('.'):
        os.remove('./primosDecimal.txt')
        
    opcAutomatico = input("Desea un numero aleatorio de n? (s/n) ")
    n = 0
    
    if (opcAutomatico == 's' or opcAutomatico == 'S'):
        n = random.randint(2, 1000000) #Con el fin de no desbordar reduci el rango de n
        print("Se ingreso n: ",n)
    else:
        n = int(input('Indica el limite de busqueda de numeros primos: '))
        
    noDeUnos = []

    filePrimosBinario = open("./primosBinario.txt", 'a')
    filePrimosDecimal = open("./primosDecimal.txt", 'a')
    
    filePrimosBinario.write('{')
    filePrimosDecimal.write('{')
    
    for i in range(n):
        if(isprime(i)):
            filePrimosBinario.write(format(i, "b") + ", ")
            filePrimosDecimal.write(str(i) + ", ")
            
    filePrimosBinario.write('}')
    filePrimosDecimal.write('}')
    
    filePrimosBinario.close()
    filePrimosDecimal.close()

    filePrimosBinario = open("./primosBinario.txt", 'r')
    filePrimosDecimal = open("./primosDecimal.txt", 'r')
    
    resultPrimosBin = filePrimosBinario.read()
    resultPrimosDec = filePrimosDecimal.read()

    patron = re.compile('\d+')
    primosBinario = patron.findall(resultPrimosBin)
    primosDecimal = patron.findall(resultPrimosDec)
    
    filePrimosBinario.close()
    filePrimosDecimal.close()

    for element in primosBinario:
        noDeUnos.append(element.count('1'))
    
    log2noUnos = []   
    log10noUnos = [] 
      
    for element in noDeUnos:
        log2noUnos.append(math.log2(element))
    for element in noDeUnos:
        log10noUnos.append(math.log10(element))

    x = np.array(range(0, len(primosBinario)))
    y = np.array(noDeUnos)
    plt.figure(figsize=(10,4))
    plt.title("Conteo de unos en cadena binaria de no primos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("No de Unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()
    
    x = np.array(range(0, len(primosBinario)))
    y = np.array(log2noUnos)
    plt.figure(figsize=(10,4))
    plt.title("log2 de conteo de unos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("log2 de No de Unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()
    
    x = np.array(range(0, len(primosBinario)))
    y = np.array(log10noUnos)
    plt.figure(figsize=(10,4))
    plt.title("log10 de conteo de unos")
    plt.xlabel("Cadenas Binarias")
    plt.ylabel("log10 de No de Unos en cadena")
    plt.plot(x, y, color = "red", label = "Array elements")
    plt.show()
    
    opc = input("Desea calcular otro valor de n? (s/n) ")

