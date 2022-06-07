import random
from prettytable import PrettyTable
from datetime import datetime
class generala:


    def ___init__(self):
        dados = []
        contadorTiradas = 1
        opcionElegida = ""
        Numeros = [1, 2, 3, 4, 5, 6]

    def tirar_dados(self, dados):
        for i in range(5):
            dados.append(random.randint(1,6))
        return dados

    def elegirProcedimiento(self, idPuntaje,):
        disponibles = self.buscarPuntajeJugador(idPuntaje)
        print("\n--- Usted puede anotarse éstas categorías:\n--> "+disponibles)
        print("\nDesea tirar otra vez? Presione:\n- P para ver los resultados parciales.\n- V para volver a tirar todos los dados."
            "\n- E para elegir qué dados tirar.\n- T para terminar y quedarse con la tirada obtenida.\n")
        procedElegido = input("Por favor, ingrese su elección: ")
        global opcionElegida
        opcionElegida = procedElegido.upper()
        return procedElegido.upper()

    def tirarTodoNuevo(self, dados):
        global contadorTiradas
        contadorTiradas = contadorTiradas + 1
        print("\n*** La tirada número",contadorTiradas,"obtuvo los siguientes dados:")
        dados.clear()
        return self.tirar_dados(dados)

    def 

        if ( Lista_dados == [1, 2, 3, 4, 5] ) or ( Lista_dados == [ 2, 3, 4, 5,6] ) or ( Lista_dados == [1, 3, 4, 5, 6] ):
            escalera == 1
        
        table = PrettyTable(["Numeros", "Puntos"])
        p = 0
        print(Lista_dados)
        
        for j in Numeros:
            table.add_row([Numeros[p], [p]])
            p += 1
            
        random.randint
        

        print(table)


generala()