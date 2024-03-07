class Conta_bancaria:
    def __unit__(self): 
        self.titular = "" 
        self.numero_conta = ""
        self.saldo = 0 

    def saque(self):
        opcao = float(input("Digite 0 para saque ou 1 para depósito\n"))
        if opcao == 0: 
            saque = float(input("Qual o valor que deseja sacar?\n"))
            self.saldo = self.saldo - saque
        else: 
            deposito = float(input("Qual o valor que deseja depositar?\n"))
            self.saldo = deposito + self.saldo
        
        return print("Seu saldo atual: R$", self.saldo)

angelo = Conta_bancaria() 

angelo.titular = "Angelo"
angelo.numero_conta = 123
angelo.saldo = 1000 

Conta_bancaria.saque(angelo) 

        
        
