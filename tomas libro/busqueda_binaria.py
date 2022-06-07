def busqueda_binaria():
    lista = list(input('lista: ').split())
    print(lista)
    x = input('numero a buscar:')
    

    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        print("[DEBUG]", "izq:", izq, "der:", der, "medio:", medio)

        if lista[medio] == x:
        # Encontramos el elemento; devolvemos su posición
            return print('posicion de su valor:', medio)
        if lista[medio] > x:
        # Seguimos buscando en el segmento de la izquierda
            der = medio - 1
        else:
        # Seguimos buscando en el segmento de la derecha
            izq = medio + 1        
        
    return print('numero no encontrado')

busqueda_binaria()