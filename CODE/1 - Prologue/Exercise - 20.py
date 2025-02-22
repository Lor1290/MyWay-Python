lista_prodotti = {"pane" : "2£", "latte" : "3£", "pizza" : "7£", "cetrioli" : "2£", "carote" : "1£"}
lista_clienti = []
cicle = True

while cicle == True:
    name = input("Ciao! Come ti chiami? ")
    print()
    print(F"Ciao {name}, felice di accoglierti nel mio supermercato! Prendi cio che ti serve, scrivi 'stop' per smettere")
    scelta = None
    spesa = []
    while scelta != "stop":
        scelta = input()
        try:
            spesa.append(lista_prodotti[scelta.lower()])
        except KeyError:
            if scelta.lower() == "stop":
                pass
            else:
                print("Hai digitato male, riprova")
                print()
    
    lista_clienti.append(spesa)
    decision = input("Vogliamo chiudere? s/n ")
    response = True
    
    while response == True:
        if decision.lower() == "s":
            response = False
        elif decision.lower() == "n":
            response = False
            cicle = False
        else:
            print("Hai digitato male, riprova")

print(lista_clienti)
    
     


