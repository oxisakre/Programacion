def favorito():
    numero = input('numero favorito? entre:[-50 y 50] ')
    
    
    
    while not numero.isdigit() or int(numero) < -50 or int(numero) > 50:
         print('un numero entre -50 y 50 y sin comas, puto')
         numero = input('numero favorito? entre:[-50 y 50] ')
    else:
        print('tu numero es:', numero)


favorito()