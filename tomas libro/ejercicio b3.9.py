import math
def maximo():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    numbers = [a, b, c, d]
    
    numbers.sort()
    res = max(str(a * b * c * d))

    print(res)

maximo()