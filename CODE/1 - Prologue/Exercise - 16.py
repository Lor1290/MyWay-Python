#File
files = input("Per prima cosa, dimmi il nome del file di testo (.TXT) che vuoi che noi andiamo ad utilizzare: ")
file = open(str(files) + ".txt")
print()
#Introduzione
print("Dimmi quale di queste azioni vuoi fare su un file di testo: ")
print("Premi 1: Leggi")
print("Premi 2: Scrivi")
print("Premi 3: Esci")
decisione = int(input())
#Programma
intro = True
while intro:
    if decisione == 1:
        print()
        print("Ecco il tuo file: ")
        file = open(str(files) + ".txt", "r")
        print(file.read())
        print("Cosa vuoi fare adesso? ")
        decisione = int(input())
    elif decisione == 2:
        print()
        print("Cosa vuoi scrivere di nuovo sul tuo testo? ")
        parole = input()
        file = open(str(files) + ".txt", "a")
        file.write("\n" + parole)
        print("Cosa vuoi fare adesso? ")
        decisione = int(input())
    else:
        intro = False
        file.close()
print()
print("Spero che questo servizio sia stato di tuo gradimento, arrivederci!")
        
