# _*_ coding: utf-8 _*_
#
# created on  Mon Aug 5 09:40:35 2019
# @file : Sace_Invader.py
# @description : joc de guerra espacial, on hi ha que aliminar a tots
# els alieniges abans de que ens màtin, hem de salvar la terra
# @author: Gilbert Viader
#
# importem la llibreria pygame i mètodes locals de pygame
import pygame, random, time
from pygame.locals import *
# importem els mètodes llibreria datetime
# emprearem el mètode now() per trobar el minut en el que ens trobem
from datetime import datetime
# importarem els mòduls on tenim les figures, posicions, ....
from figures import figures
from posicions import posicions
from xoc import xoc
from trasnEnemy import trasnEnemy
#importarem els moduls on tenim les funcions de menu i jocs 1 o 2 jugadors
from menuSpIn import menu_principal


#------------------------------ programa principal
pygame.init()
rdn = datetime.now()
random.seed(rdn.second)
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
pl_mach, pl_mon, ene_mach, ene_men, ene_me, ene_m, crash_end = figures(amplada, alsada, width, height, vel)
#començament del bucle principal
menu_principal()
# sortida del bucle, posterior tancament de la finestre pygame i l'aplicació python
#pygame.quit()
#quit()
