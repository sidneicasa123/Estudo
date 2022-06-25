"""
class ErroValor(Exception):

    def __init__(self, valor):

        self.__numero = valor

    def __str__(self):

        return "O número %i está incorreto" % self.__numero


class Estudo_Excption(object):

    def __init__(self, valor):

        self.__Valor = valor

    def VerificaValor(self):

        if self.__Valor > 0:
            print(
                "Número digitado Corretamenta, ou seja, o número digitado é maior do que 0.")
        else:
            raise ErroValor(self.__Valor)
            print("Passou aqui!")


valor = int(input("Digite um número:"))

verifica = Estudo_Excption(valor)

verifica.VerificaValor()

"""


"""

def Funcao_com_Try_Exception():
    
    try:
        v = int(input("dite um numero:"))            
    except:
         print("Ops! Valor digitado não é um valor válido, por favor, digitar um valor númerico.")
            
        
        
        
Funcao_com_Try_Exception()
"""

"""

def Teste_Assert(x):
    assert x > 0, "O numero tem que ser maior que zero"
    return "Numero maior do que zero, correto!"

pega = Teste_Assert(1)

print(pega)

"""


def t():
    try:
        v = int('aa')

    except Exception as e:
        print(e.__class__)
        print(e.__doc__)


t()
