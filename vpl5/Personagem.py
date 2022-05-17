from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    def __init__(self, energia: int, habilidade: int, velocidade: int, resistencia: int, tipo: Tipo):
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia
        self.__tipo = tipo

    def get_energia(self):
        return self.__energia
    def set_energia(self, energia):
        self.__titulo = energia   
 
    def get_habilidade(self):
        return self.__habilidade
    def set_habilidade(self, habilidade):
        self.__habilidade = habilidade   

    def get_velocidade(self):
        return self.__velocidade
    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade   

    def get_resistencia(self):
        return self.__resistencia
    def set_resistencia(self, resistencia):
        self.__resistencia = resistencia   
 
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, tipo):
        self.__tipo = tipo  

    energia = property(get_energia, set_energia)
    habilidade = property(get_habilidade, set_habilidade)
    velocidade = property(get_velocidade, set_velocidade)
    resistencia = property(get_resistencia, set_resistencia)
    tipo = property(get_tipo, set_tipo)