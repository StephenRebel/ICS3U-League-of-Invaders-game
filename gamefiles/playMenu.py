#Chracter selection menu
def char_selection():
    #Importing all necessary libraries and variables from main
    import main
    from main import pygame, title_font, big_font, med_font, background, window, BLACK, RED, DARK_GR, LIGHT_GR, screen, arrowimg, staffimg, swordimg
    pygame.init()

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
