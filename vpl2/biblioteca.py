from livro import Livro


class Biblioteca:
    def init(self):
        self.livros = []

    def incluirLivro(self, livro: Livro):
        self.livros.append(livro)

    def excluirLivro(self, livro: Livro):
        self.livros.remove(livro)

    @property
    def livros(self):
        return self.livros