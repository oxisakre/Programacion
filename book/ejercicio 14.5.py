
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return str([self.x, self.y, self.z])

    def __add__(self, otro):
        if len(str(self)) == len(str(otro)):
            sumax = (self.x + otro.x)
            sumay = (self.y + otro.y)
            sumaz = (self.z + otro.z)
            return Vector(sumax, sumay, sumaz)
        else:
            return Exception('Vectores con diferente cantidad de elementos')

    def __mul__(self, numero):
        multix = self.x * numero
        multiy = self.y * numero
        multiz = self.z * numero
        return Vector(multix, multiy, multiz)

    def producto_interno(self, otro):
        prodx = self.x * otro.x
        prody = self.y * otro.y
        prodz = self.z * otro.z
        return prodx + prody + prodz

a = Vector(4, 6, 8)
b = Vector(2, 1, 5)
c = 4
print(a + b)
print(a.producto_interno(b))
print(a * c)

        