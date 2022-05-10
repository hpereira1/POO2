class Editora:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome
        
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        
    codigo = property(get_codigo, set_codigo)
    nome = property(get_nome, set_nome)