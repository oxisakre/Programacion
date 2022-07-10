def ChangeEnough(list, money):

    if (list[0] * 0.25) + (list[1] * 0.10) + (list[2] * 0.05) + (list[3] * 0.01) == money:
        return True
    else:
        return False
