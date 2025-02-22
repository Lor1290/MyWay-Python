#Import
import pyautogui
import cv2
import time
import keyboard
#variabili
avvio = True
contatore = 0
altezza = 375
#Programma
print("produttore: Lorenzo Poli")
print()
print("Scrivi 'Avvio' per avviare il software: 'Bot di Magic Tails'")
risposta_1 = input()
print()
run_1 = True
while run_1:
    if risposta_1 != "Avvio":
        print()
        print("Fose hai sbagliato a digitare, riprova: ")
        risposta_1 = input()
    else:
        break
print("Spero che il programma sia di tuo gradimento!")
print("(Ricorda! premi 'esc' pre uscire dal programma)")
#Ciclo
print()
print("Avvio del programma tra 10 secondi. 9...8...")
time.sleep(10)
run_2 = True
while run_2:
    #Eventi
    if keyboard.is_pressed("esc") == True:
        run_2 = False
    #Funzioni    
    if avvio == True:
        if pyautogui.pixelMatchesColor(950, 589, (255, 255, 255)) == True:
            pyautogui.moveTo(950, 589)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            avvio = False 
    if contatore == 10:
        altezza += 20
        contatore = 0
    elif  pyautogui.pixelMatchesColor(725, 300, (0, 0, 0), tolerance = 10) == True:
        pyautogui.moveTo(725, altezza)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        contatore += 1
    elif pyautogui.pixelMatchesColor(878, 300, (0, 0, 0), tolerance = 10) == True:
        pyautogui.moveTo(878, altezza)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    elif pyautogui.pixelMatchesColor(1029, 300, (0, 0, 0), tolerance = 10) == True:
        pyautogui.moveTo(1029, altezza)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    elif pyautogui.pixelMatchesColor(1190, 300, (0, 0, 0), tolerance = 10) == True:
        pyautogui.moveTo(1190, altezza)
        pyautogui.mouseDown()
        pyautogui.mouseUp()   
print()
print("Spero che il programma ti sia stato di aiuto!")

