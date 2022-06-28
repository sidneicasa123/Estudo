#carrega_arquivo = open(r"C:\Users\sid-j\OneDrive\Documentos\Estudos\Python\Arquivo.csv","w")

#total_linhas = 1
# while total_linhas <= 100000:

#   carrega_arquivo.writelines("Estou carregando a linha de número: %i no arquivo\n"%total_linhas)
#   total_linhas += 1
# carrega_arquivo.close()


# Duas maneira de realizar interação dentro de um arquivo com Python

# 1 opção
lendo_arquivo = open(
    r"C:\Users\sid-j\OneDrive\Documentos\Estudos\Python\Arquivo.csv", "r")
for linha in open(r"C:\Users\sid-j\OneDrive\Documentos\Estudos\Python\Arquivo.csv"):
    print(linha)


# 2 Opção
arquivo = open(
    r"C:\Users\sid-j\OneDrive\Documentos\Estudos\Python\Arquivo.csv")
arquivo = iter(arquivo)
while True:
    try:
        pega = next(arquivo)
        print(pega)
    except StopIteration:
        break
