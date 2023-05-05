from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao(self):
        return f"{self.__nome}- Mensagem de apresentação: EAE SEU VERME, EU SOU O {self.__nome}"
 

    
    def executa_comando(self,cmd):
        if cmd == "1":
            return("Eu te respondo: BOM DIA PRA QUEM SEU ENERGUMENO?")
        elif cmd == "2":
            return(f"Eu te respondo: MEU NOME É {self.__nome}, SEU CABEÇA DE TABACO")
        elif cmd == "3":
            return("Eu te respondo: NÃO ME ENCHE O SACO E O DE OUTROS Q TA SUAVE")
        elif cmd == "4":
            return("Eu te respondo: FALOU SEU IDIOTA, NÃO VOLTA MAIS TAMBÉM")

    def boas_vindas(self):
        return(f"Eu te respondo: {self.__nome} diz: PORRA! NÃO ACREDITO Q TU ME ESCOLHEU")

    def despedida(self):
        return("Eu te respondo: FALOU SEU IDIOTA, NÃO VOLTA MAIS TAMBÉM")