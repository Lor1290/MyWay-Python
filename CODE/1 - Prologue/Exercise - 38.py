def Palindormo(parola):
    
    parola_reverse = parola[::-1]

    if parola_reverse == parola:
        print("La tua parola è palindroma!")
    
    else:
        print("La tua parola non è palindroma...")

cicle = True

print("Bevenuto nel programma che ti permette di inserire una parola a tuo piacimento è determinare se è palindroma o no")
print("Premi '1' se vuoi inserire una parola")
print("Premi '2' se vuoi uscire dal programma")
print()

while cicle:
    
    decisione = int(input("Cosa vuoi fare quindi? "))
    
    if decisione == 1:
        Parola = input("Dimmi la parola: ")
        Palindormo(Parola)
        print()
    
    elif decisione == 2:
        print("Ok, ciao!")
        cicle = False
    
    else:
        print("Hai sbagliato a digitare, riprova: ")