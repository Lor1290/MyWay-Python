# ! PRIMA VERSIONE - NABBO

print(">>> Bevenvenuto nel programma che ti permette di scrivere il tuo codice \n    Python direttamente da un programma esterno. Se tutto è stato compreso \n    COMICIAMO!")

cicle_1 = True
while cicle_1:
    print()
    print(">>> Cosa vuoi fare?")
    print("[+] Premi '1' se vuoi scegliere una directory")
    print("[+] Premi '2' se vuoi uscire dal programma")
    decision = input()
    
    if decision == "1":
        print()
        directory = input("Inserisci la directory: ")
        name = input("Inserisci il nome del file: ")
        file = open(r""+directory+name+".py", "w+")
        
        cicle_2 = True
        while cicle_2:
            print()
            print(">>> Cosa vuoi fare?")
            print("[+] Premi '1' se vuoi scivere nel file da te scelto")
            print("[+] Premi '2' se vuoi uscire dalla directory")
            decision = input()

            if decision == "1":
                print()
                print(">>> scrivi 'stop' quando vuoi uscire")

                cicle_3 = True                
                while cicle_3:

                    row = input("> ")
                    
                    if row.lower() == "stop":
                        cicle_3 = False
                    else:
                        file.write(row)
                        
            elif decision == "2":
                print("[-] uscendo dalla directory...")
                cicle_2 = False
                
            else:
                print("[-] Valore inserito non valido, riprova... ")
                
    elif decision == "2":
        print(">>> Arrivederci!")
        file.read()
        file.close()
        cicle_1 = False

    else:
        print("[-] Valore inserito non valido, riprova... ")

