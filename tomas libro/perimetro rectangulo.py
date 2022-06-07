def perimetro_rectangulo():
    a, b= input('Poner altura y base:').split()
    a = int(a)
    b = int(b)
    P = (a*2)+(b*2)
    print(P)

perimetro_rectangulo()