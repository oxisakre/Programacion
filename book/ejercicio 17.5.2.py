import random
def rat():
    minutes = 0
    ways = [1, 2, 3]

    while True:
        path = random.choice(ways)
        if path == 1:
            minutes += 3
            print('rat tried path 1')
        if path == 2:
            minutes += 5
            print('rat tried path 2')
        if path == 3:
            minutes += 7
            print('YAY path 3')
            print(f'time to scape: {minutes} minutes')
            return False


rat()