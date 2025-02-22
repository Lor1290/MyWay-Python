from math import sqrt
print("Benvenuto nel programma che ti permette di calcolare la ipotenusa di un triangolo, sapendo il suo cateto maggiore e il suo cateto minore")
Cateti = input("Dimmi adesso i valori che vuoi assegnare al cateto maggiore e al cateto minore: ")
Cateti_list = []
Cateti_list = Cateti.split()
Cateti_list = [int(i) for i in Cateti_list]
for i in Cateti_list:
    Cateti_list.append(pow(2, i))
Cateti_list[0:1] = []
print(Cateti_list)
somma = sum(Cateti_list)
ipotenusa = sqrt(somma)
print(f"La tua ipotenusa è di: {ipotenusa}")
