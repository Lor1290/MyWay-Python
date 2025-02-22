import random
import os

#Esercizio 1 - ListaRandom
def NumeriRandom(length: int, _max_:int) -> int:
    NumeriRandom = []
    for x in range(length):
        NumeriRandom[x] = random(_maqx_)

    return random.choice(NumeriRandom)

#Esercizio 2 - varianti
class Password:
    #Password (versione NO return)
    def PasswordRandom1(length: int , caracter: str):
        for x in range(length):
            print(random.choice(caracter), end = "")
    #Password (versione YES return)
    def PasswordRandom2(length: int , caracter: str) -> str:
        FinalPassword = ""
        for x in range(length):
            FinalPassword += random.choice(caracter)

        return FinalPassword

#Esercizio 3 - Creazione di un foglio txt
file = open("TestRandom.txt", "w")
def PasswordRandom2(NumList: int, length: int , caracter: str) -> str:
        for x in range(NumList):
            FinalPassword = ""
            for y in range(length):
                FinalPassword += random.choice(caracter)

            file.write(FinalPassword + "\n")

        file.close()
