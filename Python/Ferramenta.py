from psutil import OPENBSD
from classe.teste import *

import os as s
import sys


for (nome, sub, arq) in s.walk("."):
    print(nome)
    print("-------------------------------------------------------------------------------------")
    print(sub)
    print("-------------------------------------------------------------------------------------")
    print(arq)
    print("valor" * 10)
