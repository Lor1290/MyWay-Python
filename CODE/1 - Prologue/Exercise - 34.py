numeri = []
numeri_1 = []
numeri_2 = input("Inserisci una serie di numeri, poi io ti dirò se quest'ultimi sono crescenti o decrescenti: ")
numeri = numeri_2.split()
numeri = [int(i) for i in numeri]
numeri_1 = numeri_2.split()
numeri_1 = [int(i) for i in numeri]
numeri_1.sort()
if numeri != numeri_1:
    print(f"La Tua sequenza: --> {numeri} non è in ordine non decrescente... :(")
if numeri == numeri_1:
    print(f"La tua sequenza: --> {numeri} è in ordine non descrescente! :)")    
