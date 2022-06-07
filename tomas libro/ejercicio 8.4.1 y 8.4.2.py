def parametral():
    lista = input('escriba una lista:').split()
    x = input('numero: ')
    cont = 0
    posicion = lista.index(x)
    maximo = max(lista)
    max_lista = lista.index(maximo)
    tupl_max = (maximo, max_lista)
    
    for i in lista:
        if i == x:
            cont +=1


    pos_lista = []
    for i in range(len(lista)):
        if lista[i] == x:
            pos_lista.append(i)
    
    print('posiciones de su numero:', pos_lista)
    print(f'valor maximo y posicion: {tupl_max}')
    print('numeor de veces en la lista:', cont)
    print('primera aparicion:', posicion)
    
    

parametral()