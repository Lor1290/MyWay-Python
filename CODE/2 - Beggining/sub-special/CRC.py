""" CONTROLLO CRC - TEST """

# +IMPORT+
import binascii
import time

# +FUNZIONI DEL PROGRAMMA+
def Slow_Writing(Dialogue: list[str], tmp: int):
    for word in Dialogue:
        for letter in word:
            print(letter, end = "")
            time.sleep(tmp)
        print()
        
def Slow_Word(Word: str, tmp: int):
    for letter in Word:
        print(letter, end = "")
        time.sleep(tmp)
        
def Control_Input(scan: str):
    for x in scan:
        if x != "0" and x != "1":
            return False
    return True
              
# !VARIABILI!
dialogue_1 = ["[S] CONTROL CRC", "", "> Benvenuti nel mio programma per il calcolo del CRC", "> Per prima cosa, inserisci il valore in bit del messaggio che dovra essere inviato: "]
dialogue_2 = ["", "> Adesso, inserisci i bit di controllo: ", "[?] (P.s I bit di controllo, nel CRC, sarebberò ricavati da una tabella\n    internazionale. Si prega di utilizzare quest'ultima)"]
dialogue_3 = ["", "> Adesso inizieremo il processo di controllo del CRC", "[!] ALLA FINE DEL PROCESSO MOSTREREMO I RISULTATI"]

cicle_1: bool = True

# <START>

while cicle_1:

    cicle_2, cicle_3, cicle_4, cicle_5, cicle_6 = 1, 1, 1, 1, 1 # Value for the cicle    
    Slow_Writing(dialogue_1, 0.05)
    
    while cicle_2:
        
        while cicle_3: #First control - byte input
            Mx = input("[=] ")
            if Control_Input(Mx):
                cicle_3 = 0
            else:
                print("[!] Valore non valido: Riprova")
                continue
        
        Slow_Writing(dialogue_2, 0.05)

        cicle_3 = 1
        while cicle_3: # Second control - byte input
            Gx = input("[=] ")
            if Control_Input(Gx):
                    cicle_3 = 0
            else:
                print("[!] Valore non valido: Riprova")
                continue

        Slow_Word(f"\n> Dai tuoi dati inseriti, il polinomio da inviare dovrebbe essere: {Mx}" + (len(Gx)-1)*"0"+ f"\n  e quello di controllo {Gx}, è corretto? (y/n)\n", 0.05)
    
        while cicle_4: # third control - decision by user

            cont = input("[?] ")
            match cont.lower():
                case "y":
                    Slow_Word("\n> Perfetto, andiamo avanti all'ora", 0.05)
                    cicle_4, cicle_2 = 0, 0
                    Mx += (len(Gx)-1)*"0"
                case "n":
                    Slow_Word("\n> Peccato. inseriamo nuovamente i dati? (y/n)\n", 0.05)

                    while cicle_5:

                        ext_1 = input("[?] ")
                        match ext_1.lower():
                            case "y":
                                Slow_Word("\n> Perfetto, Riproviamoci\n", 0.05)
                                cicle_4, cicle_5, cicle_3 = 0, 0, 1
                            case "n":
                                Slow_Word("\n> Peccato... Allora, alla prossima!", 0.05)
                                cicle_1, cicle_2, cicle_3, cicle_4, cicle_5 = 0, 0, 0, 0, 0
                            case _:
                                Slow_Word("[!] Valore non valido: Riprova", 0.05)
                case _:
                    Slow_Word("\n[!] Valore non valido: Riprova", 0.05)
    
    if cicle_1: # OUTPUT
        Slow_Writing(dialogue_3, 0.05)
        res = binascii.crc32(Mx.encode("utf-8"), Gx.encode("utf-8"))
        
        if res == 0:
            Slow_Word(f"[=] Il resto ottenuto è: {res}. Ciò vuol dire che il polinomio è stato inviato correttamente", 0.05)
            Slow_Word(f"[?] (Il polinomio inviato è: {Mx}")
        else:
            Slow_Word(f"[=] Il resto ottenuto è: {res}. Ciò vuol dire che il polinomio non è stato inviato correttamente", 0.05)
            Slow_Word(f"[?] (il polinomio da inviare è: {Mx}" + res, 0.05)

        Slow_Word("\n> Adesso che hai finito, vuoi continuare con un altro valore? (y/n)\n", 0.05)

        while cicle_6: # CONTINUE OR SHUTDOWN
            ext_2 = input("[?] ")
            match ext_2.lower():
                case "y":
                    Slow_Word("[ :) ] Continuiamo!", 0.05)
                    cicle_6 = 0
                    cicle_2, cicle_3, cicle_4, cicle_5 = 1, 1, 1, 1, 1
                    
                case "n":
                    Slow_Word("[ :( ] Arrivederci!", 0.05)
                    cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6 = 0, 0, 0, 0, 0, 0

                case _:
                    Slow_Word("\n[!] Valore non valido: Riprova", 0.05)
                    
exit()
