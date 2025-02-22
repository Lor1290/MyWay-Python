def Furfanti_T(word: str):
    cicle = True

    while cicle:
        change = word.index("o")
        if change != len(word)-1 and word[change-1] == word[change+1]:
            word = word.replace(word[change:change+2], "")
        else:
            cicle = False

    return word

def Furfnati_C(word: str):
    vocali = "aeiou"

    for x in word:
        if x not in vocali:
            index = word.index(x)
            word = word.replace(word[index], x + "o" + x)

    return word

cicle = True
while cicle:
    print("Premi '1' per tradurre una parola nel linguaggi dei furfanti")
    print("Premi '2' per creare una parola nel linguaggio dei furfanti")
    print("Premi '3' per uscire")
    
    decision_1 = True
    while decision_1:
        match chang := input("> ").lower():
            case "1":
                word = input("[s] Inserisci una parola: ")
                print(f"[=] La tua parola tradotta è: {Furfanti_T(word)}")

                print("\n[?] Vuoi continuare? (y/n)")
                decision_2 =  True
                while decision_2:
                    match cont := input("> ").lower():
                        case "y":s
                            print("[+] Continuiamo all'ora!")
                            decision = False
                        case "n":
                            print("[-] Arrivederci!")
                            decision_2 = False
                            cicle = False
                        case _:
                            print("[!] Valore inserito non valido")
                            
            case "2":
                word = input("[s] Inserisci una parola: ")
                print(f"[=] La tua parola convertita è: {Furfanti_C(word)}")

                print("\n[?] Vuoi continuare? (y/n)")
                decision_2 =  True
                while decision_2:
                    match cont := input("> ").lower():
                        case "y":
                            print("[+] Continuiamo all'ora!")
                            decision = False
                        case "n":
                            print("[-] Arrivederci!")
                            decision_2 = False
                            cicle =  False
                        case _:
                            print("[!] Valore inserito non valido")

            case "3":
                print("[-] Arrivederci!")
                cicle = False

            case _:
                print("[!] Valore inserito non valido")
                 
