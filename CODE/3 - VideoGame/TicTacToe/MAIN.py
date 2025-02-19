#Light Green Comment: Main 
#Red Comment: Assignment
#Orange comment: Method, cicle...

#* Module and Libreries
import sys
import pygame 
import time as tm
from pygame.locals import *
from os.path import join as jn

pygame.init() #Init

#! Global variable
global fullscreen
global width
global height
width, height = 550, 700

#! Sound
Bang = pygame.mixer.Sound(jn(r"Sound/Bang!.mp3"))
# ! Font
FontIntro = pygame.font.Font(r"Font/IntroFont2.ttf", 70)
# ! Image
FavIcon = pygame.image.load(jn(r"Image/TicTacToeIcon.png"))

#* Inizializating
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Tic-Tac-Toe")
pygame.display.set_icon(FavIcon)
Resolution  = pygame.display.Info()

#* All definition / Class
class VideoGame: #TODO: MAIN CLASS

    def __init__(self, Width = Resolution.current_w, Height = Resolution.current_h): #TODO: Introduce the class
        self.W = Width
        self.H = Height             
    def intro(self): #TODO: Intro-Film     
        intro = True
        while intro:      
            def color_to_color(R, G, B, r, g, b): #TODO: Morph Effect           
                while R <= r and G <= g and B <= b:                
                    
                    for ev in pygame.event.get():
                        if ev.type == QUIT:
                            pygame.quit()  
                            sys.exit()
                    
                    screen.fill((R, G, B))
                    pygame.display.update()
                    tm.sleep(0.04)

                    R, G, B = R + 3, G + 3, B + 3
                
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.quit()  
                    sys.exit()

            color_to_color(0, 0, 0, 123, 130, 137)
            tm.sleep(1)

            #Tic
            Tic = FontIntro.render("TIC", True, "Black")
            Tic_s = Tic.get_rect()
            Tic_s.center = width/2, height/5 - 20
            
            #Tac
            Tac = FontIntro.render("TAC", True, "Black")
            Tac_s = Tac.get_rect()
            Tac_s.center = width/2, (height/5)*2 - 20
            
            #Toe
            Toe = FontIntro.render("TOE", True, "Black")
            Toe_s = Toe.get_rect()
            Toe_s.center = width/2, (height/5)*3 - 20
            
            screen.blit(Tic, Tic_s)
            pygame.display.update()
            Bang.play()
            tm.sleep(1.5)
            screen.blit(Tac, Tac_s)
            pygame.display.update()
            Bang.play()
            tm.sleep(1.5)
            screen.blit(Toe, Toe_s)
            pygame.display.update()
            Bang.play()
            tm.sleep(1.5)

#! Information about the game
C = pygame.time.Clock()
#! variables
cicle = True
fullscreen = False
TicTacToe = VideoGame()
#! Main cicle     
TicTacToe.intro()
pygame.quit()
