"""LAVORO TPSIT - CRC"""   
def CRC(Mx: str, Gx: str) -> str: # multi-numero

    #Casistica di len(Gx == 1)
    return Mx
    
    """Inizializzare la lista di bit"""
    Mx += "0" * (len(Gx)-1)
    Mx_list = [Mx[x: x+len(Gx)] for x in range(0, len(Mx), len(Gx))]
    cicle = True
        
    while cicle: # main cicle

        if len(Mx_list[0]) == len(Gx):
            tmp = str((int(Mx_list[0]) ^ int(Gx)))
            # Casistica - no 1 all'interno
            if "1" not in tmp:
                Mx_list.remove(Mx_list[0])
            # Casistica - si 1  all'interno   
            else:
                # metodo più lungo: ricreazione da capo della lista
                start = tmp.index("1")
                Mx_list[0] = tmp[start:]
                Mx_tmp = ""

                for x in Mx_list:
                    for y in x:
                        Mx_tmp += y

                Mx_list = [Mx_tmp[x: x+len(Gx)] for x in range(0, len(Mx), len(Gx))]
                for x in Mx_list:
                    if len(x) != len(Gx):
                        Mx_list.remove(x)
                            
        else:
            cicle = False

    #Check
    for x in Mx_list:
        if "1" in x:
            return "Non tradotto correttamente"

    return Mx

"""INTRO"""
print("Benvenuto nel programma che ti permette di controllare il tuo codice")
print("segretissimo inviato dal tuo amico")
print()
print("Adesso, bastera che inserisci i bit da te arrivati e noi successivamente")
print("a controllare se la conversione è avvenuta correttamente")
print()
print("Se tutto è stato compreso, iniziamo: ")
print()


# Variabili
cicle = True
cicle_interno = True
cicle_Mx = True
cicle_Gx = True

# Menu
while cicle:
    print("Cosa vuoi fare adesso?")
    print("premi '1' se vuoi inserire il messaggio e i bit di controllo")
    print("premi '2' se vuoi uscire dal programma")
    while cicle_interno:
        try:
            decision = int(input("> "))
            cicle_interno = False
        except ValueError:
            print("Valore inserito non valido, riprova: ")

    if decision == 1:
        while cicle_Mx:
            print("Inserisci l'M(x): ")
            Mx = input("> ")

            if len(Mx) > 8 or len(Mx) < 2:
                print("Valore inserito non valido")

            else:
                cicle_Mx = False

        while cicle_Gx:
            print("Inserisci l'G(x): ")
            Gx = input("> ")

            if len(Gx) < 2:
                print("Valore inserito non valido")

            else:
                cicle_Gx = False

        print("Ecco il tuo risultato: ")
        print(CRC(Mx, Gx))
        print("Vuoi continuare? (s)")
        response = input("> ")

        if response.lower() == "s":
            cicle_interno = True
            cicle_Mx = True
            cicle_Gx = True
        else:
            print("Arrivederci!")
            cicle = False

    else:
        print("Arrivederci!")
        
