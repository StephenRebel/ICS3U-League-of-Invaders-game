#Chracter selection menu
def char_selection():
    #Importing all necessary libraries and variables from main
    import main
    from main import pygame, title_font, big_font, med_font, background, window, BLACK, RED, DARK_GR, LIGHT_GR, screen, arrowimg, staffimg, swordimg, grayed_out, player_count, player_char
    pygame.init()

    #Added variables needed for this menu
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
    screen.blit(text9, (160, 100))
    screen.blit(text10, (160, 415))
    screen.blit(text11, (470, 40))
    screen.blit(text12, (475, 90))

    #Determins which player count button has been pressed, or none
    if player_count == 0:
        #Grays out unclickable buttons
        screen.blit(gray_out_enterBattle, (730, 470))
        screen.blit(gray_out_playerSelect, (100, 65))
        screen.blit(gray_out_playerSelect, (100, 380))

        #Allows for interaction with the single player and multiplayer buttons
        if 830 <= mouse[0] <= 1230 and 75 <= mouse[1] <= 175 and pressed[0] == True:
            main.player_count = 1
            main.multiplayer = False
            pygame.time.delay(100)
        elif 830 <= mouse[0] <= 1230 and 75 <= mouse[1] <= 175:
            pygame.draw.rect(screen, DARK_GR, (830, 75, 400, 100))
            pygame.draw.rect(screen, RED, (825, 70, 410, 110), 5, 8)
            screen.blit(text6, (840, 90))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (830, 75, 400, 100))
            pygame.draw.rect(screen, BLACK, (825, 70, 410, 110), 5, 8)
            screen.blit(text5, (840, 90))

        #Allows for interaction with the single player and multiplayer buttons
        if 830 <= mouse[0] <= 1230 and 225 <= mouse[1] <= 325 and pressed[0] == True:
            main.player_count = 2
            main.multiplayer = True
            pygame.time.delay(100)
        elif 830 <= mouse[0] <= 1230 and 225 <= mouse[1] <= 325:
            pygame.draw.rect(screen, DARK_GR, (830, 225, 400, 100))
            pygame.draw.rect(screen, RED, (825, 220, 410, 110), 5, 8)
            screen.blit(text8, (850, 240))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (830, 225, 400, 100))
            pygame.draw.rect(screen, BLACK, (825, 220, 410, 110), 5, 8)
            screen.blit(text7, (850, 240))

    #Determins which player count button has been pressed
    elif player_count == 1:
        #Grays out unclickable buttons
        screen.blit(gray_out_playerSelect, (100, 380))

        #Allows user to select their chracters
        if 133 <= mouse[0] <= 197 and 200 <= mouse[1] <= 264 and pressed[0] == True:
            main.player_char[0] = 1
            pygame.time.delay(100)
        elif 133 <= mouse[0] <= 197 and 200 <= mouse[1] <= 264:
            pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
            screen.blit(arrowimg, (133, 200))
            pygame.draw.rect(screen, RED, (130, 197, 70, 70), 5)
        else:
            pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
            screen.blit(arrowimg, (133, 200))
            pygame.draw.rect(screen, BLACK, (130, 197, 70, 70), 5)

        #Allows user to select their chracters
        if 208 <= mouse[0] <= 272 and 200 <= mouse[1] <= 264 and pressed[0] == True:
            main.player_char[0] = 2
            pygame.time.delay(100)
        elif 208 <= mouse[0] <= 272 and 200 <= mouse[1] <= 264:
            pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
            screen.blit(swordimg, (208, 200))
            pygame.draw.rect(screen, RED, (205, 197, 70, 70), 5)
        else:
            pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
            screen.blit(swordimg, (208, 200))
            pygame.draw.rect(screen, BLACK, (205, 197, 70, 70), 5)

        #Allows user to select their chracters
        if 283 <= mouse[0] <= 347 and 200 <= mouse[1] <= 264 and pressed[0] == True:
            main.player_char[0] = 3
            pygame.time.delay(100)
        elif 283 <= mouse[0] <= 347 and 200 <= mouse[1] <= 264:
            pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
            screen.blit(staffimg, (283, 200))
            pygame.draw.rect(screen, RED, (280, 197, 70, 70), 5)
        else:
            pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
            screen.blit(staffimg, (283, 200))
            pygame.draw.rect(screen, BLACK, (280, 197, 70, 70), 5)

        if player_char[0] == 0:
            #Grays out unclickable buttons
            screen.blit(gray_out_enterBattle, (730, 470))
        else:
            #Allows user to interact with the enter into battle button
            if 730 <= mouse[0] <= 1230 and 470 <= mouse[1] <= 645 and pressed[0] == True:
                main.window = 4
                pygame.time.delay(100)
            elif 730 <= mouse[0] <= 1230 and 470 <= mouse[1] <= 645:
                pygame.draw.rect(screen, DARK_GR, (730, 470, 500, 175))
                screen.blit(text2, (795, 485))
                screen.blit(text4, (865, 555))
            else:
                pygame.draw.rect(screen, LIGHT_GR, (730, 470, 500, 175))
                pygame.draw.rect(screen, BLACK, (720, 460, 520, 195), 10, 15)
                screen.blit(text1, (795, 485))   
                screen.blit(text3, (865, 555))            

        #Allows for interaction with the single player and multiplayer buttons
        if 830 <= mouse[0] <= 1230 and 75 <= mouse[1] <= 175 and pressed[0] == True:
            main.player_count = 1
            main.multiplayer = False
            pygame.time.delay(100)
        elif 830 <= mouse[0] <= 1230 and 75 <= mouse[1] <= 175:
            pygame.draw.rect(screen, DARK_GR, (830, 75, 400, 100))
            pygame.draw.rect(screen, RED, (825, 70, 410, 110), 5, 8)
            screen.blit(text6, (840, 90))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (830, 75, 400, 100))
            pygame.draw.rect(screen, BLACK, (825, 70, 410, 110), 5, 8)
            screen.blit(text5, (840, 90))

        #Allows for interaction with the single player and multiplayer buttons
        if 830 <= mouse[0] <= 1230 and 225 <= mouse[1] <= 325 and pressed[0] == True:
            main.player_count = 2
            main.multiplayer = True
            pygame.time.delay(100)
        elif 830 <= mouse[0] <= 1230 and 225 <= mouse[1] <= 325:
            pygame.draw.rect(screen, DARK_GR, (830, 225, 400, 100))
            pygame.draw.rect(screen, RED, (825, 220, 410, 110), 5, 8)
            screen.blit(text8, (850, 240))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (830, 225, 400, 100))
            pygame.draw.rect(screen, BLACK, (825, 220, 410, 110), 5, 8)
            screen.blit(text7, (850, 240))

    #Determins which player count button has been pressed
    else:
        if player_char[0] != 0 and player_char[1] !=0:

            #Allows user to interact with the enter into battle button
            if 730 <= mouse[0] <= 1230 and 470 <= mouse[1] <= 645 and pressed[0] == True:
                main.window = 4
                pygame.time.delay(100)
            elif 730 <= mouse[0] <= 1230 and 470 <= mouse[1] <= 645:
                pygame.draw.rect(screen, DARK_GR, (730, 470, 500, 175))
                screen.blit(text2, (795, 485))
                screen.blit(text4, (865, 555))
            else:
                pygame.draw.rect(screen, LIGHT_GR, (730, 470, 500, 175))
                pygame.draw.rect(screen, BLACK, (720, 460, 520, 195), 10, 15)
                screen.blit(text1, (795, 485))
                screen.blit(text3, (865, 555))

            #Allows user to select their chracters
            if 133 <= mouse[0] <= 197 and 200 <= mouse[1] <= 264 and pressed[0] == True:
                main.player_char[0] = 1
                pygame.time.delay(100)
            elif 133 <= mouse[0] <= 197 and 200 <= mouse[1] <= 264:
                pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
                screen.blit(arrowimg, (133, 200))
                pygame.draw.rect(screen, RED, (130, 197, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
                screen.blit(arrowimg, (133, 200))
                pygame.draw.rect(screen, BLACK, (130, 197, 70, 70), 5)

            #Allows user to select their chracters
            if 208 <= mouse[0] <= 272 and 200 <= mouse[1] <= 264 and pressed[0] == True:
                main.player_char[0] = 2
                pygame.time.delay(100)
            elif 208 <= mouse[0] <= 272 and 200 <= mouse[1] <= 264:
                pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
                screen.blit(swordimg, (208, 200))
                pygame.draw.rect(screen, RED, (205, 197, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
                screen.blit(swordimg, (208, 200))
                pygame.draw.rect(screen, BLACK, (205, 197, 70, 70), 5)

            #Allows user to select their chracters
            if 283 <= mouse[0] <= 347 and 200 <= mouse[1] <= 264 and pressed[0] == True:
                main.player_char[0] = 3
                pygame.time.delay(100)
            elif 283 <= mouse[0] <= 347 and 200 <= mouse[1] <= 264:
                pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
                screen.blit(staffimg, (283, 200))
                pygame.draw.rect(screen, RED, (280, 197, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
                screen.blit(staffimg, (283, 200))
                pygame.draw.rect(screen, BLACK, (280, 197, 70, 70), 5)

            #Allows user to select their chracters
            if 133 <= mouse[0] <= 197 and 515 <= mouse[1] <= 579 and pressed[0] == True:
                main.player_char[1] = 1
                pygame.time.delay(100)
            elif 133 <= mouse[0] <= 197 and 515 <= mouse[1] <= 579:
                pygame.draw.rect(screen, GREEN, (133, 515, 64, 64))
                screen.blit(arrowimg, (133, 515))
                pygame.draw.rect(screen, RED, (130, 512, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (133, 515, 64, 64))
                screen.blit(arrowimg, (133, 515))
                pygame.draw.rect(screen, BLACK, (130, 512, 70, 70), 5)

            #Allows user to select their chracters
            if 208 <= mouse[0] <= 272 and 515 <= mouse[1] <= 579 and pressed[0] == True:
                main.player_char[1] = 2
                pygame.time.delay(100)
            elif 208 <= mouse[0] <= 272 and 515 <= mouse[1] <= 579:
                pygame.draw.rect(screen, GREEN, (208, 515, 64, 64))
                screen.blit(swordimg, (208, 515))
                pygame.draw.rect(screen, RED, (205, 512, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (208, 515, 64, 64))
                screen.blit(swordimg, (208, 515))
                pygame.draw.rect(screen, BLACK, (205, 512, 70, 70), 5)

            #Allows user to select their chracters
            if 283 <= mouse[0] <= 347 and 515 <= mouse[1] <= 579 and pressed[0] == True:
                main.player_char[1] = 3
                pygame.time.delay(100)
            elif 283 <= mouse[0] <= 347 and 515 <= mouse[1] <= 579:
                pygame.draw.rect(screen, GREEN, (283, 515, 64, 64))
                screen.blit(staffimg, (283, 515))
                pygame.draw.rect(screen, RED, (280, 512, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (283, 515, 64, 64))
                screen.blit(staffimg, (283, 515))
                pygame.draw.rect(screen, BLACK, (280, 512, 70, 70), 5)

        else:
            #Grays out unclickable buttons
            screen.blit(gray_out_enterBattle, (730, 470))

            #Allows user to select their chracters
            if 133 <= mouse[0] <= 197 and 200 <= mouse[1] <= 264 and pressed[0] == True:
                main.player_char[0] = 1
                pygame.time.delay(100)
            elif 133 <= mouse[0] <= 197 and 200 <= mouse[1] <= 264:
                pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
                screen.blit(arrowimg, (133, 200))
                pygame.draw.rect(screen, RED, (130, 197, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (133, 200, 64, 64))
                screen.blit(arrowimg, (133, 200))
                pygame.draw.rect(screen, BLACK, (130, 197, 70, 70), 5)

            #Allows user to select their chracters
            if 208 <= mouse[0] <= 272 and 200 <= mouse[1] <= 264 and pressed[0] == True:
                main.player_char[0] = 2
                pygame.time.delay(100)
            elif 208 <= mouse[0] <= 272 and 200 <= mouse[1] <= 264:
                pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
                screen.blit(swordimg, (208, 200))
                pygame.draw.rect(screen, RED, (205, 197, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (208, 200, 64, 64))
                screen.blit(swordimg, (208, 200))
                pygame.draw.rect(screen, BLACK, (205, 197, 70, 70), 5)

            #Allows user to select their chracters
            if 283 <= mouse[0] <= 347 and 200 <= mouse[1] <= 264 and pressed[0] == True:
                main.player_char[0] = 3
                pygame.time.delay(100)
            elif 283 <= mouse[0] <= 347 and 200 <= mouse[1] <= 264:
                pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
                screen.blit(staffimg, (283, 200))
                pygame.draw.rect(screen, RED, (280, 197, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (283, 200, 64, 64))
                screen.blit(staffimg, (283, 200))
                pygame.draw.rect(screen, BLACK, (280, 197, 70, 70), 5)

            #Allows user to select their chracters
            if 133 <= mouse[0] <= 197 and 515 <= mouse[1] <= 579 and pressed[0] == True:
                main.player_char[1] = 1
                pygame.time.delay(100)
            elif 133 <= mouse[0] <= 197 and 515 <= mouse[1] <= 579:
                pygame.draw.rect(screen, GREEN, (133, 515, 64, 64))
                screen.blit(arrowimg, (133, 515))
                pygame.draw.rect(screen, RED, (130, 512, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (133, 515, 64, 64))
                screen.blit(arrowimg, (133, 515))
                pygame.draw.rect(screen, BLACK, (130, 512, 70, 70), 5)

            #Allows user to select their chracters
            if 208 <= mouse[0] <= 272 and 515 <= mouse[1] <= 579 and pressed[0] == True:
                main.player_char[1] = 2
                pygame.time.delay(100)
            elif 208 <= mouse[0] <= 272 and 515 <= mouse[1] <= 579:
                pygame.draw.rect(screen, GREEN, (208, 515, 64, 64))
                screen.blit(swordimg, (208, 515))
                pygame.draw.rect(screen, RED, (205, 512, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (208, 515, 64, 64))
                screen.blit(swordimg, (208, 515))
                pygame.draw.rect(screen, BLACK, (205, 512, 70, 70), 5)

            #Allows user to select their chracters
            if 283 <= mouse[0] <= 347 and 515 <= mouse[1] <= 579 and pressed[0] == True:
                main.player_char[1] = 3
                pygame.time.delay(100)
            elif 283 <= mouse[0] <= 347 and 515 <= mouse[1] <= 579:
                pygame.draw.rect(screen, GREEN, (283, 515, 64, 64))
                screen.blit(staffimg, (283, 515))
                pygame.draw.rect(screen, RED, (280, 512, 70, 70), 5)
            else:
                pygame.draw.rect(screen, GREEN, (283, 515, 64, 64))
                screen.blit(staffimg, (283, 515))
                pygame.draw.rect(screen, BLACK, (280, 512, 70, 70), 5)

        #Allows for interaction with the single player and multiplayer buttons
        if 830 <= mouse[0] <= 1230 and 75 <= mouse[1] <= 175 and pressed[0] == True:
            main.player_count = 1
            main.multiplayer = False
            pygame.time.delay(100)
        elif 830 <= mouse[0] <= 1230 and 75 <= mouse[1] <= 175:
            pygame.draw.rect(screen, DARK_GR, (830, 75, 400, 100))
            pygame.draw.rect(screen, RED, (825, 70, 410, 110), 5, 8)
            screen.blit(text6, (840, 90))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (830, 75, 400, 100))
            pygame.draw.rect(screen, BLACK, (825, 70, 410, 110), 5, 8)
            screen.blit(text5, (840, 90))

        #Allows for interaction with the single player and multiplayer buttons
        if 830 <= mouse[0] <= 1230 and 225 <= mouse[1] <= 325 and pressed[0] == True:
            main.player_count = 2
            main.multiplayer = True
            pygame.time.delay(100)
        elif 830 <= mouse[0] <= 1230 and 225 <= mouse[1] <= 325:
            pygame.draw.rect(screen, DARK_GR, (830, 225, 400, 100))
            pygame.draw.rect(screen, RED, (825, 220, 410, 110), 5, 8)
            screen.blit(text8, (850, 240))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (830, 225, 400, 100))
            pygame.draw.rect(screen, BLACK, (825, 220, 410, 110), 5, 8)
            screen.blit(text7, (850, 240))