import pygame, random, time
from spaceInv1 import Spaceinvader1
from spaceInv2 import Spaceinvader2

#------------------------------ definició de la funció menú principal
def menu_principal() :
    global sortida, sortir
    sortida, sortir = False, False
    yellow1, yellow2, orange1, orange2 = (224, 224, 6), (224, 224, 6), (244, 97, 6), (244, 97, 6)
    while not sortida :
        for event0 in pygame.event.get() :
            if event0.type == pygame.QUIT :
                pygame.quit()
                quit()
            elif event0.type == pygame.KEYDOWN :
                if event0.key == pygame.K_ESCAPE :
                    pygame.quit()
                    quit()
        win.blit(fons_portada, (0, 0))
        tipografia = pygame.font.Font(None, int(height/2))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if (width*3 > mouse[0]  > width) and (alsada - height*5  > mouse[1]  > alsada - height*6) :
            yellow1 = (152, 152, 11)
            orange1 = (152, 71, 11)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                score1, level = 0, 1
                Spaceinvader1()
        elif (width*6.5 > mouse[0] > width*4.5) and (alsada - height*5 > mouse[1] > alsada - height*6)  :
            yellow2 = (152, 152, 11)
            orange2 = (152, 71, 11)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                score1, level = 0, 1
                Spaceinvader2()       
        else:
            orange1, orange2 = (244, 97, 6), (244, 97, 6)
            yellow1, yellow2  = (244, 224, 6), (244, 224, 6)
        # dibuix dels dos botons
        pygame.draw.rect(win, yellow1, [width, alsada-6*height, 2*width, height/2], 0)
        pygame.draw.rect(win, orange1, [width, alsada-5.5*height, 2*width, height/2], 0)    
        other= tipografia.render(" 1 player", 1, (0, 0 ,0))
        win.blit(other, (width + vel*2, alsada-6*height+5*vel))
        pygame.draw.rect(win, yellow2, [4.5*width, alsada-6*height, 2*width, height/2], 0)
        pygame.draw.rect(win, orange2, [4.5*width, alsada-5.5*height, 2*width, height/2], 0)
        quite= tipografia.render(" 2 players", 1, (0, 0 ,0))
        win.blit(quite, (4.5*width + vel*2, alsada-6*height+5*vel))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

#------------------------------ programa principal
pygame.init()
#rdn = datetime.now()
#random.seed(rdn.second)
xoc_so = pygame.mixer.Sound("crash.wav")
# valors d'amplada i alçada de la nostra finestre
amplada = 900
alsada = 750
win = pygame.display.set_mode((amplada, alsada))
clock = pygame.time.Clock()
# nom del joc
pygame.display.set_caption("Space invader")
# inicialització de variables
width = int(amplada/7.5)
height = int(alsada/6.25)
vel = int(alsada/100)

green, red  = (0, 222, 0), (222, 0, 0)
carpeta =".\\spaceInvader\\"
portada = "title.png"
mach2 = "machine0.png"
fons_portada = pygame.image.load(carpeta + portada).convert_alpha()
fons_portada = pygame.transform.scale(fons_portada, (amplada, alsada))
pl_mach2 = pygame.image.load(carpeta + mach2).convert_alpha()
pl_mach2 = pygame.transform.scale(pl_mach2, (width, height))


