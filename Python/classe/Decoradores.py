class tracer:
    def __init__(self, umaclasse):
        print("O metodo construtor foi chamado!", umaclasse)
        self.umaclasse = umaclasse

    def __call__(self, *args):
        print("Chamei o metodo __call__", args)
        self.meu = self.umaclasse(*args)
        return self

    def __getattr__(self, str):
        print(self, str)
        return getattr(self.meu, str)


@tracer
class span:
    def spy(self):
        print()


sp = span()
sp.spy()
