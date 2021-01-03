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
enemy1img = pygame.image.load("gamefiles/images/red_enemy.png").convert_alpha()
enemy2img = pygame.image.load("gamefiles/images/orange_enemy.png").convert_alpha()
enemy3img = pygame.image.load("gamefiles/images/yellow_enemy.png").convert_alpha()
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
enemytype, enemyx, enemyy, enemywidth, enemyheight, enemyface, enemyspeed, isalive = [0, 1, 2], [-100, -100, -100], [-100, -100, -100], 64, 64, ["", "", ""], [1, 0.5], [False, False, False]
enemyball, enemyballx, enemybally, enemyballwidth, enemyballheight, enemyballface = 1, -100, -100, 18, 18, 0
explosion, explosionx, explosiony, explosionradius, explosioncolor = 1, -100, -100, 64, [255, 255, 255]
ballammo, ballisactive = 1, False
explosionammo, explosionisactive, cantakedamage = 1, False, False
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
def draw_bolt(img, x, y, face, img_num, staff, staffx, staffy, staffface):
    new_staff = pygame.transform.rotate(staff, staffface)
    screen.blit(img, (x, y))
    screen.blit(new_staff, (staffx, staffy))

#Draw pause button
def pause_button():
    import main
    from main import window

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Allow for interactions with the pause button
    if 1233 <= mouse[0] <= 1270 and 8 <= mouse[1] <= 43 and pressed[0] == True:
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
        draw_bolt(boltimg[img_num[0]], boltx[0], bolty[0], boltface[0], img_num[0], staffimg, staffx[0], staffy[0], staffface[0])
    if multiplayer == True and charability[1] == 3:
        draw_bolt(boltimg[img_num[1]], boltx[1], bolty[1], boltface[1], img_num[1], staffimg, staffx[1], staffy[1], staffface[1])

    #Enemies
    screen.blit(enemy1img, (enemyx[0], enemyy[0]))
    screen.blit(enemy2img, (enemyx[1], enemyy[1]))
    screen.blit(enemy3img, (enemyx[2], enemyy[2]))

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
    from main import charx, chary, charwidth, charheight, charface, charability, charhealth

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
    if charability[char] == 2:
        extraspeed = 0.5
    elif charability[char] == 3:
        extraspeed = 0.2

    # Movement for both players
    if charhealth[char] > 0:
        if key_type[0]:
            charface[char] = 90
            if charx[char] - 1 <= 0:
                charx[char] = 0
            else:
                charx[char] -= 2 + extraspeed
                distance_travelled[char] += 2 + extraspeed
        elif key_type[1]:
            charface[char] = 270
            if charx[char] + 1 >= size[0] - charwidth:
                charx[char] = size[0] - charwidth
            else:
                charx[char] += 2 + extraspeed
                distance_travelled[char] += 2 + extraspeed
        elif key_type[2]:
            charface[char] = 0
            if chary[char] - 1 <= 0:
                chary[char] = 0
            else:
                chary[char] -= 2 + extraspeed
                distance_travelled[char] += 2 + extraspeed
        elif key_type[3]:
            charface[char] = 180
            if chary[char] + 1 >= size[1] - charheight:
                chary[char] = size[1] - charheight
            else:
                chary[char] += 2 + extraspeed
                distance_travelled[char] += 2 + extraspeed

