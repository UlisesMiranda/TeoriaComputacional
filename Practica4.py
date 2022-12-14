# TABLERO NFA
from itertools import zip_longest
import os
import random
import re
import time
from strgen import StringGenerator
from tkinter import*
import random
import networkx as nx
import matplotlib.pyplot as plt
import graphviz

switch = {
    'a': {'B': 'be', 'R': 'f'},
    'b': {'B': 'eg', 'R': 'afc'},
    'c': {'B': 'bgd', 'R': 'fh'},
    'd': {'B': 'g', 'R': 'ch'},
    'e': {'B': 'bj', 'R': 'afi'},
    'f': {'B': 'begj', 'R': 'acik'},
    'g': {'B': 'bdjl', 'R': 'cfhk'},
    'h': {'B': 'dgl', 'R': 'ck'},
    'i': {'B': 'ejm', 'R': 'fn'},
    'j': {'B': 'egmo', 'R': 'fikn'},
    'k': {'B': 'gjlo', 'R': 'fhnp'},
    'l': {'B': 'go', 'R': 'hkp'},
    'm': {'B': 'j', 'R': 'in'},
    'n': {'B': 'mjo', 'R': 'ik'},
    'o': {'B': 'jl', 'R': 'nkp'},
    'p': {'B': 'lo', 'R': 'k'},
}


def routes(current, path):
    if not path:
        yield (current,)
        return
    first, *newpath = path
    for state in switch[current][first]:
        for route in routes(state, newpath):
            yield (current,) + route


def chess(path, estadoInicial: str, id: str):
    fileRutasPosibles = open(f'rutasPosibles{id}.txt', 'a')
    fileRutasGanadoras = open(f'rutasGanadoras{id}.txt', 'a')
    listSize = 0
    
    rutas = []

    for i, r in enumerate(routes(estadoInicial, path), 1):
        fileRutasPosibles.write(str(r) + '\n')
        rutas.append(list(r))

        if (id == 'Ply1' and r[-1] == 'p'):
            fileRutasGanadoras.write(str(r) + '\n')
            listSize += 1
        if (id == 'Ply2' and r[-1] == 'm'):
            fileRutasGanadoras.write(str(r) + '\n')
            listSize += 1

    fileRutasGanadoras.close()
    fileRutasPosibles.close()
    
    graficarRuta(rutas, id)

    return listSize


def obtenerRutaGanadoraAleatoria(fileRutas, listSize):
    fileRutasGanadoras = open(fileRutas, 'r')
    randomRutaGanadora = 0
    if (listSize):
        randomRutaGanadora = random.randint(1, listSize)
    rutaGanadora = []
    patron = re.compile('[a-p]')

    count = 1
    for line in fileRutasGanadoras:
        if (count == randomRutaGanadora):
            rutaGanadora = patron.findall(line)
            break
        count += 1

    return rutaGanadora


def corregirCruces(rutaGanadora1: list, rutaGanadora2: list):
    i = 0
    for l1, l2 in zip_longest(rutaGanadora1, rutaGanadora2, fillvalue=' '):
        if(l1 == l2):
            print("Se cruzan")
            rutaGanadora2.insert(i, rutaGanadora2[i-1])
        i += 1

    return rutaGanadora2


def recorridoRutasGanadoras(rutaJugadorInicial: list, rutaJugadorSecundario: list):
    i = 0
    for l1, l2 in zip_longest(rutaJugadorInicial, rutaJugadorSecundario):

        if not l1:
            return "principal"
        if not l2:
            return "secundario"
    return "principal"

def graficarRuta(rutas, id):
    
    # Creamos un grafo
    g = graphviz.Digraph()

    # Agregamos los nodos y las aristas a partir de las rutas
    for ruta in rutas:
        for nodo in ruta:
            g.node(nodo)
        for i in range(len(ruta)-1):
            g.edge(ruta[i], ruta[i+1])

    # Renderizamos el grafo
    g.render(format='png', filename=f'grafo{id}')

