class Livros:
    def __init__(self): 
        self._titulo = ""
        self._autor = ""
        self._editora = ""
        self._lancamento = 0000 
    def set_titulo(self, nome):
        self._titulo = nome
    def set_autor(self, nome):
        self._autor = nome
    def set_editora(self, nome):
        self._editora = nome
    def set_lancamento(self, ano):
        self._lancamento = ano 
    def get_titulo(self, nome):
        return self._titulo
    def get_autor(self, nome):
        return self._autor
    def get_editora(self, nome):
        return self._editora
    def get_lancamento(self, ano):
        return self._lancamento
    
class UI:
    @staticmethod
    def main():

        play = None 
        op = 0
        while op != 9: 
            op = UI.menu() 
            if op == 1:
                play = UI.cadastrar_livro() 
            if op == 2:
                play = UI.listar_livros() 

        

    def menu():
        print("1 - Cadastrar novo livro")
        print("2 - Listar livros")
        print("9 - Fim")
        return int(input("Opção: "))
        
    def cadastrar_livro():

        registrar_livros = Livros()
    
        input_titulo = input("Título do livro: ")
        registrar_livros.set_titulo(input_titulo)

        input_autor = input("Autor do livro: ")
        registrar_livros.set_autor(input_autor)
        
        input_editora = input("Editora do livro: ")
        registrar_livros.set_editora(input_editora)
       
        input_lancamento = input("Ano de lançamento: ")
        registrar_livros.set_lancamento(input_lancamento)


        




UI.main()