lista_1 = []
lista_1 = input("inserisci un numero di elementi a tuo piacimento dividendoli da uno spazio: ")
lista_1.split()

prova = True

while prova == True:
    elemento = input("Prova a vedere se lelemento è nella lista digitandolo. Se vuoi uscire, premi 'F': ")
    if elemento == "F" or "f":
        print("ciao!")
    elif elemento in lista_1:
        print("L'elemento è nella lista")
    elif elemento not in lista_1:
        print("L'elemento non è nella lista")

    
