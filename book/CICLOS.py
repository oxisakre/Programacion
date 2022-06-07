def definido():
    i = int(input("Cuantos numeros quiere procesar?: "))
    
    for j in range(0, i):
        x = int(input("Ingrese un numero: "))
        if x > 0:
            print("Numero positivo")
        elif x == 0:
            print("Igual a 0")
        else:
            print("Numero negativo")

definido()

def indefinido():
    x = int(input("trolo:"))

    while x % 3 != 0:
        x +=1
    if x % 3 == 0:
       print(x)

indefinido()

def interactivo():
    hay_mas_datos = "Si"
    while hay_mas_datos == "Si":
        x = int(input("Ingrese un numero: "))
    if x > 0:
        print("Numero positivo")
    elif x == 0:
        print("Igual a 0")
    else:
       print("Numero negativo")
    hay_mas_datos = input("Quiere seguir? <Si-No>: ")

interactivo()

def centinelas():
    centinela = input("Ingrese un numero (* para terminar): ")
    while centinela != "*":
        x = int(centinela)
    if x > 0:
        print("Numero positivo")
    elif x == 0:
        print("Igual a 0")
    else:
        print("Numero negativo")
    centinela = input("Ingrese un numero (* para terminar): ")

centinelas()