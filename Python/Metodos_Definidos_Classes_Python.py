
class Conta(object):

    def __init__(self, conta):

        self.__conta = conta
        self.__saldo = 1000

    def Deposito(self, valor):

        self.__saldo += valor
        #print("Saldo da conta: %.2f" % (self.__saldo))

    def Saque(self, valor):

        self.__saldo -= self.__saldo
        #print("Saldo da conta: %.2f" % (self.__saldo))

    def Extrato(self):

        print("Saldo da conta: %.2f" % (self.__saldo))

    def __str__(self):

        return "Esta classe define uma conta para o cliente."
