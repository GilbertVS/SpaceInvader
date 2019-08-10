#----------------------------- funció del posicionament de les figures
def posicions(amplada, alsada, height, width, vel) :
    x = amplada /2 - height
    y = alsada - height*2 - vel
    # posicions dels projectil
    x_tret1 = x + 2
    y_tret1 = y + width/2 - vel
    x_tret2 = x + height
    y_tret2 = y + width/2 - vel
    # posicions de les naus enemigues
    x_nau1 = vel * 10
    y_nau1 = vel
    x_nau2 = amplada / 2 - width - vel
    y_nau2 = vel
    x_nau3 = amplada - width * 3
    y_nau3 = vel
    # posicions dels enemics
    x_ali1 = vel * 3
    y_ali1 = height + 2*vel
    x_ali2 = vel * 23
    y_ali2 = height + 2*vel
    x_ali3 = vel * 43
    y_ali3 = height + 2*vel
    x_ali4 = vel * 63
    y_ali4 = height + 2*vel
    x_ali5 = vel * 83
    y_ali5 = height + 2*vel
    x_ali6 = vel * 103
    y_ali6 = height + 2*vel
    x_ali7 = vel * 13
    y_ali7 = 2*height + 2*vel
    x_ali8 = vel * 33
    y_ali8 = 2*height + 2*vel
    x_ali9 = vel * 53
    y_ali9 = 2*height + 2*vel
    x_ali10 = vel * 73
    y_ali10 = 2*height + 2*vel
    x_ali11 = vel * 93
    y_ali11 = 2*height + 2*vel
    x_ali12 = vel * 3
    y_ali12 = 3*height + 2*vel
    x_ali13 = vel * 23
    y_ali13 = 3*height + 2*vel
    x_ali14 = vel * 43
    y_ali14 = 3*height + 2*vel
    x_ali15 = vel * 63
    y_ali15 = 3*height + 2*vel
    x_ali16 = vel * 83
    y_ali16 = 3*height + 2*vel
    x_ali17 = vel * 103
    y_ali17 = 3*height + 2*vel
    return x, y, x_tret1, y_tret1, x_tret2, y_tret2, x_nau1, y_nau1, x_nau2, y_nau2, x_nau3, y_nau3, x_ali1, y_ali1, x_ali2, y_ali2, x_ali3, y_ali3, x_ali4, y_ali4, x_ali5, y_ali5, x_ali6, y_ali6, x_ali7, y_ali7, x_ali8, y_ali8, x_ali9, y_ali9, x_ali10, y_ali10, x_ali11, y_ali11, x_ali12, y_ali12, x_ali13, y_ali13, x_ali14, y_ali14, x_ali15, y_ali15, x_ali16, y_ali16, x_ali17, y_ali17
                
