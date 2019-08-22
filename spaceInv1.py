import pygame, random, time
# importem els mètodes llibreria datetime
# emprearem el mètode now() per trobar el minut en el que ens trobem
from datetime import datetime
# importarem els mòduls on tenim les figures, posicions, ....
from figures import figures
from posicions import posicions
from xoc import xoc
from trasnEnemy import trasnEnemy


#------------------------------ definició de la funció pausa
def paused(pause) :
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    pause = False
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE :
                    pause = False
                    pygame.mixer.music.unpause()
        tipograf = pygame.font.Font(None, int(height))
        pauss = tipograf.render("PAUSED", 1, (245, 245, 245))
        win.blit(pauss, (amplada/3, alsada/3))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(10)
    return pause
                        
#------------------------------ definició de la funció SpaceInvader1
def Spaceinvader1() :
    global sortir, crash
    crash, sortir, so1 = False, False, True
    score1, level = 0, 1
    pygame.mixer.music.load('TwoSteps.mp3')
    pygame.mixer.music.play(-1)
    while not sortir :       
        pause = False
        segon = datetime.now().second
        segons = datetime.now().second
        canvDir = True
        projec = False
        x, y, x_tret1, y_tret1, x_tret2, y_tret2, x_nau1, y_nau1, x_nau2, y_nau2, x_nau3, y_nau3, x_ali1, y_ali1, x_ali2, y_ali2, x_ali3, y_ali3, x_ali4, y_ali4, x_ali5, y_ali5, x_ali6, y_ali6, x_ali7, y_ali7, x_ali8, y_ali8, x_ali9, y_ali9, x_ali10, y_ali10, x_ali11, y_ali11, x_ali12, y_ali12, x_ali13, y_ali13, x_ali14, y_ali14, x_ali15, y_ali15, x_ali16, y_ali16, x_ali17, y_ali17 = posicions(amplada, alsada, height, width, vel)
        # initzialització de valors per cada figura enemiga
        nau_morta1, nau_morta2, nau_morta3 = False, False, False
        mort17, mort16, mort15, mort14, mort13, mort12, mort11, mort10 = False, False, False, False, False, False, False, False
        mort9, mort8, mort7, mort6, mort5, mort4, mort3, mort2, mort1 = False, False, False, False, False, False, False, False, False
        cont_nau1, cont_nau2, cont_nau3 = 0, 0, 0
        cont_ali1, cont_ali2, cont_ali3, cont_ali4, cont_ali5, cont_ali6, cont_ali7, cont_ali8, cont_ali9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        cont_ali10, cont_ali11, cont_ali12, cont_ali13, cont_ali14, cont_ali15, cont_ali16, cont_ali17 = 0, 0, 0, 0 ,0, 0, 0, 0
        ene_men1, ene_men2, ene_men3, ene_men4, ene_men5, ene_men6 = ene_men, ene_men, ene_men, ene_men, ene_men, ene_men
        ene_men7, ene_men8, ene_men9, ene_men10, ene_men11, ene_men12 = ene_men, ene_men, ene_men, ene_men, ene_men, ene_men
        ene_men13, ene_men14, ene_men15, ene_men16, ene_men17 = ene_men, ene_men, ene_men, ene_men, ene_men
        run, crash, pause = True, False, False
        #-------------------- aleatori del tret enemic
        aleatori = random.randint(1,3)
        if aleatori == 1 :
            x_proj = x_nau1+(width-5*vel)/2
            y_proj = y_nau1+height/2
        if aleatori == 2 :
            x_proj = x_nau2+(width-5*vel)/2
            y_proj = y_nau2+height/2
        if aleatori == 3 :
            x_proj = x_nau3+(width-5*vel)/2
            y_proj = y_nau3+height/2
        # bucle principal de la finestre pygame
        while run :
            crash = xoc(alsada, height, vel, pl_mach, ene_men17, ene_men16, ene_men15, ene_men14, ene_men13, ene_men12, ene_men11, ene_men10, ene_men9, ene_men8, ene_men7, ene_men6, ene_men5, ene_men4, ene_men3, ene_men2, ene_men1, ene_mach, crash, x, y, x_ali1, y_ali1, x_ali2, y_ali2, x_ali3, y_ali3, x_ali4, y_ali4, x_ali5, y_ali5, x_ali6, y_ali6, x_ali7, y_ali7, x_ali8, y_ali8, x_ali9, y_ali9, x_ali10, y_ali10, x_ali11, y_ali11, x_ali12, y_ali12, x_ali13, y_ali13, x_ali14, y_ali14, x_ali15, y_ali15, x_ali16, y_ali16, x_ali17, y_ali17, x_nau1, y_nau1, x_nau2, y_nau2, x_nau3, y_nau3, nau_morta1 , nau_morta2,  nau_morta3, mort1, mort2, mort3, mort4, mort5, mort6, mort7,  mort8, mort9, mort10, mort11, mort12, mort13, mort14, mort15, mort16, mort17)
            ene_men1, ene_men2, ene_men3, ene_men4, ene_men5, ene_men6, ene_men7, ene_men8, ene_men9, ene_men10, ene_men11, ene_men12, ene_men13, ene_men14, ene_men15, ene_men16, ene_men17 = trasnEnemy(ene_men, ene_me, ene_m, cont_ali1, cont_ali2, cont_ali3, cont_ali4, cont_ali5, cont_ali6, cont_ali7, cont_ali8, cont_ali9, cont_ali10, cont_ali11, cont_ali12, cont_ali13, cont_ali14, cont_ali15, cont_ali16, cont_ali17,  ene_men1, ene_men2, ene_men3, ene_men4, ene_men5, ene_men6, ene_men7, ene_men8, ene_men9, ene_men10, ene_men11, ene_men12, ene_men13, ene_men14, ene_men15, ene_men16, ene_men17)
            # bucle d'esdeveniments per entrades des del mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # variable d'entrades des de teclat
            keys = pygame.key.get_pressed()
            # condició per l'entrada de la tecla Esc    
            if keys[pygame.K_ESCAPE] :
                    pygame.quit()
                    quit()
            # condició per sortida de l'eix d'ordenades per la dreta
            if x > amplada - width :
                x = vel
            # condició per sortida de l'eix d'ordenades per l'esquerra
            if x < vel :
                x = amplada - width - vel
            # condicions per l'entrada de les tecles de desplaçamaent
            # esquerra, dreta adalt i abaix
            if crash == False :
                if keys[pygame.K_LEFT] :
                    x -= vel
                if keys[pygame.K_RIGHT] :
                    x += vel
                if keys[pygame.K_UP] and y > alsada/2 - vel:
                    y -= vel
                if keys[pygame.K_DOWN] and y < alsada - height - vel :
                    y += vel
                if keys[112]:
                    pause = True
                    pause = paused(pause)
                    
            # contarem els segons transcorreguts per avançar les tropes enemigues
            segon2 =  datetime.now().second
            if (segon < 50  and segon2  > segon+9) or (segon > 49 and 10 > segon2  and segon-49 > segon2) :
                y_nau1 += height
                y_nau2 += height
                y_nau3 += height
                y_ali1 += height
                y_ali2 += height
                y_ali3 += height
                y_ali4 += height
                y_ali5 += height
                y_ali6 += height
                y_ali7 += height
                y_ali8 += height
                y_ali9 += height
                y_ali10 += height
                y_ali11 += height
                y_ali12 += height
                y_ali13 += height
                y_ali14 += height
                y_ali15 += height
                y_ali16 += height
                y_ali17 += height
                segon = segon2
                cont_ali1, cont_ali2, cont_ali3, cont_ali4, cont_ali5, cont_ali6, cont_ali7, cont_ali8, cont_ali9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
                cont_ali10, cont_ali11, cont_ali12, cont_ali13, cont_ali14, cont_ali15, cont_ali16, cont_ali17 = 0, 0, 0, 0 ,0, 0, 0, 0
                #desplaçament de les naus enemigues
            if crash == False :
                #if projec == True :
                y_proj += vel
                if x_nau1 < - width * 2 :
                    canvDir = True
                if x_nau3 < (amplada+width) and canvDir == True:
                    x_nau1 += vel
                    x_nau2 += vel
                    x_nau3 += vel
                    x_ali1 -= int(vel/5)
                    x_ali2 -= int(vel/5)
                    x_ali3 -= int(vel/5)
                    x_ali4 -= int(vel/5)
                    x_ali5 -= int(vel/5)
                    x_ali6 -= int(vel/5)
                    x_ali7 += int(vel/5)
                    x_ali8 += int(vel/5)
                    x_ali9 += int(vel/5)
                    x_ali10 += int(vel/5)
                    x_ali11 += int(vel/5)
                    x_ali12 -= int(vel/5)
                    x_ali13 -= int(vel/5)
                    x_ali14 -= int(vel/5)
                    x_ali15 -= int(vel/5)
                    x_ali16 -= int(vel/5)
                    x_ali17 -= int(vel/5)
                else:
                    canvDir = False
                    x_nau1 -= vel
                    x_nau2 -= vel
                    x_nau3 -= vel
                    x_ali1 += int(vel/5)
                    x_ali2 += int(vel/5)
                    x_ali3 += int(vel/5)
                    x_ali4 += int(vel/5)
                    x_ali5 += int(vel/5)
                    x_ali6 += int(vel/5)
                    x_ali7 -= int(vel/5)
                    x_ali8 -= int(vel/5)
                    x_ali9 -= int(vel/5)
                    x_ali10 -= int(vel/5)
                    x_ali11 -= int(vel/5)
                    x_ali12 += int(vel/5)
                    x_ali13 += int(vel/5)
                    x_ali14 += int(vel/5)
                    x_ali15 += int(vel/5)
                    x_ali16 += int(vel/5)
                    x_ali17 += int(vel/5)
                #desplaçament dels nostres projectils
                if keys[pygame.K_RETURN] :
                    pygame.mixer.Sound.play(tret_so)
                    x_tret1 = x + 2
                    y_tret1 -= vel * 2
                    x_tret2 = x + height
                    y_tret2 -= vel * 2
                    
                else :
                    x_tret1 = x + 2
                    y_tret1 = y + width/2 - vel
                    x_tret2 = x + height
                    y_tret2 = y + width/2 - vel
                # desplaçament del projectil enemic
                if y_proj+int(alsada/20) >= alsada :
                    retornale = True
                    while retornale :
                        pygame.mixer.Sound.play(laser_so)
                        aleatori = random.randint(1,3)
                        retornale = False
                        if aleatori == 1 and nau_morta1 == False  :
                            x_proj = x_nau1+(width-5*vel)/2
                            y_proj = y_nau1+height/2
                        elif aleatori == 2  and nau_morta2 == False :
                            x_proj = x_nau2+(width-5*vel)/2
                            y_proj = y_nau2+height/2
                        elif aleatori == 3  and nau_morta3 == False:
                            x_proj = x_nau3+(width-5*vel)/2
                            y_proj = y_nau3+height/2
                        else :
                            retornale = True
                        
                if (x < x_proj < x+width) and (y < y_proj < y+height) :
                    crash = True
            #coalició d'un tret amb l'elienigena
            if (x_ali17 <  x_tret2  <  x_ali17+width/2  and  y_ali17 <  y_tret2 <  y_ali17+height and mort17 == False) or  (x_ali17 < x_tret1 < x_ali17+width/2  and  y_ali17 < y_tret1< y_ali17+height  and mort17 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali17 +=1
                 if  cont_ali17 > 2 :
                     mort17  = True
                     score1 += 1
            if (x_ali16 < x_tret2 < x_ali16+width/2  and  y_ali16 < y_tret2< y_ali16+height  and mort16 == False) or (x_ali16 < x_tret1 < x_ali16+width/2  and  y_ali16 < y_tret1< y_ali16+height  and mort16 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali16 += 1
                 if  cont_ali16 > 2 :
                     mort16  = True
                     score1 += 1
            if (x_ali15 < x_tret2 < x_ali15+width/2  and  y_ali15 < y_tret2< y_ali15+height  and mort15 == False) or (x_ali15 < x_tret1 < x_ali15+width/2  and  y_ali15 < y_tret1< y_ali15+height  and mort15 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali15 +=1
                 if  cont_ali15 > 2 :
                     mort15  = True
                     score1 += 1
            if (x_ali14 < x_tret2 < x_ali14+width/2  and  y_ali14 < y_tret2< y_ali14+height  and mort14 == False) or (x_ali14 < x_tret1 < x_ali14+width/2  and  y_ali14 < y_tret1< y_ali14+height  and mort14 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali14 += 1
                 if  cont_ali14 > 2 :
                     mort14  = True
                     score1 += 1
            if (x_ali13 < x_tret2 < x_ali13+width/2  and  y_ali13 < y_tret2< y_ali13+height  and mort13 == False) or (x_ali13 < x_tret1 < x_ali13+width/2  and  y_ali13 < y_tret1< y_ali13+height  and mort13 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali13 +=1
                 if  cont_ali13 > 2 :
                     mort13  = True
                     score1 += 1
            if (x_ali12 < x_tret2 < x_ali12+width/2  and  y_ali12 < y_tret2< y_ali12+height  and mort16 == False) or (x_ali12 < x_tret1 < x_ali12+width/2  and  y_ali12 < y_tret1< y_ali12+height  and mort12 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali12 += 1
                 if  cont_ali12 > 2 :
                     mort12  = True
                     score1 += 1
            if (x_ali11 < x_tret2 < x_ali11+width/2  and  y_ali11 < y_tret2 < y_ali11+height  and mort11 == False) or (x_ali11 < x_tret1 < x_ali11+width/2  and  y_ali11 < y_tret1< y_ali11+height  and mort11 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali11 += 1
                 if  cont_ali11 > 2 :
                     mort11  = True
                     score1 += 1
            if (x_ali10  < x_tret2 < x_ali10+width/2  and  y_ali10  < y_tret2< y_ali10+height  and mort10 == False) or (x_ali10 < x_tret1 < x_ali10+width/2  and  y_ali10 < y_tret1<y_ali10+height  and mort10 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali10 += 1
                 if  cont_ali10 > 2 :
                     mort10  = True
                     score1 += 1
            if (x_ali9 < x_tret2 < x_ali9+width/2  and  y_ali9 < y_tret2< y_ali9+height  and mort9 == False) or (x_ali9 < x_tret1 < x_ali9+width/2  and  y_ali9 < y_tret1< y_ali9+height  and mort9 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali9 += 1
                 if  cont_ali9 > 2 :
                     mort9  = True
                     score1 += 1
            if (x_ali8 < x_tret2 < x_ali8+width/2  and  y_ali8 < y_tret2< y_ali8+height  and mort8 == False) or (x_ali8 < x_tret1 < x_ali8+width/2  and  y_ali8 < y_tret1< y_ali8+height  and mort8 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali8 +=1
                 if  cont_ali8 > 2 :
                     mort8  = True
                     score1 += 1
            if (x_ali7 < x_tret2 < x_ali7+width/2  and  y_ali7 < y_tret2< y_ali7+height  and mort7 == False) or (x_ali7 < x_tret1 < x_ali7+width /2 and  y_ali7 < y_tret1< y_ali7+height  and mort7 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali7 +=1
                 if  cont_ali7 > 2 :
                     mort7  = True
                     score1 += 1
            if (x_ali6 < x_tret2 < x_ali6+width/2  and  y_ali6< y_tret2< y_ali6+height  and mort6 == False) or (x_ali6 < x_tret1 < x_ali6+width/2  and  y_ali6< y_tret1< y_ali6+height  and mort6 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali6 += 1
                 if  cont_ali6 > 2 :
                     mort6  = True
                     score1 += 1
            if (x_ali5 < x_tret2 < x_ali5+width/2  and  y_ali5 < y_tret2 < y_ali5+height  and mort5 == False) or (x_ali5 < x_tret1 < x_ali5+width/2  and  y_ali5 < y_tret1< y_ali5+height  and mort5 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali5 += 1
                 if  cont_ali5 > 2 :
                     mort5  = True
                     score1 += 1
            if (x_ali4  < x_tret2 < x_ali4+width/2  and  y_ali4  <  y_tret2 <  y_ali4+height  and mort4 == False) or (x_ali4 < x_tret1 < x_ali4+width/2  and  y_ali4 < y_tret1<y_ali4+height  and mort4 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali4 += 1
                 if  cont_ali4 > 2 :
                     mort4  = True
                     score1 += 1
            if (x_ali3 < x_tret2 < x_ali3+width/2  and  y_ali3  <  y_tret2 <  y_ali3+height  and mort3 == False) or (x_ali3 < x_tret1 < x_ali3+width/2  and  y_ali3< y_tret1< y_ali3+height  and mort3 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali3 += 1
                 if  cont_ali3 > 2 :
                     mort3  = True
                     score1 += 1
            if (x_ali2 < x_tret2 < x_ali2+width/2  and  y_ali2< y_tret2< y_ali2+height  and mort2 == False) or (x_ali2< x_tret1 < x_ali2+width/2  and  y_ali2< y_tret1< y_ali2+height  and mort2 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali2 += 1
                 if  cont_ali2 > 2 :
                     mort2  = True
                     score1 += 1
            if (x_ali1 < x_tret2 < x_ali1+width/2  and  y_ali1 < y_tret2< y_ali1+height  and mort1 == False) or (x_ali1 < x_tret1 < x_ali1+width/2  and  y_ali1 < y_tret1< y_ali1+height  and mort1 == False) :
                 x_tret1 = x + 2
                 y_tret1 = y + width/2 - vel
                 x_tret2 = x + height
                 y_tret2 = y + width/2 - vel    
                 cont_ali1 += 1
                 if  cont_ali1 > 2 :
                     mort1  = True
                     score1 += 1
            if (x_nau1 < x_tret2 < x_nau1+width-5*vel and y_nau1 < y_tret2 < y_nau1+height and nau_morta1 ==False) or (x_nau1 < x_tret1 < x_nau1+width-4*vel and y_nau1 < y_tret1 <y_nau1+height and nau_morta1 == False) :
                x_tret1 = x + 2
                y_tret1 = y + width/2 - vel
                x_tret2 = x + height
                y_tret2 = y + width/2 - vel
                cont_nau1 += 1
                if cont_nau1 > 4 :
                    nau_morta1 = True
                    score1 += 2
            if (x_nau2 < x_tret2 < x_nau2+width-5*vel and y_nau2 < y_tret2 < y_nau2+height and nau_morta2 ==False) or (x_nau2 < x_tret1 < x_nau2+width-4*vel and y_nau2 < y_tret1 <y_nau2+height and nau_morta2 == False) :
                x_tret1 = x + 2
                y_tret1 = y + width/2 - vel
                x_tret2 = x + height
                y_tret2 = y + width/2 - vel
                cont_nau2 += 1
                if cont_nau2 > 4 :
                    nau_morta2 = True
                    score1 += 2
            if (x_nau3 < x_tret2 < x_nau3+width-5*vel and y_nau3 < y_tret2 < y_nau3+height and nau_morta3 ==False) or (x_nau3 < x_tret1 < x_nau3+width-4*vel and y_nau3 < y_tret1 <y_nau3+height and nau_morta3 == False) :
                x_tret1 = x + 2
                y_tret1 = y + width/2 - vel
                x_tret2 = x + height
                y_tret2 = y + width/2 - vel
                cont_nau3 += 1
                if cont_nau3 > 4 :
                    nau_morta3 = True
                    score1 += 2
            # sortida de figures a a la nostre finestre    
            win.fill((0,0,0))
            win.blit(pl_mon, (0, alsada/2 - height/2))
            pygame.draw.ellipse(win, (244, 244, 244), [int(amplada*4/5), vel*5, width-vel, height-vel], 0)
            pygame.draw.ellipse(win, (244, 244, 244), [int(amplada/20), vel*5, vel, vel], 0)    
            pygame.draw.ellipse(win, (244, 244, 244), [int(amplada/10), vel*10, vel, vel], 0)
            pygame.draw.ellipse(win, (244, 244, 244), [int(amplada/5), vel*20, vel, vel], 0)
            pygame.draw.ellipse(win, (244, 244, 244), [int(amplada*2/5), vel*10, vel, vel], 0)
            pygame.draw.ellipse(win, (244, 244, 244), [int(amplada*3/5), vel*20, vel, vel], 0)
            #dibuixar el marcador
            tipograf = pygame.font.Font(None, int(height*0.7))
            marcador = tipograf .render("Level: {} Score: {}".format(level, score1), 1, (244, 0, 0))
            win.blit(marcador, (amplada/4, vel))
            win.blit(pl_mach, (x,y))
            if nau_morta1 == False :
                win.blit(ene_mach, (x_nau1, y_nau1))
            if nau_morta2 == False :
                win.blit(ene_mach, (x_nau2, y_nau2))
            if nau_morta3 == False :
                win.blit(ene_mach, (x_nau3, y_nau3))
            if mort1 == False : 
                win.blit(ene_men1, (x_ali1, y_ali1))
            if mort2 == False :
                win.blit(ene_men2, (x_ali2, y_ali2))
            if mort3 == False :
                win.blit(ene_men3, (x_ali3, y_ali3))
            if mort4 == False :
                win.blit(ene_men4, (x_ali4, y_ali4))
            if mort5 == False :
                win.blit(ene_men5, (x_ali5, y_ali5))
            if mort6 == False :
                win.blit(ene_men6, (x_ali6, y_ali6))
            if mort7 == False :
                win.blit(ene_men7, (x_ali7, y_ali7))
            if  mort8 == False :
                win.blit(ene_men8, (x_ali8, y_ali8))
            if mort9 == False :
                win.blit(ene_men9, (x_ali9, y_ali9))
            if mort10 == False :
                win.blit(ene_men10, (x_ali10, y_ali10))
            if mort11 == False :
                win.blit(ene_men11, (x_ali11, y_ali11))
            if mort12 == False :
                win.blit(ene_men12, (x_ali12, y_ali12))
            if mort13 == False :
                win.blit(ene_men13, (x_ali13, y_ali13))
            if mort14 == False :
                win.blit(ene_men14, (x_ali14, y_ali14))
            if mort15 == False :
                win.blit(ene_men15, (x_ali15, y_ali15))
            if mort16 == False : 
                win.blit(ene_men16, (x_ali16, y_ali16))
            if mort17 == False :
                win.blit(ene_men17, (x_ali17, y_ali17))                
            # dibuix dels dos projectils projectils
            pygame.draw.line(win, (177, 0, 0), [x_tret1, y_tret1], [x_tret1, y_tret1+int(alsada/20)], int(amplada/200))
            pygame.draw.line(win, (177, 0, 0), [x_tret2, y_tret2], [x_tret2, y_tret2+int(alsada/20)], int(amplada/200))
            # dibuixar projectil enemic
            pygame.draw.line(win, (177, 177, 0), [x_proj, y_proj], [x_proj, y_proj+int(alsada/20)], int( amplada/200))                       
            # en el cas d'haver-hi un cop dels aleanígenes a la nostra nau
            if crash == True :
                if so1 == True :
                    pygame.mixer.Sound.play(xoc_so)
                    pygame.mixer.music.stop()
                    so1 = False                    
                tipografia = pygame.font.Font(None, int(height/2))
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                win.blit(crash_end, (width*1.5, height))            
                if (width*3.5 > mouse[0]  > width*1.5) and (alsada - height > mouse[1]  > alsada - height*2) :
                    green = (0, 111, 0)
                    if click[0] == 1 or keys[pygame.K_RETURN] :
                        from menuSpIn import menu_principal
                        menu_principal()
                elif (width*6.5 > mouse[0] > width*4.5) and (alsada - height > mouse[1] > alsada - height*2)  :
                    red = (111, 0 , 0)
                    if click[0] == 1 or keys[pygame.K_RETURN] :
                        pygame.quit()
                        quit()
                else:
                    green, red  = (0, 222, 0), (222, 0, 0)
                # dibuix dels dos botons 
                pygame.draw.rect(win, green, [1.5*width, alsada-2*height, 2*width, height], 0)    
                other= tipografia.render("come on", 1, (0, 0 ,0))
                win.blit(other, (1.5*width+5*vel, alsada-2*height+5*vel))
                pygame.draw.rect(win, red, [4.5*width, alsada-2*height, 2*width, height], 0)
                quite= tipografia.render(" quited ", 1, (0, 0 ,0))
                win.blit(quite, (4.5*width+5*vel, alsada-2*height+5*vel))
            # redibuix de totes les figures
            if mort1==True and mort2==True and mort3==True and mort4==True and mort5==True and mort6==True and mort7==True and mort8==True and mort9==True and mort10==True and mort11==True and mort12==True and mort13==True and mort14==True and mort15==True and mort16==True and mort17==True and nau_morta1==True and nau_morta2==True and nau_morta3==True :
                tipografia0 = pygame.font.Font(None, int(height*0.75))
                retol = tipografia0.render("CONGRATULATIONS !!!", 1, (244, 0, 0))
                win.blit(retol, (amplada/8, alsada/2))
                pause = True
                run = False
                sortir = False
                level += 1
            pygame.display.flip()
            if pause == True and run == False and sortir == False :
                time.sleep(2)
            pygame.display.update()
            clock.tick(60)
#----------------------------- programa principal
pygame.init()
rdn = datetime.now()
random.seed(rdn.second)
xoc_so = pygame.mixer.Sound("crash.wav")
laser_so = pygame.mixer.Sound("laser.wav")
tret_so = pygame.mixer.Sound("tret.wav")
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
fons_portada = pygame.image.load(carpeta + portada).convert_alpha()
fons_portada = pygame.transform.scale(fons_portada, (amplada, alsada))
pl_mach, pl_mon, ene_mach, ene_men, ene_me, ene_m, crash_end = figures(amplada, alsada, width, height, vel)

