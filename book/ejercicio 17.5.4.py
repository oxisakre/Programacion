def pascal(n, k):
    if k == 0 or k == n:
        return 1

    p = pascal(n-1, k-1)
    p2 = pascal(n-1,k)
    return p + p2 

print(pascal(5, 2))