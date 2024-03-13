class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    def set_base(self, v):
        if v>= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v 
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return f"\nO valor da área é: {((self.__b * self.__h) / 2)}"

class UI:
    @staticmethod
    def main():
        a = int(input("Digite o valor da base: "))        
        b = int(input("Digite o valor da altura: "))        
        x = Triangulo()
        x.set_base(a)
        x.set_altura(b)
        print(x.calc_area())

UI.main() 