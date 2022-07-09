

import threading

class MinhaThread(threading.Thread):

    def __init__(self, id, contador, trava):
        self.id = id
        self.contador = contador
        self.trava = trava
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.contador):
            with self.trava:
             print("[%s] = %s" % (self.id, i))

            arq = open(r"C:\\teste\\arquivo{0}.txt".format(i), "w")
            for linha in open(r"C:\Users\sid-j\OneDrive\Documentos\Estudos\Python\Arquivo.csv"):
                arq.writelines(linha+"\n")
            arq.close()


travar = threading.Lock()
threads = []


for i in range(1):
    thread = MinhaThread(i, 10, travar)
    thread.start()
    threads.append(thread)


for i in threads:
    print("Executou todos as thread")
    i.join()

print("Fim")
