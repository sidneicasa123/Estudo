
def ListaSupermercado01():
    valor = 0
    lista = []

    def Ingredientes(itens):
        nonlocal lista, valor
        lista.append(itens)

        print(valor, lista[valor])

        valor = valor + 1

    return Ingredientes


pegaLista = ListaSupermercado01()

pegaLista("Arroz")
pegaLista("Feijão")
pegaLista("Farinha")
pegaLista("Laranja")
