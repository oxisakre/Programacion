class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def desplazar(self, dx, dy):
        """Desplaza el punto según dx y dy."""
        self.x += dx
        self.y += dy

        
class Rectangulo:
    "Representa un rectángulo en el plano"
    def __init__(self, noroeste, sudeste):
        """Crea un Rectangulo a partir de los Puntos correspondientes a las
        esquinas superior izquierda e inferior derecha"""
        self.noroeste = noroeste
        self.sudeste = sudeste
        

    def alto(self):
        return abs(self.noroeste.y - self.sudeste.y)

    def ancho(self):
        return abs(self.sudeste.x - self.noroeste.x)

    def central(self):
        return ((self.sudeste.x + self.noroeste.x)/2, (self.noroeste.y + self.sudeste.y)/2)

   

p1 = Rectangulo(Punto(2, 2), Punto(8, -2))
print(p1.central())


