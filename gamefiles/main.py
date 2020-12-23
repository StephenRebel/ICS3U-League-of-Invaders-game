import pygame
pygame.init()

#Basic game setup
pygame.display.set_caption("League Of Invaders")
size = (1280, 720)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("gamefiles/images/dirt_bg.jpg")
bg_scale = pygame.transform.scale(bg, (1280, 720))
char1img = pygame.image.load("gamefiles/images/green_char.png")
char2img = pygame.image.load("gamefiles/images/blue_char.png")

#Game variables
multiplayer = False
char, charx, chary, charwidth, charheight, charface = [1, 2], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], 64, 64, [0, 0]

#Draw characters
def draw_char(char, x, y, face):
    new_char = pygame.transform.rotate(char, face)
    screen.blit(new_char, (x, y))

#Draw the screen
def draw_screen():
    screen.blit(bg_scale, (0, 0))
    draw_char(char1img, charx[0], chary[0], charface[0])
    if multiplayer == True:
        draw_char(char2img, charx[1], chary[1], charface[1])
    pygame.display.update()

#Move character function
def move_char(char, x, y, width, height, face):

    # Detect if player hit keys
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
            x -= 1
    elif key_type[1]:
        face = 270
        if x + 1 >= size[0] - width:
            x = size[0] - width
        else:
            x += 1
    elif key_type[2]:
        face = 0
        if y - 1 <= 0:
            y = 0
        else:
            y -= 1
    elif key_type[3]:
        face = 180
        if y + 1 >= size[1] - height:
            y = size[1] - height
        else:
            y += 1 
    return x, y, face

#Main game loop
rungame = True
while rungame:

    pygame.time.delay(10)

    #Close game when quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

    #Drawing stuff
    charx[0], chary[0], charface[0] = move_char(char[0], charx[0], chary[0], charwidth, charheight, charface[0])
    if multiplayer == True:
        charx[1], chary[1], charface[1] = move_char(char[1], charx[1], chary[1], charwidth, charheight, charface[1])

    draw_screen()

pygame.quit()