"""TEST VIDEOGAME - 1"""

import time
import googletrans

#class Functionality
class FuncT:
    
    def SlowText(text: str, tmp: int): # --> Slow Output of a text
        for letter in text:
            print(letter)
            time.sleep(tmp)

    def SlowTexts(texts: list(str), tmp: int): # --> Slow Output of a series of text
        for text in texts:
            for letter in text:
                print(letter)
                time.sleep(tmp)
            print()


#class Main - Game
class Main:
    
    def intro() -> str: #Select the language 
        
        cicle_1 = 1

        while cicle_1:

            menu = ["[1] Italian -it", "[2] English -en", "[3] Spanish -es\n"]
            FuncT.SlowText("[?] Select a language from the menù: ", 0.02)
            FuncT.SlowTexts(menu, 0.05)

            decision = input("> ")
            
            match decision:
                case "1":
                    language = "it"
                    cile_1 = 0
                case "2":
                    language = "en"
                    cile_1 = 0
                case "3":
                    language = "es"
                    cile_1 = 0
                _:
                    FuncT.SlowText("[!] Invalid input, retry: ")

        return language
            
    def Start(lang) -> tuple: #Rules
        translator = googletrans.Translator()
        dialogue_1 = translator.translate(["[s] Benvenuto nel mio videogame! Qui potrai giocare assieme ad un tuo amico alla 'lotta delle mani'",
                                           "[?] Diamo una brave spiegazione a come funziona: ",
                                           "[d] Il gioco verra svolto da due giocatori, ognuno partira con un dito su ogni mano",
                                           "[d] A turni, il giocatore andrà a colpire una mano dell'altro giocatore, sommando poi sulla sua mano il numero di dita con cui è stato colpito",
                                           "[d] Se il giocatore possiede, dopo il colpo, una mano con 5 dita, quest'ultima deve essere tolta dal gioco",
                                           "[d] Se il giocatore possiede un numero pari di dita, e ha  perso una mano, potra sdoppiare il numero in questione su due mani, facendo così ritornare la mano persa",
                                           "[d] il giocatore perde quando non ha più nessuna mano in gioco",
                                           "[=] se avete capito, quindi, iniziamo!\n"], dest = [lang])

        FuncT.SlowTexts(dialogue_1, 0.05)
        FuncT.SlowText(translator.translate(["[P1] Seleziona il tuo nome, giocatore 1 \n"], dest = [lang]), 0.05)
        player_1 = input("> ")
        FuncT.SlowText(translator.translate(["[P1] Seleziona il tuo nome, giocatore 2 \n"], dest = [lang]), 0.05)
        player_2 0 input("> ")
        FuncT.SlowText(translator.translate(["[s] bene, possiamo comnciare adesso... che il gioco inizi! \n"], dest = [lang]), 0.05)

        return lang, player_1, player_2

    def Game(lang, player_1, player_2): #Mid-Game
        translator = googletrans.Translator()
        dita_01, dita_02, dita_11, dita_12 = 1, 1, 1, 1
        live_1 = 2
        live_2 = 2
        turn = 0
        
        
        while live_1 != 0 or live_2 != 0:
            if turn % 2 == 0:
                for x in range(5):
                    print("+" * dita_01 + "+" * dita_02)

                dialogue_2 = translator.translate(["[?] Cosa vuoi fare?",
                                                   "[1] Colpisci una mano dell'avversario",
                                                   "[2] Sdoppi (solo se non possiedi una mano)"], dest = [lang])

                FuncT.SlowTexts(dialogue_2, 0.05)

                cicle_1 = 1
                while cicle_1:
                    decision_1 = input("> ")

                    match decision:
                        case "1":
                            Attac = ["[?] Quale mano vuoi colpire? ",
                                     f"[s] Colpisci la mano sinistra (Ps. il giocatore 2 possiede {dita_11}",
                                     f"[d] Colpisci la mano destra (Ps. il giocatore 2 possiede {dita_12}"]
                                     
                            if dita_11 == 5:
                                Attac.remove(f"[s] Colpisci la mano sinistra (Ps. il giocatore 1 possiede {dita_11}")
                            if dita_12 == 5:
                                Attac.remove(f"[d] Colpisci la mano destra (Ps. il giocatore 1 possiede {dita_12}")   
                            
                                     
                            dialogue_3 = translator.translate(Attac, dest = [lang])

                            FuncT.SlowTexts(dialogue_3, 0.05)

                            cicle_2 = 1
                            while cicle_2:
                                decision_2 = input("> ")

                                if decision_2,lower() == "s" and dita_11 != 5 and dita_01 != 5:
                                    dita_11 += dita_01
                                    if dita_11 > 5:
                                        dita_11 -= 5

                                    cicle_2 = 0
                                    
                                if decision_2 == "d" and dita_12 != 5 and dita_02 != 5:
                                    dita_12 += dita_02
                                    if dita_12 > 5:
                                        dita_12 -= 5

                                    cicle_2 = 0

                                elif decision_2 not in "sd"