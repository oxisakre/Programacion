# Create tuple
fruits = ( 'Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apple',)

# Get value
print(fruits[1])

# Can't change value
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# Create set
fruits_set = {'Apples', 'Orange', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Add duplicate (don't add twice)
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

print(fruits_set)

def suma():
    y = 0
    for x in range(0, 100):
        y = y + x
    print(y)