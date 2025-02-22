"""IMPORT"""
import pygame # Il suo compito sarà quello di importare l'interlo modulo pygame
from pygame.locals import * # Il suo compito, invece, sarà quello di importare i metodi (le funzioni, definizioni, moduli, ecc...) da utilizzare
from os.path import join # Verrà spiegato meglio Successivamente

"""Dopo aver importato i moduli, andiamo a inizializzare il nostro schermo principale"""

"""INIZIALIZZAZZIONE"""
pygame.init() # Inizializzi TUTTE le funzioni della libreria
pygame.display.set_caption("Asteroid") # Mettiamo il nome al progetto
info = pygame.display.Info() # Richiamiamo nel programma le informazioni dello schermo
GenericW, GenericH = info.current_w, info.current_h # Assegniamo la larghezza e la altezza dello schermo

"""METODO 1 GRANDEZZA SCHERMO"""
SIZE1 = 1920, 1080
SIZE2 = 1240, 970
SIZE3 = 970, 580

"""METODO 2 GRANDEZZA SCHERMO"""
pygame.display.set_mode((0,0), pygame.FULLSCREEN)

"""METODO 3 GRANDEZZA SCHERMO"""
pygame.display.set_mode((GenericW, GenericH))

screen.fill((0,0,0))  / screen.fill("BLACK") # Coloro lo schermo (o con RGB, o con colore nome --> nome.lower())

# Main cicicle utilizzato per inizializzare il gioco
cicle = True
while cicle:

    for ev in pygame.event.get(): # Essenziale per ricavare input dal giocatore
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE: # Esce dal programma in caso si schiacci ESC
                pygame.quit()
                quit()

    pygame.display.flip() # Aggiorno lo schermo

exit()
