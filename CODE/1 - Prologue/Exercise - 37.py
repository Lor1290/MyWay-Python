#Esercizio riguardante il linguaggio rövarspråket

#Creazione
def Linguaggio_Dei_Furfanti_Creazione(parola):
    
    vocali = "aeiou"
    parola_segreta = ""
    
    for i in parola:
        
        if i in vocali: 
            parola_segreta += i
        
        else:
            parola_segreta += i + "o" + i
    
    return parola_segreta.lower()

#Menù
print("Benvenuto nel programma che ti permette di:")
print("- Creare una parola segreta data in input in linguaggio rövarspråket")
print()

cicle = True

while cicle:    
    print("Cosa vuoi fare adesso?")
    print("Premi '1' per creare una nuova parola") 
    print("Premi '2' per uscire dal programma")
    decisione = int(input())
    print()

    if decisione == 1:
        Parola = input("Dimmi la parola da creare: ")
        creazione = Linguaggio_Dei_Furfanti_Creazione(Parola) 
        print(f"Ecco la tua parola creata in linguaggio rövarspråke: {creazione}")
        print()

    elif decisione == 2:
        print("Grazie di averci utilizzato e... Arrivederci!")
        cicle = False
    
    else: 
        print("Hai sbagliato a digitare, riprova: ") 