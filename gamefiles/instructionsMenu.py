#Instructions Menu
def instructions():
    #Importing the necessary libraries and varibales from the main
    import main
    from main import pygame, window, big_font, med_font, title_font, background, BLACK, RED, DARK_GR, LIGHT_GR, WHITE, screen, size
    pygame.init()

    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Adds the backgroun to the menu
    screen.blit(background, (0, 0))

    #Declaring all the texts that will be used
    text1 = title_font.render("Instructions", True, BLACK)
    text2 = med_font.render("Defend youselves from incoming enemies!", True, WHITE)
    text3 = med_font.render("Use your chracter's unique abilities to kill your foes!", True, WHITE)
    text4 = med_font.render("If you get attacked too many times, you may lose your life!", True, WHITE)
    text5 = med_font.render("Earn points for each enemy you defeat!", True, WHITE)
    text6 = med_font.render("The game ends when you and your ally both fall!", True, WHITE)
    text7 = med_font.render("Good luck combattants!", True, WHITE)
    text8 = big_font.render("MAIN MENU", True, BLACK)
    text9 = big_font.render("MAIN MENU", True, RED)

    #Outputting all texts to the screen at proper locations
    screen.blit(text1, (455, 25))
    screen.blit(text2, (290, 120))
    screen.blit(text3, (200, 180))
    screen.blit(text4, (165, 240))
    screen.blit(text5, (320, 300))
    screen.blit(text6, (250, 360))
    screen.blit(text7, (447, 420))

    #Creates the main menu button and handles animations
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.window = 0
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text9, (493, 585))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text8, (493, 585))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 200, 555, 400, 125), 7, 10)