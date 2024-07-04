import math

class Circulo:
    def __init__(self):
        self.__raio = 0
    def set_raio(self, raio):
        self.__raio = raio 
        if raio < 0: raise ValueError()
    def get_raio(self):
        return self.__raio 
    def area(self):
         return math.pi * (self.__raio ** 2)
    def circun(self): 
        return 2 * math.pi * self.__raio 

    
class UI:
    @staticmethod
    def main(): 
        x = Circulo() 
        x.set_raio(float(input("Digite o valor do raio: ")))
        print(f"Área: {x.area():2.2f}")
        print(f"Circunferência: {x.circun():2.2f}")

UI.main()
  