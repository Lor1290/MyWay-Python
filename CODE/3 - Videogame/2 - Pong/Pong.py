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
def punteggio2(punteggio2):
    text = text1.render(str(punteggio), True, "white")
    screen.blit(text, [200, 30])
def punteggio3(punteggio3):
    text = text1.render(str(punteggio1), True, "white")
    screen.blit(text, [655, 30])
def introduzione():
    suono4.play()
    intro = True
    while intro:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_1:
                    suono4.stop()
                    suono5.play() 
                    global val
                    val += 1
                    intro = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_2:
                    suono4.stop()
                    suono5.play()
                    global val1
                    val1 += 2
                    intro = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_3:
                    suono4.stop()
                    suono5.play()
                    intro = False
        screen.fill("black")
        text = text2.render("PONG", True, "white")
        text11 = text3.render("By @Lorenzo Polis", True, "White")
        text4 = text3.render("scegli la tua modalita di gioco:", True,"white")
        text5 = text3.render("'premi 1 se vuoi fare una partita classica'", True, "white")
        text6 = text3.render("'premi 2 se vuoi fare una partita corta'", True, "White")
        text7 = text3.render("'premi 3 se vuoi fare una partita INFINITA'", True, "white")
        text8 = text3.render("(non consigliata ai deboli di cuore)", True, "white")
        text9 = text3.render("(per mettere in pausa il gioco, premi 'p')", True, "white")
        text210 = text3.render("(per riavviare la partita, premi 'r')", True, "white")
        screen.blit(text11,[321, 190])
        screen.blit(text, [300, 75])
        screen.blit(text4,[225, 270])
        screen.blit(text5,[150, 310])
        screen.blit(text6, [172, 350])
        screen.blit(text7, [150, 390])
        screen.blit(text8, [200, 420])
        screen.blit(text9, [10, 535])
        screen.blit(text210, [10, 565]) 
        pygame.display.flip()    
def vittoria1():
    suono7.play(-1)
    vittoria = True
    while vittoria:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_s:
                    vittoria = False
                if ev.key == pygame.K_n:
                    pygame.quit()
                    quit()
        screen.fill("black")
        text11 = text2.render("GAME OVER", True, "white")
        text12 = text3.render("Ha vinto il giocatore 1!", True, "white")
        text13 = text3.render("volete fare un'altra partita? (s/n)", True, "white")
        screen.blit(text11, [115, 100])
        screen.blit(text12, [275, 240])
        screen.blit(text13, [175, 565])
        pygame.display.flip()
def vittoria2():
    suono7.play(-1)
    vittoria = True
    while vittoria:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_s:
                    vittoria = False
                if ev.key == pygame.K_n:
                    pygame.quit()
                    quit()
        screen.fill("black")
        text11 = text2.render("GAME OVER", True, "white")
        text12 = text3.render("Ha vinto il giocatore 2!", True, "white")
        text13 = text3.render("volete fare un'altra partita? (s/n)", True, "white")
        screen.blit(text11, [115, 100])_w
        screen.blit(text12, [275, 240])
        screen.blit(text13, [175, 565])
        pygame.display.flip()
def riavvio():
    riavvio = True
    while riavvio:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygamequit()
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_r:
                    riavvio = False
        
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pong")
C = pygame.time.Clock()

