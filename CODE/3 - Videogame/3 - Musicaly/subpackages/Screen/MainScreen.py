"""Progect Musicaly - WALLPAPER program"""

#IMPORT
import time
import pygame
from os.path import join
from pygame.locals import *

#VARIABLE GOLBAL
global fullscreen
global main_screen
global GenericW
global GenericH
global Gfont

#LOAD
IntroMusic = pygame.mixer.Sound(join("Music/Intro.mp3"))

#MAIN CLASS
class MainScreen:
    def waiting_msg():

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

        IntroMusic.play(-1)
        if fullscreen:
            IntroFont = pygame.font.Font("font/IntroFont.ttf", Gfont[6])
            ImageFont = pygame.font.Font("font/ImageFont.ttf", Gfont[4])
        else:
            IntroFont = pygame.font.Font("font/IntroFont.ttf", Gfont[4])
            ImageFont = pygame.font.Font("font/ImageFont.ttf", Gfont[2])

        text1 = IntroFont.render("M U S I C A L Y", True, "white")
        text2 = IntroFont.render("W E   T R A N S L A T E   T H E   R E A L   M U S I C", True, "white")

        first = text1.get_rect()
        first.center = GenericW/2, GenericH/2
        second = text2.get_rect()
        second.center = GenericW/2, GenericH/2 + 100

        main_screen.blit(text1, first)
        main_screen.blit(text2, second)
        pygame.display.flip()


    
