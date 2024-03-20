
from multiprocessing.sharedctypes import Value
import random 


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
        sorteio_bola = 0 
        if sorteio_bola <= self._numBolas: 
            return random.randint(1, self._numBolas)
        else: return -1 
    
    def Sorteados(self): 
        

        




