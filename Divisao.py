from OperacaoMatematica import Opmm


class Dividir(Opmm):

    def op(self, n1, n2):
        soma = n1 / n2
        print(f"R: {soma}")