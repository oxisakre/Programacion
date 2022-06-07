from operator import length_hint
import sys
import numpy as np
def vectorial():
    vectora = float(input('vector 1: '))
    vectorb = float(input('vector 2: '))
    escalar = np.dot(vectora, vectorb)
    
    
    
    print('producto escalar: ', escalar)
        

    if abs(escalar/(len(str(vectora)) * len(str(vectorb)))) < sys.float_info.epsilon:
        print('es ortogonal')
    else:
        print('no es ortogonal')

    if abs(escalar/len(str(vectora)) * len(str(vectorb))) < -1 + sys.float_info.epsilon:
        print('son paralelos')
    else:
        print('no son paralelos')








vectorial()