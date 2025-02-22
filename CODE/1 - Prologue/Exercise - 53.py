import pygame
from pygame.locals import *
from os.path import join
import time
def pausa():
    pausa = True
    while pausa:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    pausa = False
def tile_surface(surf_little, surf_big):       
    w_little = surf_little.get_width()        
    h_little = surf_little.get_height()        
    w_big = surf_big.get_width()               
    h_big = surf_big.get_height()             
    for y in range(0, h_big, h_little):        
        for x in range(0, w_big, w_little):    
            surf_big.blit(surf_little, (x, y))

screen = pygame.display.set_mode((700, 450))
pygame.display.set_caption("Pong")
C = pygame.time.Clock()


suono3 = pygame.mixer.Sound(join(r"C:/Users/lor12/OneDrive/Desktop/Python/Pygame/Effects/pong-sound-effects_KWvqYMLz.mp3"))
suono2 = pygame.mixer.Sound(join(r"C:/Users/lor12/OneDrive/Desktop/Python/Pygame/Effects/pong-sound-effects_JEuRT93q.mp3"))
suono1 = pygame.mixer.Sound(join(r"C:/Users/lor12/OneDrive/Desktop/Python/Pygame/Effects/pong-sound-effects_Bktmp9yo.mp3"))
surf_tile = pygame.image.load(join(r"C:/Users/lor12/OneDrive/Immagini/Rullino/Polish_20230222_193553823.jpg"))
surf_tile = pygame.transform.smoothscale(surf_tile, (700, 450))
surf_back = screen.copy()
tile_surface(surf_tile, surf_back)
n3 = pygame.image.load(join(r"C:/Users/lor12/OneDrive/Immagini/Rullino/BackgroundEraser_20230222_194039838.png"))
n3 = pygame.transform.smoothscale(n3, (15, 60))
n4 = n3.get_rect()
n4.center = (30, 225)
n5 = pygame.image.load(join(r"C:/Users/lor12/OneDrive/Immagini/Rullino/BackgroundEraser_20230222_194039838.png")) 
n5 = pygame.transform.smoothscale(n5, (15, 60))
n6 = n5.get_rect()
n6.center = (669, 225)
n = pygame.image.load(join(r"C:/Users/lor12/OneDrive/Immagini/Rullino/BackgroundEraser_20230222_193945284.png"))
n = pygame.transform.smoothscale(n, (15, 15))
n1 = n.get_rect()
n1.center = (350, 225)
n1V = [3,3]
pressed = None
pressed1 = None
pressed2 = None
collisione = pygame.Rect.colliderect(n1, n4)
collisione1 = pygame.Rect.colliderect(n1, n6)

fatto = False
while not fatto:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            fatto = True
        elif ev.type == KEYDOWN and ev.key in (K_UP, K_DOWN):
            pressed = ev.key
        elif ev.type == KEYUP and ev.key == pressed:
            pressed = None
        elif ev.type == KEYDOWN and ev.key in (K_w, K_s):
            pressed1 = ev.key
        elif ev.type == KEYUP and ev.key == pressed1:
            pressed1 = None
        elif ev.type == KEYDOWN:
            if ev.key == pygame.K_1:
                screen.fill("black")
                n7 = pygame.image.load(join(r"C:/Users/lor12/OneDrive/Desktop/Python/Pygame/Sprites/eifercf.png"))
                n8 = n7.get_rect()
                n8.center = (350, 225)
                n9 = pygame.image.load(join(r"C:/Users/lor12/OneDrive/Desktop/Python/Pygame/Sprites/logo.png"))
                n10 = n9.get_rect()
                n10.center = (350, 425)
                screen.blit(n7, n8)
                screen.blit(n9, n10)
                pygame.display.flip()
                pausa()
                
            
    if n1.left < 0 or n1.right > screen.get_width():
        suono3.play()
        time.sleep(2)
        n1.center = (350, 225)
        n4.center = (30, 225)
        n6.center = (669, 225)
        time.sleep(1)
        n1V[0] *= -1
        
    if n1.top < 0 or n1.bottom > screen.get_height():
        suono2.play()
        n1V[1] *= -1
    if n4.colliderect(n1):
        suono1.play()
        n1V[0] *= -1
    if n6.colliderect(n1):
        suono1.play()
        n1V[0] *= -1
    if pressed == K_UP and n6.top > (0):
        n6.y -= 5
    if pressed == K_DOWN and n6.bottom < (449):
        n6.y += 5
    if pressed1 == K_w and n4.top > (0): 
        n4.y -= 5
    if pressed1 == K_s and n4.bottom < (449):
        n4.y += 5
                   
    n1.x += n1V[0]
    n1.y += n1V[1]
    screen.blit(surf_back, (0,0))
    screen.blit(n, n1)
    screen.blit(n3, n4)
    screen.blit(n5, n6)
    pygame.display.flip()

    C. tick(60)

pygame.quit()
