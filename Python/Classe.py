class Minha_Primeira_Classe():

    # Construtor
    def __init__(self):
        self.Nome = "Sidnei Lima Santos"
        self.Idade = 39
        self.Sexo = "Masculino"
        self.Estado_Civil = "Casado"

    # Mettodos
    def Imprime_Pessoa(self):

        print(self.Nome, "\n", self.Idade, "\n",
              self.Sexo, "\n", self.Estado_Civil)


pessoa = Minha_Primeira_Classe()

pessoa.Imprime_Pessoa()
