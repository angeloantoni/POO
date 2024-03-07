import math

class Circulo():
   
    def __init__(self):
        self.raio = 0
        
    def area(self):
        area_circ = ((self.raio)**2) * math.pi 
        return area_circ 
    
    def circunferencia(self):
        circ = (math.pi * self.area()) * 2 
        return circ  


 
a = Circulo()

a.raio = 2 
    


print(a.raio)
print(Circulo.area(a))
print(Circulo.circunferencia(a))


