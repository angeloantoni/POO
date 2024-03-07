# Classe não guarda nenhuma informação -> Apenas é o modelo 
# Objeto guarda as informações

class Aluno:

    # Método especial usado para definir os atributos

    def __init__(self):
        self.nome = "" # Atributo
        self.matricula = "" # Atributo
    
    # Método da classe Aluno

    def ano_ingresso(self):
        ano_str = self.matricula[0:4]
        ano_int = int(ano_str)
        return ano_int 

# Programação estruturada
# Função -> operação não está dentro de um tipo de variável  

def func_ano_ingresso(aluno):
    ano_str = aluno.matricula[0:4]
    ano_int = int(ano_str)
    return ano_int 

a = Aluno() # __init__ é chamado de forma invisível
b = Aluno()
c = a
a.nome = "Mateus"
a.matricula = "20231014040001"

b.nome = "Zelia"
b.matricula = "20231014040002"

turma = [a, b, c]

for aluno in turma: 
    print(aluno.nome, aluno.matricula, aluno.ano_ingresso(), func_ano_ingresso(aluno))


