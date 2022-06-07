name = 'Brand'
age = 37

# Concatenate 
print('Hello, my name is ' + name + ' and I am ' + str(age))

#String Formating

# Arguments by position

print('My name is {name} nad I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

#String Methods

s = 'helloworld'

# Capitalize String
print(s.capitalize())

# Capitalize String each word
print(s.title())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get lenght
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('d'))

# End switch
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# Add between characters
print('a'.join(s))