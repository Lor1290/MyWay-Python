Anno = int(input("Inserisci un anno: "))
if Anno < 1582:
           print(f"Mi dispiace, il tuo Anno --> {Anno} non puo essere bisestile...")
else:
    if Anno % 400 == 0 and Anno % 100 == 0:
        print(f"Il tuo Anno --> {Anno} è bisestile")
    elif Anno % 4 == 0:
        print(f"Il tuo Anno --> {Anno} è bisestile")
    else:
        print(f"Mi dispiace, il tuo Anno --> {Anno} non è bisestile...")
