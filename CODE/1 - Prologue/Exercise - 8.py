while True:
    numero = int(input("inserisci un numero intero positivo, e io verifichero se quest'ultimo è un numero primo oppure no: "))
    divisore = 2
    divisori = [1]
    numero_1 = numero
    numero_primo = [1, numero]
    if numero == 1 or numero == 2:
        print()
        print(f"Il tuo numero: {numero_1} è un numero primo!")
        print()
    else:
        while numero != 1:
            if numero % divisore != 0:
                divisore += 1
            elif numero % divisore == 0:
                numero = numero // divisore
                divisori.append(divisore)
                divisore = 2
        if divisori != numero_primo:
            print()
            print(f"Il tuo numero: {numero_1} non è un numero primo...")
            print()
        else:
            print()
            print(f"Il tuo numero: {numero_1} è un numero primo!")
            print()
