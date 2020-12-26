def menu():
    import main
    from main import pygame, window, bigFont, medFont, background, BLACK, RED, DARK_GR, LIGHT_GR, screen, size

    logo = pygame.image.load("gamefiles/images/leagueofinvaders.png")
    text1 = bigFont.render("Play", True, BLACK)
    text2 = bigFont.render("Play", True, RED)
    text3 = medFont.render("Controls", True, BLACK)
    text4 = medFont.render("Controls", True, RED)
    text5 = medFont.render("Instructions", True, BLACK)
    text6 = medFont.render("Instructions", True, RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    screen.blit(background, (0, 0))
    screen.blit(logo, ((size[0]/2) - 403, 0))
    
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.window = 1
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text2, (590, 585))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (590, 585))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 200, 555, 400, 125), 7, 10)