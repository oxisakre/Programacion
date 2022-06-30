def MaxValue(array):
    if len(array) == 0:
        raise ValueError()
    elif len(array) == 1:
        return array[0]
    else:
        j = array[0]
        y = MaxValue(array[1:])
        if y >= j: 
            return y
        else:
            return j
   
    


print(MaxValue([1, 2, 3, 5, 7, 2, 8]))