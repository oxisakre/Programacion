def plata():
    c = input('cuanta plata bro?')
    x = input('cantidad de interes?')
    n = input('numero de anos?')
    c = int(c)
    x = int(x)
    n = int(n)
    i = c * ((1 + x/100)**n)
    i = int(i)
      
    print('monto final: ', i)

plata()