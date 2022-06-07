def jesus():
    x = str(input())
    x_split = x.split()
    letras = [word[0] for word in x_split]
    
    print('primeras letras:', ''.join(letras))
    print(x.title())
    print(' '.join(word for word in x.split(' ') if word.startswith('a') or word.startswith('A')))

    
jesus()