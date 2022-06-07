def maximo():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    numbers = [a, b, c, d]
    max_product = -float("inf")
    
    
    for n in numbers:
        for n2 in numbers:
            if n == n2:
                continue
            res = n * n2 
            if res > max_product:
                max_product = res

    print(max_product)

maximo()




    


    