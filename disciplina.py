class Disciplina:
    def __init__(self, nome, semestre, media, ch, aprovado):
        self.__nome = nome
        self.__semestre = semestre
        self.__media = media
        self.__ch = ch
        self.__aprovado = media >= 60

    def __str__(self):
        if self.__aprovado:
            return f"nome: {self.__nome}\n 
        semestre: {self.__semestre}\n media: {self.__media}\n  
        carga horária: {self.__ch}\n
        - aprovado."
           
        else: 
            self.__aprovado:
            return f"nome: {self.__nome}\n 
        semestre: {self.__semestre}\n media: {self.__media}\n  
        carga horária: {self.__ch}\n
        - reprovado."
           

        
    
    
class Historico:
    def __init__(self):
        self.__aluno = ""
        self.__disciplinas = Disciplina

    def Inserir(Disciplina): 




