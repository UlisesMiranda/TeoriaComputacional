
import graphviz
import pandas as pd 

def graficarRuta(estadosConectados):
    
    # Creamos un grafo
    g = graphviz.Digraph()

    # Agregamos los nodos y las aristas a partir de las rutas
    for key, value in estadosConectados.items():
        g.node(str(key))
        for v in value:
            g.edge(str(key), str(v))

    # Renderizamos el grafo
    g.render(format='png', filename=f'grafo_cambiosEstados')
    
estadosConectados = {
    1: {2, 3, 4, 1},
    2: {2,3,4,5,6,7},
    3: {2,3,4,8,9,1},
    4: {2,3,4,10,1},
    5: {2,3,4,11,12,1},
    6: {6,2,3,4,13,14,1},
    7: {2,3,4,15,1},
    8: {2,3,4,16,1},
    9: {2,3,4,17,1},
    10: {2,3,4,18,1},
    11: {2,3,4,19,1},
    12: {2,3,4,20},
    13: {2,3,4,21,1},
    14: {2,3,4,22,1},
    15: {2,3,4,23,1},
    16: {2,3,4,24,1},
    17: {2,3,4,25,1},
    18: {2,3,4,26,1},
    19: {2,3,4,27,1},
    20: {2,3,4,28,1},
    21: {2,3,4,29,1},
    22: {2,3,4,30,1},
    23: {2,3,4,31,1},
    24: {2,3,4,32,1},
    25: {2,3,4,33,1},
    26: {2,3,4,34,1},
    27: {2,3,4,35,1},
    28: {2,3,4,36,1},
    29: {2,3,4,37,1},
    30: {2,3,4,8, 9, 1},
    31: {2,3,4,38,1},
    32: {2,3,4,39,1},
    33: {2,3,4,1},
    34: {2,3,4,39,1},
    35: {3,4,40,1},
    36: {3,4,41,1},
    37: {2,3,4,42,10,1},
    38: {2,3,4,43,1},
    39: {3,4,43,44,1},
    40: {2,3,4,45,1},
    41: {2,3,4,6,7,46,1},
    42: {2,3,4,47,1},
    43: {3,4,48,1},
    44: {2,3,4,5, 49, 6, 7,1},
    45: {2,3,4,50,1},
    46: {2,3,4,51,1},
    47: {2,3,4,1},
    48: {2,3,4,52,6,7,1},
    49: {2,3,4,53,1},
    50: {2,3,4,1},
    51: {2,3,4,1},
    52: {2,3,4,11,12,54,1},
    53: {2,3,4,1},
    54:{2,3,4,1}
}

f = open("textocovid.txt", "r")
evaluacionAutomata = open("evaluacionAutomata.txt", "w")

texto = f.read()

gripe_conteo = [] 
contagio_conteo = [] 
distancia_conteo = [] 
calentura_conteo = [] 
covid_conteo = [] 
cansancio_conteo = [] 
cubrebocas_conteo = [] 
dolor_conteo = [] 
aux = 0
estado = 1

