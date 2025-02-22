intro = True
while intro:
    parola = input("Per favore, inserisci una parola per capire se quest'ultima sia palindroma o meno: ")
    palindromo = parola[:: -1]
    if parola == palindromo:
        print()
        print("Si, la tua parola è palindroma. Evvai!")
        print()
        risposta = input("Vuoi fare un'altra prova? (s/n): ")
        print()
        if risposta == "n":
            intro = False
    else:
        print()
        print("La tua parola non è palindroma... Mi dispiace :(")
        print()
        risposta = input("Vuoi fare un'altra prova? (s/n): ")
        print()
        if risposta == "n":
            intro = False
print("Arrivederci allora!")
