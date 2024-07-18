from datetime import date, datetime, timedelta

class Paciente:
    def __init__(self, nome, nascimento):
        if nome == "": raise ValueError("Nome informado é inválido")
        if nascimento > date.today().year - timedelta(days = 365): raise ValueError("Data pelo menos 1 ano")  
        self.__nome = nome
        self.__nascimento = nascimento 

    def Idade(self):
       dia_nascimento = self.__nascimento.day
       mes_nascimento = self.__nascimento.month
       ano_nascimento = self.__nascimento.year

       idade = date.today().year - ano_nascimento
       return idade  
    
#    def __str__(self):
#        return f("Nome: {}\n CPF: {}\n Telefone: {}\n")


