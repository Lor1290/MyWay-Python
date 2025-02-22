import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

texture = pygame.image.load("AsteroideBig1.png")

rect = pygame.Rect(200, 200, 100, 100)

pygame.draw.rect(screen, texture, rect)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