for letra in texto.lower():
    evaluacionAutomata.write(f"Estado actual: {estado}\tRecibe letra: {letra}\n")
    aux += 1
    if (estado == 1):
        if (letra == "c"):
            estado = 2
        elif (letra == "d"):
            estado = 3
        elif (letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 2):
        if (letra == "c"):
            estado = 2
        elif (letra == "d"):
            estado = 3
        elif (letra == "g"):
            estado = 4
        elif (letra == "a"):
            estado = 5
        elif (letra == "o"):
            estado = 6
        elif (letra == "u"):
            estado = 7
        else:
            estado = 1
        continue

    if (estado == 3):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "i"):
            estado = 8
        elif(letra == "o"):
            estado = 9
        else:
            estado = 1
        continue

    if (estado == 4):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "r"):
            estado = 10
        else:
            estado = 1
        continue

    if (estado == 5):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "l"):
            estado = 11
        elif (letra == "n"):
            estado = 12
        else:
            estado = 1
        continue

    if (estado == 6):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "n"):
            estado = 13
        elif (letra == "v"):
            estado = 14
        else:
            estado = 1
        continue

    if (estado == 7):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "b"):
            estado = 15
        else:
            estado = 1
        continue

    if (estado == 8):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "s"):
            estado = 16
        else:
            estado = 1
        continue

    if (estado == 9):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "l"):
            estado = 17
        else:
            estado = 1
        continue

    if (estado == 10):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "i"):
            estado = 18
        else:
            estado = 1
        continue

    if (estado == 11):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "e"):
            estado = 19
        else:
            estado = 1
        continue

    if (estado == 12):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "s"):
            estado = 20
        else:
            estado = 1
        continue

    if (estado == 13):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "t"):
            estado = 21
        else:
            estado = 1
        continue

    if (estado == 14):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "i"):
            estado = 22
        else:
            estado = 1
        continue

    if (estado == 15):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "r"):
            estado = 23
        else:
            estado = 1
        continue

    if (estado == 16):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "t"):
            estado = 24
        else:
            estado = 1
        continue

    if (estado == 17):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "o"):
            estado = 25
        else:
            estado = 1
        continue

    if (estado == 18):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "p"):
            estado = 26
        else:
            estado = 1
        continue

    if (estado == 19):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "n"):
            estado = 27
        else:
            estado = 1
        continue

    if (estado == 20):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "a"):
            estado = 28
        else:
            estado = 1
        continue

    if (estado == 21):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "a"):
            estado = 29
        else:
            estado = 1
        continue

    if (estado == 22): 
        if (letra == "c"):
            estado = 2
        # Estado que completa la palabra COVID
        elif(letra == "d"):
            covid_conteo.append(aux-5)
            estado = 30
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 23):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "e"):
            estado = 31
        else:
            estado = 1
        continue

    if (estado == 24):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "a"):
            estado = 32
        else:
            estado = 1
        continue

    if (estado == 25): 
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "r"):
            # Estado que completa la palabra DOLOR
            dolor_conteo.append(aux-5)
            estado = 33
        else:
            estado = 1
        continue

    if (estado == 26): 
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        # Estado que completa la palabra GRIPE
        elif(letra == "e"):
            gripe_conteo.append(aux-5)
            estado = 34
        else:
            estado = 1
        continue
  
    if (estado == 27):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "t"):
            estado = 35
        else:
            estado = 1
        continue

    if (estado == 28):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "n"):
            estado = 36
        else:
            estado = 1
        continue

    if (estado == 29):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 37
        else:
            estado = 1
        continue

    if (estado == 30):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "i"):
            estado = 8
        elif(letra == "o"):
            estado = 9
        else:
            estado = 1
        continue

    if (estado == 31):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "b"):
            estado = 38
        else:
            estado = 1
        continue

    if (estado == 32):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "n"):
            estado = 39
        else:
            estado = 1
        continue

    if (estado == 33):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 34):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "n"):
            estado = 39
        else:
            estado = 1
        continue

    if (estado == 35):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "u"):
            estado = 40
        else:
            estado = 1
        continue

    if (estado == 36):
        if (letra == "c"):
            estado = 41
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 37):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "i"):
            estado = 42
        elif(letra == "r"):
            estado = 10
        else:
            estado = 1
        continue

    if (estado == 38):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "o"):
            estado = 43
        else:
            estado = 1
        continue

    if (estado == 39):
        if (letra == "c"):
            estado = 44
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "o"):
            estado = 43
        else:
            estado = 1
        continue

    if (estado == 40):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "r"):
            estado = 45
        else:
            estado = 1
        continue

    if (estado == 41):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "a"):
            estado = 6
        elif(letra == "i"):
            estado = 46
        elif(letra == "o"):
            estado = 6
        elif(letra == "u"):
            estado = 7
        else:
            estado = 1
        continue

    if(estado == 42):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        # Estado que completa la palabra CONTAGIO
        elif(letra == "o"):
            contagio_conteo.append(aux-8)
            estado = 47
        else:
            estado = 1
        continue

    if (estado == 43):
        if (letra == "c"):
            estado = 48
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 44):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "a"):
            estado = 5
        elif(letra == "i"):
            estado = 49
        elif(letra == "o"):
            estado = 6
        elif(letra == "u"):
            estado = 7
        else:
            estado = 1
        continue

    if (estado == 45): 
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        # Estado que completa la palabra CALENTURA
        elif(letra == "a"):
            calentura_conteo.append(aux-9)
            estado = 50
        else:
            estado = 1
        continue

    if (estado == 46): 
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        # Estado que completa la palabra CANSANCIO
        elif(letra == "o"):
            cansancio_conteo.append(aux - 9)
            estado = 51
        else:
            estado = 1
        continue

    if (estado == 47):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 48):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "a"):
            estado = 52
        elif(letra == "o"):
            estado = 6
        elif(letra == "u"):
            estado = 7
        else:
            estado = 1
        continue

    if (estado == 49):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
            
        # Estado que completa la palabra DISTANCIA
        elif(letra == "a"):
            distancia_conteo.append(aux - 9)
            estado = 53
        else:
            estado = 1
        continue

    if (estado == 50):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 51):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 52): 
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        elif(letra == "l"):
            estado = 11
        elif(letra == "n"):
            estado = 12
        # Estado que completa la palabra CUBREBOCAS
        elif(letra == "s"):
            cubrebocas_conteo.append(aux - 10)
            estado = 54
        else:
            estado = 1
        continue

    if (estado == 53):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

    if (estado == 54):
        if (letra == "c"):
            estado = 2
        elif(letra == "d"):
            estado = 3
        elif(letra == "g"):
            estado = 4
        else:
            estado = 1
        continue

f.close()
evaluacionAutomata.close()

datos = {
    "Palabras": ["Gripe","Contagio","Distancia","Calentura","Covid","Cansancio","Cubrebocas","Dolor"],
    "Frecuencia": [len(gripe_conteo),len(contagio_conteo),len(distancia_conteo),len(calentura_conteo),len(covid_conteo),len(cansancio_conteo),len(cubrebocas_conteo),len(dolor_conteo)],
    "Posiciones": [gripe_conteo, contagio_conteo,distancia_conteo,calentura_conteo,covid_conteo,cansancio_conteo,cubrebocas_conteo,dolor_conteo]
}
resultadosDf = pd.DataFrame(datos)
resultadosDf.to_excel("ResultadosObtenidos.xlsx")
print(resultadosDf)

graficarRuta(estadosConectados)

# Convertir el diccionario en un dataframe
estadosDf = pd.DataFrame(estadosConectados.items(), columns=['Estado', 'Conexiones'])
estadosDf.to_excel("Tabla de estados.xlsx")

print(estadosDf)