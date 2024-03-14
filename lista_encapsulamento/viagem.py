from multiprocessing.sharedctypes import Value
35.7

class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0
    def set_distancia(self, v):       
        if v >= 0: self.__distancia = v
        else: raise ValueError()
    def set_tempo(self, v):       
        if v >= 0: self.__tempo = v
        else: raise ValueError()
    def get_distancia(self): 
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def vel_media(self): 
        return (f"A veolocidade média é: {self.__distancia/self.__tempo:.2f} km/h")
    
class UI: 
    @staticmethod 
    def main():
        input_distancia = float(input("Digite a quilometragem percorrrida: "))
        input_tempo = float(input("Digite o tempo gasto: "))
        main = Viagem()
        main.set_distancia(input_distancia)
        main.set_tempo(input_tempo)
        print(main.vel_media())

UI.main()

        


    