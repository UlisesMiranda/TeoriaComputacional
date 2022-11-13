
import genCadenasAleatoriasBin as gca
import peticionesServidor as server
import time;
import cv2
import numpy as np
import os


def main():
    
    mensajeFile = "./archivoMensaje.txt"
    encendido = server.isOn()
    
    if encendido:
            
        print("El servidor esta encendido")
        print("->Generando cadenas...")
        
        gca.genCadenasAleatoriasBin(64, 1000000, mensajeFile)
        
        print("Cadenas generadas")
        print("Enviando mensaje")
        print("En espera...")
        time.sleep(1)
        print("->Iniciando peticion")
        server.peticion(mensajeFile)
        print("-----Peticion terminada-----\n")
        main();
    else:
        print("El servidor está apagado")
        exit()
            
def dibujarGrafoAutomata():
 
    #Crea una imagen con tres canales [nofilas, columnas]
    img = np.ones((900,1000,3),np.uint8)
    #Establece un mismo color BRG para todos los píxeles de fondo
    img[:,:,:] = [78, 29, 40]

    #Tipo linea
    tipolinea = cv2.LINE_4

    radio = 50
    color = (255, 255, 255)
    grosor = 2
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.circle(img, (300, 200), radio, color, grosor, tipolinea )
    cv2.circle (img, (700, 200), radio, color, grosor, tipolinea)
    cv2.circle (img, (500, 300), radio, color, grosor, tipolinea)
    
    cv2.circle(img, (400, 500), radio, color, grosor, tipolinea )
    cv2.circle(img, (400, 500), 40, color, grosor, tipolinea )
    
    cv2.circle (img, (600, 500), radio, color, grosor, tipolinea)
    cv2.circle (img, (600, 700), radio, color, grosor, tipolinea)
    cv2.circle (img, (400, 700), radio, color, grosor, tipolinea)
    
    cv2.arrowedLine(img, (100, 330), (250, 200), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (350, 200), (650, 200), (255, 255, 255), 1, tipolinea)
    cv2.line(img, (750, 200), (800, 100), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (800, 100), (700, 150), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (700, 250), (550, 300), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (450, 300), (300, 250), (255, 255, 255), 1, tipolinea)
    
    
    #Automata paridad
    cv2.line(img, (450, 500), (500, 450), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (500, 450), (550, 480), (255, 255, 255), 1, tipolinea,  0, 0.3)
    cv2.line(img, (550, 500), (500, 550), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (500, 550), (450, 520), (255, 255, 255), 1, tipolinea,  0, 0.3)
    
    cv2.line(img, (600, 550), (650, 600), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (650, 600), (620, 650), (255, 255, 255), 1, tipolinea,  0, 0.3)
    cv2.line(img, (600, 650), (550, 600), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (550, 600), (570, 550), (255, 255, 255), 1, tipolinea,  0, 0.3)
    
    cv2.line(img, (550, 700), (500, 650), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (500, 650), (450, 680), (255, 255, 255), 1, tipolinea,  0, 0.3)
    cv2.line(img, (450, 700), (500, 750), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (500, 750), (550, 720), (255, 255, 255), 1, tipolinea,  0, 0.3)
    
    cv2.line(img, (400, 650), (450, 600), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (450, 600), (420, 550), (255, 255, 255), 1, tipolinea,  0, 0.3)
    cv2.line(img, (400, 550), (350, 600), (255, 255, 255), 1, tipolinea)
    cv2.arrowedLine(img, (350, 600), (380, 650), (255, 255, 255), 1, tipolinea,  0, 0.3)
    
    
    cv2.arrowedLine(img, (500, 350), (400, 450), (255, 255, 255), 1, tipolinea)    
    
    cv2.putText(img, "Start", (50, 350), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "Ready", (260, 200), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "Sending", (650, 200), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "paridad", (450, 300), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "timeout", (800, 100), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "data in", (470, 150), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.putText(img, "q0", (380, 500), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "q1", (580, 500), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "q2", (580, 700), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "q3", (380, 700), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.putText(img, "0", (530, 600), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "0", (660, 600), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "0", (320, 600), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "0", (460, 600), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "1", (490, 430), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "1", (490, 580), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "1", (490, 640), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "1", (490, 780), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imwrite("img.png",img)
    #Mostrar imagen
    cv2.imshow('polylineas',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if 'archivoMensaje.txt' in os.listdir('.'):
    os.remove('./archivoMensaje.txt')
if 'cadenasGeneradasAcumuladas.txt' in os.listdir('.'):
    os.remove('./cadenasGeneradasAcumuladas.txt')
if 'cadenasAceptadas.txt' in os.listdir('.'):
    os.remove('./cadenasAceptadas.txt')
if 'cadenasRechazadas.txt' in os.listdir('.'):
    os.remove('./cadenasRechazadas.txt')   
    
dibujarGrafoAutomata();       
main(); 



        
        
        
     