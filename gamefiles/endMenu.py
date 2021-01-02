#Menu to display the end of the game and show some interesting stats
def end_menu():
    import main 
    from main import pygame, window, title_font, big_font, sml_font, BLACK, RED, DARK_GR, LIGHT_GR, background, screen, player_score, enemies_killed, abilities_used, time_played, distance_travelled, menuselectsound, reset_menu
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

    #Initiate all the texts
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

    #Initiate all the stats
    stat1 = sml_font.render(str(sum(player_score)), True, BLACK)
    stat2 = sml_font.render(str(player_score[0]), True, BLACK)
    stat3 = sml_font.render(str(player_score[1]), True, BLACK)
    stat4 = sml_font.render(str(sum(enemies_killed)), True, BLACK)
    stat5 = sml_font.render(str(enemies_killed[0]), True, BLACK)
    stat6 = sml_font.render(str(enemies_killed[1]), True, BLACK)
    stat7 = sml_font.render(str(sum(abilities_used)), True, BLACK)
    stat8 = sml_font.render(str(abilities_used[0]), True, BLACK)
    stat9 = sml_font.render(str(abilities_used[1]), True, BLACK)
    stat10 = sml_font.render(str(round(time_played)) + "secs", True, BLACK)
    stat11 = sml_font.render(str(distance_travelled[0]), True, BLACK)
    stat12 = sml_font.render(str(distance_travelled[1]), True, BLACK)

    #Output all stats and text to the screen
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
    screen.blit(stat1, (430, 160))
    screen.blit(stat2, (430, 190))
    screen.blit(stat3, (430, 220))
    screen.blit(stat4, (430, 280))
    screen.blit(stat5, (430, 310))
    screen.blit(stat6, (430, 340))
    screen.blit(stat7, (430, 400))
    screen.blit(stat8, (430, 430))
    screen.blit(stat9, (430, 460))
    screen.blit(stat10, (430, 520))
    screen.blit(stat11, (430, 580))
    screen.blit(stat12, (430, 610))

    #Main menu button to return and play again if wanted
    pygame.draw.rect(screen, BLACK, (800, 540, 410, 135), 5, 8)
    if 805 <= mouse[0] <= 1205 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        menuselectsound.play()
        reset_menu()
        main.window = 0
        pygame.time.delay(100)
    elif 805 <= mouse[0] <= 1205 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (805, 545, 400, 125))
        screen.blit(text2, (855, 575))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (805, 545, 400, 125))
        screen.blit(text1, (855, 575))