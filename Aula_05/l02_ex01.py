import math

class Circulo:
    def __init__(self):
        self._raio = 0

    def raio(self):
        return self._raio
    
    def setRaio(self, novo_raio):
        self._raio = novo_raio

    def calc_area(self):
        area = math.pi * (self._raio ** 2)
        return area 
    
    def calc_circ(self):
        C = 2 * math.pi * self._raio
        return C

        
a = Circulo() 
a.setRaio(10)

print("Área:", a.calc_area())
print("Circunferência:", a.calc_circ())