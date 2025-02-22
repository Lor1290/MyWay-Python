numeri_1 = []
numeri_pos_pari = []
numeri_pos_dispari = []
numeri_val_pari = []
numeri = input("Inserisci una serie di numeri: Io ti stampero quelli in posizione dispari, quelli in posizione pari e ti stamperò nuova lista che contiene solo gli elementi pari: ")
numeri_1 = numeri.split()
numeri_1 = [int(i) for i in numeri_1]
numeri_pos_pari = numeri_1[0::2]
numeri_pos_dispari = numeri_1[1::2]
for i in numeri_1:
    if i % 2 == 0:
        numeri_val_pari.append(i)
print(f"La lista con i tuoi numeri in posizione pari è: --> {numeri_pos_pari}")
print(f"La lista con i tuoi numeri in posizione dispari è: --> {numeri_pos_dispari}")
print(f"I tuoi numeri pari erano: --> {numeri_val_pari}")
