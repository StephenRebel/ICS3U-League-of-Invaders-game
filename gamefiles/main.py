import pygame
import random, math, time
pygame.init()

from startMenu import menu
from controlsMenu import controls
from instructionsMenu import instructions
from playMenu import char_selection
from pauseMenu import pause

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
char, charx, chary, charwidth, charheight, charface, charability, charhealth = [1, 2], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], 64, 64, [0, 0], [0, 0], [3, 3]
arrowx, arrowy, arrowwidth, arrowheight, arrowface, arrowcollisionoccured = [-100, -100], [0, 0], [10, 10], [62, 62], [0, 0], [False, False]
swordx, swordy, swordwidth, swordheight, swordface = [-100, -100], [0, 0], [22, 22], [50, 50], [0, 0]
boltx, bolty, boltwidth, boltheight, boltface, staffx, staffy, staffface = [-100, - 100], [0, 0], [64, 64], [64, 64], [0, 0], [-100, -100], [-100, -100], [0, 0]
swordcooldownstarted, swordstarttime, swordpassedtime, boltcooldownstarted, boltstarttime, boltpassedtime = [False, False], [0, 0], [0, 0], [False, False], [0, 0], [0, 0]
starttime, cooldownstarted, passedtime = [0, 0], [False, False], [0, 0]
isactive, canuse = [False, False], [True, True]
enemytype, enemy, enemyx, enemyy, enemywidth, enemyheight, enemyface, enemyspeed = [1, 2, 3], [[1], [1], [1]], [[300], [300], [300]], [[200], [300], [100]], 64, 64, [[""], [""], [""]], [1, 0.5]
enemyball, enemyballx, enemybally, enemyballwidth, enemyballheight, enemyballface = [1], [-100], [-100], 18, 18, [0]
explosion, explosionx, explosiony, explosionradius, explosioncolor = [1], [-100], [-100], 64, [[255, 255, 255]]
ballammo, ballisactive = [1], [False]
explosionammo, explosionisactive, cantakedamage = [1], [False], [False]
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
player_score = [0, 0]

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
    screen.blit(enemy1img, (enemyx[0][0], enemyy[0][0]))
    screen.blit(enemy2img, (enemyx[1][0], enemyy[1][0]))
    screen.blit(enemy3img, (enemyx[2][0], enemyy[2][0]))

    #Spike ball
    screen.blit(ballimg, (enemyballx[0], enemybally[0]))

    #Explosion
    pygame.draw.circle(screen, explosioncolor[0], [explosionx[0] + 32, explosiony[0] + 32], explosionradius / 2)

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
    from main import charx, chary, charwidth, charheight, charface, charability

    keys = pygame.key.get_pressed()
    key_type = []
    if char == 1:
        key_type.append(keys[pygame.K_LEFT])
        key_type.append(keys[pygame.K_RIGHT])
        key_type.append(keys[pygame.K_UP])
        key_type.append(keys[pygame.K_DOWN])
        i = 0
    elif char == 2:
        key_type.append(keys[pygame.K_a])
        key_type.append(keys[pygame.K_d])
        key_type.append(keys[pygame.K_w])
        key_type.append(keys[pygame.K_s])
        i = 1

    #Changes speed based on ability
    extraspeed = 0
    if charability[i] == 2:
        extraspeed = 0.5
    elif charability[i] == 3:
        extraspeed = 0.2

    # Movement for both players
    if key_type[0]:
        charface[i] = 90
        if charx[i] - 1 <= 0:
            charx[i] = 0
        else:
            charx[i] -= 2 + extraspeed
    elif key_type[1]:
        charface[i] = 270
        if charx[i] + 1 >= size[0] - charwidth:
            charx[i] = size[0] - charwidth
        else:
            charx[i] += 2 + extraspeed
    elif key_type[2]:
        charface[i] = 0
        if chary[i] - 1 <= 0:
            chary[i] = 0
        else:
            chary[i] -= 2 + extraspeed
    elif key_type[3]:
        charface[i] = 180
        if chary[i] + 1 >= size[1] - charheight:
            chary[i] = size[1] - charheight
        else:
            chary[i] += 2 + extraspeed

