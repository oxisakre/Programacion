def binary():
    binario = input('numero binario: ')

    for i in binario:
        if i in '23456789':
           return print('no es binario')
            
            

    print(int(binario, base=2))

binary()