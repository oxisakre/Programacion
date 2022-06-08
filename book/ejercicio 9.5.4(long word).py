def jisus():
    print('buscador de palabra mas larga con su letra elegida')
    texto = input('escribi algo: ')
    letra = input('letra:')
    max_palabra = ''
    for i in texto.split():
        if letra in i:
            palabra = i
            if len(palabra) > len(max_palabra):
                max_palabra = palabra

    print(max_palabra)
        
    


jisus()