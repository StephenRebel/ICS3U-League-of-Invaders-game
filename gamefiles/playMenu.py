#Chracter selection menu
def char_selection():
    #Importing all necessary libraries and variables from main
    import main
    from main import pygame, title_font, big_font, med_font, background, window, BLACK, RED, DARK_GR, LIGHT_GR, screen, arrowimg, staffimg, swordimg, grayed_out, player_count, player_char
    pygame.init()

    GREEN = (0, 230, 0)
    gray_out_enterBattle = pygame.transform.scale(grayed_out, (500, 175))
    gray_out_playerSelect = pygame.transform.scale(grayed_out, (275, 275))

    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Generating the background
    screen.blit(background, (0, 0))

    #Creating all the text that will be used
    text1 = title_font.render("ENTER INTO", True, BLACK)
    text2 = title_font.render("ENTER INTO", True, RED)
    text3 = title_font.render("BATTLE", True, BLACK)
    text4 = title_font.render("BATTLE", True, RED)
    text5 = big_font.render("SINGLEPLAYER", True, BLACK)
    text6 = big_font.render("SINGLEPLAYER", True, RED)
    text7 = big_font.render("MULTIPLAYER", True, BLACK)
    text8 = big_font.render("MULTIPLAYER", True, RED)
    text9 = med_font.render("PLAYER 1", True, BLACK)
    text10 = med_font.render("PLAYER 2", True, BLACK)
    text11 = big_font.render("Select your", True, BLACK)
    text12 = big_font.render("characters", True, BLACK)

    #Button locations template
    pygame.draw.rect(screen, LIGHT_GR, (830, 75, 400, 100))
    pygame.draw.rect(screen, BLACK, (825, 70, 410, 110), 5, 8)
    pygame.draw.rect(screen, LIGHT_GR, (830, 225, 400, 100))
    pygame.draw.rect(screen, BLACK, (825, 220, 410, 110), 5, 8)
    pygame.draw.rect(screen, LIGHT_GR, (730, 470, 500, 175))
    pygame.draw.rect(screen, BLACK, (720, 460, 520, 195), 10, 15)
    pygame.draw.rect(screen, LIGHT_GR, (100, 65, 275, 275), 20, 30)
    pygame.draw.rect(screen, LIGHT_GR, (120, 85, 235, 235))
    pygame.draw.rect(screen, BLACK, (95, 60, 285, 285), 5, 35)
    pygame.draw.rect(screen, LIGHT_GR, (100, 380, 275, 275), 20, 30)
    pygame.draw.rect(screen, LIGHT_GR, (120, 400, 235, 235))
    pygame.draw.rect(screen, BLACK, (95, 375, 285, 285), 5, 35)

    #Text outputted to screen
    screen.blit(text1, (795, 485))
    screen.blit(text3, (865, 555))
    screen.blit(text5, (840, 90))
    screen.blit(text7, (850, 240))
    screen.blit(text9, (160, 100))
    screen.blit(text10, (160, 415))
    screen.blit(text11, (470, 40))
    screen.blit(text12, (475, 90))

    #Outputting images to the screen
    pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
    screen.blit(arrowimg, (133, 200))
    pygame.draw.rect(screen, BLACK, (130, 197, 70, 70), 5)
    pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
    screen.blit(swordimg, (208, 200))
    pygame.draw.rect(screen, BLACK, (205, 197, 70, 70), 5)
    pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
    screen.blit(staffimg, (283, 200))
    pygame.draw.rect(screen, BLACK, (280, 197, 70, 70), 5)
    pygame.draw.rect(screen, GREEN, (133, 515, 64, 64))
    screen.blit(arrowimg, (133, 515))
    pygame.draw.rect(screen, BLACK, (130, 512, 70, 70), 5)
    pygame.draw.rect(screen, GREEN, (208, 515, 64, 64))
    screen.blit(swordimg, (208, 515))
    pygame.draw.rect(screen, BLACK, (205, 512, 70, 70), 5)
    pygame.draw.rect(screen, GREEN, (283, 515, 64, 64))
    screen.blit(staffimg, (283, 515))
    pygame.draw.rect(screen, BLACK, (280, 512, 70, 70), 5)

    if player_count == 0:
        screen.blit(gray_out_enterBattle, (730, 470))
        screen.blit(gray_out_playerSelect, (100, 65))
        screen.blit(gray_out_playerSelect, (100, 380))
    
    elif player_count == 1:
        screen.blit(gray_out_playerSelect, (100, 380))
        if player_char[0] == 0:
            screen.blit(gray_out_enterBattle, (730, 470))

    else:
        if player_char[0] != 0 and player_char[1] !=0:
            pass
        else:
            screen.blit(gray_out_enterBattle, (730, 470))