#Use ability function
def use_ability(char):
    from main import charx, chary, charface, charability, charhealth, isactive, canuse

    keys = pygame.key.get_pressed()
    key_type = []
    if char == 0: key_type.append(keys[pygame.K_SPACE])
    elif char == 1: key_type.append(keys[pygame.K_e])

    if key_type[0] and isactive[char] == False and canuse[char] == True and charhealth[char] > 0:
        isactive[char] = True
        canuse[char] = False
        abilities_used[char] += 1

        #Arrow ability    
        if charability[char] == 1:
            from main import arrowx, arrowy, arrowwidth, arrowheight, arrowface
            bowuse.play()
            arrowface[char] = charface[char]
            if arrowface[char] == 0 or arrowface[char] == 180:
                arrowwidth[char], arrowheight[char] = 8, 64
                arrowx[char], arrowy[char] = charx[char] + (charwidth / 2) - arrowwidth[char] / 2, chary[char] + (charheight / 2)
            elif arrowface[char] == 90 or arrowface[char] == 270:
                arrowwidth[char], arrowheight[char] = 64, 8
                arrowx[char], arrowy[char] = charx[char] + (charwidth / 2), chary[char] + (charheight / 2) - arrowheight[char] / 2

        #Sword ability
        elif charability[char] == 2:
            from main import swordx, swordy, swordwidth, swordheight, swordface
            sworduse.play()
            swordface[char] = charface[char]
            if swordface[char] == 0:
                swordwidth[char], swordheight[char] = 22, 50
                swordx[char], swordy[char] = charx[char], chary[char] - charheight + 10
            elif swordface[char] == 90:
                swordwidth[char], swordheight[char] = 50, 22
                swordx[char], swordy[char] = charx[char] - charwidth + 10, chary[char]
            elif swordface[char] == 180:
                swordwidth[char], swordheight[char] = 22, 50
                swordx[char], swordy[char] = charx[char], chary[char] + charheight - 10
            elif swordface[char] == 270:
                swordwidth[char], swordheight[char] = 50, 22
                swordx[char], swordy[char] = charx[char] + charwidth - 10, chary[char]   

        #Mage bolt ability
        elif charability[char] == 3:
            from main import boltx, bolty, boltface, img_num
            staffuse.play()
            boltface[char] = charface[char]
            img_num[char] = random.randrange(0, 3)
            if boltface[char] == 0:
                boltx[char], bolty[char] = charx[char], chary[char] - charheight - 128
            elif boltface[char] == 90:
                boltx[char], bolty[char] = charx[char] - charwidth - 128, chary[char]
            elif boltface[char] == 180:
                boltx[char], bolty[char] = charx[char], chary[char] + charheight + 128
            elif boltface[char] == 270:
                boltx[char], bolty[char] = charx[char] + charwidth + 128, chary[char]

#Run ability function
def run_ability(char):
    from main import charx, chary, charface, charability, isactive, canuse

    #Arrow ability
    if charability[char] == 1 and isactive[char] == True:
        from main import arrowface, arrowx, arrowy
        if arrowface[char] == 0 and arrowy[char] > -64:
            arrowy[char] -= 10
        elif arrowface[char] == 180 and arrowy[char] < size[1] + 64:
            arrowy[char] += 10
        elif arrowface[char] == 270 and arrowx[char] < size[0] + 64:
            arrowx[char] += 10
        elif arrowface[char] == 90 and arrowx[char] > -64:
            arrowx[char] -= 10
        else:
            isactive[char] = False

    #Sword ability
    if charability[char] == 2 and isactive[char] == True:
        from main import swordx, swordy, swordwidth, swordheight, swordface, swordcooldownstarted, swordstarttime, swordpassedtime
        if swordface[char] == 0:
            swordwidth[char], swordheight[char] = 22, 50
            swordx[char], swordy[char] = charx[char] + swordwidth[char], chary[char] - charheight + 10
        elif swordface[char] == 90:
            swordwidth[char], swordheight[char] = 50, 22
            swordx[char], swordy[char] = charx[char] - charwidth + 10, chary[char] + swordheight[char]
        elif swordface[char] == 180:
            swordwidth[char], swordheight[char] = 22, 50
            swordx[char], swordy[char] = charx[char] + swordwidth[char], chary[char] + charheight 
        elif swordface[char] == 270:
            swordwidth[char], swordheight[char] = 50, 22
            swordx[char], swordy[char] = charx[char] + charwidth, chary[char]+ swordheight[char]
        #Makes the sword appear for 0.5 seconds
        swordcooldownstarted[char], swordstarttime[char], swordpassedtime[char] = ability_cooldown(swordcooldownstarted[char], swordstarttime[char], swordpassedtime[char])
        if swordpassedtime[char] >= 500:
            swordpassedtime[char] = 0
            swordcooldownstarted[char] = False
            isactive[char] = False
            swordx[char], swordy[char] = -100, -100

    #Mage bolt ability
    if charability[char] == 3 and isactive[char] == True:
        from main import staffx, staffy, staffface, boltcooldownstarted, boltstarttime, boltpassedtime
        staffface[char] = charface[char]
        if staffface[char] == 0:
            staffx[char], staffy[char] = charx[char], chary[char] - charheight
        elif staffface[char] == 90:
            staffx[char], staffy[char] = charx[char] - charwidth, chary[char]
        elif staffface[char] == 180:
            staffx[char], staffy[char] = charx[char], chary[char] + charheight
        elif staffface[char] == 270:
            staffx[char], staffy[char] = charx[char] + charwidth, chary[char]
        #Makes the bolt disapear after 1 second
        boltcooldownstarted[char], boltstarttime[char], boltpassedtime[char] = ability_cooldown(boltcooldownstarted[char], boltstarttime[char], boltpassedtime[char])
        if boltpassedtime[char] >= 1000:
            boltpassedtime[char] = 0
            boltcooldownstarted[char] = False
            isactive[char] = False
            boltx[char], bolty[char] = -100, -100
            staffx[char], staffy[char] = -100, -100

    #Starts the cooldown after ability is done
    from main import cooldownstarted, starttime, passedtime, arrowcollisionoccured
    if isactive[char] == False and canuse[char] == False and arrowcollisionoccured[char] == False:
        cooldownstarted[char], starttime[char], passedtime[char] = ability_cooldown(cooldownstarted[char], starttime[char], passedtime[char])
        if passedtime[char] >= 1000:
            passedtime[char] = 0
            cooldownstarted[char] = False
            canuse[char] = True

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
    if main.ballammo > 0 and main.ballisactive == False:
        main.ballammo -= 1
        main.enemyballface = main.enemyface[1]
        main.enemyballx, main.enemybally = main.enemyx[1], main.enemyy[1]
        main.ballisactive = True
    #Spike ball flies through the air
    if main.ballisactive == True:
        if main.enemyballface == "North" and main.enemybally > - main.enemyballheight:
            main.enemybally -= 3
            main.enemyballx += 5 * math.sin(0.1 * main.enemybally)
        elif main.enemyballface == "East" and main.enemyballx < size[0] + main.enemyballwidth:
            main.enemyballx += 3
            main.enemybally += (5 * math.sin(0.1 * enemyballx))
        elif main.enemyballface == "South" and main.enemybally < size[1] + main.enemyballheight:
            main.enemybally += 3
            main.enemyballx += 5 * math.sin(0.1 * enemybally)
        elif main.enemyballface == "West" and main.enemyballx > - main.enemyballwidth:
            main.enemyballx -= 3
            main.enemybally += (5 * math.sin(0.1 * main.enemyballx))
        else:
            main.ballisactive = False
            main.ballammo += 1

