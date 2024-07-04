
class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0.0

    def set_distancia(self, distancia):
        self.__distancia = distancia
        if distancia < 0: raise ValueError()
    def get_distancia(self):
        return self.__distancia 
    def set_tempo(self, tempo):
        self.__tempo = tempo
        if tempo <= 0: raise ValueError()
    def get_tempo(self):
        return self.__tempo 
    def velocidademedia(self):
        vm = self.__distancia / self.__tempo
        return f"A velocidade média é: {vm:2.2f}km/h"

class UI:
    @staticmethod
    def main(): 

        x = Viagem()
        x.set_distancia(float(input("Digite a distância em km: ")))
        x.set_tempo(float(input("Digite o tempo em horas: ")))
        print(x.velocidademedia())

UI.main()