#Use ability function
def use_ability(char):
    from main import charx, chary, charwidth, charheight, charface, charability, isactive, canuse

    keys = pygame.key.get_pressed()
    key_type = []
    if char == 1:
        key_type.append(keys[pygame.K_SPACE])
        i = 0
    elif char == 2:
        key_type.append(keys[pygame.K_e])
        i = 1
    #Arrow ability    
    if charability[i] == 1 and key_type[0] and isactive[i] == False and canuse[i] == True:
        from main import arrowx, arrowy, arrowwidth, arrowheight, arrowface
        bowuse.play()
        arrowface[i] = charface[i]
        if arrowface[i] == 0 or arrowface[i] == 180:
            arrowwidth[i], arrowheight[i] = 8, 64
            arrowx[i], arrowy[i] = charx[i] + (charwidth / 2) - arrowwidth[i] / 2, chary[i] + (charheight / 2)
        elif arrowface[i] == 90 or arrowface[i] == 270:
            arrowwidth[i], arrowheight[i] = 64, 8
            arrowx[i], arrowy[i] = charx[i] + (charwidth / 2), chary[i] + (charheight / 2) - arrowheight[i] / 2
        isactive[i] = True
        canuse[i] = False

    #Sword ability
    elif charability[i] == 2 and key_type[0] and isactive[i] == False and canuse[i] == True:
        from main import swordx, swordy, swordwidth, swordheight, swordface
        sworduse.play()
        swordface[i] = charface[i]
        if swordface[i] == 0:
            swordwidth[i], swordheight[i] = 22, 50
            swordx[i], swordy[i] = charx[i], chary[i] - charheight + 10
        elif swordface[i] == 90:
            swordwidth[i], swordheight[i] = 50, 22
            swordx[i], swordy[i] = charx[i] - charwidth + 10, chary[i]
        elif swordface[i] == 180:
            swordwidth[i], swordheight[i] = 22, 50
            swordx[i], swordy[i] = charx[i], chary[i] + charheight - 10
        elif swordface[i] == 270:
            swordwidth[i], swordheight[i] = 50, 22
            swordx[i], swordy[i] = charx[i] + charwidth - 10, chary[i]   
        isactive[i] = True
        canuse[i] = False

    #Mage bolt ability
    elif charability[i] == 3 and key_type[0] and isactive[i] == False and canuse[i] == True:
        from main import boltx, bolty, boltface, img_num
        staffuse.play()
        img_num[i] = random.randrange(0,3)
        boltface[i] = charface[i]
        if boltface[i] == 0:
            boltx[i], bolty[i] = charx[i], chary[i] - charheight - 128
        elif boltface[i] == 90:
            boltx[i], bolty[i] = charx[i] - charwidth - 128, chary[i]
        elif boltface[i] == 180:
            boltx[i], bolty[i] = charx[i], chary[i] + charheight + 128
        elif boltface[i] == 270:
            boltx[i], bolty[i] = charx[i] + charwidth + 128, chary[i]
        isactive[i] = True
        canuse[i] = False

