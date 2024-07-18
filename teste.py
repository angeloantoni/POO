from datetime import datetime
from datetime import date


nascimento = datetime.strptime("19/02/2001", "%d/%m/%Y")

dia_nascimento = nascimento.day
mes_nascimento = nascimento.month
ano_nascimento = nascimento.year

idade = date.today().year - ano_nascimento 

print(idade)




