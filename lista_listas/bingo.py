
from multiprocessing.sharedctypes import Value
import random 
from random import sample


class Bingo:
    def __init__(self):
        self._numBolas = 0
        self._bolas = 0

    def set_numBolas(self, numBolas):
        if numBolas >= 0: self._numBolas = numBolas
        else: raise ValueError("Digite um inteiro positivo") 

    def set_bolas(self, bolas):
        if bolas >= 0: self._bolas = bolas
        else: raise ValueError("Digite um inteiro positivo")
    
    def get_numBolas(self):
        return self._numBolas 
    
    def get_bolas(self):
        return self._bolas 
    
    def Proximo(self):
        sorteio_bola = []
        while len(sorteio_bola) < self._numBolas:
            numero = random.randint(1, self._numBolas)
            if numero not in sorteio_bola: 
                sorteio_bola.append(numero)
        return sorteio_bola


    def Sorteados(self):    
        self._lista = []
        for i in range(self._numBolas): 
            bola = self.Proximo()
            if bola not in self._lista:
                self._lista.append(bola)
        return self._lista
    
class Play:
    @staticmethod
    def main():
      num_bolas = int(input("Qual a quantidade de bolas a serem sorteadas? "))        
      play = Bingo()
      play.set_numBolas(num_bolas)
      print(play.Proximo())

Play.main()


        
        
        

        




