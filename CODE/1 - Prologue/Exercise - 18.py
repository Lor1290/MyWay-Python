file = open("stringhe.txt", "x")
print("Benvenuto nel programma che ti permette di aggiungere stringhe (e il loro opposto) ad un file di testo denominato come 'stringhe.txt'. Per prima cosa dimmi, quindi...")
print()
print("Cosa vuoi fare?")
print("Premi 1: Leggerlo")
print("Premi 2: Scriverci una nuova stringa (e il suo contrario)")
print("Premi 3: Cancellare tutto")
print("Premi 4: Esci dal programma")
decisione = int(input())
intro = True
while intro:
    if decisione == 1:
        print()
        file = open("stringhe.txt", "r")
        print(file.read())
        print()
        print("Cosa vuoi fare adesso?")
        print("Premi 1: Leggerlo")
        print("Premi 2: Scriverci una nuova stringa (e il suo contrario)")
        print("Premi 3: Cancellare tutto")
        print("Premi 4: Esci dal programma")
        decisione = int(input())
    elif decisione == 2:
        print()
        stringa = input("Inserisci la stringa che vuoi aggiungere: ")
        stringa_opposta = stringa[::-1]
        file = open("stringhe.txt", "a")
        file.writelines(["\n" + str(stringa), "\n" + str(stringa_opposta), "\n "])
        print()
        print("Cosa vuoi fare adesso?")
        print("Premi 1: Leggerlo")
        print("Premi 2: Scriverci una nuova stringa (e il suo contrario)")
        print("Premi 3: Cancellare tutto")
        print("Premi 4: Esci dal programma")
        decisione = int(input())
    elif decisione == 3:
        file = open("stringhe.txt", "w")
        file.write("")
        print()
        print("Cosa vuoi fare adesso?")
        print("Premi 1: Leggerlo")
        print("Premi 2: Scriverci una nuova stringa (e il suo contrario)")
        print("Premi 3: Cancellare tutto")
        print("Premi 4: Esci dal programma")
        decisione = int(input())
    else:
        file.close()
        intro = False
print()
print("Il programma è finito, spero sia stato di tuo gradimento!")
    
        
        
        

