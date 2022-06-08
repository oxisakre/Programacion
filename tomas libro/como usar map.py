myList = ['1', '2', '3', '4']  # currently strings
myList
['1', '2', '3', '4']

map(int, myList)   # now ints
[1, 2, 3, 4]

map(float, myList)  # now floats
[1.0, 2.0, 3.0, 4.0]



def addToFive(x):
     return x + 5

l = [1,2,3,4,5]

map(addToFive, l)
[6, 7, 8, 9, 10]