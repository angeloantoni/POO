class Entrada: 
    def __init__(self):
        self.__dia = "dom"
        self.__horario = 0
    def set_dia(self, dia):
        dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
        if dia in dias: 
            self.__dia = dia
        else: 
            raise ValueError("Digite um dia existente")
    def get_dia(self): 
        return self.__dia 
    def set_horario(self, horario): 
        if horario >= 0 and horario <= 23:
            self.__horario = horario 
        else:
            raise ValueError("Digite um horário entre 0h e 23h")
    def get_horario(self):
        return self.__horario 
    def ValorEntrada(self): 
        valor_ingresso = 16.00
        dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
        if self.__dia == dias[1] or self.__dia == dias[2] or self.__dia == dias[4]:
            valor_ingresso = f"O valor do ingresso custa R${16.00:2.2f}"
        elif self.__dia == dias[3]: 
            valor_ingresso = f"O valor do ingresso custa R${8.00:2.2f}"
        else: 
            valor_ingresso = f"O valor do ingresso custa R${20.00:2.2f}" 
        if 17 <= self.__horario <= 23:
            valor_ingresso += valor_ingresso * 0.5
        else: 
            valor_ingresso = valor_ingresso
        return valor_ingresso

class UI:
    @staticmethod
    def main():

        x = Entrada()
        dia = str(input("Digite o dia de compra do ingresso: "))
        horario = float(input("Digite o horário de compra do ingresso: "))
        x.set_dia(dia)
        x.set_horario(horario)

        print(x.ValorEntrada())

UI.main()



        

        

