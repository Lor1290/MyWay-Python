#Progetto videogico 2: Riproduzione di Space Invaders
#Import
import pygame
from os.path import join
from pygame.locals import *
import time
#Import(delle funzioni)
timer = pygame.time.Clock()
#Definizioni
def pilImageToSurface(pilImage):
    mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
    return pygame.image.fromstring(data, size, mode).convert_alpha()

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    if pilImage.format == 'GIF' and pilImage.is_animated:
        for frame in ImageSequence.Iterator(pilImage):
            pygameImage = pilImageToSurface(frame.convert('RGBA'))
            frames.append(pygameImage)
    else:
        frames.append(pilImageToSurface(pilImage))
    return frames

def introduzione():
    run = True
    run1 = True
    run2 = True
    run3 = True
    run4 = True
    run5 = True
    run6 = True
    intro = True
    #Testi iniziali
    text4 = text1.render("S C O R E <  1  >      H I - S C O R E      S C O R E <  2  >", True, "white")
    screen.blit(text4,[77, 10])
    text13 = text1.render("0 0 0 0", True, "white")
    screen.blit(text13,[115, 40])
    text14 = text1.render("0 0 0 0", True, "white")
    screen.blit(text14,[290, 40])
    text15 = text1.render("0 0 0 0", True, "white")
    screen.blit(text15,[460, 40])
    text12 = text1.render("C R E D I T  0 0", True, "white")
    screen.blit(text12,[395, 710])
    #Ciclo
    while intro:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    intro = False
        #Ciclo intterno 1
        while run:
            global contatore
            text5 = "P L A Y"
            timer.tick(FPS)
            if contatore < velocità*len(text5):
                contatore +=1
            elif contatore >= velocità*len(text5):
                contatore = 0
                run = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text5_1 = text1.render(text5[0:contatore//velocità], True, "white")
            screen.blit(text5_1,[290, 180])
            pygame.display.flip()
        #Ciclo interno 2
        while run1:
            text6 = "S P A C E         I N V A D E R S"
            timer.tick(FPS)
            if contatore < velocità*len(text6):
                contatore +=1
            elif contatore >= velocità*len(text6):
                contatore = 0
                run1 = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text6_1 = text1.render(text6[0:contatore//velocità], True, "white")
            screen.blit(text6_1,[198, 240])
            pygame.display.flip()
        #Ciclo interno 3
        while run2:
            text7 = "*S C O R E   A D V A N C E   T A B L E*"
            timer.tick(FPS)
            if contatore < velocità*len(text7):
                contatore +=1
            elif contatore >= velocità*len(text7):
                contatore = 0
                run2 = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text7_1 = text1.render(text7[0:contatore//velocità], True, "white")
            screen.blit(text7_1,[156, 370])
            pygame.display.flip()
        #Ciclo interno 4
        while run3:
            screen.blit(i4, image4)
            text8 = "= ?   M Y S T E R Y"
            timer.tick(FPS)
            if contatore < velocità*len(text8):
                contatore +=1
            elif contatore >= velocità*len(text8):
                contatore = 0
                run3 = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text8_1 = text1.render(text8[0:contatore//velocità], True, "white")
            screen.blit(text8_1,[273, 414])
            pygame.display.flip()
        #Ciclo interno 5
        while run4:
            screen.blit(i1, image1)
            text9 = "= 3 0  P O I N T S"
            timer.tick(FPS)
            if contatore < velocità*len(text9):
                contatore +=1
            elif contatore >= velocità*len(text9):
                contatore = 0
                run4 = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text9_1 = text1.render(text9[0:contatore//velocità], True, "white")
            screen.blit(text9_1,[273, 464])
            pygame.display.flip()
        #Ciclo interno 6
        while run5:
            screen.blit(i3, image3)
            text10 = "= 2 0  P O I N Y S"
            timer.tick(FPS)
            if contatore < velocità*len(text10):
                contatore +=1
            elif contatore >= velocità*len(text10):
                contatore = 0
                run5 = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text10_1 = text1.render(text10[0:contatore//velocità], True, "white")
            screen.blit(text10_1,[273, 514])
            pygame.display.flip()
        #Ciclo interno 7
        while run6:
            screen.blit(i2, image2)
            
            text11 = "= 1 0   P O I N T S"
            timer.tick(FPS)
            if contatore < velocità*len(text11):
                contatore +=1
            elif contatore >= velocità*len(text11):
                contatore = 0
                run5 = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text11_1 = text1.render(text11[0:contatore//velocità], True, "white")
            screen.blit(text11_1,[273, 564])
            pygame.display.flip()
        #Variabili dei cicli interni    
        text5_1 = text1.render("", True, "white")
        text6_1 = text1.render("", True, "white")
        text7_1 = text1.render("", True, "white")
        text8_1 = text1.render("", True, "white")
        text9_1 = text1.render("", True, "white")
        text10_1 = text1.render("", True, "white")
        text11 = text1.render("", True, "white") 
        pygame.display.flip()
#Import dei file
pygame.init()
text1 = pygame.font.Font(r"../File per il gioco/Font/space_invaders.ttf", 19)
text2 = pygame.font.Font(r"../File per il gioco/Font/space_invaders.ttf", 50)
text3 = pygame.font.Font(r"../File per il gioco/Font/space_invaders.ttf", 100)
i1 = pygame.image.load(join(r"../File per il gioco/Mostri/SpaceInvader2.png"))
i2 = pygame.image.load(join(r"../File per il gioco/Mostri/SpaceInvaders1.png"))
i3 = pygame.image.load(join(r"../File per il gioco/Mostri/SpaceInvaders2.png"))
i4 = pygame.image.load(join(r"../File per il gioco/Mostri/SpaceInvaders3.png"))
#Variabili grafiche
i1 = pygame.transform.smoothscale(i1, (45, 35))
image1 = i1.get_rect()
image1.center = (245, 470)
i2 = pygame.transform.smoothscale(i2, (45, 35))
image2 = i2.get_rect()
image2.center = (245, 570)
i3 = pygame.transform.smoothscale(i3, (45, 35))
image3 = i3.get_rect()
image3.center = (245, 520)
i4 = pygame.transform.smoothscale(i4, (55, 35))
image4 = i4.get_rect()
image4.center = (243, 420)

image = Image.open(rr"../File per il gioco/Mostri/SpaceInvaders1.png")
draw = ImageDraw.Draw(image)
mode = image.mode
size = image.size
data = image.tortring()
immagins = pygame.image.fromstring(data, size, mode)
#variabili
contatore = 0
velocità = 4
FPS = 60
#Schermo
screen = pygame.display.set_mode((660, 780))
pygame.display.set_caption("Space Invaders")
screen.fill("black")
introduzione()
pygame.display.flip()
#Logica di gioco
#Comandi
#Gli 'output'