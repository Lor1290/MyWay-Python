print("Benvenuto nel programma che ti permette di controllare se un insieme 'B' è presente all'interno di un insieme 'A'. Ricordati! 'B' dovra essere piu corto di 'A', e dovra contenere più di un elemento NUMERICO.")
print()
insieme_A = input("Inserisci adesso gli elementi presenti nell'insieme 'A': ")
print()
insieme_B = input("Inserisci poi gli elementi dell'insieme 'B': ")
print()
if insieme_B in insieme_A:
    print(f"Il tuo insieme 'B' è presente nell'insieme 'A'")
else:
    print(f"Il tuo insieme 'B' non è presente nell'insieme 'A' ...")

