#Menu to display the end of the game and show some interesting stats
def end_menu():
    import main 
    from main import pygame, window, title_font, big_font, sml_font, BLACK, RED, DARK_GR, LIGHT_GR, background, player_score, screen
    pygame.init()

    #Allows for a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Handles mouse interaction
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Setpup the screen
    screen.blit(background, (0, 0))

    text1 = big_font.render("MAIN MENU", True, BLACK)
    text2 = big_font.render("MAIN MENU", True, RED)
    text3 = title_font.render("GAME OVER", True, BLACK)
    text4 = sml_font.render("Total Score:", True, BLACK)
    text5 = sml_font.render("P1 Score:", True, BLACK)
    text6 = sml_font.render("P2 Score:", True, BLACK)
    text7 = sml_font.render("Total enemies killed:", True, BLACK)
    text8 = sml_font.render("P1 enemies killed:", True, BLACK)
    text9 = sml_font.render("P2 enemies killed:", True, BLACK)
    text10 = sml_font.render("Total abilities used: ", True, BLACK)
    text11 = sml_font.render("P1 abilities used:", True, BLACK)
    text12 = sml_font.render("P2 abilities used:", True, BLACK)
    text13 = sml_font.render("Time played:", True, BLACK)
    text14 = sml_font.render("P1 distance travelled:", True, BLACK)
    text15 = sml_font.render("P2 distance travelled:", True, BLACK)

    pygame.draw.rect(screen, LIGHT_GR, (50, 25, 500, 670), 50, 75)
    pygame.draw.rect(screen, LIGHT_GR, (100, 75, 400, 570))
    pygame.draw.rect(screen, BLACK, (45, 20, 510, 680), 8, 80)
    screen.blit(text3, (122, 30))
    pygame.draw.rect(screen, BLACK, (70, 110, 460, 2))
    screen.blit(text4, (80, 160))
    screen.blit(text5, (80, 190))
    screen.blit(text6, (80, 220))
    screen.blit(text7, (80, 280))
    screen.blit(text8, (80, 310))
    screen.blit(text9, (80, 340))
    screen.blit(text10, (80, 400))
    screen.blit(text11, (80, 430))
    screen.blit(text12, (80, 460))
    screen.blit(text13, (80, 520))
    screen.blit(text14, (80, 580))
    screen.blit(text15, (80, 610))

    #Main menu button to return and play again if wanted
    pygame.draw.rect(screen, BLACK, (800, 540, 410, 135), 5, 8)
    if 805 <= mouse[0] <= 1205 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        main.window = 0
        pygame.time.delay(100)
    elif 805 <= mouse[0] <= 1205 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (805, 545, 400, 125))
        screen.blit(text2, (855, 575))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (805, 545, 400, 125))
        screen.blit(text1, (855, 575))
