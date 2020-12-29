#Pause menu for mid game pauses
def pause():
    import main
    from main import pygame, window, big_font, med_font, RED, BLACK, LIGHT_GR, DARK_GR, grayed_out, screen, size
    pygame.init()

    gray_out_screen = pygame.transform.scale(grayed_out, (1280, 720))
    GRAY = (128, 128, 128)

    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Generating all needed text
    text1 = big_font.render("PAUSED", True, BLACK)
    text2 = med_font.render("Resume game", True, BLACK)
    text3 = med_font.render("Resume game", True, RED)
    text4 = med_font.render("Main menu", True, BLACK)
    text5 = med_font.render("Main menu", True, RED)

    #Graying out the play screen and generating the pause box
    screen.blit(gray_out_screen, (0, 0))
    pygame.draw.rect(screen, GRAY, ((size[0]/2) - 240, (size[1]/2) - 270, 480, 520), 15, 30)
    pygame.draw.rect(screen, GRAY, ((size[0]/2) - 225, (size[1]/2) - 255, 450, 490))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 243, (size[1]/2) - 273, 486, 526), 3, 35)

    if 440 <= mouse[0] <= 840 and 300 <= mouse[1] <= 125 and pressed[0] == True: