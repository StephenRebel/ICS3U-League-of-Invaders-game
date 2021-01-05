import pygame
import random, math, time
pygame.init()

from startMenu import menu
from controlsMenu import controls
from instructionsMenu import instructions
from playMenu import char_selection
from pauseMenu import pause
from endMenu import end_menu

#Basic game setup
pygame.display.set_caption("League Of Invaders")
clock = pygame.time.Clock()
size = (1280, 720)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("gamefiles/images/dirt_bg.jpg").convert_alpha()
bg_scale = pygame.transform.scale(bg, (1280, 720))
char1img = pygame.image.load("gamefiles/images/green_char.png").convert_alpha()
char2img = pygame.image.load("gamefiles/images/blue_char.png").convert_alpha()
arrowimg = pygame.image.load("gamefiles/images/arrow.png").convert_alpha()
swordimg = pygame.image.load("gamefiles/images/sword.png").convert_alpha()
staffimg = pygame.image.load("gamefiles/images/staff.png").convert_alpha()
enemyimg = [pygame.image.load("gamefiles/images/red_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/orange_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/yellow_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/green_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/boss_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/turquoise_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/white_enemy.png").convert_alpha(),]
ballimg = pygame.image.load("gamefiles/images/spike_ball.png").convert_alpha()
boltimg = [pygame.image.load("gamefiles/images/fire_ball.png").convert_alpha(), pygame.image.load("gamefiles/images/ice_spikes.png").convert_alpha(), pygame.image.load("gamefiles/images/green_rock.png").convert_alpha()]
heartimg = pygame.image.load("gamefiles/images/heart.png").convert_alpha()
emptyheartimg = pygame.image.load("gamefiles/images/heart_empty.png").convert_alpha()

#Game variables
multiplayer = False
char, charx, chary, charwidth, charheight, charface, charability, charhealth = [0, 1], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], 64, 64, [0, 0], [0, 0], [3, 3]
arrowx, arrowy, arrowwidth, arrowheight, arrowface, arrowcollisionoccured = [-100, -100], [-100, -100], [10, 10], [62, 62], [0, 0], [False, False]
swordx, swordy, swordwidth, swordheight, swordface = [-100, -100], [-100, -100], [22, 22], [50, 50], [0, 0]
boltx, bolty, boltwidth, boltheight, boltface, staffx, staffy, staffface = [-100, -100], [0, 0], [64, 64], [64, 64], [0, 0], [-100, -100], [-100, -100], [0, 0]
swordcooldownstarted, swordstarttime, swordpassedtime, boltcooldownstarted, boltstarttime, boltpassedtime = [False, False], [0, 0], [0, 0], [False, False], [0, 0], [0, 0]
starttime, cooldownstarted, passedtime = [0, 0], [False, False], [0, 0]
isactive, canuse = [False, False], [True, True]
enemytype, enemyx, enemyy, enemywidth, enemyheight, enemyface, enemyspeed, isalive, enemypoints, benemyhealth, benemyhit = [0, 1, 2, 3, 4, 5, 6], [-100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100], [64, 64, 64, 64, 96, 32, 64], [64, 64, 64, 64, 96, 32, 64], ["", "", "", "", "", "", ""], [1, 0.25, 0, 0.5, 0.35, 1.25, 0.75], [False, False, False, False, False, False, False], [20, 40, 20, 10, 100, 30, 30], 4, [False, False]
enemyball, enemyballx, enemybally, enemyballwidth, enemyballheight, enemyballface = 1, -100, -100, 18, 18, 0
explosion, explosionx, explosiony, explosionradius, explosioncolor = 1, -100, -100, 64, [255, 255, 255]
ballammo, ballisactive, ballcanshoot, ballcooldownstarted, ballstarttime, ballpassedtime = 1, False, True, False, 0, 0
invisiblevalue, decrease, isinvisible, invisiblecooldownstarted, invisiblestarttime, invisiblepassedtime = 255, True, False, False, 0, 0
explosionammo, explosionisactive, cantakedamage, explosioncanshoot, explosioncooldownstarted, explosionstarttime, explosionpassedtime = 1, False, False, True, False, 0, 0
img_num = [0, 0]

#Menu setup
window = 0
title_font = pygame.font.SysFont("Cambria", 65)
big_font = pygame.font.SysFont("Cambria", 54)
med_font = pygame.font.SysFont("Cambria", 36)
sml_font = pygame.font.SysFont("Cambria", 24)
background = pygame.image.load("gamefiles/images/game_background.jpg").convert_alpha()
grayed_out = pygame.image.load("gamefiles/images/gray_out.png").convert_alpha()
menuselectsound = pygame.mixer.Sound("gamefiles/sounds/menu_select_sound.wav")
sworduse = pygame.mixer.Sound("gamefiles/sounds/sword_use.wav")
bowuse = pygame.mixer.Sound("gamefiles/sounds/bow_use.wav")
staffuse = pygame.mixer.Sound("gamefiles/sounds/staff_use.wav")
enemyhit = pygame.mixer.Sound("gamefiles/sounds/enemy_hit.wav")
playerhit = pygame.mixer.Sound("gamefiles/sounds/player_hit.wav")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GR = (211, 211, 211)
DARK_GR = (71, 71, 71)
WHITE = (255, 255, 255)
player_count = 0
player_score, enemies_killed, abilities_used, time_played, distance_travelled = [0, 0], [0, 0], [0, 0], 0, [0, 0]

