def wc():
    lineas = 0
    palabras = 0
    letras = 0
    torta = 0
    archivo = open('testing.txt', 'r')

    for line in archivo:
            lineas +=1
            pala = line.split()
            palabras = palabras + len(pala)
            letras += sum(len(palabras) for palabras in pala)

    for i in archivo:
            caca = i.split()
            torta += i + len(caca)

    
    print(torta)
    
            
    
    print(lineas)
    print(palabras)
    print(letras)
    

wc()