estado = 0
def estadoQ0 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 1
        print("Movimiento de q0 a q1")
    if(entrada == 1):
        estado = 3
        print("Movimiento de q0 a q3")
def estadoQ1 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 0
        print("Movimiento de q1 a q0")
    if(entrada == 1):
        estado = 2
        print("Movimiento de q1 a q2")
def estadoQ2 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 3
        print("Movimiento de q2 a q3")
    if(entrada == 1):
        estado = 1
        print("Movimiento de q2 a q1")
def estadoQ3 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 2
        print("Movimiento de q3 a q2")
    if(entrada == 1):
        estado = 0
        print("Movimiento de q4 a q0")
        
def maquinaEstadosFinitos(entrada):
    global estado;
    switch = {
        0 :estadoQ0,
        1 :estadoQ1,
        2 :estadoQ2,
        3 :estadoQ3,
    }
    func = switch.get(estado, lambda: None)
    return func(entrada) 

def automata1s0spares(cadena):
    estado = 0;
    
    for letter in cadena:
        maquinaEstadosFinitos(int(letter))

    if(estado == 0): 
        print("Es cadena valida")
        return True;
    else:
        print("No es valida")
        return False;
    
automata1s0spares("0011");
    