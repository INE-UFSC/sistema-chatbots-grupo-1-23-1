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
        return f"{self.__nome}- Mensagem de apresentação: EAE SEU PAU NO CU, EU SOU O {self.__nome}"
 
    def mostra_comandos(self):
        return("1 - Bom dia \n2 - Qual o seu nome? \n3 - Quero um conselho \n4 - Adeus")
    
    def executa_comando(self,cmd):
        if cmd == "1":
            return("Eu te respondo: BOM DIA PRA QUEM SEU MERDA?")
        elif cmd == "2":
            return(f"Eu te respondo: MEU NOME É {self.__nome}, SEU CABEÇA PIKA")
        elif cmd == "3":
            return("Eu te respondo: NÃO ME ENCHE O SACO E DE OUTROS Q TA SUAVE")
        elif cmd == "4":
            return("Eu te respondo: FALOU SEU MERDA, NÃO VOLTA MAIS TAMBÉM")

    def boas_vindas(self):
        return("Eu te respondo: Cleiton diz: PORRA NÃO ACREDITO Q TU ME ESCOLHEU")

    def despedida(self):
        return("Eu te respondo: FALOU SEU MERDA, NÃO VOLTA MAIS TAMBÉM")