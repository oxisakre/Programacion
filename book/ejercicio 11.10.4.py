def grep():
    archivo = open('testing.txt', 'r')
    frase = 'todo'
    

    for line in archivo:
        pala = line.split()
        if frase in pala:
            print(pala)


grep()