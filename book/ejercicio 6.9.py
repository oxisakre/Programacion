def jesus():
    palabra = str(input('escribi pa: '))
    
    print('consonantes: ', end='')
    for c in palabra:
        if c not in 'AEIOUaeiou':
            print(c, end='')
        
    print(' ')
    print('vocales: ', end='')
    for d in palabra:
        if d in 'AEIOUaeiou':
            print(d, end='')

    print(' ')
    palabra2 = palabra.replace(' ', '')
    if palabra2 == palabra2[::-1]:
        print('es un palindromo!')
    if not palabra2 == palabra2[::-1]:
        print('no es palindromo')
       

jesus()