"""BLACK JACK - BY LORENZO POLI"""

import time
import random
from random import randint

class Func:
    def sprint(word: str, tmp: int):
        for x in word:
            print(x, end = "")
            time.sleep(tmp)
    def sprints(words: list, tmp: int):
        for x in word:
            for y in x:
                print(y, end = "")
                time.sleep(tmp)
            ptint()

class Main:
    def intro():
        Func.sprint("[s] Benvenuto nel mio casinò! iniziamo una partità? (y/n)", 0.05)
        
        while True:
            match decision = input(">>> ").lower():
                case "y":
                    Func.slowprint("[+] perfetto, cominciamo all'ora!", 0.05)
                    return True
                case "n":
                    Func.slowprint("[:(] Arrivederci... e alla prossima!", 0.05)
                    return False
                case _:
                    Func.slowprint("[!] valore inserito non valido, riprova...", 0.05)

    def player():
        Func.sprint("\n[?] Quanti giocatori siete? (non più di 6)", 0.05)

        while True:
            player = input(">>> ").lower()
            if player not in ("1", "2", "3", "4", "5", "6"):
                Func.sprint("[!] valore inserito non valido, riprova...", 0.05)
            else:
                return int(player)

    def name(player: int):
        List_name = []
        
        Func.sprint("\n[=] Inserite adesso i vostri nomi...", 0.05)
        while len(List_name) < player:
            name = input(">>> ")
            Func.sprint(f"[?] Sei sicuro di voler usare il nome: {name}, giocatore {x}? (y/n)", 0.05)

            cicle = True
            while cicle:
                match decision = input(">>> ").lower():
                    case "y":
                         Func.slowprint("[+] perfetto, passiamo al prossimo giocatore", 0.05)
                         List_name.append(name)
                         cicle = False
                    case "n":
                        Func.slowprint("[-] Ok, cambiamo nome all'ora...", 0.05)
                        cicle = False
                    case _:
                        Func.sprint("[!] valore inserito non valido, riprova...", 0.05)

        return List_name
                        
                      
    def game(List_name: list):
        Func.sprint("\n[+] inizia il bancone...", 0.05)       
        while True:
            List_H_B = [] #Mano del bancone
            List_H_P = [[] for x in range len(List_name)] #Mano dei player
            
            List_H_B.append(random.randint(1, 11))
            List_H_B.append(random.randint(1, 10))

            if sum(List_H_B) == 21:
                Func.sprints("[!] Il bancone ha fatto Black-Jack!", 0.05)
                Func.sprints("[?] Volete continuare? (y/n)", 0.05)

                cicle = True
                while cicle:
                    match cont = input(">>> ").lower():
                        case "y":
                            Func.sprints("[+] perfetto, continuiamo!", 0.05)
                            cicle = False
                        case "n":
                            Func.sprint("[:(] Arrivederci... e alla prossima!", 0.05)
                            return False
                        case _:
                            Func.sprint("[!] valore inserito non valido, riprova...", 0.05)

            else:
                Func.sprint(f"[?] Il bancone ha, per adesso, un: {List_H_B[0]}", 0.05)  
                for x in range len(List_name):
                    Func.sprint(f"{List_name[x]} è il tuo tuno...", 0.05)  
                    List_H_P[x].append(random.randint(1, 11))
                    List_H_P[x].append(random.randint(1, 10))
                    
                    if sum(List_H_P[x]):
                        Func.sprint(f"[+] {List_name[x]}, hai fatto Black-Jack!", 0.05)

                    else:
                        cont = True
                        while cont and sum(List_name[x]) <= 21:
                            Func.sprint(f"[+] Cosa vuoi fare, {List_name[x]}, pescare '1' o restare '2' ", 0.05)

                            deci = True
                            while deci:
                                match decision = input(">>> "):
                                    case "1":
                                       List_H_P[x].append(random.randint(1, 11))
                                       if sum(List_H_P[x]) > 21 and List_H_P[x].count(11) > 0:
                                           List_H_P[x][List_H_P[x].index(11)] = 1                                                         
                                            deci = False                                            
                                    case "n":
                                        deci = False
                                        cont = False
                                    case _:
                                        Func.sprint("[!] valore inserito non valido, riprova...", 0.05)

                            Func.sprint(f"[+] La tua mano, per adesso, è: {"".join(List_H_P[x] (for x + " " in List_H_P[x]))}", 0.05)

    def game_ending(List_Player: list, List_Point: list, List_Point_B: list):
        Func.sprint("[-] Adesso che tutto è stato piazzato, vediamo cosa ha da offrire il bancone...", 0.05)

        cicle = True
        while cicle and sum(List_Point_B) <= 21:
            List_Point_B.append(random.randint(1, 11))
            
            if sum(List_Point_B) > 21 and List_Point_B.count(11) > 0:
                List_Point_B[List_Point_B.index(11)] = 1
            elif sum(List_Point_B) in (16, 17 18, 19, 20):
                                                          
