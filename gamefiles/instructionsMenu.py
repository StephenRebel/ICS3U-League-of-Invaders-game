def menu():
    import main
    from main import pygame, window, bigFont, medFont, background, BLACK, RED, DARK_GR, LIGHT_GR, screen, size

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    screen.blit(background, (0, 0))
    
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.window = 1
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 194, 561, 389, 114))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 194, 561, 389, 114))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 200, 555, 400, 125), 7, 10)