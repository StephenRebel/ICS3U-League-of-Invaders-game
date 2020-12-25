import pygame
import random
pygame.init()

#Basic game setup
pygame.display.set_caption("League Of Invaders")
size = (1280, 720)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("gamefiles/images/dirt_bg.jpg")
bg_scale = pygame.transform.scale(bg, (1280, 720))
char1img = pygame.image.load("gamefiles/images/green_char.png")
char2img = pygame.image.load("gamefiles/images/blue_char.png")
arrowimg = pygame.image.load("gamefiles/images/arrow.png")
enemyimg = pygame.image.load("gamefiles/images/red_enemy.png")

#Game variables
multiplayer = True
char, charx, chary, charwidth, charheight, charface, charability = [1, 2], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], 64, 64, [0, 0], [1, 1]
arrowx, arrowy, arrowwidth, arrowheight, arrowface = [-100, -100], [0, 0], [10, 10], [62, 62], [0, 0]
enemyx, enemyy, enemywidth, enemyheight, enemyface = 300, 200, 64, 64, 0
ammo, isshooting = [1, 1], [False, False]

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

#Draw enemies
def draw_enemy(img, x, y, face):
    new_enemy = pygame.transform.rotate(img, face)
    screen.blit(new_enemy, (x, y))

#Draw the screen
def draw_screen():
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

    #Enemy
    draw_enemy(enemyimg, enemyx, enemyy, enemyface)

    pygame.display.update()

#Move character function
def move_char(char, x, y, width, height, face):
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

    # Movement for both players
    if key_type[0]:
        face = 90
        if x - 1 <= 0:
            x = 0
        else:
            x -= 2
    elif key_type[1]:
        face = 270
        if x + 1 >= size[0] - width:
            x = size[0] - width
        else:
            x += 2
    elif key_type[2]:
        face = 0
        if y - 1 <= 0:
            y = 0
        else:
            y -= 2
    elif key_type[3]:
        face = 180
        if y + 1 >= size[1] - height:
            y = size[1] - height
        else:
            y += 2 
    return x, y, face

#Use ability function
def use_ability(char, charx, chary, charwidth, charheight, charface, ability, ammo, x, y, width, height, face, isshooting):
    keys = pygame.key.get_pressed()
    key_type = []
    if char == 1:
        key_type.append(keys[pygame.K_SPACE])
        i = 0
    elif char == 2:
        key_type.append(keys[pygame.K_e])
        i = 1
        
    #Arrow ability    
    if ability == 1 and key_type[0] and ammo[i] > 0 and isshooting[i] == False:
        ammo[i] -= 1
        face[i] = charface
        if face[i] == 0 or face[i] == 180:
            width[i], height[i] = 8, 64
            x[i], y[i] = charx + (charwidth / 2) - width[i] / 2, chary + (charheight / 2)
        elif face[i] == 90 or face[i] == 270:
            width[i], height[i] = 64, 8
            x[i], y[i] = charx + (charwidth / 2), chary + (charheight / 2) - height[i] / 2
        isshooting[i] = True
    return x[i], y[i], width[i], height[i], face[i], isshooting[i], ammo[i]

#Run ability function
def run_ability(char, ability, ammo, isshooting, x, y, face):
    i = 0
    if char == 1:
        i = 0
    elif char == 2:
        i = 1
    if ability == 1 and isshooting[i] == True:
        if face[i] == 0 and y[i] > -64:
            y[i] -= 10
        elif face[i] == 180 and y[i] < size[1] + 64:
            y[i] += 10
        elif face[i] == 270 and x[i] < size[0] + 64:
            x[i] += 10
        elif face[i] == 90 and x[i] > -64:
            x[i] -= 10
        else:
            isshooting[i] = False
            ammo[i] += 1
    return x[i], y[i], isshooting[i], ammo[i]
  
#Find closest character
def find_closest_char():
    if multiplayer:
        if (abs(enemyx - charx[0]) ** 2 + abs(enemyy - chary[0]) ** 2) < (abs(enemyx - charx[1]) ** 2 + abs(enemyy - chary[1]) ** 2):
            closest_char = [charx[0], chary[0]]
        else:
            closest_char = [charx[1], chary[1]]
    else:
        closest_char = [charx[0], chary[0]]
    return closest_char

