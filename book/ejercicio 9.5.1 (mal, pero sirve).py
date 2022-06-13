import random
from collections import Counter
def cantidad():
    frase = ('hola', 'que', 'linda', 'mañana', 'eh')
    p_cadena = []
    
    for i in range(5):
        elegir = random.choice(frase)
        p_cadena.append(elegir)
    
    l_cadena = str(p_cadena)
    l_cadena = l_cadena.replace(',', ' ')
    l_cadena = l_cadena.replace(']', '')
    l_cadena = l_cadena.replace('[', '')
    l_cadena = l_cadena.replace("'", '')
    palabras = dict(Counter(p_cadena))
    letras = dict(Counter(l_cadena))
   
    print('frase:', str(l_cadena))
    print('letras:', letras)
    print('palabras:', palabras)
    
    
cantidad()