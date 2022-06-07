def devolver():
    x = int(input('dar numero:'))
    
    if x % 2 == 0:
        print('Enhorabuena es par!')
    else:
        print('Es impar :/')
    
    print('digitos:', len(str(x)))

devolver() 


def divisible():
        x = int(input('divisible:'))
        
        while (x % 10 != 0):
            x -=1
        print(x)
        
divisible()