#Run function to move enemy
def move_enemy(enemyx, enemyy, enemywidth, enemyheight):
    closest_char = find_closest_char()

    #Move enemy towards closest character
    if (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) == 0:
        slope = 0.01
    else:
        slope = abs(((enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2)) / ((enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2)))
    if slope < 1:
        if (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx -= 1
        elif (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx += 1
        if (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy -= slope * 1
        elif (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy += slope * 1
    else:
        if (enemyy + enemyy / 2) - (closest_char[1] + charheight / 2) == 0:
            slope = 0.01
        else:
            slope = abs(((enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2)) / ((enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2)))             
        if (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) > 0:
            enemyx -= slope * 1
        elif (enemyx + enemywidth / 2) - (closest_char[0] + charwidth / 2) < 0:
            enemyx += slope * 1
        if (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) > 0:
            enemyy -= 1
        elif (enemyy + enemyheight / 2) - (closest_char[1] + charheight / 2) < 0:
            enemyy += 1
    return enemyx, enemyy

#Run function to detect collision between enemy and player
def enemy_player_collision(enemyx, enemyy, enemywidth, enemyheight, char, charx, chary):
    for enemyxpos in range(int(enemyx), int(enemyx + enemywidth)):
        if charx + charwidth >= enemyxpos >= charx:
            for enemyypos in range(int(enemyy), int(enemyy + enemyheight)):
                if chary + charheight >= enemyypos >= chary:
                    charx, chary = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                    return charx, chary
    return charx, chary

#Run function to detect collision between enemy and arrow
def enemy_arrow_collision(enemyx, enemyy, enemywidth, enemyheight, arrowx, arrowy, arrowwidth, arrowheight, isshooting, ammo):
    for enemyxpos in range(int(enemyx), int(enemyx + enemywidth)):
        if arrowx + arrowwidth >= enemyxpos >= arrowx:
            for enemyypos in range(int(enemyy), int(enemyy + enemyheight)):
                if arrowy + arrowheight >= enemyypos >= arrowy:
                    arrowx, arrowy = -64, -64 
                    isshooting = False
                    ammo += 1
                    enemyx, enemyy = (random.randrange(enemywidth, size[0] - enemywidth), random.randrange(enemyheight, size[1] - enemyheight))
                    return enemyx, enemyy, arrowx, arrowy, isshooting, ammo
    return enemyx, enemyy, arrowx, arrowy, isshooting, ammo
      

#Main game loop
rungame = True
while rungame:

    pygame.time.delay(10)

    #Close game when quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

    #Drawing stuff

    #Drawing characters
    charx[0], chary[0], charface[0] = move_char(char[0], charx[0], chary[0], charwidth, charheight, charface[0])
    if multiplayer == True:
        charx[1], chary[1], charface[1] = move_char(char[1], charx[1], chary[1], charwidth, charheight, charface[1])

    #Drawing Arrows
    if charability[0] == 1:
        arrowx[0], arrowy[0], arrowwidth[0], arrowheight[0], arrowface[0], isshooting[0], ammo[0] = use_ability(char[0], charx[0], chary[0], charwidth, charheight, charface[0], charability[0], ammo, arrowx, arrowy, arrowwidth, arrowheight, arrowface, isshooting)
        arrowx[0], arrowy[0], isshooting[0], ammo[0] = run_ability([char[0]], charability[0], ammo, isshooting, arrowx, arrowy, arrowface)
    if multiplayer == True and charability[1] == 1:
        arrowx[1], arrowy[1], arrowwidth[1], arrowheight[1], arrowface[1], isshooting[1], ammo[1] = use_ability(char[1], charx[1], chary[1], charwidth, charheight, charface[1], charability[1], ammo, arrowx, arrowy, arrowwidth, arrowheight, arrowface, isshooting)
        arrowx[1], arrowy[1], isshooting[1], ammo[1] = run_ability(char[1], charability[1], ammo, isshooting, arrowx, arrowy, arrowface)

    #Drawing Enemies
    enemyx, enemyy = move_enemy(enemyx, enemyy, enemywidth, enemyheight)

    #Enemy collision with player
    charx[0], chary[0] = enemy_player_collision(enemyx, enemyy, enemywidth, enemyheight, char[0], charx[0], chary[0])  
    if multiplayer:
        charx[1], chary[1] = enemy_player_collision(enemyx, enemyy, enemywidth, enemyheight, char[1], charx[1], chary[1])  

    #Enemy collision with arrow
    if charability[0] == 1:
        enemyx, enemyy, arrowx[0], arrowy[0], isshooting[0], ammo[0] = enemy_arrow_collision(enemyx, enemyy, enemywidth, enemyheight, arrowx[0], arrowy[0], arrowwidth[0], arrowheight[0], isshooting[0], ammo[0])
    if charability[1] == 1 and multiplayer == True:
        enemyx, enemyy, arrowx[1], arrowy[1], isshooting[1], ammo[1] = enemy_arrow_collision(enemyx, enemyy, enemywidth, enemyheight, arrowx[1], arrowy[1], arrowwidth[1], arrowheight[1], isshooting[1], ammo[1])
    
    draw_screen()

pygame.quit()