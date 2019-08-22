#------------------------------ funció del xoc amb l'enemic
def xoc2(pl_mort1, pl_mort2, alsada, height, vel, pl_mach, pl_mach2, ene_men17, ene_men16, ene_men15, ene_men14, ene_men13, ene_men12, ene_men11, ene_men10, ene_men9, ene_men8, ene_men7, ene_men6, ene_men5, ene_men4, ene_men3, ene_men2, ene_men1, ene_mach, crash, x, y, x2, y2, x_ali1, y_ali1, x_ali2, y_ali2, x_ali3, y_ali3, x_ali4, y_ali4, x_ali5, y_ali5, x_ali6, y_ali6, x_ali7, y_ali7, x_ali8, y_ali8, x_ali9, y_ali9, x_ali10, y_ali10, x_ali11, y_ali11, x_ali12, y_ali12, x_ali13, y_ali13, x_ali14, y_ali14, x_ali15, y_ali15, x_ali16, y_ali16, x_ali17, y_ali17, x_nau1, y_nau1, x_nau2, y_nau2, x_nau3, y_nau3, nau_morta1 , nau_morta2,  nau_morta3, mort1, mort2, mort3, mort4, mort5, mort6, mort7,  mort8, mort9, mort10, mort11, mort12, mort13, mort14, mort15, mort16, mort17) :
        # conversions de les figures a rectangles
        # jugador 1
        player_rect = pl_mach.get_rect()
        player_rect.top = y
        player_rect.left = x
        #jugador 2
        player2_rect = pl_mach2.get_rect()
        player2_rect.top = y2
        player2_rect.left = x2
        # enemic 17
        enemy17_rect = ene_men17.get_rect()
        enemy17_rect.top = y_ali17
        enemy17_rect.left =  x_ali17
        # enemic 16
        enemy16_rect = ene_men16.get_rect()
        enemy16_rect.top = y_ali16
        enemy16_rect.left =  x_ali16
        # enemic 15
        enemy15_rect = ene_men15.get_rect()
        enemy15_rect.top = y_ali15
        enemy15_rect.left =  x_ali15
        # enemic 14
        enemy14_rect = ene_men14.get_rect()
        enemy14_rect.top = y_ali14
        enemy14_rect.left =  x_ali14
        # enemic 13
        enemy13_rect = ene_men13.get_rect()
        enemy13_rect.top = y_ali13
        enemy13_rect.left =  x_ali13
        # enemic 12
        enemy12_rect = ene_men12.get_rect()
        enemy12_rect.top = y_ali12
        enemy12_rect.left =  x_ali12
        # enemic 11
        enemy11_rect = ene_men11.get_rect()
        enemy11_rect.top = y_ali11
        enemy11_rect.left =  x_ali11
        # enemic 10
        enemy10_rect = ene_men10.get_rect()
        enemy10_rect.top = y_ali10
        enemy10_rect.left =  x_ali10
        # enemic 9
        enemy9_rect = ene_men9.get_rect()
        enemy9_rect.top = y_ali9
        enemy9_rect.left =  x_ali9
        # enemic 8
        enemy8_rect = ene_men8.get_rect()
        enemy8_rect.top = y_ali8
        enemy8_rect.left =  x_ali8
        # enemic 7
        enemy7_rect = ene_men7.get_rect()
        enemy7_rect.top = y_ali7
        enemy7_rect.left =  x_ali7
        # enemic 6
        enemy6_rect = ene_men6.get_rect()
        enemy6_rect.top = y_ali6
        enemy6_rect.left =  x_ali6
        # enemic 5
        enemy5_rect = ene_men5.get_rect()
        enemy5_rect.top = y_ali5
        enemy5_rect.left =  x_ali5
        # enemic 4
        enemy4_rect = ene_men4.get_rect()
        enemy4_rect.top = y_ali4
        enemy4_rect.left =  x_ali4
        # enemic 3
        enemy3_rect = ene_men3.get_rect()
        enemy3_rect.top = y_ali3
        enemy3_rect.left =  x_ali3
        # enemic 2
        enemy2_rect = ene_men2.get_rect()
        enemy2_rect.top = y_ali2
        enemy2_rect.left =  x_ali2
        # enemic 1
        enemy1_rect = ene_men1.get_rect()
        enemy1_rect.top = y_ali1
        enemy1_rect.left =  x_ali1
        # nau enemic 1
        nau1_rect = ene_mach.get_rect()
        nau1_rect.top = y_nau1
        nau1_rect.left =  x_nau1
        # nau enemic 3
        nau3_rect = ene_mach.get_rect()
        nau3_rect.top = y_nau3
        nau3_rect.left =  x_nau3
        # enemic 2
        nau2_rect = ene_mach.get_rect()
        nau2_rect.top = y_nau2
        nau2_rect.left =  x_nau2   
        # coalicions del jugador 1 amb l'enemic
        if player_rect.colliderect(enemy17_rect) and mort17 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy16_rect) and mort16 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy15_rect) and mort15 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy14_rect) and mort14 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy13_rect) and mort13 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy12_rect) and mort12 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy11_rect) and mort11 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy10_rect) and mort10 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy9_rect) and mort9 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy8_rect) and mort8 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy7_rect) and mort7 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy6_rect) and mort6 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy5_rect) and mort5 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy4_rect) and mort4 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy3_rect) and mort3 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy2_rect) and mort2 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if player_rect.colliderect(enemy1_rect) and mort1 == False :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if (player_rect.colliderect(nau3_rect) and nau_morta3 == False) or (y_nau3 > alsada - height - vel and nau_morta3 == False) :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if (player_rect.colliderect(nau2_rect) and nau_morta2 == False) or (y_nau2 > alsada - height - vel and nau_morta2 == False) :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        if (player_rect.colliderect(nau1_rect) and nau_morta1 == False) or (y_nau1 > alsada - height - vel and nau_morta1 == False) :
                pl_mort1 = True
                if pl_mort2 == True :
                        crash = True
        # coalicions del jugador 2 amb l'enemic
        if player2_rect.colliderect(enemy17_rect) and mort17 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy16_rect) and mort16 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy15_rect) and mort15 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy14_rect) and mort14 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy13_rect) and mort13 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy12_rect) and mort12 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy11_rect) and mort11 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy10_rect) and mort10 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy9_rect) and mort9 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy8_rect) and mort8 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy7_rect) and mort7 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy6_rect) and mort6 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy5_rect) and mort5 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy4_rect) and mort4 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy3_rect) and mort3 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy2_rect) and mort2 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if player2_rect.colliderect(enemy1_rect) and mort1 == False :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if (player2_rect.colliderect(nau2_rect) and nau_morta2 == False) or (y_nau2 > alsada - height - vel and nau_morta2 == False) :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        if (player2_rect.colliderect(nau1_rect) and nau_morta1 == False) or (y_nau1 > alsada - height - vel and nau_morta1 == False) :
                pl_mort2 = True
                if pl_mort1 == True :
                        crash = True
        return crash, pl_mort1, pl_mort2
