# create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use contructor
#person2 = dict(first_name= 'Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
print(people[1]['name'])
