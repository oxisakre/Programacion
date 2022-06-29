def combinaciones(letras, k, palabra=""):
    if len(palabra) == k:
        print(palabra, end=' ')
        return
    for letra in letras:
        combinaciones(letras, k, palabra + letra)


combinaciones(('a', 'b', 'c'), 0)