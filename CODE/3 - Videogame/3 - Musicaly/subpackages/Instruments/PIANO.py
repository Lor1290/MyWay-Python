"""Progect Musicaly - PIANO program"""

#IMPORT
import time
import pygame
from os.path import join
from pygame.locals import *

#MAIN CLASS
class Piano:
    def Keyboard(song: list):  #SONG
        _Keyboard_ = [LA, SI, DO, RE, MI, FA, SOL]

        pygame.init()
        piano_screen = pygame.display.set_mode((880, 500))
        pygame.display.set_caption("Musicaly")
        pygame.display.set_icon("")
        

