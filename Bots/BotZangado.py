from Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao_zangado(self):
        print("Cleiton - Mensagem de apresentação: EAE SEU PAU NO CU, EU SOU O CLEITON")
 
    def mostra_comandos(self):
        print("1 - Bom dia")
        print("2 - Qual o seu nome?")
        print("3 - Quero um conselho")
        print("4 - Adeus")
    
    def executa_comando_zangado(self,cmd):
        if cmd == "1":
            print("Eu te respondo: BOM DIA PRA QUEM SEU MERDA?")
        elif cmd == "2":
            print(f"Eu te respondo: MEU NOME É {self.__nome}, SEU CABEÇA PIKA")
        elif cmd == "3":
            print("Eu te respondo: NÃO ME ENCHE O SACO E DE OUTROS Q TA SUAVE")
        elif cmd == "4":
            print("Eu te respondo: FALOU SEU MERDA, NÃO VOLTA MAIS TAMBÉM")

    def boas_vindas_zangado(self):
        print("Eu te respondo: Cleiton diz: PORRA NÃO ACREDITO Q TU ME ESCOLHEU")

    def despedida_zangado(self):
        print("Eu te respondo: FALOU SEU MERDA, NÃO VOLTA MAIS TAMBÉM")