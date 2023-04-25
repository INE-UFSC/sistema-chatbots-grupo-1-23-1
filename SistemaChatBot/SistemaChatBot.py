from ..Bots.BotZangado import BotZangado
from ..Bots.BotFeliz import BotFeliz

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = lista_bots
        self.__bot = None

    def boas_vindas(self):
        print("Olá, este é o sistema de chatbots do Grupo 1 :D")

    def mostra_menu(self):
        print("Os chats disponíveis no momento são:")
        for i in range(len(self.__lista_bots)):
            print(f"{i} - {self.__lista_bots[i].apresentacao()}")

    def escolhe_bot(self):
        num_bot = int(input("Digite o número do chatbot desejado: "))
        if num_bot >= 0 and num_bot < len(self.__lista_bots):
            self.__bot = self.__lista_bots[num_bot]
            print(f"Você escolheu o chatbot {self.__bot.nome}")
            self.__bot.boas_vindas()
        else:
            print("Opção inválida")

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        cmd = input("Digite o comando desejado: ")
        self.__bot.executa_comando(cmd)

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()

        while True:
            self.mostra_comandos_bot()
            self.le_envia_comando()
            if self.__bot.termina_conversa:
                break

        self.__bot.despedida()
