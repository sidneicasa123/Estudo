

# ===================================================================================================================================

class Minha_Primeira_Classe():

    # Construtor
    def __init__(self, cao):

        self.cao = cao

    def cachorro(self):

        self.cao.late()


class Cachorro():

    # Construtor
    def __init__(self):
        self.Latir = "AuAuAuAuAuAuAuAu!!!!!"

    def late(self):
        print(self.Latir)


cao = Cachorro()
pessoa = Minha_Primeira_Classe(cao)
pessoa.cachorro()


# herança de classe.

class heranca(Minha_Primeira_Classe):
    def __init__(self, cao):
        super().__init__(cao)


heranca = heranca(cao)

heranca.cachorro()


# private

class privado(object):
    def __init__(self):
        self.__idade = 10

    def imprime(self):
        print(self.__idade)


pri = privado()

pri.imprime()
