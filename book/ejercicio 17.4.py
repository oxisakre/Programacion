def MaxValue(array):
    if len(array) == 0:
        return ValueError()
    elif len(array) == 1:
        return array[0]
    else:
        j = array[0]
        y = MaxValue(array[1:])
        return y if y >= j else j

   
    


print(MaxValue([1, 2, 3, 5, 7, 2, 8]))