def game(modoJuego: int, dosJugadores: bool, ):
    listSize1 = 0
    listSize2 = 0

    if dosJugadores == 1:
        print("\nSe eligi?? un jugador: ")

        if (modoJuego == 2):
            size = str(random.randint(1, 10))  # Para evitar morir
            print("tama??o: ", size)

            cadenaAleatoria = StringGenerator("[RB]{%s}" % size).render_list(1)
            print("Cadena generada: ", cadenaAleatoria)

            print("\nGenerando rutas... ")
            listSize1 = chess(cadenaAleatoria[0], 'a', 'Ply1')
        else:
            cadena = input("Ingrese su ruta: ")

            print("\nGenerando rutas... ")
            listSize1 = chess(cadena, 'a', 'Ply1')

        print("-------Rutas generadas-------")

        rutaGanadora1 = obtenerRutaGanadoraAleatoria(
            "rutasGanadorasPly1.txt", listSize1)

        if(rutaGanadora1):
            print("Ruta elegida para jugador1: ", rutaGanadora1)
            return list(zip_longest(rutaGanadora1, ['']))
        else:
            print("No hay ruta ganadora")

    else:
        print("\nSe eligieron dos jugadores: ")

        if modoJuego == 2:
            sizeJug1 = str(random.randint(1, 10))
            sizeJug2 = str(random.randint(1, 10))

            print("Tama??o1: ", sizeJug1)
            print("Tama??o2: ", sizeJug2)

            cadenaAleatoria1 = StringGenerator(
                "[RB]{%s}" % sizeJug1).render_list(1)
            print("Cadena generada para jug 1: ", cadenaAleatoria1)

            cadenaAleatoria2 = StringGenerator(
                "[RB]{%s}" % sizeJug2).render_list(1)
            print("Cadena generada para jug 2: ", cadenaAleatoria2)

            print("\nGenerando rutas... ")
            listSize1 = chess(cadenaAleatoria1[0], 'a', 'Ply1')
            listSize2 = chess(cadenaAleatoria2[0], 'd', 'Ply2')
        else:
            cadena1 = input("Ingrese su ruta jugador 1: ")
            cadena2 = input("Ingrese su ruta jugador 2: ")

            print("\nGenerando rutas... ")
            listSize1 = chess(cadena1, 'a', 'Ply1')
            listSize2 = chess(cadena2, 'd', 'Ply2')

        print("-------Rutas generadas-------")

        print("\nEligiendo ruta ganadora de cada jugador...")

        rutaGanadoraPly1 = obtenerRutaGanadoraAleatoria(
            "rutasGanadorasPly1.txt", listSize1)
        rutaGanadoraPly2 = obtenerRutaGanadoraAleatoria(
            "rutasGanadorasPly2.txt", listSize2)

        if (rutaGanadoraPly1 and rutaGanadoraPly2):
            print("Ruta elegida para jugador1: ", rutaGanadoraPly1)
            print("Ruta elegida para jugador2: ", rutaGanadoraPly2)

            startPlayer = random.randint(0,1)

            if (startPlayer == 0):
                print("\nEmpieza jugador 1 (JUGADOR PRINCIPAL)")
                rutaGanadoraPly2 = corregirCruces(
                    rutaGanadoraPly1, rutaGanadoraPly2)
                ganador = recorridoRutasGanadoras(
                    rutaGanadoraPly1, rutaGanadoraPly2)

                print("Ruta final para jugador1: ", rutaGanadoraPly1)
                print("Ruta final para jugador2: ", rutaGanadoraPly2)

                if (ganador == "principal"):
                    print("\n----------Gana el jugador 1-----------")
                    return list(zip_longest(rutaGanadoraPly1, rutaGanadoraPly2)) #return(jugadorPrincipal, jugadorSecundario)
                else:
                    print("\n----------Gana el jugador 2-----------")
                    return list(zip_longest(rutaGanadoraPly1, rutaGanadoraPly2))

            else:
                print("\nEmpieza jugador 2 (JUGADOR PRINCIPAL)")
                rutaGanadoraPly1 = corregirCruces(
                    rutaGanadoraPly2, rutaGanadoraPly1)
                ganador = recorridoRutasGanadoras(
                    rutaGanadoraPly2, rutaGanadoraPly1)

                print("Ruta final para jugador1: ", rutaGanadoraPly1)
                print("Ruta final para jugador2: ", rutaGanadoraPly2)

                if (ganador == "principal"):
                    print("\n----------Gana el jugador 2-----------")
                    return list(zip_longest(rutaGanadoraPly2, rutaGanadoraPly1))
                else:
                    print("\n----------Gana el jugador 1-----------")
                    return list(zip_longest(rutaGanadoraPly2, rutaGanadoraPly1))

        elif (rutaGanadoraPly1):
            print("Ruta elegida para jugador1: ", rutaGanadoraPly1)
            print("\nNo hay ruta ganadora para el jugador 2")

            print("\n----------Gana el jugador 1-----------")

            return list(zip_longest(rutaGanadoraPly1, rutaGanadoraPly2))

        elif (rutaGanadoraPly2):
            print("\nNo hay ruta ganadora para el jugador 1")
            print("Ruta elegida para jugador2: ", rutaGanadoraPly2)

            print("\n----------Gana el jugador 2-----------")
            return list(zip_longest(rutaGanadoraPly2, rutaGanadoraPly1))

        else:
            print("\nNo hay rutas ganadoras de ningun jugador")
            print("\n----------Nadie gana-----------")


