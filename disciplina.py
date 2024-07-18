class Disciplina:
    def __init__(self, nome, semestre, media, ch):
        self.__nome = nome
        self.__semestre = semestre
        self.__media = media
        self.__ch = ch
        self.__aprovado = media >= 60
    def get_semestre(self):
        return self.__semestre  
    def get_media(self):
        return self.__media        
    def __str__(self):
        if self.__aprovado:
            return f"{self.__nome}-{self.__semestre}-{self.__media}-{self.__ch} - aprovado"
        else:    
            return f"{self.__nome}-{self.__semestre}-{self.__media}-{self.__ch} - reprovado"

class Historico:
    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []
    def inserir(self, disc):
        self.__disciplinas.append(disc)
    def listar(self):
        return self.__disciplinas
    def listar_semestre(self, semestre):
        x = []
        for disc in self.__disciplinas:
            if disc.get_semestre() == semestre:
                x.append(disc)
        return x        
    def IRA(self):
        if len(self.__disciplinas) == 0: return 0
        soma = 0
        for disc in self.__disciplinas:
            soma += disc.get_media()
        return soma / len(self.__disciplinas)
    def carga_horaria(self):
        disciplinas_aprovadas = [d for d in self.__disciplinas if d.media >= 60]
        return sum(d.ch for d in disciplinas_aprovadas)
    def __str__(self):
        return f"Aluno: {self.nome_aluno}, Disciplinas no histórico: {len(self.disciplinas)}"
        

class UI: 
    @staticmethod
    def main(): 

# Criando algumas disciplinas
        disciplina1 = Disciplina("Matemática", "2023.2", 7.5, 60, "Aprovado")
        disciplina2 = Disciplina("Física", "2023.2", 6.0, 45, "Aprovado")
        disciplina3 = Disciplina("Programação", "2023.1", 8.0, 75, "Aprovado")

        # Criando um histórico para um aluno
        historico_aluno = Historico("João")
        historico_aluno.inserir(disciplina1)
        historico_aluno.inserir(disciplina2)
        historico_aluno.inserir(disciplina3)

        # Testando os métodos do histórico
        print("Listagem de disciplinas:")
        for d in historico_aluno.listar():
            print(d)

        print("\nDisciplinas do semestre 2023.2:")
        for d in historico_aluno.listar_semestre("2023.2"):
            print(d)

        print("\nDisciplina(s) com maior média:")
        for d in historico_aluno.maior_media():
            print(d)

        print("\nIRA (média das médias das disciplinas aprovadas):", historico_aluno.ira())
        print("Total de CH (carga horária das disciplinas aprovadas):", historico_aluno.total_ch())

        print("\nInformações do histórico:")
        print(historico_aluno)

UI.main()