val = 0
val1 = 0
text3 = pygame.font.Font(r"./File per il videogame/Retro Gaming.ttf", 25)
text2 = pygame.font.Font(r"./File per il videogame/Retro Gaming.ttf", 100)
text1 = pygame.font.Font(r"./File per il videogame/Retro Gaming.ttf", 50)
suono4 = pygame.mixer.Sound(join(r"./File per il videogame/all-galaga-1981-sounds_lYvmh6E6.mp3"))
suono5 = pygame.mixer.Sound(join(r"./File per il videogame/all-galaga-1981-sounds_lnC2cF9l.mp3"))
suono7 = pygame.mixer.Sound(join(r"./File per il videogame/all-galaga-1981-sounds_Je5Lq9HL.mp3"))
suono8 = pygame.mixer.Sound(join(r"./File per il videogame/all-galaga-1981-sounds_c7ZeQXsh.mp3"))
introduzione()
suono6 = pygame.mixer.Sound(join(r"./File per il videogame/all-galaga-1981-sounds_lYvmh6E6.mp3"))
punteggio = 0
punteggio1 = 0
FPS = 60
TIMERSHOT = pygame.event.custom_type()
pygame.time.set_timer(TIMERSHOT, 10000)
suono3 = pygame.mixer.Sound(join(r"./File per il videogame/pong-sound-effects_KWvqYMLz.mp3"))
suono2 = pygame.mixer.Sound(join(r"./File per il videogame/pong-sound-effects_JEuRT93q.mp3"))
suono1 = pygame.mixer.Sound(join(r"./File per il videogame/pong-sound-effects_Bktmp9yo.mp3"))
surf_tile = pygame.image.load(join(r"./File per il videogame/Untitled 02-25-2023 09-38-55.png"))
surf_tile = pygame.transform.smoothscale(surf_tile, (900, 600))
surf_back = screen.copy()
tile_surface(surf_tile, surf_back)
n3 = pygame.image.load(join(r"./File per il videogame/Immagine 2023-02-25 223940.png"))
n3 = pygame.tsransform.smoothscale(n3, (15, 70))
n4 = n3.get_rect()
n4.center = (30, 300)
n5 = pygame.image.load(join(r"./File per il videogame/Immagine 2023-02-25 223940.png")) 
n5 = pygame.transform.smoothscale(n5, (15, 70))
n6 = n5.get_rect()
n6.center = (870, 300)
n = pygame.image.load(join(r"./File per il videogame/Immagine 2023-02-25 2257591.png"))
n = pygame.transform.smoothscale(n, (15, 15))
n1 = n.get_rect()
n1.center = (425, 300)
velx = 4
vely = 4
n1V = [velx,vely]
pressed = None
pressed1 = None
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
            if ev.key == pygame.K_p:
                suono5.play()
                screen.fill("black")
                text27 = text2.render("PAUSA", True, "white")
                text21 = text3.render("Premi la BARRA SPAZZIATRICE per continuare", True, "white")
                screen.blit(text27, [250, 225])
                screen.blit(text21, [110, 565])
                pygame.display.flip()
                pausa()
            if ev.key == pygame.K_r:
                pygame.time.set_timer(TIMERSHOT, 10000)
                punteggio = 0
                punteggio1 = 0
                FPS = 60
                n1.center = (425, 300)
                n4.center = (30, 300)
                n6.center = (870, 300)
                n1V[0] *= -1
        elif ev.type == TIMERSHOT:
            FPS += 15
    
                
    if n1.left < 0:
        suono3.play()
        time.sleep(2)
        n1.center = (425, 300)
        n4.center = (30, 300)
        n6.center = (870, 300)
        FPS = 60
        time.sleep(1)
        n1V[0] *= -1
        punteggio1 += 1
        pygame.time.set_timer(TIMERSHOT, 10000)
    if n1.right > screen.get_width():
        suono3.play()
        time.sleep(2)
        n1.center = (425, 300)
        n4.center = (30, 300)
        n6.center = (870, 300)
        FPS = 60
        time.sleep(1)
        n1V[0] *= -1
        punteggio += 1
        pygame.time.set_timer(TIMERSHOT, 10000)
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
    if pressed == K_DOWN and n6.bottom < (599):
        n6.y += 5
    if pressed1 == K_w and n4.top > (0): 
        n4.y -= 5
    if pressed1 == K_s and n4.bottom < (599):
        n4.y += 5
    if val == 1:
        if punteggio == 21:
            vittoria1()
            punteggio1 = 0
            punteggio = 0
            suono7.stop()
            introduzione()
        if punteggio1 == 21:
            vittoria2()  
            punteggio1 = 0
            punteggio = 0
            suono7.stop()
            introduzione()
    if val1 == 2:
        if punteggio == 11:
            vittoria1()
            punteggio1 = 0
            punteggio = 0
            suono7.stop()
            introduzione()
        if punteggio1 == 11:
            vittoria2()  
            punteggio1 = 0
            punteggio = 0            suono7.stop()
            introduzione()
                    
    n1.x += n1V[0]
    n1.y += n1V[1]
    screen.blit(surf_back, (0,0))
    screen.blit(n, n1)
    screen.blit(n3, n4)
    screen.blit(n5, n6)
    punteggio2(punteggio2)
    punteggio3(punteggio3)
    pygame.display.flip()
    C. tick(FPS)
pygame.quit()
