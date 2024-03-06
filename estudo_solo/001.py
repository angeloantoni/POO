class Bola: 
    conta_bolas = 0
    forma = "redonda"

    def __init__(self, diametro):
        self.diametro = diametro 
        Bola.conta_bolas += 1


#Exemplo de plataforma de streaming 

    # atributos -> características do filme
    # métodos -> funções que o usuário pode fazer com o filme
    # instância -> cada um dos filmes vai ser uma instância da classe filme
    #filme = Filme()
    # filme.play 
    # filme.duracao 

    #Objeto é algo que encapsula. Ex: texto = "Meu nome é Ângelo" -> texto é um objeto da classe string
    #class String():
    #   def replace

class Filme():
    nome = "As tranças do rei careca"
    tempo = 90
    genero = "comédia"
    
