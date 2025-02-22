#Import
from pygame.locals import *
from os.path import join
from curses import wrapper
import pygame
import time
import sys
import curses

#Schermo
pygame.init()
screen = pygame.display.set_mode((400, 600), pygame.RESIZABLE)
pygame.display.set_caption("🐍 TETRIS 🐍")
screen.fill((0, 197, 0))
pygame.display.update()

#Variabili
fullscreen = False

#Immagini


#Definizioni
def pausa():
    pausa = True

    while pausa:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#Ciclo principale                        
while True:

    #Eventi
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                screen.fill((0, 197, 0))
                pygame.display.update()
            else:
                screen = pygame.display.set_mode((450, 700), pygame.RESIZABLE)
                screen.fill((0, 197, 0))
                pygame.display.update()

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screen.fill((0, 197, 0))
            pygame.display.update()
   
pygame.quit()