#Run ability function
def run_ability(char):
    from main import charx, chary, charface, charability, isactive, canuse
    i = 0
    if char == 1:
        i = 0
    elif char == 2:
        i = 1

    #Arrow ability
    if charability[i] == 1 and isactive[i] == True:
        from main import arrowface, arrowx, arrowy
        if arrowface[i] == 0 and arrowy[i] > -64:
            arrowy[i] -= 10
        elif arrowface[i] == 180 and arrowy[i] < size[1] + 64:
            arrowy[i] += 10
        elif arrowface[i] == 270 and arrowx[i] < size[0] + 64:
            arrowx[i] += 10
        elif arrowface[i] == 90 and arrowx[i] > -64:
            arrowx[i] -= 10
        else:
            isactive[i] = False

    #Sword ability
    if charability[i] == 2 and isactive[i] == True:
        from main import swordx, swordy, swordwidth, swordheight, swordface, swordcooldownstarted, swordstarttime, swordpassedtime
        if swordface[i] == 0:
            swordwidth[i], swordheight[i] = 22, 50
            swordx[i], swordy[i] = charx[i] + swordwidth[i], chary[i] - charheight + 10
        elif swordface[i] == 90:
            swordwidth[i], swordheight[i] = 50, 22
            swordx[i], swordy[i] = charx[i] - charwidth + 10, chary[i] + swordheight[i]
        elif swordface[i] == 180:
            swordwidth[i], swordheight[i] = 22, 50
            swordx[i], swordy[i] = charx[i] + swordwidth[i], chary[i] + charheight 
        elif swordface[i] == 270:
            swordwidth[i], swordheight[i] = 50, 22
            swordx[i], swordy[i] = charx[i] + charwidth, chary[i]+ swordheight[i]
        #Makes the sword appear for 0.5 seconds
        swordcooldownstarted[i], swordstarttime[i], swordpassedtime[i] = ability_cooldown(swordcooldownstarted[i], swordstarttime[i], swordpassedtime[i])
        if swordpassedtime[i] >= 500:
            swordpassedtime[i] = 0
            swordcooldownstarted[i] = False
            isactive[i] = False
            swordx[i], swordy[i] = -100, -100

    #Mage bolt ability
    if charability[i] == 3 and isactive[i] == True:
        from main import staffx, staffy, staffface, boltcooldownstarted, boltstarttime, boltpassedtime
        staffface[i] = charface[i]
        if staffface[i] == 0:
            staffx[i], staffy[i] = charx[i], chary[i] - charheight
        elif staffface[i] == 90:
            staffx[i], staffy[i] = charx[i] - charwidth, chary[i]
        elif staffface[i] == 180:
            staffx[i], staffy[i] = charx[i], chary[i] + charheight
        elif staffface[i] == 270:
            staffx[i], staffy[i] = charx[i] + charwidth, chary[i]
        #Makes the bolt disapear after 1 second
        boltcooldownstarted[i], boltstarttime[i], boltpassedtime[i] = ability_cooldown(boltcooldownstarted[i], boltstarttime[i], boltpassedtime[i])
        if boltpassedtime[i] >= 1000:
            boltpassedtime[i] = 0
            boltcooldownstarted[i] = False
            isactive[i] = False
            boltx[i], bolty[i] = -100, -100
            staffx[i], staffy[i] = -100, -100

    #Starts the cooldown after ability is done
    from main import cooldownstarted, starttime, passedtime, arrowcollisionoccured
    if isactive[i] == False and canuse[i] == False and arrowcollisionoccured[i] == False:
        cooldownstarted[i], starttime[i], passedtime[i] = ability_cooldown(cooldownstarted[i], starttime[i], passedtime[i])
        if passedtime[i] >= 1000:
            passedtime[i] = 0
            cooldownstarted[i] = False
            canuse[i] = True

#Gets the cooldown after an ability has been used
def ability_cooldown(cooldownstarted, starttime, passedtime):
    if cooldownstarted == False:
        cooldownstarted = True
        starttime = pygame.time.get_ticks()
    if cooldownstarted == True:
        passedtime = pygame.time.get_ticks() - starttime
    return cooldownstarted, starttime, passedtime

#Run spike ball function
def enemy_shoot_spike_ball(enemy): 
    from main import enemyx, enemyy, enemyface, enemyballx, enemybally, enemyballwidth, enemyballheight, enemyballface, ballammo, ballisactive   
    i = enemy - 1

    #Enemy shoots the spike ball 
    if ballammo[i] > 0 and ballisactive[i] == False:
        ballammo[i] -= 1
        enemyballface[i] = enemyface[1][i]
        enemyballx[i], enemybally[i] = enemyx[1][i], enemyy[1][i]
        ballisactive[i] = True
    #Spike ball flies through the air
    if ballisactive[i] == True:
        if enemyballface[i] == "North" and enemybally[i] > - enemyballheight:
            enemybally[i] -= 3
            enemyballx[i] += 5 * math.sin(0.1 * enemybally[i])
        elif enemyballface[i] == "East" and enemyballx[i] < size[0] + enemyballwidth:
            enemyballx[i] += 3
            enemybally[i] += (5 * math.sin(0.1 * enemyballx[i]))
        elif enemyballface[i] == "South" and enemybally[i] < size[1] + enemyballheight:
            enemybally[i] += 3
            enemyballx[i] += 5 * math.sin(0.1 * enemybally[i])
        elif enemyballface[i] == "West" and enemyballx[i] > - enemyballwidth:
            enemyballx[i] -= 3
            enemybally[i] += (5 * math.sin(0.1 * enemyballx[i]))
        else:
            ballisactive[i] = False
            ballammo[i] += 1

