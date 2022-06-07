from tkinter.ttk import Separator


def jesus():
    cadena = 'separar'
    contador = 0
    
    print('agregar en la cadena:', ','.join(cadena))
    cadena = ','.join(cadena)
    for n in cadena:
        
        if n == ',':
            contador = contador + 1
    print('numero de comas ingresadas:', contador)


    cadena2 = 'mi archivo de texto.txt'
    contador2 = 0
    
    print('reemplazar caracter', cadena2.replace(' ', '_'))
    cadena2 = cadena2.replace(' ', '_')
    for j in cadena2:
        
        if j == '_':
            contador2 = contador2 + 1
    print('numero de modificaciones:', contador2)

    cadena3 = 'Su clave es: 8869'

    print('reemplazar numero:', cadena3.replace('8869', 'XXXX'))

    s = '2552552550'
    
    print('agregar en la cadena:', '.'.join(s[i:i+3] for i in range(0, len(s), 3)))


jesus()