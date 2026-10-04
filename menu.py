from Divisao import Dividir
from Soma import Somar
from Multiplicacao import Multiplica
from Subtracao import Subtrai


class Menu:

    def mn(self):

        self.operacoes = {
            "soma": Somar,
            "subtracao": Subtrai,
            "multiplicacao": Multiplica,
            "divisao": Dividir
        }

        print("----- MENU -----")
        print("-----> Soma;")
        print("-----> Subtração;")
        print("-----> Multiplicação;")
        print("-----> Divisão.")

        scanner = input("Escreva sua Resposta: ")

        n1 = int(input("Primeiro numero: "))
        n2 = int(input("Segundo numero: "))

        if scanner in self.operacoes:

            classe = self.operacoes[scanner]
            operacao = classe()

            operacao.op(n1, n2)