
class TorreDeControl:

    def __init__(self):
        self.initial = None
        self.final = None
        self.arribos = []
        self.partidas = []


    def nuevo_arribo(self, element):
        self.arribos.append(element)
        self.initial = element
    
    def nueva_partida(self, element):
        self.final = element
        self.partidas.append(element)
    
    def estado_pista(self):
        partidas = ','.join(str(v) for v in self.partidas)
        arribos = ','.join(str(i) for i in self.arribos)
        return f"vuelos por despegar: {partidas} \nvuelos por aterrizar: {arribos}"

    def asignar_pista(self):
        if len(self.arribos) != 0:
            print(f"el vuelo {self.arribos[0]} aterrizo con exito.")
            self.arribos.pop(0)
            if len(self.arribos) != 0: 
                self.initial = self.arribos[0]
            else:
                self.initial = None
                return

        if len(self.arribos) == 0 and len(self.partidas) > 0:
            print(f"el vuelo {self.partidas[0]} despego con exito.")
            self.partidas.pop(0)
            if len(self.partidas) != 0:
                self.final = self.partidas[0]
            else:
                self.final = None
            



milista = TorreDeControl()
milista.nueva_partida("AR123")
milista.nueva_partida("IB56")
milista.nuevo_arribo("NEW98")
milista.nueva_partida("AE63")
milista.nuevo_arribo("GRE20")
print(milista.estado_pista())
milista.asignar_pista()
print(milista.estado_pista())
milista.asignar_pista()
print(milista.estado_pista())
milista.asignar_pista()
print(milista.estado_pista())
milista.asignar_pista()
print(milista.estado_pista())
milista.asignar_pista()
print(milista.estado_pista())