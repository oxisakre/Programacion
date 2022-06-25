def recursiva():
    x = int(input('numerito:'))

    while x > 0:
        print('numero:', x, 'digitos:', len(str(x)))
        x -= 1
        

recursiva()
