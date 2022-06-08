def encontrar():
    lista = list(input('lista: ').split())
    print(lista)
    x = input('numero a buscar: ')
    

    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        print("izq:", izq, "der:", der, "medio:", medio)

        if lista[medio] == x:        
            return print('posicion de su valor:', medio)
        if lista[medio] > x:        
            der = medio - 1
        else:        
            izq = medio + 1        
        
    print('numero no encontrado')
    losto = []
    if izq >= der:
        lista.append(x)
    
    while lista:
        minimum = lista[0]  
        for i in lista: 
            if i < minimum:
                minimum = x
        losto.append(minimum)
        lista.remove(minimum)
    
    print('lista ordenada:', losto)
    
        
    
    
        
    
    




encontrar()
