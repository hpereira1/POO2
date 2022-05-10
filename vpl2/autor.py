class Autor:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome
        
        @property
        def nome(self):
            return self.__nome
        
        @property
        def codigo(self):
            return self.__codigo

        @nome.setter
        def nome(self,nome):
            self.__nome = nome

        @codigo.setter
        def codigo(self, codigo):
            self.__codigo = codigo
