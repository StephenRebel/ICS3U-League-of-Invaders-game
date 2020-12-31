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
bg = pygame.image.load("gamefiles/images/dirt_bg.jpg")
bg_scale = pygame.transform.scale(bg, (1280, 720))
char1img = pygame.image.load("gamefiles/images/green_char.png")
char2img = pygame.image.load("gamefiles/images/blue_char.png")
arrowimg = pygame.image.load("gamefiles/images/arrow.png")
swordimg = pygame.image.load("gamefiles/images/sword.png")
staffimg = pygame.image.load("gamefiles/images/staff.png")
enemy1img = pygame.image.load("gamefiles/images/red_enemy.png")
enemy2img = pygame.image.load("gamefiles/images/orange_enemy.png")
ballimg = pygame.image.load("gamefiles/images/spike_ball.png")
boltimg = [pygame.image.load("gamefiles/images/fire_ball.png"), pygame.image.load("gamefiles/images/ice_spikes.png"), pygame.image.load("gamefiles/images/green_rock.png")]
heartimg = pygame.image.load("gamefiles/images/heart.png")
emptyheartimg = pygame.image.load("gamefiles/images/heart_empty.png")

#Game variables
multiplayer = False
char, charx, chary, charwidth, charheight, charface, charability, charhealth = [1, 2], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], 64, 64, [0, 0], [0, 0], [3, 3]
arrowx, arrowy, arrowwidth, arrowheight, arrowface, arrowcollisionoccured = [-100, -100], [0, 0], [10, 10], [62, 62], [0, 0], [False, False]
swordx, swordy, swordwidth, swordheight, swordface = [-100, -100], [0, 0], [22, 22], [50, 50], [0, 0]
boltx, bolty, boltwidth, boltheight, boltface, boltcollisionoccured, staffx, staffy, staffface = [-100, - 100], [0, 0], [64, 64], [64, 64], [0, 0], [False, False], [-100, -100], [-100, -100], [0, 0]
swordcooldownstarted, swordstarttime, swordpassedtime, boltcooldownstarted, boltstarttime, boltpassedtime = [False, False], [0, 0], [0, 0], [False, False], [0, 0], [0, 0]
starttime, cooldownstarted, passedtime = [0, 0], [False, False], [0, 0]
isactive, canuse = [False, False], [True, True]
enemy1, enemy1x, enemy1y, enemy1width, enemy1height, enemy1face, enemy1speed = [1], [300], [200], [64], [64], [""], [1]
enemy2, enemy2x, enemy2y, enemy2width, enemy2height, enemy2face, enemy2speed = [1], [300], [300], [64], [64], [""], [0.5]
enemyballx, enemybally, enemyballwidth, enemyballheight, enemyballface = [-100], [-100], [18], [18], [0]
ballammo, ballisshooting = [1], [False]
img_num = 0

#Menu setup
window = 0
title_font = pygame.font.SysFont("Cambria", 65)
big_font = pygame.font.SysFont("Cambria", 54)
med_font = pygame.font.SysFont("Cambria", 36)
sml_font = pygame.font.SysFont("Cambria", 24)
background = pygame.image.load("gamefiles/images/game_background.jpg")
grayed_out = pygame.image.load("gamefiles/images/gray_out.png")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GR = (211, 211, 211)
DARK_GR = (71, 71, 71)
WHITE = (255, 255, 255)
player_count = 0

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
    if face == 0:
        y -= 100
    elif face == 90:
        x -= 100
    elif face == 180:
        y += 100
    elif face == 270:
        x += 100
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
        draw_bolt(boltimg[img_num], boltx[0], bolty[0], boltface[0], img_num, staffimg, staffx[0], staffy[0], staffface[0])
    if multiplayer == True and charability[1] == 3:
        draw_bolt(boltimg[img_num], boltx[1], bolty[1], boltface[1], img_num, staffimg, staffx[1], staffy[1], staffface[1])

    #Red Enemy
    screen.blit(enemy1img, (enemy1x[0], enemy1y[0]))
    screen.blit(enemy2img, (enemy2x[0], enemy2y[0]))

    #Orange Enemy
    screen.blit(ballimg, (enemyballx[0], enemybally[0]))

    #Pause Button
    pause_button()

    #Cooldown
    draw_cooldowns()

    #Hearts
    draw_hearts(heartimg, emptyheartimg)


