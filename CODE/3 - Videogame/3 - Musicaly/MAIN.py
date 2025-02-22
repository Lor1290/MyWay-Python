
"""Progect Musicaly - MAIN program"""

#IMPORT
import time
import pygame
import MainScreen
from os.path import join
from pygame.locals import *

#DEFINITION
class MainFunction:          
    def fadein(Fcolor: list, Lcolo: list, tm: float, step: int):
        while true:
            if Fcolor[0] <= Lcolor[0]:
                Fcolor[0] += step
            if Fcolor[1] <= Lcolor[1]:
                Fcolor[1] += step
            if Fcolor[2] <= Lcolor[2]:
                Fcolor[2] += step

            else:
                break

            screen.fill(Fcolor)
            pygame.display.flip()
            time.sleep(tm)

    def fadeout(Fcolor: list, Lcolo: list, tm: float, step: int):
        while true:

            if Fcolor[0] >= Lcolor[0]:
                Fcolor[0] -= step
            if Fcolor[1] >= Lcolor[1]:
                Fcolor[1] -= step
            if Fcolor[2] >= Lcolor[2]:
                Fcolor[2] -= step

            else:
                break

            screen.fill(Fcolor)
            pygame.display.flip()
            time.sleep(tm)
        
pygame.init()

#VARIABLE
fullscreen = False
Gfont = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}

SIZE = WIDTH, HEIGHT = 900, 600
GenericW, GenericH = 900, 600

Icon = pygame.image.load(join("img/Icon.png"))
info = pygame.display.Info()

#LOAD
IntroMusic = pygame.mixer.Sound(join("Music/Intro.mp3"))

#SCREEN
main_screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Musicaly")
pygame.display.set_icon(Icon)

#PROGRAM
while main:

    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                fullscreen = not fullscreen
                if fullscreen:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    GenericW, GenericH = info.current_w, info.current_h
                    g1, g2 = 60, 40
                else:
                    pygame.display.set_mode(SIZE)
                    GenericW, GenericH = 900, 600

    time.sleep(2)
    MainScreen.waiting_msg()