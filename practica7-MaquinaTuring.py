import random
import re
import time
from tkinter import*


def maquina_turing(cinta):
    
    f = open('resultadosMaquinaTuring.txt', 'w')
    
    cinta = list(cinta)
    
    estado = 'q0'
    index = 0
    
    f.write(f"({str(estado)}, X, R): {str(cinta)}\n")
    
    while estado != "qf":
        if estado == 'q0':
            if index >= len(cinta):
                return False
            
            if cinta[index] == '0':
                cinta[index] = 'X'
                index += 1
                estado = 'q1'
                
                f.write(f"({str(estado)}, X, R): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index += 1
                estado = 'q3'
                
                f.write(f"({str(estado)}, Y, R): {str(cinta)}\n")
                
            else:
                return False
        elif estado == 'q1':
            
            if index >= len(cinta):
                return False
            
            if cinta[index] == '0':
                cinta[index] = '0'
                index += 1
                
                f.write(f"({str(estado)}, 0, R): {str(cinta)}\n")
                
            elif cinta[index] == '1':
                cinta[index] = 'Y'
                index -= 1
                estado = 'q2'
                
                f.write(f"({str(estado)}, Y, L): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index += 1
                
                f.write(f"({str(estado)}, Y, R): {str(cinta)}\n")
            else:
                return False
        elif estado == 'q2':
            
            if index >= len(cinta):
                return False
            
            if cinta[index] == '0':
                cinta[index] = '0'
                index -= 1
                
                f.write(f"({str(estado)}, 0, L): {str(cinta)}\n")
            elif cinta[index] == 'X':
                cinta[index] = 'X'
                index += 1
                estado = 'q0'
                
                f.write(f"({str(estado)}, X, R): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index -= 1
                
                f.write(f"({str(estado)}, Y, L): {str(cinta)}\n")
            else:
                return False
        elif estado == 'q3':
            if index >= len(cinta):
                estado = 'qf'
                
                f.write(f"({str(estado)}, B, R): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index += 1
                
                f.write(f"({str(estado)}, Y, R): {str(cinta)}\n")
            else:
                return False
    return True

def graficarMaquina():
    ventana = Tk()
    canvas = Canvas(ventana, width=600, height=600)
    canvas.pack()
    ventana.title("MAQUINA DE TURING")
    
    f = open('resultadosMaquinaTuring.txt', 'r')
    text = f.read()
    
    matchesCinta = re.findall(r'\[(.*?)\]', text)
    matchesRegla = re.findall(r'\((.*?)\)', text)
    matchesEstado = re.findall(r'q[0-9]+', text)
    
    canvas.create_rectangle(150, 100, 250, 200, fill="#f4d03f")

    for i, (matchCinta, matchEstado, matchRegla) in enumerate(zip(matchesCinta, matchesEstado, matchesRegla)):
        
        canvas.delete('estado')
        canvas.delete('cinta')
        canvas.update()
        
        canvas.create_text(200, 150, text=matchEstado, fill="white", font=("Arial", 15,"bold"), tags='estado')
        canvas.create_text(200, 250, text=matchCinta, fill="black", font=("Arial", 15,"bold"), tags='cinta')
        canvas.create_text(450, 25 + 20*i, text=matchRegla, fill="black", font=("Arial", 15,"bold"))
        
        canvas.update()
        time.sleep(2)
    
    print("Animacion terminada")
    canvas.place(x=0, y=0)
    ventana.mainloop()


# Creamos un menu para elejir el modo
print("Elija el modo:")
print("1. Automatico")
print("2. Manual")
opc = input("Inserte su opcion deseada: ")
entrada = ""

# Creamos una cadena aleatoria o le pedimos al usuario su cadena
if opc == '1':
    cantidadCeros = random.randint(1, 50)
    cantidadUnos = random.randint(1, 50)
    print("Cantidad ceros: ", cantidadCeros)
    print("Cantidad unos: ", cantidadUnos)
    
    for i in range(cantidadCeros):
        entrada += '0'
    for i in range(cantidadUnos):
        entrada += '1'
else:
    entrada = input("Inserte su cadena: ")

# Mostramos la cadena creada
print("Su entrada fue: ", entrada)

esValida = maquina_turing(entrada)

# Verificamos los resultados         
if esValida:
    print("Cadena aceptada")
else:
    print("No es valida")
    
if len(entrada) < 10:
    graficarMaquina()
 