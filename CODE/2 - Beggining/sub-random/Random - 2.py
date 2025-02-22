#Programma-Simulazione di un registro scolastico 
import matplotlib
import numpy as np

#Variabili
domanda = None

#Cicli
run_1 = True
run_2 = True
run_4 = True

try:
    file = open("Registro_Scolastico.txt", "x")
    file = open("Registro_Scolastico.txt", "r")
    if file.readline() == "":
        file = open("Registro_Scolastico.txt", "a")
        file.writelines(["\n_______________________________________________________________________________________________________________________________________________________", "\n| Registro Scolastico 2022/2023                         Scuola: Antonio Fogazzaro                         Paese: San Giorgio di Livenza (Caorle)      |", "\n|                                                                                                                                                     |"
, "\n| Alunni:                                         |    Matematica    |    S.T.A    |    Diritto    |    Fisica    |    Chimica    |    Economia    |  |"])              

except FileExistsError:
    file = open("Registro_Scolastico.txt", "r")
    if file.readline() == "":
        file = open("Registro_Scolastico.txt", "a")
        file.writelines(["\n_______________________________________________________________________________________________________________________________________________________", "\n| Registro Scolastico 2022/2023                         Scuola: Antonio Fogazzaro                         Paese: San Giorgio di Livenza (Caorle)      |", "\n|                                                                                                                                                     |"
, "\n| Alunni:                                         |    Matematica    |    S.T.A    |    Diritto    |    Fisica    |    Chimica    |    Economia    |  |"])              

print("Benvenuto nel programma che ti permette di simulare un registro scolastico. Il suo funzionamento è particolarmente semplice: Ti bastera scrivere i nomi degli studenti e i loro voti. Se vorrai, potrai poi visualizzarli sia su foglio, sia si un grafico")
print()
inizio_programma = input("Se hai capito, scrivi 'X' per iniziare. Scrivi invece 'E' per uscire dal programma: ")

while run_1:
    file = open("Registro_Scolastico.txt", "r")
    if inizio_programma == "X":
        print()
        print("Queste sono le azioni che potrai fare: ")
        print("Scrivi 1 --> Apri il file (leggerlo) Ps: Solo se il file presenta contenuto")
        print("Scrivi 2 --> Apri il file (vederlo graficamente) Ps: Solo se il file presenta contenuto")
        print("Scrivi 3 --> Aggiungi un nome al registo")
        print("Scrivi 4 --> Aggiungi un voto al registro")
        print("Scrivi 5 --> Elimina un nome dal registro")
        print("Scrivi 6 --> Elimina un voto dal registro")
        print("Scrivi 7 --> Chiudi il registro")
        decisione = int(input())

        if decisione == 1:
            print()
            print("Ecco il tuo testo: ")
            print()
            print(file.read())
            print()
            print()
            print()
            print("Decidi adesso cosa fare...")

        elif decisione == 2:
            print("sus")

        elif decisione == 3:
            while run_2:
                run_3 = True
                file = open("Registro_Scolastico.txt", "a")
                print()
                alunno = input("Decidi il nome dell'alunno, o dell'alunna, che vuoi aggiungere (Sia nome che cognome): ")
                file.write("\n|" + alunno + " " * (149 - len(alunno)) + "|")
                print()
                print("Vuoi aggiungere un altro nome? (S/N)")
                domanda = input()
                while run_3:
                    if domanda == "N":
                        run_3 = False
                        run_2 = False
                    elif domanda == "S":
                        run_3 = False
                    else:
                        print()
                        print("Hai sbagliato a scrivere, riprova: ")
                        domanda = input()
    
        elif decisione == 4:
            while run_4:
                file = open("Registro_Scolastico.txt", "r+")
                if file.readline() == "|Gorghetto":
                    file.write("among us")
                
        elif decisione == 5:
            print("sus")

        elif decisione == 6:
            print("sus")

        elif decisione == 7:
            run_1 = False

        else:
            print("Hai sbagliato a scrivere, riprova: ")
            decisione = int(input())

    elif inizio_programma == "E":
        run_1 = False

    else:
        print()
        inizio_programma = input("Hai sbagliato a premere letterà, riprova: ")

print()
print("Arrivederci! Spero che questo programma ti sia stato di aiuto")
file.close()    
