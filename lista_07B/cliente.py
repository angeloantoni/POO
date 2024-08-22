class Cliente:
    def __init__(self):
        self.__id = 0
        self.__nome = ""
        self.__email = "" 
        self.__fone = "" 

    def setId(self, id):
        if type(id) == int:
            self.__id = id
        else: raise ValueError()
    def getId(self):
        return self.__id
    
    def setNome(self, nome):
        if type(nome) == str:
            self.__nome = nome
        else: raise ValueError()
    def getNome(self):
        return self.__nome 
    
    def setEmail(self, email):
        if type(email) == str:
            self.__email = email
        else: raise ValueError()
    def getEmail(self):
        return self.__email

    def setFone(self, fone):
        if type(fone) == str:
            self.__fone = fone
        else: raise ValueError()
        
    def getFone(self):
        return self.__fone 
    
    def __str__(self):
        return f" Id: {self.__id}\n Nome: {self.__nome}\n E-mail: {self.__email}\n Fone: {self.__fone} "

'''
cliente1 = Cliente()

cliente1.setId(1)
cliente1.setEmail("teste@gmail.com")
cliente1.setFone("8488888")
cliente1.setNome("Angelo")


print(cliente1.__str__())

'''