if 'rutasGanadorasPly1.txt' in os.listdir('.'):
    os.remove('./rutasGanadorasPly1.txt')
if 'rutasGanadorasPly2.txt' in os.listdir('.'):
    os.remove('./rutasGanadorasPly2.txt')
if 'rutasPosiblesPly1.txt' in os.listdir('.'):
    os.remove('./rutasPosiblesPly1.txt')
if 'rutasPosiblesPly2.txt' in os.listdir('.'):
    os.remove('./rutasPosiblesPly2.txt')

print("BIENVENIDO")
print("Escoja su modo de juego: ")
print("1. Manual")
print("2. Automatico")
modoJuego = int(input("Inserte el no. de su opci??n: "))

patron = re.compile('[a-p]')
rutaAgrupada = []

if (modoJuego == 1):
    print("\nElija cuantos jugadores desea: ")
    print("1. Un jugador")
    print("2. Dos jugadores")
    dosJugadores = int(input("Ingrese su opcion: "))

    rutaAgrupada = game(modoJuego, dosJugadores)
else:
    dosJugadores = random.randint(0, 1)
    rutaAgrupada = game(modoJuego, dosJugadores)

ventana = Tk()
canv = Canvas(ventana, width=800, height=800)
ventana.geometry("800x800")

canv.create_rectangle(0, 0, 200, 200, width=0, fill='red')
canv.create_rectangle(200, 0, 400, 200, width=0, fill='black')
canv.create_rectangle(400, 0, 600, 200, width=0, fill='red')
canv.create_rectangle(600, 0, 800, 200, width=0, fill='black')
canv.create_text(20, 20, text="a", fill="white", font=('Helvetica 15 bold'))
canv.create_text(220, 20, text="b", fill="white", font=('Helvetica 15 bold'))
canv.create_text(420, 20, text="c", fill="white", font=('Helvetica 15 bold'))
canv.create_text(620, 20, text="d", fill="white", font=('Helvetica 15 bold'))

canv.create_rectangle(0, 200, 200, 400, width=0, fill='black')
canv.create_rectangle(200, 200, 400, 400, width=0, fill='red')
canv.create_rectangle(400, 200, 600, 400, width=0, fill='black')
canv.create_rectangle(600, 200, 800, 400, width=0, fill='red')
canv.create_text(20, 220, text="e", fill="white", font=('Helvetica 15 bold'))
canv.create_text(220, 220, text="f", fill="white", font=('Helvetica 15 bold'))
canv.create_text(420, 220, text="g", fill="white", font=('Helvetica 15 bold'))
canv.create_text(620, 220, text="h", fill="white", font=('Helvetica 15 bold'))

