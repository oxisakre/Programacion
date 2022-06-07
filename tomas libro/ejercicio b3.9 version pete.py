from audioop import maxpp


def probar():
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        res1 = a*b
        res2 = a*c
        res3 = a*d
        res4 = b*c
        res5 = b*d
        res6 = c*d
         
        print(max(res1, res2, res3, res4, res5, res6))

probar()