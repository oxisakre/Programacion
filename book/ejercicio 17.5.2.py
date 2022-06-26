import random
def rat(w, minutes=0):
    if w == 1:
        
        print(1)
        return rat((random.randint(1, 3)), minutes + 5)
    if w == 2:
        
        print(2)
        return rat((random.randint(1, 3)), minutes + 3)
    if w == 3:
        minutes += 7
        return f"escapaste!, en {minutes} minutos"


print(rat(random.randint(1, 3)))