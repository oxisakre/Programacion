def cp():
    with open('testing.txt', 'r') as archivo1, open('copia.txt', 'a') as archivo2:

        for line in archivo1:
            archivo2.write(line)

    
cp()