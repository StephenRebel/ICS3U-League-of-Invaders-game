def menu():
    import main
    from main import pygame, window, big_font, med_font, background, BLACK, RED, DARK_GR, LIGHT_GR, screen, size
    pygame.init()

    logo = pygame.image.load("gamefiles/images/leagueofinvaders.png")
    text1 = big_font.render("Play", True, BLACK)
    text2 = big_font.render("Play", True, RED)
    text3 = med_font.render("Controls", True, BLACK)
    text4 = med_font.render("Controls", True, RED)
    text5 = med_font.render("Instructions", True, BLACK)
    text6 = med_font.render("Instructions", True, RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    screen.blit(background, (0, 0))
    screen.blit(logo, ((size[0]/2) - 403, 0))
    
    # Play Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.window = 1
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text2, (590, 585))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (590, 585))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 200, 555, 400, 125), 7, 10)

    #Controls Button
    if 128 <= mouse[0] <= 372 and 578 <= mouse[1] <= 657 and pressed[0] == True:
        main.window = 2
    elif 128 <= mouse[0] <= 372 and 578 <= mouse[1] <= 657:
        pygame.draw.rect(screen, DARK_GR, (128, 578, 244, 79))
        screen.blit(text4, (178, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (128, 578, 244, 79))
        screen.blit(text3, (178, 595))
    pygame.draw.rect(screen, BLACK, (125, 575, 250, 85), 5, 8)

    #Instructions Button
    if 908 <= mouse[0] <= 1152 and 578 <= mouse[1] <= 657 and pressed[0] == True:
        main.window = 3
    elif 908 <= mouse[0] <= 1152 and 578 <= mouse[1] <= 657:
        pygame.draw.rect(screen, DARK_GR, (908, 578, 244, 79))
        screen.blit(text6, (928, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (908, 578, 244, 79))
        screen.blit(text5, (928, 595))
    pygame.draw.rect(screen, BLACK, (905, 575, 250, 85), 5, 8)