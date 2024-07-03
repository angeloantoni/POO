import math

class Circulo:
    def __init__(self):
        self.raio = 0
    def calc_area(self):
        return math.pi * (self.raio ** 2)
    def calc_circu(self): 
        return 2 * math.pi * self.raio
    

x = Circulo()
x.raio = 2

print(f"{x.calc_area():2f}")
print(f"{x.calc_circu():2f}")
    