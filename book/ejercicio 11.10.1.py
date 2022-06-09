from itertools import islice
def jesus():
    x = int(input('filas por leer: '))
    archivo = open('testing.txt', 'r+') 
    
    for leer in islice(archivo, 0, x):    
        print(leer, end='')

jesus()