#Move character function
def move_char(char, x, y, width, height, face, ability):
    keys = pygame.key.get_pressed()
    key_type = []

    if char == 1:
        key_type.append(keys[pygame.K_LEFT])
        key_type.append(keys[pygame.K_RIGHT])
        key_type.append(keys[pygame.K_UP])
        key_type.append(keys[pygame.K_DOWN])
    elif char == 2:
        key_type.append(keys[pygame.K_a])
        key_type.append(keys[pygame.K_d])
        key_type.append(keys[pygame.K_w])
        key_type.append(keys[pygame.K_s])

    #Changes speed based on ability
    extraspeed = 0
    if ability == 2:
        extraspeed = 0.5
    elif ability == 3:
        extraspeed = 0.2

    # Movement for both players
    if key_type[0]:
        face = 90
        if x - 1 <= 0:
            x = 0
        else:
            x -= 2 + extraspeed
    elif key_type[1]:
        face = 270
        if x + 1 >= size[0] - width:
            x = size[0] - width
        else:
            x += 2 + extraspeed
    elif key_type[2]:
        face = 0
        if y - 1 <= 0:
            y = 0
        else:
            y -= 2 + extraspeed
    elif key_type[3]:
        face = 180
        if y + 1 >= size[1] - height:
            y = size[1] - height
        else:
            y += 2 + extraspeed
    return x, y, face

#Use ability function
def use_ability(char, charx, chary, charwidth, charheight, charface, ability, x, y, width, height, face, isactive, canuse, img_num):
    keys = pygame.key.get_pressed()
    key_type = []
    if char == 1:
        key_type.append(keys[pygame.K_SPACE])
    elif char == 2:
        key_type.append(keys[pygame.K_e])

    #Arrow ability    
    if ability == 1 and key_type[0] and isactive == False and canuse == True:
        face = charface
        if face == 0 or face == 180:
            width, height = 8, 64
            x, y = charx + (charwidth / 2) - width / 2, chary + (charheight / 2)
        elif face == 90 or face == 270:
            width, height = 64, 8
            x, y = charx + (charwidth / 2), chary + (charheight / 2) - height / 2
        isactive = True
        canuse = False

    #Sword ability
    elif ability == 2 and key_type[0] and isactive == False and canuse == True:
        face = charface
        if face == 0:
            width, height = 22, 50
            x, y = charx, chary - charheight + 10
        elif face == 90:
            width, height = 50, 22
            x, y = charx - charwidth + 10, chary
        elif face == 180:
            width, height = 22, 50
            x, y = charx, chary + charheight - 10
        elif face == 270:
            width, height = 50, 22
            x, y = charx + charwidth - 10, chary   
        isactive = True
        canuse = False

    #Mage bolt ability
    elif ability == 3 and key_type[0] and isactive == False and canuse == True:
        img_num = random.randrange(0,3)
        face = charface
        if face == 0:
            x, y = charx , chary - charheight
        elif face == 90:
            x, y = charx - charwidth, chary
        elif face == 180:
            x, y = charx, chary + charheight
        elif face == 270:
            x, y = charx + charwidth, chary
        isactive = True
        canuse = False
    return x, y, width, height, face, isactive, canuse, img_num

