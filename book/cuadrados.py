def imprimir_cuadrados():
    print("Se calcularán cuadrados de números")
    
    n1 = int(input("Ingrese un número entero: "))
    print("el valor de n1 es:", n1)
    n2 = int(input("Ingrese otro número entero: "))
    print("el valor de n2 es:", n2)
    
    for x in range(n1, n2):
        print("el valor de x es:", x)
        print(x * x)
    
    print("Es todo por ahora")

imprimir_cuadrados()