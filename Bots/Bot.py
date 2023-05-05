from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.comandos = {}

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    def mostra_comandos(self):
        return("1 - Bom dia \n2 - Qual o seu nome? \n3 - Quero um conselho \n4 - Adeus")
    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
