import math
class Entrada_cinema:
    def __init__(self): 
        self.dia = ""
        self.horario = 0

    def entrada_inteira(self):
        valor_base = 0 
        if self.dia == "segunda" or self.dia == "terça" or self.dia == "quinta":
            valor_base = 16.0
            if self.horario >= 17 and self.horario <= 24:
                valor_base = (valor_base*0.5) + valor_base
        if self.dia == "quarta":
            valor_base = 8.0
        if self.dia == "sexta" or self.dia == "sábado" or self.dia == "domingo":
            valor_base = 20.0
            if self.horario >= 17 and self.horario <= 0:
                valor_base = (valor_base*0.5) + valor_base

        return valor_base 


cinemark = Entrada_cinema()

cinemark.dia = "quarta"
cinemark.horario = 17
print(Entrada_cinema.entrada_inteira(cinemark))

