"""


#1° Exemplo -- Neste caso o objeto de interação só pode ser percorrido uma única vez por que o própio objeto está sendo retornado

class Soma_Quatrado(object):
    def __init__(self,x,y): 
        self.inicio = x
        self.fim = y
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.inicio < self.fim:
            self.inicio += 1
            return self.inicio**2
        else:
            raise StopIteration


interavel = Soma_Quatrado(1,10)

#Estou passando o objeto para uma lista onde eu consigo interar nos valores quantas vezes eu quiser. já que a classe já foi interada e está vazia.
lista = list(interavel)

# neste caso o objeto já foi interado anteriormente.
for i in interavel:
    print(i)

#Posso realizar interações quantas vezes eu quiser por que os dados estão em uma lista.    
for i in lista:
    print(i)

"""




"""
2º Exemplo - Neste exemplo eu consigo intere quantas vezes eu quiser porque eu implementei o metodo Next 
em outro objeto, ou seja, ele esvazia o objeto "Soma_Quatrado_Next" 
e toda as vezes que o objeto "Soma_Quatrado" for chamado ele irá chamar 
novamente o objeto "Soma_Quatrado_Next" isto resolve o problema.
"""

"""

class Soma_Quatrado(object):
    def __init__(self, x, y):
        self.inicio = x
        self.fim = y

    def __iter__(self):
        return Soma_Quatrado_Next(self.inicio, self.fim)



class Soma_Quatrado_Next(object):
    def __init__(self, x, y):
        self.inicio = x
        self.fim = y

    def __next__(self):
        if self.inicio < self.fim:
            self.inicio += 1
            return self.inicio**2
        else:
            raise StopIteration
  

interavel = Soma_Quatrado(1, 10)

# neste caso o objeto já foi interado anteriormente.
for i in interavel:
    print(i)
    
print("\n")

for i in interavel:
    print(i)


"""



class Soma_Quatrado(object):
    def __init__(self, x, y):
        self.inicio = x
        self.fim = y

    def __iter__(self):
        for i in range(self.inicio+1, self.fim+1):
            yield i**2


interavel = Soma_Quatrado(1, 10)

dicionario = dict(enumerate(list(interavel)))

print(dicionario)

for i in interavel:
    print(i)


print("\n")


for i in interavel:
    print(i)


