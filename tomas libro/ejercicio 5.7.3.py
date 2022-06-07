import time
def contra():
    count = 0

    while count < 3:
        password = input('password: ')
        if password == 'perro':
            time.sleep(1)
            print(bool('entra tranqui pa'))
            break
        else:
            time.sleep(1)
            print(bool())
            count += 1
    
    
contra()