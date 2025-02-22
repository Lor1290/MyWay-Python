#Introduzione
print("Benvenuto nel programma che ti permette di stampare le circonferenze e le aree di cerchi con raggio '1' fino ad un limite a tuo piacimento che adesso deciderai")
print()
Volte = int(input("Dimmi, quindi, fino a che raggio vuoi arrivare: "))
#Variabili
Raggio = 1
Area = 3.14
Circonferenza = 6.28
Moltiplicatore = 1
print("R".center(20) + "Circ.".center(38) + "Area".center(23))
#Calcoli
for i in range(Volte):
    Raggio_1 = (Raggio * Moltiplicatore)
    Area_1 = (Area * Moltiplicatore * Moltiplicatore)
    Circonferenza_1 = Circonferenza * Moltiplicatore
    
    print(str(round(Raggio_1, 1)).center(20) + str(round(Circonferenza_1,1)).center(36) + str(round(Area_1,1)).center(27))
    Moltiplicatore += 1
print()
print("Il programma è finito, spero ti sia stato di aiuto!")

    
    
    
    
