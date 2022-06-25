from re import X


def potencia():
    x = int(input('x:'))
    b = int(input('b:'))
    cont = 0

    
    for i in range(0, 100):
            if x ** i == b:
                print("es potencia")
                print(f"{x} elevado a {i} es {b}")
                return
            if x ** i != b:
                cont +=1
                if cont == 100:
                    print("no es potencia")
                    return False
                    

potencia()