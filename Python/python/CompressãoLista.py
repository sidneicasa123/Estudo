#lista = [x for x in range(21) if x % 2 == 0]
# print(lista)

#lista = [x for x in open(r"C:\Users\sid-j\OneDrive\Documentos\Estudos\Python\Arquivo.csv")]
# print(lista)


#lista = [x+y+z for x in "ABC" for y in "DEF" for z in "GHI"]
# print(lista)


dicionario = [x for x in [1-10]]
print(list(dicionario))


l1 = [10, 20, 30, 40, 50]
l2 = ["Item1", "Item2", "Item3", "Item4", "Item5"]

zipado = zip(l1, l2)

print(dict(zipado))


def soma(x, y):
    return x * y


li = map(soma, range(10), range(10))
l = list(li)
print(l)


def taboada(x, y):
    return x * y


i = [taboada(x, y) for x in range(11) for y in range(11)]
print(i)
