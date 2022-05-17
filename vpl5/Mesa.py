from AbstractMesa import *


class Mesa(AbstractMesa):
    def __init__(self, jogador1: Jogador, jogador2: Jogador, cartaJogador1: Carta, cartaJogador2: Carta):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__cartaJogador1 = cartajogador1
        self.__cartaJogador2 = cartajogador2

    def get_jogador1(self):
        return self.__jogador1 
    def set_jogador1(self, jogador1):
        self.__jogador1 = jogador1

    def get_jogador2(self):
        return self.__jogador2 
    def set_jogador2(self, jogador2):
        self.__jogador2 = jogador2

    def get_cartaJogador1(self):
        return self.__cartaJogador1 
    def set_cartaJogador1(self, cartaJogador1):
        self.__cartaJogador1 = cartaJogador1

    def get_cartaJogador2(self):
        return self.__cartaJogador2
    def set_cartaJogador2(self, cartaJogador2):
        self.__cartaJogador2 = cartaJogador2