#Run shoot explosion function
def enemy_shoot_explosion():
    import main

    #Shoot the exlosion
    if main.explosionammo > 0 and main.explosionisactive == False:
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
    from main import enemyx, enemyy, enemywidth, enemyheight, enemyspeed, enemyface
    closest_char = find_closest_char(enemyx[enemytype], enemyy[enemytype])
    if (enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2) == 0:
        slope = 0.01
    else:
        slope = abs(((enemyy[enemytype] + enemyheight / 2) - (closest_char[1] + charheight / 2)) / ((enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2)))
    if slope < 1:
        if (enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx[enemytype] -= enemyspeed[enemytype]
            enemyface[enemytype] = "West"
        elif (enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx[enemytype] += enemyspeed[enemytype]
            enemyface[enemytype] = "East"
        if (enemyy[enemytype] + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy[enemytype] -= slope * enemyspeed[enemytype]
        elif (enemyy[enemytype] + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy[enemytype] += slope * enemyspeed[enemytype]
    else:
        if (enemyy[enemytype] + enemyy[enemytype] / 2) - (closest_char[1] + charheight / 2) == 0:
            slope = 0.01
        else:
            slope = abs(((enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2)) / ((enemyy[enemytype] + enemyheight / 2) - (closest_char[1] + charheight / 2)))             
        if (enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx[enemytype] -= slope * enemyspeed[enemytype]
        elif (enemyx[enemytype] + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx[enemytype] += slope * enemyspeed[enemytype]
        if (enemyy[enemytype] + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy[enemytype] -= enemyspeed[enemytype]
            enemyface[enemytype] = "North"
        elif (enemyy[enemytype] + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy[enemytype] += enemyspeed[enemytype]
            enemyface[enemytype] = "South"

def spawn_enemy(enemytype):
    import main
    if main.isalive[enemytype] == False:
        main.isalive[enemytype] = True
        chooseside = round(random.randrange(1, 5))
        if chooseside == 1:
            main.enemyx[enemytype], main.enemyy[enemytype] = random.randrange(enemywidth, size[0] - enemywidth), 0
        elif chooseside == 2:
            main.enemyx[enemytype], main.enemyy[enemytype] = 0, random.randrange(enemyheight, size[1] - enemyheight)
        elif chooseside == 3:
            main.enemyx[enemytype], main.enemyy[enemytype] = random.randrange(enemywidth, size[0] - enemywidth), size[1] - enemyheight
        elif chooseside == 4:
            main.enemyx[enemytype], main.enemyy[enemytype] = size[0] - enemywidth, random.randrange(enemyheight, size[1] - enemyheight)

def give_points(char, enemytype):
    import main

    if main.isalive[enemytype] == False:
        if enemytype == 0:
            main.player_score[char] += 25
        elif enemytype == 1:
            main.player_score[char] += 40
        elif enemytype == 2:
            main.player_score[char] += 10
        main.enemies_killed[char] += 1

#Run function to detect collision between enemy and player
def enemy_player_collision(char, enemytype):
    from main import enemyx, enemyy, enemywidth, enemyheight, isalive, charx, chary, charhealth

    for enemyxpos in range(int(enemyx[enemytype]), int(enemyx[enemytype] + enemywidth)):
        if charx[char] + charwidth >= enemyxpos >= charx[char]:
            for enemyypos in range(int(enemyy[enemytype]), int(enemyy[enemytype] + enemyheight)):
                if chary[char] + charheight >= enemyypos >= chary[char]:
                    isalive[enemytype] = False
                    playerhit.play()
                    charhealth[char] -= 1
                    if charhealth[char] <= 0:
                        charx[char], chary[char] = -100000, -100000
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

    for main.enemyxpos in range(int(main.explosionx), int(main.explosionx + main.explosionradius)):
        if main.charx[char] + main.charwidth >= main.enemyxpos >= main.charx[char]:
            for main.enemyypos in range(int(main.explosiony), int(main.explosiony + main.explosionradius)):
                if main.chary[char] + main.charheight >= main.enemyypos >= main.chary[char]:
                    playerhit.play()
                    main.charhealth[char] -= 1
                    if main.charhealth[char] <= 0:
                        main.charx[char], main.chary[char] = -100000, -100000
                    break
            break

#Run function to detect collision between enemy and arrow
def enemy_arrow_collision(char, enemytype):
    from main import enemyx, enemyy, enemywidth, enemyheight, isalive, arrowx, arrowy, arrowwidth, arrowheight, isactive, canuse, cooldownstarted, starttime, passedtime, arrowcollisionoccured
    
    for enemyxpos in range(int(enemyx[enemytype]), int(enemyx[enemytype] + enemywidth)):
        if arrowx[char] + arrowwidth[char] >= enemyxpos >= arrowx[char]:
            for enemyypos in range(int(enemyy[enemytype]), int(enemyy[enemytype] + enemyheight)):
                if arrowy[char] + arrowheight[char] >= enemyypos >= arrowy[char]:
                    enemyhit.play()
                    isalive[enemytype] = False
                    give_points(char, enemytype)
                    arrowcollisionoccured[char] = True
                    arrowx[char], arrowy[char] = -100000, -100000 
                    isactive[char] = False
                    break
            break

    if arrowcollisionoccured[char] == True:
        cooldownstarted[char], starttime[char], passedtime[char] = ability_cooldown(cooldownstarted[char], starttime[char], passedtime[char])
        if passedtime[char] >= 1000:
            passedtime[char] = 0
            cooldownstarted[char] = False
            arrowcollisionoccured[char] = False
            canuse[char] = True

#Run function to detect collision between enemy and sword
def enemy_sword_collision(char, enemytype):
    from main import enemyx, enemyy, enemywidth, enemyheight, isalive, swordx, swordy, swordwidth, swordheight, isactive, canuse, cooldownstarted, starttime, passedtime

    for enemyxpos in range(int(enemyx[enemytype]), int(enemyx[enemytype] + enemywidth)):
        if swordx[char] + swordwidth[char] >= enemyxpos >= swordx[char]:
            for enemyypos in range(int(enemyy[enemytype]), int(enemyy[enemytype] + enemyheight)):
                if swordy[char] + swordheight[char] >= enemyypos >= swordy[char]:
                    enemyhit.play()
                    isalive[enemytype] = False
                    give_points(char, enemytype)
                    break
            break

#Run function to detect collision between enemy and mage bolt
def enemy_bolt_collision(char, enemytype):
    from main import enemyx, enemyy, enemywidth, enemyheight, isalive, boltx, bolty, boltwidth, boltheight, isactive, canuse, cooldownstarted, starttime, passedtime, boltface, multiplayer

    for enemyxpos in range(int(enemyx[enemytype]), int(enemyx[enemytype] + enemywidth)):
        if (boltx[char]) + boltwidth[char] >= enemyxpos >= (boltx[char]):
            for enemyypos in range(int(enemyy[enemytype]), int(enemyy[enemytype] + enemyheight)):
                if (bolty[char]) + boltheight[char] >= enemyypos >= (bolty[char]):
                    enemyhit.play()
                    isalive[enemytype] = False
                    give_points(char, enemytype)
                    break
            break

#Run function to reset menu variables when using a button to take you back to main menu
def reset_menu():
    import main
    import playMenu

    main.player_count, main.charability, main.charx, main.chary, main.arrowx, main.arrowy, main.swordx, main.swordy, main.boltx, main.bolty, main.staffx, main.staffy = 0, [0,0], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], [-100, -100], [0, 0], [-100, -100], [-100, -100], [-100, -100], [-100, -100], [-100, -100], [-100, -100]
    main.enemyx, main.enemyy, main.isalive = [-100, -100, -100], [-100, -100, -100], [False, False, False]
    main.charhealth = [3, 3]
    main.charface, main.arrowface, main.swordface = [0, 0], [0, 0], [0, 0]
    main.enemyballx, main.enemybally, main.explosionx, main.explosiony, main.ballisactive, main.ballammo, main.explosionammo, main.explosionisactive, main.cantakedamage, main.explosioncolor = -100, -100, -100, -100, False, 1, 1, False, False, [255, 255, 255]
    playMenu.selected = [0, 0]
    main.swordcooldownstarted, main.swordstarttime, main.swordpassedtime, main.boltcooldownstarted, main.boltstarttime, main. boltpassedtime = [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]
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
            
        #Drawing Arrows
        if charability[0] == 1:
            use_ability(char[0])
            run_ability(char[0])
        if multiplayer == True and charability[1] == 1:
            use_ability(char[1])
            run_ability(char[1])
        #Drawing Swords
        if charability[0] == 2:
            use_ability(char[0]) 
            run_ability(char[0])
        if multiplayer == True and charability[1] == 2:
            use_ability(char[1]) 
            run_ability(char[1])
        #Drawing mage bolts
        if charability[0] == 3:
            use_ability(char[0]) 
            run_ability(char[0])  
        if multiplayer == True and charability[1] == 3:
            use_ability(char[1]) 
            run_ability(char[1])

        #Spawning enemies
        spawn_enemy(enemytype[0])
        spawn_enemy(enemytype[1])
        spawn_enemy(enemytype[2])

        #Drawing Enemies
        move_enemy(enemytype[0])
        move_enemy(enemytype[1])

        #Drawing enemy spike ball
        enemy_shoot_spike_ball()

        #Drawing the explosion
        enemy_shoot_explosion()
        
        #Enemy collision with player
        enemy_player_collision(char[0], enemytype[0])  
        if multiplayer:
            enemy_player_collision(char[1], enemytype[0])  
        enemy_player_collision(char[0], enemytype[1])  
        if multiplayer:
            enemy_player_collision(char[1], enemytype[1])  
        enemy_player_collision(char[0], enemytype[2])  
        if multiplayer:
            enemy_player_collision(char[1], enemytype[2])  
            
        #Enemy spike ball collision with player
        player_ball_collision(char[0])
        if multiplayer:
            player_ball_collision(char[1])

        #Explosion collision with player
        if cantakedamage == True:
            explosion_player_collision(char[0])
            if multiplayer == True:
                explosion_player_collision(char[1])

        #Enemy collision with arrow
        if charability[0] == 1:
           enemy_arrow_collision(char[0], enemytype[0])
           enemy_arrow_collision(char[0], enemytype[1])
           enemy_arrow_collision(char[0], enemytype[2])
        if charability[1] == 1 and multiplayer == True:
            enemy_arrow_collision(char[1], enemytype[0])
            enemy_arrow_collision(char[1], enemytype[1])
            enemy_arrow_collision(char[1], enemytype[2])
        #Enemy collision with sword
        if charability[0] == 2:
            enemy_sword_collision(char[0], enemytype[0])
            enemy_sword_collision(char[0], enemytype[1])
            enemy_sword_collision(char[0], enemytype[2])
        if charability[1] == 2 and multiplayer == True:
            enemy_sword_collision(char[1], enemytype[0])  
            enemy_sword_collision(char[1], enemytype[1])   
            enemy_sword_collision(char[1], enemytype[2])
        #Enemy collision with mage bolt
        if charability[0] == 3:
            enemy_bolt_collision(char[0], enemytype[0])
            enemy_bolt_collision(char[0], enemytype[1])
            enemy_bolt_collision(char[0], enemytype[2])
        if charability[1] == 3 and multiplayer == True:
            enemy_bolt_collision(char[1], enemytype[0])
            enemy_bolt_collision(char[1], enemytype[1])
            enemy_bolt_collision(char[1], enemytype[2])   

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