#Draw characters
def draw_char(img, x, y, face):
    new_char = pygame.transform.rotate(img, face)
    screen.blit(new_char, (x, y))

#Draw arrows
def draw_arrow(img, x, y, face):
    new_arrow = pygame.transform.rotate(img, face)
    if face == 0 or face == 180:
        x -= 30
    elif face == 90 or face == 270:
        y -= 30
    screen.blit(new_arrow, (x, y))

#Draw swords
def draw_sword(img, x, y, face):
    new_sword = pygame.transform.rotate(img, face)
    newx = x
    newy = y
    if face == 0:
        newx = x - 22
    elif face == 90:
        newy = y - 22
    elif face == 180:
        newx = x - 22
        newy -= 10
    elif face == 270:
        newx -= 10
        newy = y - 22
    screen.blit(new_sword, (newx, newy))

#Draw mage bolts
def draw_bolt(img, x, y, face, staff, staffx, staffy, staffface):
    new_staff = pygame.transform.rotate(staff, staffface)
    screen.blit(img, (x, y))
    screen.blit(new_staff, (staffx, staffy))

#Draw pause button
def pause_button():
    import main

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Allow for interactions with the pause button
    if 1233 <= mouse[0] <= 1270 and 8 <= mouse[1] <= 43 and pressed[0] == True:
        menuselectsound.play()
        main.window = 5
        pygame.time.delay(100)
    elif 1233 <= mouse[0] <= 1270 and 8 <= mouse[1] <= 43:
        pygame.draw.rect(screen, DARK_GR, (1235, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, DARK_GR, (1237, 12, 8, 27))
        pygame.draw.rect(screen, DARK_GR, (1258, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, DARK_GR, (1260, 12, 8, 27))
        pygame.draw.rect(screen, BLACK, (1234, 8, 14, 35), 2, 20)
        pygame.draw.rect(screen, BLACK, (1257, 8, 14, 35), 2, 20)
    else:
        pygame.draw.rect(screen, LIGHT_GR, (1235, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, LIGHT_GR, (1237, 12, 8, 27))
        pygame.draw.rect(screen, LIGHT_GR, (1258, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, LIGHT_GR, (1260, 12, 8, 27))
        pygame.draw.rect(screen, BLACK, (1234, 8, 14, 35), 2, 20)
        pygame.draw.rect(screen, BLACK, (1257, 8, 14, 35), 2, 20)

#Draw the cooldown indicators
def draw_cooldowns():
    pos = (0, 0)
    font = med_font
    if passedtime[0] / 1000 == 1 or passedtime[0] / 1000 == 0:
        cooldown = "READY!"
        pos = (527, 637)
        font = sml_font
    else:
        cooldown = str(round(1 - passedtime[0] / 1000, 2))
        pos = (535, 627)
        font = med_font
    pygame.draw.rect(screen, BLACK, (515, 595, 110, 110), 0, 0, 30, 0, 30, 0)
    pygame.draw.rect(screen, DARK_GR, (520, 600, 100, 100), 0, 0, 30, 0, 30, 0)
    pygame.draw.rect(screen, LIGHT_GR, (520, 600, passedtime[0] / 10, 100), 0, 0, 30, 0, 30, 0)
    p1cooldown = font.render((cooldown), True, WHITE)
    screen.blit(p1cooldown, pos)
    if multiplayer:
        if passedtime[1] / 1000 == 1 or passedtime[1] / 1000 == 0:
            cooldown = "READY!"
            pos = (670, 637)
            font = sml_font
        else:
            cooldown = str(round(1 - passedtime[1] / 1000, 2))
            pos = (675, 627)
            font = med_font
        pygame.draw.rect(screen, BLACK, (655, 595, 110, 110), 0, 0, 0, 30, 0, 30)
        pygame.draw.rect(screen, DARK_GR, (660, 600, 100, 100), 0, 0, 0, 30, 0, 30)
        pygame.draw.rect(screen, LIGHT_GR, (760, 600, 0.99 - passedtime[1] / 1000 * 100, 100), 0, 0, 0, 30, 0, 30)
        p2cooldown = font.render((cooldown), True, WHITE)
        screen.blit(p2cooldown, pos)

#Draws the amount of hearts the players have
def draw_hearts(img, empty_img):
    #Character 1
    for i in range(0, charhealth[0]):
        screen.blit(img, (400 - 100 * i, 620))
    for i in range(0, 3 - charhealth[0]):
        screen.blit(empty_img, (200 + 100 * i, 620))

    #Character 2
    if multiplayer:
        for i in range(0, charhealth[1]):
            screen.blit(img, (820 + 100 * i, 620))
        for i in range(0, 3 - charhealth[1]):
            screen.blit(empty_img, (1020 - 100 * i, 620))

#Creates the text that will show total player score
def draw_player_score(player_score):
    #Sum all values of the list to get total score
    total_score = sum(player_score)
    score = big_font.render("Score: " + str(total_score), True, BLACK)
    pygame.draw.rect(screen, BLACK, (465, 5, 385, 80), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, LIGHT_GR, (470, 10, 375, 70), 0, 30, 30, 30, 30)
    screen.blit(score, (500, 10))

#Draw the screen
def draw_screen():
    #Background
    screen.blit(bg_scale, (0, 0))

    #Character
    draw_char(char1img, charx[0], chary[0], charface[0])
    if multiplayer == True:
        draw_char(char2img, charx[1], chary[1], charface[1])

    #Arrow
    if charability[0] == 1:
        draw_arrow(arrowimg, arrowx[0], arrowy[0], arrowface[0])
    if multiplayer == True and charability[1] == 1:
        draw_arrow(arrowimg, arrowx[1], arrowy[1], arrowface[1])

    #Sword
    if charability[0] == 2:
        draw_sword(swordimg, swordx[0], swordy[0], swordface[0])
    if multiplayer == True and charability[1] == 2:
        draw_sword(swordimg, swordx[1], swordy[1], swordface[1])

    #Mage bolt
    if charability[0] == 3:
        draw_bolt(boltimg[img_num[0]], boltx[0], bolty[0], boltface[0], staffimg, staffx[0], staffy[0], staffface[0])
    if multiplayer == True and charability[1] == 3:
        draw_bolt(boltimg[img_num[1]], boltx[1], bolty[1], boltface[1], staffimg, staffx[1], staffy[1], staffface[1])

    #Enemies
    for i in range(len(enemytype)):
        screen.blit(enemyimg[i], (enemyx[i], enemyy[i]))

    #Draw boss health
    pygame.draw.rect(screen, BLACK, (enemyx[4], enemyy[4] - 25, enemywidth[4], 15))
    pygame.draw.rect(screen, RED, (enemyx[4], enemyy[4] - 25, enemywidth[4] / 4 * benemyhealth, 15))

    #Spike ball
    screen.blit(ballimg, (enemyballx, enemybally))

    #Explosion
    pygame.draw.circle(screen, explosioncolor, [explosionx + 32, explosiony + 32], explosionradius / 2)

    #Pause Button
    pause_button()

    #Cooldown
    draw_cooldowns()

    #Hearts
    draw_hearts(heartimg, emptyheartimg)

    #Total score
    draw_player_score(player_score)

#Move character function
def move_char(char):
    import main

    keys = pygame.key.get_pressed()
    key_type = []
    if char == 0:
        key_type.append(keys[pygame.K_LEFT])
        key_type.append(keys[pygame.K_RIGHT])
        key_type.append(keys[pygame.K_UP])
        key_type.append(keys[pygame.K_DOWN])
    elif char == 1:
        key_type.append(keys[pygame.K_a])
        key_type.append(keys[pygame.K_d])
        key_type.append(keys[pygame.K_w])
        key_type.append(keys[pygame.K_s])

    #Changes speed based on ability
    extraspeed = 0
    if main.charability[char] == 2:
        extraspeed = 0.5
    elif main.charability[char] == 3:
        extraspeed = 0.2

    # Movement for both players
    if main.charhealth[char] > 0:
        if key_type[0]:
            main.charface[char] = 90
            if main.charx[char] - 1 <= 0:
                main.charx[char] = 0
            else:
                main.charx[char] -= 2 + extraspeed
                main.distance_travelled[char] += 2 + extraspeed
        elif key_type[1]:
            main.charface[char] = 270
            if main.charx[char] + 1 >= size[0] - charwidth:
                main.charx[char] = size[0] - charwidth
            else:
                main.charx[char] += 2 + extraspeed
                main.distance_travelled[char] += 2 + extraspeed
        elif key_type[2]:
            main.charface[char] = 0
            if main.chary[char] - 1 <= 0:
                main.chary[char] = 0
            else:
                main.chary[char] -= 2 + extraspeed
                main.distance_travelled[char] += 2 + extraspeed
        elif key_type[3]:
            main.charface[char] = 180
            if main.chary[char] + 1 >= size[1] - charheight:
                main.chary[char] = size[1] - charheight
            else:
                main.chary[char] += 2 + extraspeed
                main.distance_travelled[char] += 2 + extraspeed

#Use ability function
def use_ability(char):
    import main

    keys = pygame.key.get_pressed()
    key_type = []
    if char == 0: key_type.append(keys[pygame.K_SPACE])
    elif char == 1: key_type.append(keys[pygame.K_e])

    if key_type[0] and main.isactive[char] == False and main.canuse[char] == True and main.charhealth[char] > 0:
        main.isactive[char] = True
        main.canuse[char] = False
        main.abilities_used[char] += 1

        #Arrow ability    
        if main.charability[char] == 1:
            bowuse.play()
            main.arrowface[char] = main.charface[char]
            if main.arrowface[char] == 0 or main.arrowface[char] == 180:
                main.arrowwidth[char], main.arrowheight[char] = 8, 64
                main.arrowx[char], main.arrowy[char] = main.charx[char] + (charwidth / 2) - main.arrowwidth[char] / 2, main.chary[char] + (charheight / 2)
            elif main.arrowface[char] == 90 or main.arrowface[char] == 270:
                main.arrowwidth[char], main.arrowheight[char] = 64, 8
                main.arrowx[char], main.arrowy[char] = main.charx[char] + (charwidth / 2), main.chary[char] + (charheight / 2) - main.arrowheight[char] / 2

        #Sword ability
        elif charability[char] == 2:
            sworduse.play()
            main.swordface[char] = main.charface[char]
            if main.swordface[char] == 0:
                main.swordwidth[char], main.swordheight[char] = 22, 50
                main.swordx[char], main.swordy[char] = main.charx[char], main.chary[char] - charheight + 10
            elif main.swordface[char] == 90:
                main.swordwidth[char], main.swordheight[char] = 50, 22
                main.swordx[char], main.swordy[char] = main.charx[char] - charwidth + 10, main.chary[char]
            elif main.swordface[char] == 180:
                main.swordwidth[char], main.swordheight[char] = 22, 50
                main.swordx[char], main.swordy[char] = main.charx[char], main.chary[char] + charheight - 10
            elif main.swordface[char] == 270:
                main.swordwidth[char], main.swordheight[char] = 50, 22
                main.swordx[char], main.swordy[char] = main.charx[char] + charwidth - 10, main.chary[char]   

        #Mage bolt ability
        elif main.charability[char] == 3:
            staffuse.play()
            main.boltface[char] = main.charface[char]
            main.img_num[char] = random.randrange(0, 3)
            if main.boltface[char] == 0:
                main.boltx[char], main.bolty[char] = main.charx[char], main.chary[char] - charheight - 128
            elif main.boltface[char] == 90:
                main.boltx[char], main.bolty[char] = main.charx[char] - charwidth - 128, main.chary[char]
            elif main.boltface[char] == 180:
                main.boltx[char], main.bolty[char] = main.charx[char], main.chary[char] + charheight + 128
            elif main.boltface[char] == 270:
                main.boltx[char], main.bolty[char] = main.charx[char] + charwidth + 128, main.chary[char]

#Run ability function
def run_ability(char):
    import main

    #Arrow ability
    if main.charability[char] == 1 and main.isactive[char] == True:
        from main import arrowface, arrowx, arrowy
        if main.arrowface[char] == 0 and main.arrowy[char] > -64:
            main.arrowy[char] -= 10
        elif main.arrowface[char] == 180 and main.arrowy[char] < size[1] + 64:
            main.arrowy[char] += 10
        elif main.arrowface[char] == 270 and main.arrowx[char] < size[0] + 64:
            main.arrowx[char] += 10
        elif main.arrowface[char] == 90 and main.arrowx[char] > -64:
            main.arrowx[char] -= 10
        else:
            main.isactive[char] = False

    #Sword ability
    if main.charability[char] == 2 and main.isactive[char] == True:
        if main.swordface[char] == 0:
            main.swordwidth[char], main.swordheight[char] = 22, 50
            main.swordx[char], main.swordy[char] = main.charx[char] + main.swordwidth[char], main.chary[char] - charheight + 10
        elif main.swordface[char] == 90:
            main.swordwidth[char], main.swordheight[char] = 50, 22
            main.swordx[char], main.swordy[char] = main.charx[char] - charwidth + 10, main.chary[char] + main.swordheight[char]
        elif main.swordface[char] == 180:
            main.swordwidth[char], main.swordheight[char] = 22, 50
            main.swordx[char], main.swordy[char] = main.charx[char] + main.swordwidth[char], main.chary[char] + charheight 
        elif main.swordface[char] == 270:
            main.swordwidth[char], main.swordheight[char] = 50, 22
            main.swordx[char], main.swordy[char] = main.charx[char] + charwidth, main.chary[char] + main.swordheight[char]
        #Makes the sword appear for 0.5 seconds
        main.swordcooldownstarted[char], main.swordstarttime[char], main.swordpassedtime[char] = ability_cooldown(main.swordcooldownstarted[char], main.swordstarttime[char], main.swordpassedtime[char])
        if main.swordpassedtime[char] >= 500:
            main.swordpassedtime[char] = 0
            main.swordcooldownstarted[char] = False
            main.isactive[char] = False
            main.swordx[char], main.swordy[char] = -100, -100
            main.benemyhit[char] = False

    #Mage bolt ability
    if main.charability[char] == 3 and main.isactive[char] == True:
        from main import staffx, staffy, staffface, boltcooldownstarted, boltstarttime, boltpassedtime
        main.staffface[char] = main.charface[char]
        if main.staffface[char] == 0:
            main.staffx[char], main.staffy[char] = main.charx[char], main.chary[char] - charheight
        elif main.staffface[char] == 90:
            main.staffx[char], main.staffy[char] = main.charx[char] - charwidth, main.chary[char]
        elif main.staffface[char] == 180:
            main.staffx[char], main.staffy[char] = main.charx[char], main.chary[char] + charheight
        elif staffface[char] == 270:
            main.staffx[char], main.staffy[char] = main.charx[char] + charwidth, main.chary[char]
        #Makes the bolt disapear after 1 second
        main.boltcooldownstarted[char], main.boltstarttime[char], main.boltpassedtime[char] = ability_cooldown(main.boltcooldownstarted[char], main.boltstarttime[char], main.boltpassedtime[char])
        if main.boltpassedtime[char] >= 500:
            main.boltpassedtime[char] = 0
            main.boltcooldownstarted[char] = False
            main.isactive[char] = False
            main.boltx[char], main.bolty[char] = -100, -100
            main.staffx[char], main.staffy[char] = -100, -100
            main.benemyhit[char] = False

    #Starts the cooldown after ability is done
    if main.isactive[char] == False and main.canuse[char] == False and main.arrowcollisionoccured[char] == False:
        main.cooldownstarted[char], main.starttime[char], main.passedtime[char] = ability_cooldown(main.cooldownstarted[char], main.starttime[char], main.passedtime[char])
        if main.passedtime[char] >= 1000:
            main.passedtime[char] = 0
            main.cooldownstarted[char] = False
            main.canuse[char] = True

#Gets the cooldown after an ability has been used
def ability_cooldown(cooldownstarted, starttime, passedtime):
    if cooldownstarted == False:
        cooldownstarted = True
        starttime = pygame.time.get_ticks()
    if cooldownstarted == True:
        passedtime = pygame.time.get_ticks() - starttime
    return cooldownstarted, starttime, passedtime

#Run spike ball function
def enemy_shoot_spike_ball(): 
    import main
    #Enemy shoots the spike ball 
    if main.ballammo > 0 and main.ballisactive == False and main.ballcanshoot == True:
        main.ballammo -= 1
        main.enemyballface = main.enemyface[1]
        main.enemyballx, main.enemybally = main.enemyx[1], main.enemyy[1]
        main.ballisactive = True
        main.ballcanshoot = False
    #Spike ball flies through the air
    if main.ballisactive == True:
        if main.enemyballface == "North" and main.enemybally > -main.enemyballheight * 3:
            main.enemybally -= 3
            main.enemyballx += 5 * math.sin(0.1 * main.enemybally)
        elif main.enemyballface == "East" and main.enemyballx < size[0] + main.enemyballwidth * 3:
            main.enemyballx += 3
            main.enemybally += (5 * math.sin(0.1 * enemyballx))
        elif main.enemyballface == "South" and main.enemybally < size[1] + main.enemyballheight * 3:
            main.enemybally += 3
            main.enemyballx += 5 * math.sin(0.1 * enemybally)
        elif main.enemyballface == "West" and main.enemyballx > -main.enemyballwidth * 3:
            main.enemyballx -= 3
            main.enemybally += (5 * math.sin(0.1 * main.enemyballx))
        else:
            main.ballisactive = False
            main.ballammo += 1
    else:
        main.ballcooldownstarted, main.ballstarttime, main.ballpassedtime = ability_cooldown(main.ballcooldownstarted, main.ballstarttime, main.ballpassedtime)
        if main.ballpassedtime >= 2000:
            main.ballpassedtime = 0
            main.ballcooldownstarted = False
            main.ballcanshoot = True

#Run shoot explosion function
def enemy_shoot_explosion():
    import main

    #Shoot the exlosion
    if main.explosionammo > 0 and main.explosionisactive == False and main.explosioncanshoot == True:
        main.cantakedamage = False
        main.explosionammo -= 1
        main.explosionx, main.explosiony = find_closest_char(main.enemyx[2], main.enemyy[2])
        main.explosionisactive = True
    #Explosion countdown
    if main.explosionisactive == True:
        if main.explosioncolor[0] > 82 and main.explosioncolor[1] > 72 and main.explosioncolor[2] > 0:
            main.explosioncolor[0] -= 0.67
            main.explosioncolor[1] -= 0.71
            main.explosioncolor[2] -= 1
        else:
            main.explosionammo += 1
            main.explosioncolor = [255, 255, 255]
            main.cantakedamage = True
            main.explosionisactive = False
            main.explosioncanshoot = False
    else:
        main.explosioncooldownstarted, main.explosionstarttime, main.explosionpassedtime = ability_cooldown(main.explosioncooldownstarted, main.explosionstarttime, main.explosionpassedtime)
        if main.explosionpassedtime >= 2000:
            main.explosionpassedtime = 0
            main.explosioncooldownstarted = False
            main.explosioncanshoot = True

#Run the invisible function
def enemy_invisible():
    import main

    enemyimg[6].set_alpha(main.invisiblevalue)
    if main.invisiblevalue == 0:
        main.isinvisible = True
        main.invisiblecooldownstarted, main.invisiblestarttime, main.invisiblepassedtime = ability_cooldown(main.invisiblecooldownstarted, main.invisiblestarttime, main.invisiblepassedtime)
        if main.invisiblepassedtime >= 3000:
            main.decrease = False
            main.invisiblepassedtime = 0
            main.invisiblecooldownstarted = False
            main.isinvisible = False
    elif main.invisiblevalue >= 255:
        main.decrease = True
    if main.isinvisible == False:
        if main.decrease == True and main.invisiblevalue >= 1:
            main.invisiblevalue -= 1
        elif main.decrease == False and main.invisiblevalue <= 255:
            main.invisiblevalue += 1

#Find closest character
def find_closest_char(enemyx, enemyy):
    if multiplayer:
        if (abs(enemyx - charx[0]) ** 2 + abs(enemyy - chary[0]) ** 2) < (abs(enemyx - charx[1]) ** 2 + abs(enemyy - chary[1]) ** 2):
            closest_char = [charx[0], chary[0]]
        else:
            closest_char = [charx[1], chary[1]]
    else:
        closest_char = [charx[0], chary[0]]
    return closest_char

#Run function to move enemy
def move_enemy(enemytype):
    import main
    closest_char = find_closest_char(enemyx[enemytype], enemyy[enemytype])
    if (main.enemyx[enemytype] + main.enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2) == 0:
        slope = 0.01
    else:
        slope = abs(((main.enemyy[enemytype] + main.enemyheight[enemytype] / 2) - (closest_char[1] + charheight / 2)) / ((main.enemyx[enemytype] + main.enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2)))
    if slope < 1:
        if (main.enemyx[enemytype] + main.enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2) > 0:
            main.enemyx[enemytype] -= main.enemyspeed[enemytype]
            main.enemyface[enemytype] = "West"
        elif (main.enemyx[enemytype] + main.enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2) < 0:
            main.enemyx[enemytype] += main.enemyspeed[enemytype]
            main.enemyface[enemytype] = "East"
        if (main.enemyy[enemytype] + main.enemyheight[enemytype] / 2) - (closest_char[1] + charheight / 2) > 0:
            main.enemyy[enemytype] -= slope * main.enemyspeed[enemytype]
        elif (main.enemyy[enemytype] + main.enemyheight[enemytype] / 2) - (closest_char[1] + charheight / 2) < 0:
            main.enemyy[enemytype] += slope * main.enemyspeed[enemytype]
    else:
        if (main.enemyy[enemytype] + main.enemyy[enemytype] / 2) - (closest_char[1] + charheight / 2) == 0:
            slope = 0.01
        else:
            slope = abs(((enemyx[enemytype] + enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2)) / ((enemyy[enemytype] + enemyheight[enemytype] / 2) - (closest_char[1] + charheight / 2)))             
        if (main.enemyx[enemytype] + main.enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2) > 0:
            main.enemyx[enemytype] -= slope * main.enemyspeed[enemytype]
        elif (main.enemyx[enemytype] + main.enemywidth[enemytype] / 2) - (closest_char[0] + charwidth / 2) < 0:
            main.enemyx[enemytype] += slope * main.enemyspeed[enemytype]
        if (main.enemyy[enemytype] + main.enemyheight[enemytype] / 2) - (closest_char[1] + charheight / 2) > 0:
            main.enemyy[enemytype] -= main.enemyspeed[enemytype]
            main.enemyface[enemytype] = "North"
        elif (main.enemyy[enemytype] + main.enemyheight[enemytype] / 2) - (closest_char[1] + charheight / 2) < 0:
            main.enemyy[enemytype] += main.enemyspeed[enemytype]
            main.enemyface[enemytype] = "South"

def spawn_enemy(enemytype):
    import main
    if main.isalive[enemytype] == False:
        main.isalive[enemytype] = True
        chooseside = round(random.randrange(1, 5))
        if chooseside == 1:
            main.enemyx[enemytype], main.enemyy[enemytype] = random.randrange(enemywidth[enemytype], size[0] - enemywidth[enemytype]), 0
        elif chooseside == 2:
            main.enemyx[enemytype], main.enemyy[enemytype] = 0, random.randrange(enemyheight[enemytype], size[1] - enemyheight[enemytype])
        elif chooseside == 3:
            main.enemyx[enemytype], main.enemyy[enemytype] = random.randrange(enemywidth[enemytype], size[0] - enemywidth[enemytype]), size[1] - enemyheight[enemytype]
        elif chooseside == 4:
            main.enemyx[enemytype], main.enemyy[enemytype] = size[0] - enemywidth[enemytype], random.randrange(enemyheight[enemytype], size[1] - enemyheight[enemytype])

def give_points(char, enemytype):
    import main

    main.player_score[char] += enemypoints[enemytype]
    main.enemies_killed[char] += 1

def collision_sorting(char, enemytype):
    import main

    if enemytype == 4 and main.benemyhealth == 1 and main.benemyhit[char] == False:
        enemyhit.play()
        main.isalive[enemytype] = False
        main.benemyhealth = 4
        give_points(char, enemytype)
    elif enemytype == 4 and main.benemyhit[char] == False:
        if main.charability[char] != 1:
            main.benemyhit[char] = True
        enemyhit.play()
        main.benemyhealth -= 1
    elif enemytype != 4:
        if enemytype == 6:
            main.invisiblevalue = 255
            main.invisiblecooldownstarted = False
            main.isinvisible = False
        enemyhit.play()
        main.isalive[enemytype] = False
        give_points(char, enemytype)

#Run function to detect collision between enemy and player
def enemy_player_collision(char, enemytype):
    import main

    for enemyxpos in range(int(main.enemyx[enemytype]), int(main.enemyx[enemytype] + main.enemywidth[enemytype])):
        if charx[char] + charwidth >= enemyxpos >= charx[char]:
            for enemyypos in range(int(main.enemyy[enemytype]), int(main.enemyy[enemytype] + main.enemyheight[enemytype])):
                if main.chary[char] + charheight >= enemyypos >= main.chary[char]:
                    main.isalive[enemytype] = False
                    playerhit.play()
                    main.charhealth[char] -= 1
                    if enemytype == 4:
                        main.benemyhealth = 4
                    if main.charhealth[char] <= 0:
                        main.charx[char], main.chary[char] = -100000, -100000
                    break
            break

#Run function to detect collision between enemy and ball
def player_ball_collision(char):
    import main

    for ballxpos in range(int(main.enemyballx + 18), int(main.enemyballx + 48)):
        if main.charx[char] + main.charwidth >= ballxpos >= main.charx[char]:
            for ballypos in range(int(main.enemybally + 18), int(main.enemybally + 48)):
                if main.chary[char] + main.charheight >= ballypos >= main.chary[char]:
                    playerhit.play()
                    main.enemyballx, enemybally = -100000, -100000 
                    main.ballisactive = False
                    main.ballammo += 1
                    main.charhealth[char] -= 1
                    if main.charhealth[char] <= 0:
                        main.charx[char], main.chary[char] = -100000, -100000
                    break
            break

#Run function to detect collision between explosion and player
def explosion_player_collision(char):
    import main

    for enemyxpos in range(int(main.explosionx), int(main.explosionx + main.explosionradius)):
        if main.charx[char] + main.charwidth >= enemyxpos >= main.charx[char]:
            for enemyypos in range(int(main.explosiony), int(main.explosiony + main.explosionradius)):
                if main.chary[char] + main.charheight >= enemyypos >= main.chary[char]:
                    playerhit.play()
                    main.charhealth[char] -= 1
                    if main.charhealth[char] <= 0:
                        main.charx[char], main.chary[char] = -100000, -100000
                    break
            break
    main.explosionx, main.explosiony = -100, -100

#Run function to detect collision between enemy and arrow
def enemy_arrow_collision(char, enemytype):
    import main

    for enemyxpos in range(int(main.enemyx[enemytype]), int(main.enemyx[enemytype] + main.enemywidth[enemytype])):
        if main.arrowx[char] + main.arrowwidth[char] >= enemyxpos >= main.arrowx[char]:
            for enemyypos in range(int(main.enemyy[enemytype]), int(main.enemyy[enemytype] + main.enemyheight[enemytype])):
                if main.arrowy[char] + main.arrowheight[char] >= enemyypos >= main.arrowy[char]:
                    collision_sorting(char, enemytype)
                    main.arrowcollisionoccured[char] = True
                    main.arrowx[char], main.arrowy[char] = -100000, -100000 
                    main.isactive[char] = False
                    break
            break

    if main.arrowcollisionoccured[char] == True:
        main.cooldownstarted[char], main.starttime[char], main.passedtime[char] = ability_cooldown(main.cooldownstarted[char], main.starttime[char], main.passedtime[char])
        if main.passedtime[char] >= 1000:
            main.passedtime[char] = 0
            main.cooldownstarted[char] = False
            main.arrowcollisionoccured[char] = False
            main.canuse[char] = True

#Run function to detect collision between enemy and sword
def enemy_sword_collision(char, enemytype):
    import main

    for enemyxpos in range(int(main.enemyx[enemytype]), int(main.enemyx[enemytype] + main.enemywidth[enemytype])):
        if main.swordx[char] + main.swordwidth[char] >= enemyxpos >= main.swordx[char]:
            for enemyypos in range(int(main.enemyy[enemytype]), int(main.enemyy[enemytype] + main.enemyheight[enemytype])):
                if main.swordy[char] + main.swordheight[char] >= enemyypos >= main.swordy[char]:
                    collision_sorting(char, enemytype)
                    break
            break

#Run function to detect collision between enemy and mage bolt
def enemy_bolt_collision(char, enemytype):
    import main

    for enemyxpos in range(int(main.enemyx[enemytype]), int(main.enemyx[enemytype] + main.enemywidth[enemytype])):
        if (main.boltx[char]) + main.boltwidth[char] >= enemyxpos >= (main.boltx[char]):
            for enemyypos in range(int(main.enemyy[enemytype]), int(main.enemyy[enemytype] + main.enemyheight[enemytype])):
                if (main.bolty[char]) + main.boltheight[char] >= enemyypos >= (main.bolty[char]):
                    collision_sorting(char, enemytype)
                    break
            break

#Run function to reset menu variables when using a button to take you back to main menu
def reset_menu():
    import main
    import playMenu

    main.player_count, main.charability, main.charx, main.chary, main.arrowx, main.arrowy, main.swordx, main.swordy, main.boltx, main.bolty, main.staffx, main.staffy = 0, [0,0], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], [-100, -100], [0, 0], [-100, -100], [-100, -100], [-100, -100], [-100, -100], [-100, -100], [-100, -100]
    main.enemyx, main.enemyy, main.isalive = [-100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100], [False, False, False, False, False, False, False]
    main.benemyhealth = 4
    main.charhealth = [3, 3]
    main.charface, main.arrowface, main.swordface = [0, 0], [0, 0], [0, 0]
    main.enemyballx, main.enemybally, main.explosionx, main.explosiony, main.ballisactive, main.ballammo, main.explosionammo, main.explosionisactive, main.cantakedamage, main.explosioncolor = -100, -100, -100, -100, False, 1, 1, False, False, [255, 255, 255]
    playMenu.selected = [0, 0]
    main.swordcooldownstarted, main.swordstarttime, main.swordpassedtime, main.boltcooldownstarted, main.boltstarttime, main.boltpassedtime = [False, False], [0, 0], [0, 0], [False, False], [0, 0], [0, 0]
    main.passedtime, main.cooldownstarted, main.starttime, main.isactive, main.canuse = [0, 0], [False, False], [0, 0], [False, False], [True, True]
    main.player_score, main.enemies_killed, main.abilities_used, main.time_played, main.distance_travelled = [0, 0], [0, 0], [0, 0], 0, [0, 0]

#Main game loop
rungame = True
while rungame:

    pygame.time.delay(10)
    
    #Close game when quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
    
    if window != 4:
        gamestart = pygame.time.get_ticks()

    #Main menu
    if window == 0:
        menu()

    #Control menu
    elif window == 1:
        controls()

    #Instruction menu
    elif window == 2:
        instructions()

    #Character select menu
    elif window == 3:
        char_selection()

    #Main game
    elif window == 4:
        #Start game time
        gametime = round((pygame.time.get_ticks() - gamestart) / 1000, 2)

        #Drawing characters
        move_char(char[0])
        if multiplayer == True:
            move_char(char[1])
            
        #Drawing abilities
        for i in range(1, 4):
            if charability[0] == i:
                use_ability(char[0])
                run_ability(char[0])
            if multiplayer == True and charability[1] == i:
                use_ability(char[1])
                run_ability(char[1])

        #Spawning enemies
        for i in range(len(enemytype)):
            spawn_enemy(enemytype[i])

        #Drawing Enemies
        for i in range(len(enemytype)):
            move_enemy(enemytype[i])

        #Drawing enemy spike ball
        enemy_shoot_spike_ball()

        #Drawing the explosion
        enemy_shoot_explosion()

        #Sets the invisible value for the invisible enemy
        enemy_invisible()
        
        #Enemy collision with player
        for i in range(len(enemytype)):
            enemy_player_collision(char[0], enemytype[i])  
            if multiplayer:
                enemy_player_collision(char[1], enemytype[i])  
            
        #Enemy spike ball collision with player
        player_ball_collision(char[0])
        if multiplayer:
            player_ball_collision(char[1])

        #Explosion collision with player
        if cantakedamage == True:
            explosion_player_collision(char[0])
            if multiplayer == True:
                explosion_player_collision(char[1])

        for i in range(len(enemytype)):
            #Enemy collision with arrow
            if charability[0] == 1:
                enemy_arrow_collision(char[0], enemytype[i])
            if charability[1] == 1 and multiplayer == True:
                enemy_arrow_collision(char[1], enemytype[i])
            #Enemy collision with sword
            if charability[0] == 2:
                enemy_sword_collision(char[0], enemytype[i])
            if charability[1] == 2 and multiplayer == True:
                enemy_sword_collision(char[1], enemytype[i])  
            #Enemy collision with mage bolt
            if charability[0] == 3:
                enemy_bolt_collision(char[0], enemytype[i])
            if charability[1] == 3 and multiplayer == True:
                enemy_bolt_collision(char[1], enemytype[i])  

        #Ends game when players lose all health
        if multiplayer == False:
            if charhealth[0] <= 0:
                window = 6
        elif multiplayer == True:
            if charhealth[0] <= 0 and charhealth[1] <= 0:
                window = 6
            
        #Draw all the changes
        draw_screen()

    #Pause window
    elif window == 5:
        pause()

    #End screen
    elif window == 6:
        end_menu()

    pygame.display.update()
    
pygame.quit()