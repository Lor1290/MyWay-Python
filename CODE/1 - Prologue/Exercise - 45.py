print("benvenuto nel programma che ti permette di 'carpire' le varie sequenze date proprtio da te! Adesso, iniziamo!")
print()
numeri = []
numeri_1 = []
numeri_2 = []
numeri_3 = input("Inserisci una serie di numeri, poi io ti dirò se quest'ultimi sono crescenti o decrescenti: ")
numeri = numeri_3.split()
numeri = [int(i) for i in numeri]
numeri_1 = numeri_3.split()
numeri_1 = [int(i) for i in numeri]
numeri_1.sort()
numeri_2 = numeri_3.split()
numeri_2 = [int(i) for i in numeri]
numeri_2.sort()
numeri_2.reverse()
cre = 1
dec = 1
non_crescente = False
non_decrescente = False
for i in numeri:    
    if cre == len(numeri):
        break
    elif i == numeri_1[cre]:
        non_crescente = True
        cre += 1
    elif i != numeri_1[cre]:
        cre += 1
for i in numeri:
    if dec == len(numeri):
        break
    elif i == numeri_2[dec]:
        non_decrescente = True
        dec += 1
    elif i != numeri_2[dec]:
        dec += 1
if non_crescente == True and numeri == numeri_1:
    print(f"La tua sequenza: --> {numeri} è in ordnine non crescente! :)")
elif non_decrescente == True and numeri == numeri_2:
    print(f"La tua sequenza: --> {numeri} è in ordine non decrescente! :)")
elif numeri == numeri_1:
    print(f"La tua sequenza: --> {numeri} è in ordine crescente! :)")
elif numeri == numeri_2:
    print(f"La tua sequenza: --> {numeri} è in ordine decrescente! :)")
else:
    print(f"La tua sequenza: --> {numeri} non è ne crescente, ne decresnete, ne non decrescente e neanche non crescente... Mi dispiace :(")
