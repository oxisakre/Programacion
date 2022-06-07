import random

def numeral():
    print('BUUUUENNASSSS')
    codigo = ecodigo
    intentos = 1
    propuesta = input('numero de 4 digitos:')

    while propuesta != codigo:
        intentos += 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print(f'tu numero {propuesta} ',f'tiene {aciertos} aciertos ',f'y {coincidencias} coincidencias')
        propuesta = input('otro numero papi: ')


def ecodigo():
    numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    codigo = ''

    for i in range(4):
        ganador = random.choice(numeros)
        while ganador in codigo:
            ganador = random.choice(numeros)
        codigo = codigo + ganador
    return codigo

def analizar_propuesta(propuesta, codigo):
    aciertos = 0
    coincidencias = 0
    
    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    return aciertos, coincidencias

numeral()
    