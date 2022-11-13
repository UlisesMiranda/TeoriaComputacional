estado = 0
def estadoQ0 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 1
    if(entrada == 1):
        estado = 3
def estadoQ1 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 0
    if(entrada == 1):
        estado = 2
def estadoQ2 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 3
    if(entrada == 1):
        estado = 1
def estadoQ3 (entrada) :
    global estado
    
    if(entrada == 0):
        estado = 2
    if(entrada == 1):
        estado = 0
        
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
    global estado
    estado = 0
    for letter in cadena:
        maquinaEstadosFinitos(int(letter))
        
    return estado == 0;


    
    