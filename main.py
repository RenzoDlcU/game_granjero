import pygame, sys
from pygame.locals import *

pygame.init()
size = 800,700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego del Granjero - FIS UNICA")

fondo = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/fondo.jpg").convert()
fondoP = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/fondop.jpg").convert()
fondoG = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/win.jpg").convert()
zorro = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/zorro.png").convert_alpha()
maiz = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/maiz.png").convert_alpha()
gallina = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/gallina.png").convert_alpha()
barco = pygame.image.load("C:/Users/renzo/Desktop/juego/resource/barco.png").convert_alpha()


zorro_iz = 1
zorro_de = 0
maiz_iz = 1
maiz_de = 0
gallina_iz = 1
gallina_de = 0
barcoP = 0
barcoC = 0
##
barco_iz_z = 0
barco_de_z = 0
barco_iz_m = 0
barco_de_m = 0
barco_iz_g = 0
barco_de_g = 0


ganador = False
perdedor = False






while True:
    #COMPROBAR GANADOR
    if zorro_iz == 0 and maiz_iz == 0 and gallina_iz == 0:
        if zorro_de == 1 and maiz_de == 1 and gallina_de == 1:
            ganador = True
    #COMPROBAR PERDEDOR
    if barcoC == 0:
        if zorro_iz == 1 and gallina_iz == 1 and maiz_iz == 0:
            perdedor = True
        if zorro_de == 1 and gallina_de == 1 and maiz_de == 0:
            perdedor = True
        if gallina_iz == 1 and maiz_iz == 1 and zorro_iz == 0:
            perdedor = True
        if gallina_de == 1 and maiz_de == 1 and zorro_de == 0:
            perdedor = True


    if perdedor == True:
        screen.blit(fondoP,(0,0))
        zorro_iz =0
        zorro_de = 0
        maiz_iz = 0
        maiz_de = 0
        gallina_iz = 0
        gallina_de = 0

    elif ganador == True:
        screen.blit(fondoG,(0,0))
        zorro_iz = 0
        zorro_de = 0
        maiz_iz = 0
        maiz_de = 0
        gallina_iz = 0
        gallina_de = 0
    else:
        screen.blit(fondo,(0,0))


    if barcoP == 0:
        screen.blit(barco,(160,500))
        if barco_iz_z == 1:
            screen.blit(zorro,(190,490))
        if barco_iz_m == 1:
            screen.blit(maiz,(190,490))
        if barco_iz_g == 1:
            screen.blit(gallina,(190,490))
    if barcoP == 1:
        screen.blit(barco,(490,500))
        if barco_de_z == 1:
            screen.blit(zorro,(520,490))
        if barco_de_m == 1:
            screen.blit(maiz,(520,490))
        if barco_de_g == 1:
            screen.blit(gallina,(520,490))


    if zorro_iz == 1:
        screen.blit(zorro,(0,390))
    if maiz_iz == 1:
        screen.blit(maiz,(80,390))
    if gallina_iz == 1:
        screen.blit(gallina,(160,390))

    if zorro_de == 1:
        screen.blit(zorro,(520,390))
    if maiz_de == 1:
        screen.blit(maiz,(600,390))
    if gallina_de == 1:
        screen.blit(gallina,(680,390))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_x:
                if barcoC == 0:
                    if barcoP == 0:
                        barco_iz_z = 1
                    if barcoP == 1:
                        barco_de_z = 1
                    zorro_iz = 0
                    zorro_de = 0
            elif event.key == K_z:
                if barcoP == 0:
                    zorro_iz = 1
                    zorro_de = 0
                    barco_iz_z = 0
                if barcoP == 1:
                    zorro_iz = 0
                    zorro_de = 1
                    barco_de_z = 0

            elif event.key == K_m:
                if barcoC == 0:
                    if barcoP == 0:
                        barco_iz_m = 1
                    if barcoP == 1:
                        barco_de_m = 1
                    maiz_iz = 0
                    maiz_de = 0
            elif event.key == K_n:
                if barcoP == 0:
                    maiz_iz = 1
                    maiz_de = 0
                    barco_iz_m = 0
                if barcoP == 1:
                    maiz_iz = 0
                    maiz_de = 1
                    barco_de_m = 0

            elif event.key == K_g:
                if barcoC == 0:
                    if barcoP == 0:
                        barco_iz_g = 1
                    if barcoP == 1:
                        barco_de_g = 1
                    gallina_iz = 0
                    gallina_de = 0
            elif event.key == K_f:
                if barcoP == 0:
                    gallina_iz = 1
                    gallina_de = 0
                    barco_iz_g = 0
                if barcoP == 1:
                    gallina_iz = 0
                    gallina_de = 1
                    barco_de_g = 0


            elif event.key == K_RIGHT:
                barcoP = 1
            elif event.key == K_LEFT:
                barcoP = 0


    pygame.display.update()
