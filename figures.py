import pygame
#------------------------------ funció de càrrega de figures i transformacions
def figures(amplada, alsada, width, height, vel):
    # càrrega de fitxers
    carpeta = ".\\spaceInvader\\"
    player_machine = "machineP.png"
    planeta = "planeta.png"
    enemy_machine = "ship2.png"
    enemy_men = "enemy2.png"
    enemy_me = "enemy3.png"
    enemy_m = "enemy4.png"
    end_crash = "crash.png"
    #icona del joc
    logo = "logo.png"
    logo = pygame.image.load(carpeta + logo)
    pygame.display.set_icon(logo)
    # conversió d'imatges
    pl_mach = pygame.image.load(carpeta + player_machine).convert_alpha()
    pl_mach = pygame.transform.scale(pl_mach, (width, height))
    pl_mon = pygame.image.load(carpeta + planeta).convert_alpha()
    pl_mon = pygame.transform.scale(pl_mon, (amplada, int(alsada*2/3)))
    ene_mach = pygame.image.load(carpeta + enemy_machine).convert_alpha()
    ene_mach = pygame.transform.scale(ene_mach, (int(width - 5*vel), height))
    ene_men = pygame.image.load(carpeta + enemy_men).convert_alpha()
    ene_men = pygame.transform.scale(ene_men, (int(width/2), height - 4*vel))
    ene_me = pygame.image.load(carpeta + enemy_me).convert_alpha()
    ene_me = pygame.transform.scale(ene_me, (int(width/2), height - 4*vel))
    ene_m = pygame.image.load(carpeta + enemy_m).convert_alpha()
    ene_m = pygame.transform.scale(ene_m, (int(width/2), height - 4*vel))
    crash_end = pygame.image.load(carpeta + end_crash).convert_alpha()
    crash_end = pygame.transform.scale(crash_end, (int(amplada*0.65), int(alsada/2)))
    return pl_mach, pl_mon, ene_mach, ene_men, ene_me, ene_m, crash_end


