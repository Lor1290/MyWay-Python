import pygame
from pygame.locals import *
from os.path import join
import keyboard
def tile_surface(surf_little, surf_big):       
    w_little = surf_little.get_width()        
    h_little = surf_little.get_height()        
    w_big = surf_big.get_width()               
    h_big = surf_big.get_height()             
    for y in range(0, h_big, h_little):        
        for x in range(0, w_big, w_little):    
            surf_big.blit(surf_little, (x, y))


pygame.init()
screen = pygame.display.set_mode((700, 450))
C = pygame.time.Clock()

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
n1.topleft = (350, 225)
n1V = [3,3]

done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
       

    if n1.left < 0 or n1.right > screen.get_width():
        n1V[0] *= -1
    if n1.top < 0 or n1.bottom > screen.get_height():
        n1V[1] *= -1
   

    n1.x += n1V[0]
    n1.y += n1V[1]
    screen.blit(surf_back, (0,0))
    screen.blit(n, n1)
    screen.blit(n3, n4)
    screen.blit(n5, n6)
    pygame.display.flip()

    C. tick(60)

pygame.quit()
    

    




