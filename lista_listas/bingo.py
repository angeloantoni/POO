
from multiprocessing.sharedctypes import Value
import random 
from random import sample


class Bingo:
    def __init__(self):
        self._numBolas = 0
        self._bolas = 0

    def set_numBolas(self, numBolas):
        if numBolas >= 0: self._numBolas = numBolas
        else: raise ValueError() 

    def set_bolas(self, bolas):
        if bolas >= 0: self._bolas = bolas
        else: raise ValueError()
    
    def get_numBolas(self):
        return self._numBolas 
    
    def get_bolas(self):
        return self._bolas 
    
    def Proximo(self):
        sorteio_bola = random.randint(1, self._numBolas)
        return sorteio_bola

    def Sorteados(self):    
        self._lista = []
        for i in range(self._numBolas): 
            bola = self.Proximo()
            if bola not in self._lista:
                self._lista.append(bola)
        return self._lista

    def Remove(self):
        while len(self._lista) < self._numBolas: 
            bola = self.Proximo()
            if bola not in self._lista:
                self._lista.append(bola)
        return self._lista

class Play:
    @staticmethod
    def main():        
      play = Bingo()
      play.set_numBolas(10)

      print(play.Sorteados())

Play.main()



        
        
        

        




