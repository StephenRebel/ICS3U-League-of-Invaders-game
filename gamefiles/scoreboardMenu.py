def show_score():
    import main

    f = open("highscores.txt", "a+")
    f.close()
    #Create a list of the scores, converts them from strings to ints and sorts them
    f = open("highscores.txt", "r")
    scores = f.read().splitlines()
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    scores.sort(reverse = True)

    #Convert back to string and replaces any blank space with "No score Data"
    for i in range(len(scores)):
        scores[i] = str(scores[i])
    for i in range(3 - len(scores)):
        scores.append("No Score Data")
    f.close()

    return scores

def save_score():
    import main

    main.has_saved = True
    #Convert scores to ints and add player score to the end
    f = open("highscores.txt", "r")
    main.highscores[0] = f.read().splitlines()
    for i in range(len(main.highscores[0])):
        main.highscores[0][i] = int(main.highscores[0][i])
    main.highscores[0].append(sum(main.player_score))
    main.highscores[1].append(main.user_name)
    f.close()

    #Sorts and removes all the lowest scores until there are 3 left
    main.highscores[0].sort(reverse = True)
    while len(main.highscores[0]) > 3:
        main.highscores[0].pop(-1)

    #Rewrite the file with the new scores
    f = open("highscores.txt", "w")
    for i in range(len(main.highscores[0])):
        f.write(str(main.highscores[0][i]) + "\n")
    f.close()

def enter_name():
    import main
    from main import pygame, screen, LIGHT_GR, DARK_GR, BLACK, sml_font

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, BLACK, (95, 495, 160, 40))

    if 100 <= mouse[0] <= 235 and 500 <= mouse[1] <= 530 and pressed[0] == True:
        if main.text_box_active == False:
            main.text_box_active = True
            pygame.draw.rect(screen, DARK_GR, (100, 500, 150, 30))
        else:
            main.text_box_active = False
            pygame.draw.rect(screen, LIGHT_GR, (100, 500, 150, 30))
        pygame.time.delay(200)
    else:
        if main.text_box_active == False:
            pygame.draw.rect(screen, DARK_GR, (100, 500, 150, 30))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (100, 500, 150, 30))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if main.text_box_active == True:
                if event.key == pygame.K_BACKSPACE:
                    main.user_name = main.user_name[:-1]
                elif len(main.user_name) < 9:
                    main.user_name += event.unicode

    txt_surface = sml_font.render(main.user_name, True, BLACK)
    screen.blit(txt_surface, (100, 500))

def scoreboard_menu():
    import main
    from main import pygame, back_ground, screen, LIGHT_GR, DARK_GR, BLACK, RED, GOLD, SILVER, BRONZE, size, menu_select_sound, reset_menu, big_font, med_font, sml_font
    pygame.init()

    #Allows for a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Handles mouse interaction
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Setpup the screen
    screen.blit(back_ground, (0, 0))

    #Initiate all the texts
    text1 = sml_font.render("MAIN MENU", True, BLACK)
    text2 = sml_font.render("MAIN MENU", True, RED)
    text3 = big_font.render("LEADERBOARD", True, BLACK)
    text4 = big_font.render("1", True, BLACK)
    text5 = big_font.render("2", True, BLACK)
    text6 = big_font.render("3", True, BLACK)
    text7 = med_font.render(show_score()[0], True, BLACK)
    text8 = med_font.render(show_score()[1], True, BLACK)
    text9 = med_font.render(show_score()[2], True, BLACK)
    text10 = sml_font.render("SAVE SCORE", True, BLACK)
    text11 = sml_font.render("SAVE SCORE", True, RED)

    #Draw all the things
    pygame.draw.rect(screen, BLACK, (size[0] / 2 - 500 / 2 - 5, 20, 510, 680), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, LIGHT_GR, (size[0] / 2 - 500 / 2, 25, 500, 670), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, BLACK, (400, 110, 480, 3))
    pygame.draw.circle(screen, GOLD, (485, 200), 75)
    screen.blit(text4, (467, 165))
    screen.blit(text7, (600, 175))
    pygame.draw.rect(screen, BLACK, (400, 300, 480, 3))
    pygame.draw.circle(screen, SILVER, (485, 400), 75)
    screen.blit(text5, (467, 365))
    screen.blit(text8, (600, 375))
    pygame.draw.rect(screen, BLACK, (400, 500, 480, 3))
    pygame.draw.circle(screen, BRONZE, (485, 600), 75)
    screen.blit(text6, (467, 565))
    screen.blit(text9, (600, 575))
    screen.blit(text3, (450, 50))

    #Save button to add player score to leader board
    pygame.draw.rect(screen, BLACK, (70, 540, 210, 135), 5, 8)
    if 75 <= mouse[0] <= 255 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        pygame.draw.rect(screen, DARK_GR, (75, 545, 200, 125))
        screen.blit(text11, (110, 595))
        menu_select_sound.play()
        if main.has_saved == False:
            save_score()
        pygame.time.delay(200)
    elif 75 <= mouse[0] <= 255 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (75, 545, 200, 125))
        screen.blit(text11, (110, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (75, 545, 200, 125))
        screen.blit(text10, (110, 595))

    #Main menu button to return and play again if wanted
    pygame.draw.rect(screen, BLACK, (980, 540, 210, 135), 5, 8)
    if 985 <= mouse[0] <= 1165 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        menu_select_sound.play()
        reset_menu()
        main.window = 0
        pygame.time.delay(200)
    elif 985 <= mouse[0] <= 1165 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (985, 545, 200, 125))
        screen.blit(text2, (1020, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (985, 545, 200, 125))
        screen.blit(text1, (1020, 595))

    enter_name()