#Run ability function
def run_ability(charx, chary, ability, isactive, canuse, x, y, face, cooldownstarted, starttime, passedtime, collisionoccured, swordcooldownstarted, swordstarttime, swordpassedtime, boltcooldownstarted, boltstarttime, boltpassedtime, staffx, staffy):
    #Arrow ability
    if ability == 1 and isactive == True:
        if face == 0 and y > -64:
            y -= 10
        elif face == 180 and y < size[1] + 64:
            y += 10
        elif face == 270 and x < size[0] + 64:
            x += 10
        elif face == 90 and x > -64:
            x -= 10
        else:
            isactive = False

    #Sword ability
    if ability == 2 and isactive == True:
        if face == 0:
            width, height = 22, 50
            x, y = charx + width, chary - charheight + 10
        elif face == 90:
            width, height = 50, 22
            x, y = charx - charwidth + 10, chary + height
        elif face == 180:
            width, height = 22, 50
            x, y = charx + width, chary + charheight 
        elif face == 270:
            width, height = 50, 22
            x, y = charx + charwidth, chary + height
        #Makes the sword appear for 0.5 seconds
        swordcooldownstarted, swordstarttime, swordpassedtime = ability_cooldown(swordcooldownstarted, swordstarttime, swordpassedtime)
        if swordpassedtime >= 500:
            swordpassedtime = 0
            swordcooldownstarted = False
            isactive = False
            x, y = -100, 0

    #Mage bolt ability
    if ability == 3 and isactive == True:
        staffface = face
        if face == 0:
            staffx, staffy = charx , chary - charheight
        elif face == 90:
            staffx, staffy = charx - charwidth, chary
        elif face == 180:
            staffx, staffy = charx, chary + charheight
        elif face == 270:
            staffx, staffy = charx + charwidth, chary
        #Makes the bolt disapear after 1 second
        boltcooldownstarted, boltstarttime, boltpassedtime = ability_cooldown(boltcooldownstarted, boltstarttime, boltpassedtime)
        if boltpassedtime >= 1000:
            boltpassedtime = 0
            boltcooldownstarted = False
            isactive = False
            x, y = -100, -100
            staffx, staffy = -100, -100


    #Starts the cooldown after ability is done
    if isactive == False and canuse == False and collisionoccured == False:
        cooldownstarted, starttime, passedtime = ability_cooldown(cooldownstarted, starttime, passedtime)
        if passedtime >= 1000:
            passedtime = 0
            cooldownstarted = False
            canuse = True
    return x, y, face, isactive, canuse, cooldownstarted, starttime, passedtime, swordcooldownstarted, swordstarttime, swordpassedtime, boltcooldownstarted, boltstarttime, boltpassedtime, staffx, staffy

#Gets the cooldown after an ability has been used
def ability_cooldown(cooldownstarted, starttime, passedtime):
    if cooldownstarted == False:
        cooldownstarted = True
        starttime = pygame.time.get_ticks()
    if cooldownstarted == True:
        passedtime = pygame.time.get_ticks() - starttime
    return cooldownstarted, starttime, passedtime

