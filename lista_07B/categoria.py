class Categoria:
    def __init__(self):
        self.__id = 0
        self.__descricao = ""
    def setId(self, id):
        if type(id) == int:
            self.__id = id
        else: raise ValueError()
        