canv.create_rectangle(0, 400, 200, 600, width=0, fill='red')
canv.create_rectangle(200, 400, 400, 600, width=0, fill='black')
canv.create_rectangle(400, 400, 600, 600, width=0, fill='red')
canv.create_rectangle(600, 400, 800, 600, width=0, fill='black')
canv.create_text(20, 420, text="i", fill="white", font=('Helvetica 15 bold'))
canv.create_text(220, 420, text="j", fill="white", font=('Helvetica 15 bold'))
canv.create_text(420, 420, text="k", fill="white", font=('Helvetica 15 bold'))
canv.create_text(620, 420, text="l", fill="white", font=('Helvetica 15 bold'))

canv.create_rectangle(0, 600, 200, 800, width=0, fill='black')
canv.create_rectangle(200, 600, 400, 800, width=0, fill='red')
canv.create_rectangle(400, 600, 600, 800, width=0, fill='black')
canv.create_rectangle(600, 600, 800, 800, width=0, fill='red')
canv.create_text(20, 620, text="m", fill="white", font=('Helvetica 15 bold'))
canv.create_text(220, 620, text="n", fill="white", font=('Helvetica 15 bold'))
canv.create_text(420, 620, text="o", fill="white", font=('Helvetica 15 bold'))
canv.create_text(620, 620, text="p", fill="white", font=('Helvetica 15 bold'))

canv.pack()

time.sleep(3)

print("\nRuta agrupada de los jugadores: ", rutaAgrupada)
if rutaAgrupada:

    for camino in rutaAgrupada:

        print("\nRuta del jugador PRINCIPAL: ", camino[0])
        print("Ruta del jugador SECUNDARIO: ", camino[1])
    

        if (camino[0] == 'a'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(50, 50, 150, 150, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'b'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(250, 50, 350, 150, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'c'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(450, 50, 550, 150, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'd'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(650, 50, 750, 150, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'e'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(50, 250, 150, 350, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'f'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(250, 250, 350, 350, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'g'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(450, 250, 550, 350, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'h'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(650, 250, 750, 350, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'i'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(50, 450, 150, 550, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'j'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(250, 450, 350, 550, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'k'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(450, 450, 550, 550, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'l'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(650, 450, 750, 550, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'm'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(50, 650, 150, 750, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'n'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(250, 650, 350, 750, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'o'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(450, 650, 550, 750, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        if (camino[0] == 'p'):
            canv.delete("circulo1")
            canv.update()
            ball = canv.create_oval(650, 650, 750, 750, fill="#f4d03f", tags = "circulo1")
            canv.update()
            time.sleep(1.5)

        # CAMINO DEL JUGADOR SECUNDARIO
        if (camino[1] == 'a'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(50, 50, 150, 150, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'b'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(250, 50, 350, 150, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'c'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(450, 50, 550, 150, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'd'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(650, 50, 750, 150, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'e'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(50, 250, 150, 350, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'f'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(250, 250, 350, 350, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'g'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(450, 250, 550, 350, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'h'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(650, 250, 750, 350, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'i'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(50, 450, 150, 550, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'j'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(250, 450, 350, 550, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'k'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(450, 450, 550, 550, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'l'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(650, 450, 750, 550, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'm'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(50, 650, 150, 750, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'n'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(250, 650, 350, 750, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'o'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(450, 650, 550, 750, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        if (camino[1] == 'p'):
            canv.delete("circulo2")
            canv.update()
            ball = canv.create_oval(650, 650, 750, 750, fill="#2ecc71", tags = "circulo2")
            canv.update()
            time.sleep(1.5)

        canv.update()

print("-------RUTAS TERMINADAS-------")
canv.place(x=0, y=0)
ventana.mainloop()
