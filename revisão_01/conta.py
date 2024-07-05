''' 
Questão 03: Uma Conta Bancária  

Atributos: nome do titular da conta; número da conta; saldo.
Métodos: operações de depósito e saque. 
Programa para testar a classe

'''

class Conta: 
    def __init__(self):
        self.__titular = ""
        self.__conta = ""
        self.__saldo = 0.0
    def set_titular(self, nome):
        self.__titular = nome 
    def get_titular(self):
        return self.__titular 
    def set_conta(self, conta):
        self.__conta = conta
    def get_conta(self):
        return self.__conta
    def set_saldo(self, saldo):
        self.__saldo = saldo 
    def get_saldo(self):
        return self.__saldo
    def operacoes(self):
        operacao = int(input("Digite a operação que deseja realizar: \n 0 - Depósito \n 1 - Saque \n"))
        if operacao == 0:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            self.__saldo += valor_deposito 
            print(f"Seu saldo atual é: R$ {self.__saldo}")
        elif operacao == 1: 
            valor_deposito = float(input("Digite o valor que deseja sacar: "))
            self.__saldo -= valor_deposito 
            print(f"Seu saldo atual é: R$ {self.__saldo}")
        else: print("Operação inválida.")
    def __str__(self):
        print(f"Titular: {self.__titular}\n Número da conta: {self.__conta}\n Saldo: {self.__saldo}")

class UI:
    @staticmethod
    def main():

        x = Conta()
        x.set_titular(input("Digite o nome do titular da conta: "))
        x.set_conta(int(input("Digite o número da conta: ")))
        x.operacoes()


UI.main() 


     




