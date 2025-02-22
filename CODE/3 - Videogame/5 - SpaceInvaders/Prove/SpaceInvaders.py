#Progetto videogico 2: Riproduzione di Space Invaders
#Import
import pygame
from os.path import join
from pygame.locals import *
import time
#Definizioni
def introduzione():
    intro = True
    while intro:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    intro = False
        text4 = text1.render("S C O R E < 1 >      H I - S C O R E      S C O R E < 2 > ", True, "white")
        text8 = text1.render("P L A Y", True, "white")
        text9 = text1.render("S P A CE       I N V A D E R S", True, "white")
        text10 = text1.render("*S C O R E   A D V A N C E   T A B L E*", True, "white")
        screen.blit(text10,[190, 370])
        screen.blit(text9,[215, 240])
        screen.blit(text8,[285, 180])
        screen.blit(text5,[155, 50])
        screen.blit(text4,[75, 10])
        screen.blit(text6,[293, 50])
        screen.blit(text7,[425, 50])
        pygame.display.flip()
#Import dei file
pygame.init()
text1 = pygame.font.Font(r"../File per il gioco/Font/space_invaders.ttf", 19)
text2 = pygame.font.Font(r"../File per il gioco/Font/space_invaders.ttf", 50)
text3 = pygame.font.Font(r"../File per il gioco/Font/space_invaders.ttf", 100)
#Variabili
#Schermo
screen = pygame.display.set_mode((660, 780))
pygame.display.set_caption("Space Invaders")
screen.fill("black")
introduzione()
pygame.display.flip()