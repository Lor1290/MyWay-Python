import pygame
from pygame.locals import *

pygame.init()
screen= pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tetris")

quadrato = pygame.Surface((50, 50))
quadrato.fill("red")
quadrato1 = quadrato.get_rect()
quadrato2 = [1, 1]

falso = False
while not falso:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
    if quadrato1.left < 0 or quadrato1.right > 800:
        quadrato2[0] *= -1
    if quadrato1.top < 0 or quadrato1.bottom > 600:
        quadrato2[1] *= -1

    quadrato1.x += quadrato2[0]
    quadrato1.y += quadrato2[1]
    screen.fill("white")
    screen.blit(quadrato, quadrato1)
    pygame.display.flip()
pygame.quit()
  
    
