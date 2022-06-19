from math import factorial
import statistics
def jesus():
    lista = [3, 35, 37, 41, 7, 39, 45, 80, 67, 59, 61, 97, 19]
    sumatoria = sum(lista)
    print('la suma total: ', sumatoria)
    print('promedio:', float("{:.2f}".format(statistics.fmean(lista))))

    # el % es el resto de la devision, si hago 999/40 es 24, entonces 24*40 es 960, que 999-960 es 39, por ende el 999%40 es = 39
    print('estos numeros son primos:', end='')
    for n in lista:
            if n % 2 != 0 and n % 3 != 0 and n % 7 != 0 and n % 5 != 0 or n == 7 or n == 2 or n ==3:
                print(n, end=' ')

    
    print(' ')
    print('factorial de cada numero:')
    for n in lista:
        print(factorial(n), end=' ')



        

    


jesus()