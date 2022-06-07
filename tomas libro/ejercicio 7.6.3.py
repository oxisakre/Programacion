def presidente():
    votantes = (('Pablo', 'Hombre'), ('Gerardo', 'Hombre'), ('Enrique', 'Mujer'))
    p = votantes[1]
    
    
    for n in votantes:
        if n <= p:
            print(f'estimado {n}, vote por mi')




presidente()