from random import randrange

class SorteioLoteria:
    def __init__(self, quantidade_numeros):
        if quantidade_numeros > 0:
            self.__quantidade_numeros = quantidade_numeros
        else: raise ValueError("valor inválido!")
        
    def get_quantidadeNumeros(self):
        return self.__quantidade_numeros
  
    def sorteio(self):
        numeros_sorteados = []

        for i in range(self.__quantidade_numeros):
            if i not in numeros_sorteados:
                numeros_sorteados.append(randrange(0, 60))
            

        return numeros_sorteados
    
class UI:
    @staticmethod
    def main():
        op = -1
        while(op != 0):
            op = int(input("Escolha o tipo de sorteio: \n 1 - Quadra\n 2 - Quina\n 3 - Sena\n 0 - Sair\n"))
            if op == 1:
                aposta = SorteioLoteria(4)
                print(aposta.sorteio())
                break
            elif op == 2:
                aposta = SorteioLoteria(5)
                print(aposta.sorteio())
                break
            elif op == 3:
                aposta = SorteioLoteria(6)
                print(aposta.sorteio())
                break

UI.main()
            