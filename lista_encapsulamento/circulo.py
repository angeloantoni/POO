import math

class Circulo: 
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, v):
        self.__raio = v
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        print(f"A área do círculo é: {(math.pi) * (self.__raio ** 2):.2f}")
    def calc_circuferencia(self):
        print(f"A circunferência do círculo é: {(2 * math.pi * self.__raio):.2f}")

class UI:
    @staticmethod
    def main():
        a = float(input("Digite o valor do raio: "))
        x = Circulo()
        x.set_raio(a)
        x.calc_area()
        x.calc_circuferencia()

UI.main()



