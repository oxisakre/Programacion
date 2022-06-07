import random 
from itertools import product
from collections import Counter

def jesus():
        baraja = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        cartas = ('♦', '♥', '♠', '♣')
        resultado = []
        cantidad = 0
        contador = 0
        ganador = []
        while cantidad != 4:
                
                for i in range(5):
                        elegir = random.choice(baraja) 
                        simbolo = random.choice(cartas)
                        resultado.append(elegir)
                        ganador.append(elegir)
                        ganador.append(simbolo)
                        
                        print(elegir, end='')
                        print(str(simbolo), end=' ')
                print(' ')                
                
                poker = Counter(resultado)
                contar = (poker.most_common(1))
                cantidad = contar[0][1]
                
                if cantidad == 4:
                        print('', end='')
                        print(f'cantidad de intentos: {contador}')
                        ganador = ''.join(str(ganador).split(','))
                        ganador = ''.join(str(ganador).split(' '))
                        
                        return print(f'{ganador}<--- Poker!!!')

                else:
                        resultado = []
                        ganador = []
                        contador +=1
                
                        
        
jesus()