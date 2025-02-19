#Test videogame: Rulette Russa
#Import
import time
import sys
import keyboard
#Definizioni
def print_ASCII(immagine, delay):
    for i in immagine:
        i.center(75)
        print(i)
        time.sleep(delay)

def print_listtesto(text_list, delay):
    for i in text_list:
        for I in i:
            sys.stdout.write(I)
            sys.stdout.flush()
            time.sleep(delay)

def print_testo(text, delay):
    for i in text:
        print(i, end="")
        sys.stdout.flush()
        time.sleep(delay)
#Immagini ASCII
immagine1 = [
     "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█"
    ,"█    ,▄███████,       █'     ▄▄▄▄▄▄         █"
    ,"█   ▄███████▌▒╢       █    ,█▀▀▀`▒▓█▄       █" 
    ,"█   ████▀╙`' ╓▓       █    ▐▒▒╥┐,╦▓▓▌       █"
    ,"█   ╙██▓'    ╟▌╢      █     ▒  ║╫`░╫`       █"
    ,"█    ▐▌░  ,░░▒▓       █     ]▒.░~▒ ▒        █"
    ,"█  ▄████▄ ▒╢▓╩╨       █     ╓╨Ñ╖╓gÑW,,      █"
    ,"█ ███████]▒▌          █▄▄██▄█  ╙─'  ██████▄,█"
    ,"███████████▄µ         ███████▄▌[Ñ╙▓▓█████████"
    ,"█████████████▄        █████▄║▄▄▄▄▓▓▄▄▄███████"
    ,"██████████████▄      ▐████████     ██████████"
    ,"███████████████▄,,,,,▐████████,,,,▄██████████" ]                                             
#Intro
a = "26 novembre 1955".center(75)
print_testo(a ,0.05)
print("")
b = "Vorkutinskij ispravitelno-trudovoj lager (Vorkutlag)".center(75)
time.sleep(2)
print_testo(b ,0.05)
print("")
c = "1800 Km a Nord-Est di Mosca...".center(75)
time.sleep(2)
print_testo(c, 0.05)
print("")
time.sleep(1)
print("")
#Intro ASCII
print_ASCII(immagine1, 0.1)
#Intro
print("")
d = "Удостоверение личности/ carta di identita: "
print_testo(d, 0.05)
