import random
def rat(w):
    global minutes
    
    if w == 1:
        minutes = 5
        print(1)
        return rat(random.choice(tubos))
    if w == 2:
        print(2)
        return rat(random.choice(tubos))
    if w == 3:
        minutes =+ 7
        return f"escapaste!, en {minutes} minutos"

tubos = [1, 2, 3]
print(rat(random.choice(tubos)))