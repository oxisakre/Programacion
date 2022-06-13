
from math import gcd


class Fraccion():

    def __init__(self, dividendo, divisor):
        self.endo = dividendo
        self.isor = divisor

    def __str__(self) -> str:
        return str(f"{self.endo}/{self.isor}")

    def __add__(self, otra):
        sumaendo = (self.endo*otra.isor)  + (otra.endo*self.isor)
        sumaisor = (self.isor * otra.isor) // gcd(self.isor,otra.isor)

        return Fraccion(sumaendo, sumaisor)        

    def __mul__(self, otra):
        proendo = self.endo * otra.endo
        proisor = self.isor * otra.isor

        return Fraccion(proendo, proisor)

a = Fraccion(2, 5)
b = Fraccion(7, 2)
print(a + b)

        









