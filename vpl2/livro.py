from webbrowser import get
from editora import Editora
from autor import Autor
from capitulo import Capitulo
lista_autor = []
lista_capitulo = []
class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__titulo = titulo
        self.__codigo = codigo
        self.__ano = ano
        self.__editora = editora
        self.__autor = autor
        self.__numeroCapitulo = numeroCapitulo
        self.__tituloCapitulo = tituloCapitulo
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo     
    
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano
    
    def get_editora(self):
        return self.__editora
    
    def set_editora(self, editora):
        self.__editora = editora
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_numeroCapitulo(self):
        return self.__numeroCapitulo

    def set_numeroCapitulo(self, numeroCapitulo):
        self.__numeroCapitulo = numeroCapitulo

    def get_tituloCapitulo(self):
        return self.__tituloCapitulo

    def set_tituloCapitulo(self, tituloCapitulo):
        self.__tituloCapitulo = tituloCapitulo

    titulo = property(get_titulo, set_titulo)
    codigo = property(get_codigo, set_codigo)
    editora = property(get_editora, set_editora)
    ano = property(get_ano, set_ano)
    autor = property(get_autor, set_autor)
    numeroCapitulo = property(get_numeroCapitulo, set_numeroCapitulo)
    tituloCapitulo = property(get_tituloCapitulo, set_tituloCapitulo)


    def incluirAutor(self, autor: Autor):
        codigo = int(input())
        nome = input()
        autor = Autor(codigo, nome)
        if autor not in lista_autor:
            lista_autor.append(autor)


    def excluirAutor(self, autor: Autor):
        if autor in lista_autor:
            lista_autor.remove(autor)


    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        numeroCapitulo = int(input())
        tituloCapitulo = input()
        capitulo = Capitulo(numeroCapitulo, tituloCapitulo)
        lista_capitulo.append(capitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        if tituloCapitulo in lista_capitulo:
            lista_capitulo.remove(tituloCapitulo)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        if tituloCapitulo in lista_capitulo:
            return tituloCapitulo
