from Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao_feliz(self):
        print("Jorge - Mensagem de apresentação: Bom dia meu raio de sol XD")
 
    def mostra_comandos(self):
        print("1 - Bom dia")
        print("2 - Qual o seu nome?")
        print("3 - Quero um conselho")
        print("4 - Adeus")
    
    def executa_comando_feliz(self,cmd):
        if cmd == "1":
            print("Eu te respondo: BOM DIA MEU CONSAGRADO!! XD")
        elif cmd == "2":
            print(f"Eu te respondo: MEU NOME É {self.__nome}, BONITO NÃO? XD")
        elif cmd == "3":
            print("Eu te respondo: VIVA UM DIA DE CADA VEZ, A VIDA É BELA, CARPE DIEM!!! XD")
        elif cmd == "4":
            print("Eu te respondo: ADEUS MEU REI, TENHA UM ÓTIMO DIA, ATÉ UMA PŔOXIMA!! XD")

    def boas_vindas_feliz(self):
        print("Eu te respondo: Jorge diz: UHUUUUL, VOCÊ ME ESCOLHEU!!! XD")

    def despedida_feliz(self):
        print(f"Eu te respondo: ADEUS MEU REI, TENHA UM ÓTIMO DIA, ATÉ UMA PŔOXIMA!! XD")
