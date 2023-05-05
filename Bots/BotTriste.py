from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao(self):
        return (f"{self.__nome}- Mensagem de apresentação: A cada dia a morte se aproxima...Bom dia.")



    def executa_comando(self, cmd):
        if cmd == "1":
            return ("Eu te respondo: Mais um dia de tristeza, bom dia.")
        elif cmd == "2":
            return (f"Eu te respondo: Meu nome é {self.__nome}, apesar de niguem se importa com isso")
        elif cmd == "3":
            return ("Eu te respondo: Apenas fique no seu quarto chorando.")
        elif cmd == "4":
            return ("Eu te respondo: Adeus...*sniff*.")

    def boas_vindas(self):
        return (f"Eu te respondo: {self.__nome} diz: Espero que você nao me abandone")

    def despedida(self):
        return ("Eu te respondo: Adeus...*sniff*.")