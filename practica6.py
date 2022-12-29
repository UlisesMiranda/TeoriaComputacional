import random

cadena = ''
entraCerradura = random.randint(0, 1)
print(entraCerradura)

if entraCerradura == 1:
    vecesCerradura = random.randint(1, 1000)
    
    for i in range(vecesCerradura):
        primerParte = random.randint(0, 1)
        if primerParte == 0:
            cadena += '0'
        else:
            cadena += '10'
        
segundaParte = random.randint(0, 1)
if segundaParte == 0:
    cadena += ''
else:
    cadena += '1'
        
        
print("Cadena generada: ", cadena)