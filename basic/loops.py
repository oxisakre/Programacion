people = ['John', 'Paul', 'Sara', 'Susan']

# simple for loop
for person in people:
    print(f'Current Person: {person}')

# break
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

# continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

###
count = 0
while count <= 10:
    print(f'count: {count}')
    count +=1