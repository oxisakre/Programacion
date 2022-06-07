def buscar_impar():
    x = int(input("trolo:"))
    
    #"""Divide el número recibido por 2 hasta que sea impar."""
    while x % 2 == 0:
        x //= 2
    if x % 2 != 0:
        print('es impar:', x)
    
    #"""Devuelve el menor factor primo del número x."""
    for n in range(2, x):
        if x % n == 0 and n % 2 != 0 and n % 3 != 0:
            return print('numero primo:', n)




buscar_impar()