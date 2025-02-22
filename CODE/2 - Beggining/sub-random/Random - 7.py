#Import
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#File
file = open("MediaScolastica.txt")
file = open("MediaScolastica.txt", "r+")
for line in file:
    valore = ("<<<MediaScolastica          2023          Scuola: Antonio Fogazzaro>>>" in line)
    if valore == True:
        break
    else:
        file.writelines(["<<<MediaScolastica          2023          Scuola: Antonio Fogazzaro>>>","\n", "\nAlunno           |     Storia     |     Italiano     |     Greco     |     Latino     |     Inglese     |","\n                 |                |                  |               |                |                 |".center(10)])
#Grafico    
print("Benvenuto nel programma che ti permette di scrivere, modificare o cancellare voti di ragazzi all'interno di un file di testo, per poi vederli direttamente in un grafico (o in un foglio stesso) che mostra le medie delle varie materie")
print()
print("Ricorda! Le matererie dei ragazzi saranno: 'Storia' 'Italiano' 'Greco' 'Latino' 'Inglese'")
print()
#Ciclo
run = True
while run:
    print()
    print("Cosa vuoi fare adesso?")
    print("1 --> Aggiungere un alunno al 'registro'")
    print("2 --> Aggiungere un voto ad un alunno")
    print("3 --> Modificare un voto di un alunno")
    print("4 --> Togliere un voto ad un alunno")
    print("5 --> Chiudi il programma")
    decisione = int(input())
    print()

    if decisione == 1:
        run_1 = True
        print("Con questo comando potrai solo AGGIUNGERE nuovi alunni. Se hai sbagliato quindi a schiacciare tasto, premi 'F' altrimenti premi 'C'")
        decisione = input()
        while run_1:
            if decisione == "F":
                run_1 = False                
            elif decisione == "C":
                print()
                print("Dimmi il nome dell'alunno che vuoi aggiungere al Registro: ")
                alunno = input()                        
                file.writelines(["\n" + alunno + ":" + "                 |                |                  |               |                |                 |".center(5), "\n"])
                run_1 = False
            else:
                print()
                print("Fose hai sbagliato a digitare, riprova: ")
                decisione = input()
    if decisione == 2:
        run_2 = True
        print("Con questo comando potrai solo AGGIUNGERE voti agli alunni. Se hai sbagliato a schiacciare tasto, premi 'F', altrimenti premi 'C'")
        decisione = input()
        while run_2:
            if decisione == "F":
                run_2 = False
            elif decisione == "C":
                print()
                print("Dimmi il") 
            else:
                print()
                print("Forse hai sbagliato a digitare, riprova: ")
                decisione = input()
    if decisione == 3:
        print("sus")
    if decisione == 4:
        print("sus")
    if decisione == 5:
        print()
        print("Spero che questo programma ti sia stato di aiuto, arrivederci!")
        run = False

#Chiusura
file.close()
    
