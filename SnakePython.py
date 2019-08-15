#-*- coding: utf-8-*-
#importarem els mòduls pygame per la finestre del joc, random i time per trobar els nombres
#aleatoris, finalment datetime ens trobarà una posició en la sèrie aleatoria
import pygame, time, random
from datetime import datetime
# posició nova aleatòria
random.seed(datetime.now().second*43)
# começament de la finestre pygame
pygame.init()
# so del xoc amb una pared o la cua de la serp
#crash_sound = pygame.mixer.Sound(".\\snakePython\\crash.wav")
pygame.mixer.music.load("crash.mp3")

# valors d'amplada i alçada de la nostre finestre
amplada = 950
alsada = 690
finestre = pygame.display.set_mode((amplada, alsada))
# nom del joc
pygame.display.set_caption("snake python")
# variable de repetició del bucle pygame
moment = pygame.time.Clock()
# inicialització de variables
ample = int(amplada/60)
alt = int(alsada/30)
vel = int(amplada/190)
sortir, run, ordenada, abcisa, pause, aleatori, crash = False, True, True, True, False, True, False 
x_canvi, y_canvi = 0, 0
cont_Ale = 1
x_Ale = ample + vel
y_Ale = alt + vel
x_canvi += vel
x, y = [], []
y = []
level, score1 = 1, 0
# bucle de tornar a començar
while not(sortir) :
    for i in range(0,81) :
        x.append(amplada/2)
        y.append(alsada/2)
    run = True
    # bucle de redibuixar la nostra finestre pygame
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sortir = True
            elif event.type == pygame.KEYDOWN  :
                if event.key == pygame.K_ESCAPE :
                    run = False
                    sortir = True
                if event.key == pygame.K_RIGHT and ordenada == True :
                    y_canvi = 0
                    x_canvi += vel
                    abcisa, ordenada = True, False
                if event.key == pygame.K_LEFT and ordenada  == True:
                    y_canvi = 0
                    x_canvi -= vel
                    abcisa, ordenada = True, False
                if event.key == pygame.K_UP and abcisa == True :
                    x_canvi = 0
                    y_canvi -= vel
                    abcisa, ordenada = False, True
                if event.key == pygame.K_DOWN and abcisa == True :
                    abcisa, ordenada = False, True
                    x_canvi = 0
                    y_canvi += vel
                if event.key == 112 :
                    pause = True
        while pause :
            for event2 in pygame.event.get() :
                if event2.type  == pygame.QUIT :
                    pause = False
                elif event2.type == pygame.KEYDOWN :
                    if event2.key == pygame.K_RIGHT or event2.key == pygame.K_LEFT or event2.key == pygame.K_UP :
                        pause = False
                    if event2.key == pygame.K_DOWN or event2.key == pygame.K_ESCAPE or event2.key == 112 :
                        pause = False
            tipografia = pygame.font.SysFont("serif", int(amplada/15))
            texte = tipografia.render("PAUSED", 1, (121, 121, 121))
            finestre.blit(texte, (amplada/5, alsada/3))            
            pygame.display.update()
            moment.tick(30)
        finestre.fill((184, 254, 114))
        if x[0] >= amplada*0.7 :
            #x[0] = ample + vel
            crash = True
        if x[0] <= ample :
            #x[0] = amplada*0.7 - vel
            crash = True
        if y[0] >= alsada*0.9 :
            #y[0] = alt + vel
            crash = True
        if y[0] <= alt :
            #y[0] = alsada*0.9 - vel
            crash = True
        index = 80
        while index > 0 :
            x[index] = x[index-1]
            y[index] = y[index-1]
            index -= 1
        x[0] += x_canvi
        y[0] += y_canvi    
        if x[0] <= x_Ale + ample/2 <= x[0]+ample :
            if y[0] <= y_Ale + alt/2 <= y[0]+alt :
                aleatori = True
                score1 += cont_Ale
                cont_Ale += 1
                
        if aleatori == True :
            x_Ale = random.randrange(ample + vel, amplada*0.7 - vel)
            y_Ale = random.randrange(alt + vel, alsada*0.9 - vel)
            aleatori = False

        tipografia1 = pygame.font.SysFont("serif", int(alt))
        aleatori = tipografia1.render("{}".format(cont_Ale), 1, (21, 21, 21))
        if cont_Ale < 10 :
            finestre.blit(aleatori, (x_Ale, y_Ale))
        tipografia2 = pygame.font.SysFont("serif", int(amplada/15))
        nivell = tipografia2.render("LEVEL :", 1, (21, 21, 154))
        finestre.blit(nivell, (amplada*0.7+vel*9, alt))
        tipografia3 = pygame.font.SysFont("serif", int(amplada/10))
        n = tipografia3. render("{}".format(level), 1, (21, 21, 154))
        finestre.blit(n, (amplada*0.7+20*vel, alt*3))
        score = tipografia2.render("SCORE 1:", 1, (71, 124, 71))
        finestre.blit(score, (amplada*0.7+vel*5, alt*7))
        s_nom = tipografia2.render("{}".format(score1), 1, (71, 124, 71))
        finestre.blit(s_nom, (amplada*0.7+vel*20, alt*9+vel))
        pygame.draw.rect(finestre, (254, 254, 124), (ample, alt, amplada*0.7, alsada*0.9), vel*2)
        pygame.draw.rect(finestre, (54, 154, 54), (x[0],  y[0], ample, alt))
        if cont_Ale > 1 :
            for i in range(1, 11) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(1,11) :
                    if x[i]==x[0] and y[i]==y[0]:
                        crash = True                         
        if cont_Ale > 2 :
            for i in range(11, 21) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(11,21) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True
        if cont_Ale > 3 :
            for i in range(21, 31) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(21,31) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True
        if cont_Ale > 4 :
            for i in range(31, 41) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(31,41) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True
        if cont_Ale > 5 :
            for i in range(41, 51) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(41, 51) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True
        if cont_Ale > 6 :
            for i in range(51, 61) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(51, 61) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True
        if cont_Ale > 7 :
            for i in range(61, 71) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(61, 71) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True               
        if cont_Ale > 8 :
            for i in range(71, 81) :
                pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                for i in range(71, 81) :
                    if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                        crash = True
        if cont_Ale > 9 :
            run = False
            level += 1
            sortir, ordenada, abcisa, aleatori = False, True, True, True 
            x_canvi, y_canvi = 0, 0
            cont_Ale = 1
            x_canvi +=vel
            texte = tipografia2.render("LEVEL {}".format(level), 1, (121, 121, 121))
            finestre.blit(texte, (amplada/5, alsada/3)) 
        if crash == True :
            pygame.mixer.music.play(-1)
            run = False
            sortir = True
            xoc = tipografia3.render("CRASH !!", 1, (144, 64, 64))
            finestre.blit(xoc, (amplada/7, alsada/3))
        pygame.display.flip()
        if run == False :
            time.sleep(3)
        if crash == True:
            pygame.mixer.music.stop()
            time.sleep(2)
        pygame.display.update()
        moment.tick(30)
# sortir de la pantalla pygame
pygame.quit()
quit()
