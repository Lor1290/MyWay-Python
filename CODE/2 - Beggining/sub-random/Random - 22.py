"""CALCOLO CODICE FISCALE - Lorenzo Poli"""

#IMPORT
import time
import pygame
from os.path import join
from pygame.locals import *

pygame.init() #Inizializzazione

#VARIABILI
application = True
fullscreen = False

Icon = pygame.image.load(join("img/CodiceIcon.png"))
Info = pygame.display.info()

GenericW, GenericH = 900, 600

#SCHERO
main_screen = pygame.display.set_mode(GenericW, GenericH)
pygame.display.set_caption("CodiceFiscale")
pygame.display.set_icon(Icon)

#CICLO PRINCIPALE
while application:
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:

            if ev.key == pygame.ESCAPE:
                pygame.quit()
                quit()

            if ev.key == pygame.K_SPACE:
                fullscreen = not fullscreen
                if fullscreen:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    pygame.display.set_mode(GenericW, GenericH)

