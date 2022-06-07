import random
def numero():
    x = random.randrange(0, 100)
    count = 0
    print('adivinar numero entre 0 y 100')

    while count < 5:
        n = int(input('numero: '))
        if n > x:
            print('el numero es mas chico')
        if n < x:
            print('el numero es mas grande')
        if n == x:
            print('ATINASTE WEY')
            break

numero()