#Run spike ball function
def enemy_shoot_spike_ball(enemyx, enemyy, enemyface, ballx, bally, ballwidth, ballheight, ballface, ammo, ballisactive):   
    #Enemy shoots the spike ball 
    if ammo > 0 and ballisactive == False:
        ammo -= 1
        ballface = enemyface
        ballx, bally = enemyx, enemyy
        ballisactive = True
    #Spike ball flies through the air
    if ballisactive == True:
        if ballface == "North" and bally > - ballheight:
            bally -= 3
            ballx += 5 * math.sin(0.1 * bally)
        elif ballface == "East" and ballx < size[0] + ballwidth:
            ballx += 3
            bally += (5 * math.sin(0.1 * ballx))
        elif ballface == "South" and bally < size[1] + ballheight:
            bally += 3
            ballx += 5 * math.sin(0.1 * bally)
        elif ballface == "West" and ballx > - ballwidth:
            ballx -= 3
            bally += (5 * math.sin(0.1 * ballx))
        else:
            ballisactive = False
            ammo += 1
    return ballx, bally, ballface, ammo, ballisactive
  
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
def move_enemy(enemyx, enemyy, enemywidth, enemyheight, enemyspeed, enemyface):
    closest_char = find_closest_char(enemyx, enemyy)
    if (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) == 0:
        slope = 0.01
    else:
        slope = abs(((enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2)) / ((enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2)))
    if slope < 1:
        if (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx -= enemyspeed
            enemyface = "West"
        elif (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx += enemyspeed
            enemyface = "East"
        if (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy -= slope * enemyspeed
        elif (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy += slope * enemyspeed
    else:
        if (enemyy + enemyy / 2) - (closest_char[1] + charheight / 2) == 0:
            slope = 0.01
        else:
            slope = abs(((enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2)) / ((enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2)))             
        if (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx -= slope * enemyspeed
        elif (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx += slope * enemyspeed
        if (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy -= enemyspeed
            enemyface = "North"
        elif (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy += enemyspeed
            enemyface = "South"
    return enemyx, enemyy, enemyface

#Run function to detect collision between enemy and player
def enemy_player_collision(enemyx, enemyy, enemywidth, enemyheight, charx, chary, charhealth):
    for enemyxpos in range(int(enemyx), int(enemyx + enemywidth)):
        if charx + charwidth >= enemyxpos >= charx:
            for enemyypos in range(int(enemyy), int(enemyy + enemyheight)):
                if chary + charheight >= enemyypos >= chary:
                    enemyx, enemyy = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))    
                    charhealth -= 1
                    if charhealth == 0:
                        charx, chary = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                        charhealth = 3
                    return charx, chary, charhealth, enemyx, enemyy
    return charx, chary, charhealth, enemyx, enemyy

#Run function to detect collision between enemy and arrow
def enemy_arrow_collision(enemyx, enemyy, enemywidth, enemyheight, arrowx, arrowy, arrowwidth, arrowheight, isactive, canuse, cooldownstarted, starttime, passedtime, collisionoccured):
    for enemyxpos in range(int(enemyx), int(enemyx + enemywidth)):
        if arrowx + arrowwidth >= enemyxpos >= arrowx:
            for enemyypos in range(int(enemyy), int(enemyy + enemyheight)):
                if arrowy + arrowheight >= enemyypos >= arrowy:
                    collisionoccured = True
                    enemyx, enemyy = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                    arrowx, arrowy = -64, -64 
                    isactive = False
    if collisionoccured == True:
        cooldownstarted, starttime, passedtime = ability_cooldown(cooldownstarted, starttime, passedtime)
        if passedtime >= 1000:
            passedtime = 0
            cooldownstarted = False
            collisionoccured = False
            canuse = True
            return enemyx, enemyy, arrowx, arrowy, isactive, canuse, cooldownstarted, starttime, passedtime, collisionoccured
    return enemyx, enemyy, arrowx, arrowy, isactive, canuse, cooldownstarted, starttime, passedtime, collisionoccured

#Run function to detect collision between enemy and sword
def enemy_sword_collision(enemyx, enemyy, enemywidth, enemyheight, swordx, swordy, swordwidth, swordheight, isactive, canuse, cooldownstarted, starttime, passedtime):
    for enemyxpos in range(int(enemyx), int(enemyx + enemywidth)):
        if swordx + swordwidth >= enemyxpos >= swordx:
            for enemyypos in range(int(enemyy), int(enemyy + enemyheight)):
                if swordy + swordheight >= enemyypos >= swordy:
                    enemyx, enemyy = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
    return enemyx, enemyy, swordx, swordy, isactive, canuse, cooldownstarted, starttime, passedtime

#Run function to detect collision between enemy and ball
def player_ball_collision(ballx, bally, charx, chary, charwidth, charheight, isactive, ammo, charhealth):
    for ballxpos in range(int(ballx + 18), int(ballx + 48)):
        if charx + charwidth >= ballxpos >= charx:
            for ballypos in range(int(bally + 18), int(bally + 48)):
                if chary + charheight >= ballypos >= chary:
                    ballx, bally = -64, -64 
                    isactive = False
                    ammo += 1
                    charhealth -= 1
                    if charhealth == 0:
                        charx, chary = (random.randrange(charwidth, size[0] - charwidth), random.randrange(charheight, size[1] - charheight))
                        charhealth = 3
                    return ballx, bally, charx, chary, isactive, ammo, charhealth
    return ballx, bally, charx, chary, isactive, ammo, charhealth

#Run function to reset menu variables when using a button to take you back to main menu
def reset_menu():
    import main
    import playMenu
    from playMenu import selected
    from main import player_count, charability, charx, chary, charhealth, arrowx, arrowy, swordx, swordy, enemy1x, enemy1y, enemy2x, enemy2y, charface, arrowface, swordface

    main.player_count, main.charability, main.charx, main.chary, main.arrowx, main.arrowy, main.swordx, main.swordy, main.enemy1x, main.enemy1y, main.enemy2x, main.enemy2y = 0, [0,0], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], [-100, -100], [0, 0], [-100, -100], [0, 0], [300], [200], [200], [200]
    main.charhealth = [3, 3]
    main.charface, main.arrowface, main.swordface = [0, 0], [0, 0], [0, 0]
    playMenu.selected = [0,0]
    
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
        charx[0], chary[0], charface[0] = move_char(char[0], charx[0], chary[0], charwidth, charheight, charface[0], charability[0])
        if multiplayer == True:
            charx[1], chary[1], charface[1] = move_char(char[1], charx[1], chary[1], charwidth, charheight, charface[1], charability[1])
            
        #Drawing Arrows
        if charability[0] == 1:
            arrowx[0], arrowy[0], arrowwidth[0], arrowheight[0], arrowface[0], isactive[0], canuse[0], img_num = use_ability(char[0], charx[0], chary[0], charwidth, charheight, charface[0], charability[0], arrowx[0], arrowy[0], arrowwidth[0], arrowheight[0], arrowface[0], isactive[0], canuse[0], img_num)
            arrowx[0], arrowy[0], arrowface[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], swordcooldownstarted[0], swordstarttime[0], swordpassedtime[0], boltcooldownstarted[0], boltstarttime[0], boltpassedtime[0], staffx[0], staffy[0] = run_ability(charx[0], chary[0], charability[0], isactive[0], canuse[0], arrowx[0], arrowy[0], arrowface[0], cooldownstarted[0], starttime[0], passedtime[0], arrowcollisionoccured[0], swordcooldownstarted[0], swordstarttime[0], swordpassedtime[0], boltcooldownstarted[0], boltstarttime[0], boltpassedtime[0], staffx[0], staffy[0])
        if multiplayer == True and charability[1] == 1:
            arrowx[1], arrowy[1], arrowwidth[1], arrowheight[1], arrowface[1], isactive[1], canuse[1], img_num = use_ability(char[1], charx[1], chary[1], charwidth, charheight, charface[1], charability[1], arrowx[1], arrowy[1], arrowwidth[1], arrowheight[1], arrowface[1], isactive[1], canuse[1], img_num)
            arrowx[1], arrowy[1], arrowface[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], swordcooldownstarted[1], swordstarttime[1], swordpassedtime[1], boltcooldownstarted[1], boltstarttime[1], boltpassedtime[1], staffx[1], staffy[1] = run_ability(charx[1], chary[1], charability[1], isactive[1], canuse[1], arrowx[1], arrowy[1], arrowface[1], cooldownstarted[1], starttime[1], passedtime[1], arrowcollisionoccured[1], swordcooldownstarted[1], swordstarttime[1], swordpassedtime[1], boltcooldownstarted[1], boltstarttime[1], boltpassedtime[1], staffx[1], staffy[1])

        #Drawing Swords
        if charability[0] == 2:
            swordx[0], swordy[0], swordwidth[0], swordheight[0], swordface[0], isactive[0], canuse[0], img_num = use_ability(char[0], charx[0], chary[0], charwidth, charheight, charface[0], charability[0], swordx[0], swordy[0], swordwidth[0], swordheight[0], swordface[0], isactive[0], canuse[0], img_num) 
            swordx[0], swordy[0], swordface[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], swordcooldownstarted[0], swordstarttime[0], swordpassedtime[0], boltcooldownstarted[0], boltstarttime[0], boltpassedtime[0], staffx[0], staffy[0] = run_ability(charx[0], chary[0], charability[0], isactive[0], canuse[0], swordx[0], swordy[0], swordface[0], cooldownstarted[0], starttime[0], passedtime[0], arrowcollisionoccured[0], swordcooldownstarted[0], swordstarttime[0], swordpassedtime[0], boltcooldownstarted[0], boltstarttime[0], boltpassedtime[0], staffx[0], staffy[0])
        if multiplayer == True and charability[1] == 2:
            swordx[1], swordy[1], swordwidth[1], swordheight[1], swordface[1], isactive[1], canuse[1], img_num = use_ability(char[1], charx[1], chary[1], charwidth, charheight, charface[1], charability[1], swordx[1], swordy[1], swordwidth[1], swordheight[1], swordface[1], isactive[1], canuse[1], img_num) 
            swordx[1], swordy[1], swordface[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], swordcooldownstarted[1], swordstarttime[1], swordpassedtime[1], boltcooldownstarted[1], boltstarttime[1], boltpassedtime[1], staffx[1], staffy[1] = run_ability(charx[1], chary[1], charability[1], isactive[1], canuse[1], swordx[1], swordy[1], swordface[1], cooldownstarted[1], starttime[1], passedtime[1], arrowcollisionoccured[1], swordcooldownstarted[1], swordstarttime[1], swordpassedtime[1], boltcooldownstarted[1], boltstarttime[1], boltpassedtime[1], staffx[1], staffy[1])

        #Drawing mage bolts
        if charability[0] == 3:
            boltx[0], bolty[0], boltwidth[0], boltheight[0], boltface[0], isactive[0], canuse[0], img_num = use_ability(char[0], charx[0], chary[0], charwidth, charheight, charface[0], charability[0], boltx[0], bolty[0], boltwidth[0], boltheight[0], boltface[0], isactive[0], canuse[0], img_num) 
            boltx[0], bolty[0], staffface[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], swordcooldownstarted[0], swordstarttime[0], swordpassedtime[0], boltcooldownstarted[0], boltstarttime[0], boltpassedtime[0], staffx[0], staffy[0] = run_ability(charx[0], chary[0], charability[0], isactive[0], canuse[0], boltx[0], bolty[0], charface[0], cooldownstarted[0], starttime[0], passedtime[0], boltcollisionoccured[0], swordcooldownstarted[0], swordstarttime[0], swordpassedtime[0], boltcooldownstarted[0], boltstarttime[0], boltpassedtime[0], staffx[0], staffy[0])
        if multiplayer == True and charability[1] == 3:
            boltx[1], bolty[1], boltwidth[1], boltheight[1], boltface[1], isactive[1], canuse[1], img_num = use_ability(char[1], charx[1], chary[1], charwidth, charheight, charface[1], charability[1], boltx[1], bolty[1], boltwidth[1], boltheight[1], boltface[1], isactive[1], canuse[1], img_num) 
            boltx[1], bolty[1], staffface[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], swordcooldownstarted[1], swordstarttime[1], swordpassedtime[1], boltcooldownstarted[1], boltstarttime[1], boltpassedtime[1], staffx[1], staffy[1] = run_ability(charx[1], chary[1], charability[1], isactive[1], canuse[1], boltx[1], bolty[1], charface[1], cooldownstarted[1], starttime[1], passedtime[1], boltcollisionoccured[1], swordcooldownstarted[1], swordstarttime[1], swordpassedtime[1], boltcooldownstarted[1], boltstarttime[1], boltpassedtime[1], staffx[1], staffy[1])


        #Drawing Enemies
        enemy1x[0], enemy1y[0], enemy1face[0] = move_enemy(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], enemy1speed[0], enemy1face[0])
        enemy2x[0], enemy2y[0], enemy2face[0] = move_enemy(enemy2x[0], enemy2y[0], enemy2width[0], enemy1height[0], enemy2speed[0], enemy2face[0])

        #Drawing enemy spike ball
        enemyballx[0], enemybally[0], enemyballface[0], ballammo[0], ballisshooting[0] = enemy_shoot_spike_ball(enemy2x[0], enemy2y[0], enemy2face[0], enemyballx[0], enemybally[0], enemyballwidth[0], enemyballheight[0], enemyballface[0], ballammo[0], ballisshooting[0])

        #Enemy collision with player
        charx[0], chary[0], charhealth[0], enemy1x[0], enemy1y[0] = enemy_player_collision(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], charx[0], chary[0], charhealth[0])  
        if multiplayer:
            charx[1], chary[1], charhealth[1], enemy1x[0], enemy1y[0] = enemy_player_collision(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], charx[1], chary[1], charhealth[1])  
        charx[0], chary[0], charhealth[0], enemy2x[0], enemy2y[0] = enemy_player_collision(enemy2x[0], enemy2y[0], enemy2width[0], enemy2height[0], charx[0], chary[0], charhealth[0])  
        if multiplayer:
            charx[1], chary[1], charhealth[1], enemy2x[0], enemy2y[0] = enemy_player_collision(enemy2x[0], enemy2y[0], enemy2width[0], enemy2height[0], charx[1], chary[1], charhealth[1])  

        #Enemy collision with arrow
        if charability[0] == 1:
            enemy1x[0], enemy1y[0], arrowx[0], arrowy[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], arrowcollisionoccured[0] = enemy_arrow_collision(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], arrowx[0], arrowy[0], arrowwidth[0], arrowheight[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], arrowcollisionoccured[0])
        if charability[1] == 1 and multiplayer == True:
            enemy1x[0], enemy1y[0], arrowx[1], arrowy[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], arrowcollisionoccured[1] = enemy_arrow_collision(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], arrowx[1], arrowy[1], arrowwidth[1], arrowheight[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], arrowcollisionoccured[1])
        if charability[0] == 1:
            enemy2x[0], enemy2y[0], arrowx[0], arrowy[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], arrowcollisionoccured[0] = enemy_arrow_collision(enemy2x[0], enemy2y[0], enemy2width[0], enemy2height[0], arrowx[0], arrowy[0], arrowwidth[0], arrowheight[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0], arrowcollisionoccured[0])
        if charability[1] == 1 and multiplayer == True:
            enemy2x[0], enemy2y[0], arrowx[1], arrowy[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], arrowcollisionoccured[1] = enemy_arrow_collision(enemy2x[0], enemy2y[0], enemy2width[0], enemy2height[0], arrowx[1], arrowy[1], arrowwidth[1], arrowheight[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1], arrowcollisionoccured[1])
        
        #Enemy collision with sword
        if charability[0] == 2:
            enemy1x[0], enemy1y[0], swordx[0], swordy[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0] = enemy_sword_collision(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], swordx[0], swordy[0], swordwidth[0], swordheight[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0])
        if charability[1] == 2 and multiplayer == True:
            enemy1x[0], enemy1y[0], swordx[1], swordy[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1] = enemy_sword_collision(enemy1x[0], enemy1y[0], enemy1width[0], enemy1height[0], swordx[1], swordy[1], swordwidth[1], swordheight[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1])
        if charability[0] == 2:
            enemy2x[0], enemy2y[0], swordx[0], swordy[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0] = enemy_sword_collision(enemy2x[0], enemy2y[0], enemy2width[0], enemy2height[0], swordx[0], swordy[0], swordwidth[0], swordheight[0], isactive[0], canuse[0], cooldownstarted[0], starttime[0], passedtime[0])
        if charability[1] == 2 and multiplayer == True:
            enemy2x[0], enemy2y[0], swordx[1], swordy[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1] = enemy_sword_collision(enemy2x[0], enemy2y[0], enemy2width[0], enemy2height[0], swordx[1], swordy[1], swordwidth[1], swordheight[1], isactive[1], canuse[1], cooldownstarted[1], starttime[1], passedtime[1])
                       
        #Enemy spike ball collision with player
        enemyballx[0], enemybally[0], charx[0], chary[0], ballisshooting[0], ballammo[0], charhealth[0] = player_ball_collision(enemyballx[0], enemybally[0], charx[0], chary[0], charwidth, charheight, ballisshooting[0], ballammo[0], charhealth[0])
        if multiplayer:
            enemyballx[0], enemybally[0], charx[1], chary[1], ballisshooting[0], ballammo[0], charhealth[1] = player_ball_collision(enemyballx[0], enemybally[0], charx[1], chary[1], charwidth, charheight, ballisshooting[0], ballammo[0], charhealth[1])

        #Draw all the changes
        draw_screen()

    #Pause window
    elif window == 5:
        pause()

    pygame.display.update()
    
pygame.quit()