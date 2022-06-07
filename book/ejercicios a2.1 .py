def jesus():
    a, b, c = input('ahora a b c:').split()
    a = float(a)
    b = float(b)
    c = float(c)
    print(((b * b) - (4 * a * c)) / (2 * a))
    print(((b * b) - (4 * a * c)) // (2 * a))
    print((b * b - 4 * a * c) / (2 * a))
    print(b * b - 4 * a * c / 2 * a)
    print((b * b) - (4 * a * c / 2 * a))
    print(1 / 2 * b)
    print(b / 2)

jesus()