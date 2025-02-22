#Import
from pygame.locals import *
from os.path import join
from curses import wrapper
import random
import pygame
import time
import sys
import curses

#Schermo
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Variabili
intro = True

#Immagini
Surf_Tetris_1 = pygame.image.load(join("photo/Tetris_1.png"))
Rect_Tetris_1 = Surf_Tetris_1.get_rect()
Rect_Tetris_1 = ((650, 250))
Surf_Tetris_2 = pygame.image.load(join("photo/Tetris_2.png"))
Rect_Tetris_2 = Surf_Tetris_2.get_rect()
Rect_Tetris_2 = ((650, 250))
Surf_Tetris_3 = pygame.image.load(join("photo/Tetris_3.png"))
Rect_Tetris_3 = Surf_Tetris_3.get_rect()
Rect_Tetris_3 = ((650, 250))
Surf_Tetris_4 = pygame.image.load(join("photo/Tetris_4.png"))
Rect_Tetris_4 = Surf_Tetris_4.get_rect()
Rect_Tetris_4 = ((650, 250))

#Suoni
sound_1 = pygame.mixer.Sound(join("sound/nintendo-game-boy-intro_nIvrw1x5.mp3"))

#Font
Font_1 = pygame.font.Font("font/TETRIS.TTF", 50)
Font_2 = pygame.font.Font("font/Early GameBoy.ttf", 80)

#testi
text_1 = Font_2.render("THECOMPANY©", True, "black") 
text_2 = Font_1.render("T", True, "white")
text_3 = Font_1.render("E", True, "white")
text_4 = Font_1.render("T", True, "white")
text_5 = Font_1.render("R", True, "white")
text_6 = Font_1.render("I", True, "white")
text_7 = Font_1.render("S", True, "white")

#Definizioni    

#Schermo
def tile_surface(surf_little, surf_big):
    w_little = surf_little.get_width()
    h_little = surf_little.get_height()        
    w_big = surf_big.get_width()               
    h_big = surf_big.get_height()             
    for y in range(0, h_big, h_little):
        for x in range(0, w_big, w_little):
            surf_big.blit(surf_little, (x, y))

#Dissolvenza entrata/uscita 1
def fade_1(width, height, position, color_1, color_2): 

    #Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    fade = pygame.Surface((width, height))
    fade.fill(color_1)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.fill(color_2)
        screen.blit(fade, (position , 0))
        pygame.display.update()
        pygame.time.delay(5)

    Y = 900
    while Y != 350:
        screen.blit(fade, (position , 0))
        screen.blit(text_1, [350, Y])
        pygame.display.update()
        pygame.time.delay(20)
        Y -= 10

    sound_1.play()
    time.sleep(1)

    BackGround = pygame.Surface((width, height)) 
    for alpha in range(0, 300):
        BackGround.set_alpha(alpha)
        fade.fill(color_2)
        screen.blit(BackGround, (position , 0))
        pygame.display.update()
        pygame.time.delay(10)

#Dissolvenza entrata/uscita 2
def fade_2(width, height, position, color_1, color_2):

    #Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    fade = pygame.Surface((width, height))
    fade.fill(color_1)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.fill(color_2)
        screen.blit(fade, (position , 0))
        pygame.display.update()
        pygame.time.delay(5)

    for i in range(random.randint(30, 40)):

        screen.blit(Surf_Tetris_1, Rect_Tetris_1)
        pygame.display.update()
        time.sleep(1)
        screen.blit(Surf_Tetris_2, Rect_Tetris_2)
        pygame.display.update()
        time.sleep(1)
        screen.blit(Surf_Tetris_3, Rect_Tetris_3)
        pygame.display.update()
        time.sleep(1)
        screen.blit(Surf_Tetris_4, Rect_Tetris_4)
        pygame.display.update()
        time.sleep(1)

    BackGround = pygame.Surface((width, height)) 
    for alpha in range(0, 300):
        BackGround.set_alpha(alpha)
        screen.fill(color_2)
        screen.blit(BackGround, (position , 0))
        pygame.display.update()
        pygame.time.delay(10)
            
#Pausa
def break_1():
    pausa = True

    while pausa:

        #Eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
#Ciclo principale                        
while intro:

    #Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                  pygame.quit()
                  sys.exit()

    #Intro Gameboy
    time.sleep(2)
    fade_1(1340, 1080, 100, "white", "black")
    fade_2(1340, 1080, 100, "black", "black")
    
       
pygame.quit()