#Run shoot explosion function
def enemy_shoot_explosion(enemy):
    from main import enemyx, enemyy, explosionx, explosiony, explosionradius, explosioncolor, explosionammo, explosionisactive, cantakedamage
    i = enemy - 1

    #Shoot the exlosion
    if explosionammo[i] > 0 and explosionisactive[i] == False:
        cantakedamage[i] = False
        explosionammo[i] -= 1
        explosionx[i], explosiony[i] = find_closest_char(enemyx[2][i], enemyy[2][i])
        explosionisactive[i] = True
    #Explosion countdown
    if explosionisactive[i] == True:
        if explosioncolor[i][0] > 82 and explosioncolor[i][1] > 72 and explosioncolor[i][2] > 0:
            explosioncolor[i][0] -= 0.67
            explosioncolor[i][1] -= 0.71
            explosioncolor[i][2] -= 1
        else:
            explosionammo[i] += 1
            explosioncolor[i] = [255, 255, 255]
            cantakedamage[i] = True
            explosionisactive[i] = False
  
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
def move_enemy(enemytype, enemy):
    from main import enemyx, enemyy, enemywidth, enemyheight, enemyspeed, enemyface
    t = enemytype - 1
    i = enemy - 1
    closest_char = find_closest_char(enemyx[t][i], enemyy[t][i])
    if (enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2) == 0:
        slope = 0.01
    else:
        slope = abs(((enemyy[t][i] + enemyheight / 2) - (closest_char[1] + charheight / 2)) / ((enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2)))
    if slope < 1:
        if (enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx[t][i] -= enemyspeed[t]
            enemyface[t][i] = "West"
        elif (enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx[t][i] += enemyspeed[t]
            enemyface[t][i] = "East"
        if (enemyy[t][i] + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy[t][i] -= slope * enemyspeed[t]
        elif (enemyy[t][i] + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy[t][i] += slope * enemyspeed[t]
    else:
        if (enemyy[t][i] + enemyy[t][i] / 2) - (closest_char[1] + charheight / 2) == 0:
            slope = 0.01
        else:
            slope = abs(((enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2)) / ((enemyy[t][i] + enemyheight / 2) - (closest_char[1] + charheight / 2)))             
        if (enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx[t][i] -= slope * enemyspeed[t]
        elif (enemyx[t][i] + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx[t][i] += slope * enemyspeed[t]
        if (enemyy[t][i] + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy[t][i] -= enemyspeed[t]
            enemyface[t][i] = "North"
        elif (enemyy[t][i] + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy[t][i] += enemyspeed[t]
            enemyface[t][i] = "South"

#Run function to detect collision between enemy and player
def enemy_player_collision(char, enemytype, enemy):
    from main import enemyx, enemyy, enemywidth, enemyheight, charx, chary, charhealth
    c = 0
    if char == 1:
        c = 0
    elif char == 2:
        c = 1
    t = enemytype - 1
    i = enemy - 1
    for enemyxpos in range(int(enemyx[t][i]), int(enemyx[t][i] + enemywidth)):
        if charx[c] + charwidth >= enemyxpos >= charx[c]:
            for enemyypos in range(int(enemyy[t][i]), int(enemyy[t][i] + enemyheight)):
                if chary[c] + charheight >= enemyypos >= chary[c]:
                    playerhit.play()
                    enemyx[t][i], enemyy[t][i] = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))    
                    charhealth[c] -= 1
                    if charhealth[c] == 0:
                        charx[c], chary[c] = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                        charhealth[c] = 3
                    break
            break

#Run function to detect collision between explosion and player
def explosion_player_collision(explosion, char):
    from main import explosionx, explosiony, explosionradius, charx, chary, charhealth, cantakedamage
    e = explosion - 1
    i = char - 1

    for enemyxpos in range(int(explosionx[e]), int(explosionx[e] + explosionradius)):
        if charx[i] + charwidth >= enemyxpos >= charx[i]:
            for enemyypos in range(int(explosiony[e]), int(explosiony[e] + explosionradius)):
                if chary[i] + charheight >= enemyypos >= chary[i]:
                    playerhit.play()
                    charhealth[i] -= 1
                    if charhealth[i] == 0:
                        charx[i], chary[i] = (random.randrange(explosionradius, size[0] - explosionradius), random.randrange(explosionradius, size[1] - explosionradius))
                        charhealth[i] = 3
                    break
            break

#Run function to detect collision between enemy and arrow
def enemy_arrow_collision(char, enemytype, enemy):
    from main import enemyx, enemyy, enemywidth, enemyheight, arrowx, arrowy, arrowwidth, arrowheight, isactive, canuse, cooldownstarted, starttime, passedtime, arrowcollisionoccured
    t = enemytype - 1
    i = enemy - 1
    c = char - 1
    
    for enemyxpos in range(int(enemyx[t][i]), int(enemyx[t][i] + enemywidth)):
        if arrowx[c] + arrowwidth[c] >= enemyxpos >= arrowx[c]:
            for enemyypos in range(int(enemyy[t][i]), int(enemyy[t][i] + enemyheight)):
                if arrowy[c] + arrowheight[c] >= enemyypos >= arrowy[c]:
                    enemyhit.play()
                    arrowcollisionoccured[c] = True
                    enemyx[t][i], enemyy[t][i] = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                    arrowx[c], arrowy[c] = -64, -64 
                    isactive[c] = False
                    if enemytype == 1:
                        player_score[c] += 25
                    elif enemytype == 2:
                        player_score[c] += 40
                    elif enemytype == 3:
                        player_score[c] += 10

    if arrowcollisionoccured[c] == True:
        cooldownstarted[c], starttime[c], passedtime[c] = ability_cooldown(cooldownstarted[c], starttime[c], passedtime[c])
        if passedtime[c] >= 1000:
            passedtime[c] = 0
            cooldownstarted[c] = False
            arrowcollisionoccured[c] = False
            canuse[c] = True

#Run function to detect collision between enemy and sword
def enemy_sword_collision(char, enemytype, enemy):
    from main import enemyx, enemyy, enemywidth, enemyheight, swordx, swordy, swordwidth, swordheight, isactive, canuse, cooldownstarted, starttime, passedtime
    t = enemytype - 1
    i = enemy - 1
    c = char - 1
    swordcollisionoccured = [False, False]

    for enemyxpos in range(int(enemyx[t][i]), int(enemyx[t][i] + enemywidth)):
        if swordx[c] + swordwidth[c] >= enemyxpos >= swordx[c]:
            for enemyypos in range(int(enemyy[t][i]), int(enemyy[t][i] + enemyheight)):
                if swordy[c] + swordheight[c] >= enemyypos >= swordy[c]:
                    enemyhit.play()
                    enemyx[t][i], enemyy[t][i] = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                    swordcollisionoccured[c] = True
    
    if swordcollisionoccured[c] == True:
        #Adding points to the individual players score based on enemy type
        if enemytype == 1:
            player_score[c] += 25
        elif enemytype == 2:
            player_score[c] += 40
        elif enemytype == 3:
            player_score[c] += 10

#Run function to detect collision between enemy and mage bolt
def enemy_bolt_collision(char, enemytype, enemy):
    from main import enemyx, enemyy, enemywidth, enemyheight, boltx, bolty, boltwidth, boltheight, isactive, canuse, cooldownstarted, starttime, passedtime, boltface, multiplayer
    t = enemytype - 1
    i = enemy - 1
    c = char - 1
    boltcollisionoccured = [False, False]

    for enemyxpos in range(int(enemyx[t][i]), int(enemyx[t][i] + enemywidth)):
        if (boltx[c]) + boltwidth[c] >= enemyxpos >= (boltx[c]):
            for enemyypos in range(int(enemyy[t][i]), int(enemyy[t][i] + enemyheight)):
                if (bolty[c]) + boltheight[c] >= enemyypos >= (bolty[c]):
                    enemyhit.play()
                    enemyx[t][i], enemyy[t][i] = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                    boltcollisionoccured[c] = True

    if boltcollisionoccured[c] == True:
        #Adding points to the individual players score based on enemy type
        if enemytype == 1:
            player_score[c] += 25
        elif enemytype == 2:
            player_score[c] += 40
        elif enemytype == 3:
            player_score[c] += 10

#Run function to detect collision between enemy and ball
def player_ball_collision(char, enemyball):
    from main import enemyballx, enemybally, charx, chary, charhealth, charwidth, charheight, ballisactive, ballammo
    b = enemyball - 1
    c = char - 1

    for ballxpos in range(int(enemyballx[b] + 18), int(enemyballx[b] + 48)):
        if charx[c] + charwidth >= ballxpos >= charx[c]:
            for ballypos in range(int(enemybally[b] + 18), int(enemybally[b] + 48)):
                if chary[c] + charheight >= ballypos >= chary[c]:
                    playerhit.play()
                    enemyballx[b], enemybally[b] = -64, -64 
                    ballisactive[b] = False
                    ballammo[b] += 1
                    charhealth[c] -= 1
                    if charhealth[c] == 0:
                        charx[c], chary[c] = (random.randrange(charwidth, size[0] - charwidth), random.randrange(charheight, size[1] - charheight))
                        charhealth[c] = 3
                    break
            break

#Run function to reset menu variables when using a button to take you back to main menu
def reset_menu():
    import main
    import playMenu
    from playMenu import selected
    from main import player_count, charability, charx, chary, charhealth, arrowx, arrowy, swordx, swordy, enemyx, enemyy, charface, arrowface, swordface, enemyballx, enemybally, explosionx, explosiony

    main.player_count, main.charability, main.charx, main.chary, main.arrowx, main.arrowy, main.swordx, main.swordy = 0, [0,0], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], [-100, -100], [0, 0], [-100, -100], [0, 0]
    main.enemyx, main.enemyy = [[300], [300], [300]], [[200], [300], [100]]
    main.charhealth = [3, 3]
    main.charface, main.arrowface, main.swordface = [0, 0], [0, 0], [0, 0]
    main.enemyballx, main.enemybally, main.explosionx, main.explosiony = [-100], [-100], [-100], [-100]
    playMenu.selected = [0, 0]
    main.player_score = [0, 0]
    
#Main game loop
rungame = True
while rungame:

    pygame.time.delay(10)
    
    #Close game when quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
    
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

        #Drawing Enemies
        move_enemy(enemytype[0], enemy[0][0])
        move_enemy(enemytype[1], enemy[1][0])

        #Drawing enemy spike ball
        enemy_shoot_spike_ball(enemy[1][0])

        #Drawing the explosion
        enemy_shoot_explosion(enemy[2][0])

        if cantakedamage[0] == True:
            explosion_player_collision(explosion[0], char[0])
            if multiplayer == True:
                explosion_player_collision(explosion[0], char[1])
        
        #Enemy collision with player
        enemy_player_collision(char[0], enemytype[0], enemy[0][0])  
        if multiplayer:
            enemy_player_collision(char[1], enemytype[0], enemy[0][0])  
        enemy_player_collision(char[0], enemytype[1], enemy[1][0])  
        if multiplayer:
            enemy_player_collision(char[1], enemytype[1], enemy[1][0])  
        enemy_player_collision(char[0], enemytype[2], enemy[2][0])  
        if multiplayer:
            enemy_player_collision(char[1], enemytype[2], enemy[2][0])  

        #Enemy collision with arrow
        if charability[0] == 1:
           enemy_arrow_collision(char[0], enemytype[0], enemy[0][0])
           enemy_arrow_collision(char[0], enemytype[1], enemy[1][0])
           enemy_arrow_collision(char[0], enemytype[2], enemy[2][0])
        if charability[1] == 1 and multiplayer == True:
            enemy_arrow_collision(char[1], enemytype[0], enemy[0][0])
            enemy_arrow_collision(char[1], enemytype[1], enemy[1][0])
            enemy_arrow_collision(char[1], enemytype[2], enemy[2][0])
        #Enemy collision with sword
        if charability[0] == 2:
            enemy_sword_collision(char[0], enemytype[0], enemy[0][0])
            enemy_sword_collision(char[0], enemytype[1], enemy[1][0])
            enemy_sword_collision(char[0], enemytype[2], enemy[2][0])
        if charability[1] == 2 and multiplayer == True:
            enemy_sword_collision(char[1], enemytype[0], enemy[0][0])  
            enemy_sword_collision(char[1], enemytype[1], enemy[1][0])   
            enemy_sword_collision(char[1], enemytype[2], enemy[2][0])
        #Enemy collision with mage bolt
        if charability[0] == 3:
            enemy_bolt_collision(char[0], enemytype[0], enemy[0][0])
            enemy_bolt_collision(char[0], enemytype[1], enemy[1][0])
            enemy_bolt_collision(char[0], enemytype[2], enemy[2][0])
        if charability[1] == 3 and multiplayer == True:
            enemy_bolt_collision(char[1], enemytype[0], enemy[0][0])
            enemy_bolt_collision(char[1], enemytype[1], enemy[1][0])
            enemy_bolt_collision(char[1], enemytype[2], enemy[2][0])    

        #Enemy spike ball collision with player
        player_ball_collision(char[0], enemyball[0])
        if multiplayer:
            player_ball_collision(char[1], enemyball[0])
            
        #Draw all the changes
        draw_screen()

    #Pause window
    elif window == 5:
        pause()

    pygame.display.update()
    
pygame.quit()