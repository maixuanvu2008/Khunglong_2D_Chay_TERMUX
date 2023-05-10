import pygame

import random

# initialize pygame

pygame.init()

# set screen size

SCREEN_WIDTH = 480

SCREEN_HEIGHT = 320

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set window title

pygame.display.set_caption("PyDino")

# load images

dino_img = pygame.image.load("images/dino.png").convert_alpha()

cactus_img = pygame.image.load("images/cactus.png").convert_alpha()

bird_img = pygame.image.load("images/bird.png").convert_alpha()

# set game variables

dino_x, dino_y = 50, 240

dino_width, dino_height = 50, 50

dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

dino_jump, dino_jump_speed = False, 14

cactus_width, cactus_height = 20, 50

cactus_gap = 120

cactus_x, cactus_y = SCREEN_WIDTH, 260

cactus_speed = 6

cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)

bird_x, bird_y = SCREEN_WIDTH/2, 120

bird_width, bird_height = 40, 30

bird_speed = 8

bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

score = 0

font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

game_over = False

# draw background

def draw_background():

    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (0, 290), (SCREEN_WIDTH, 290), 2)

    pygame.draw.line(screen, (200, 200, 200), (0, 291), (SCREEN_WIDTH, 291), 1)

# draw objects: cactus, bird, and dino

def draw_objects():

    screen.blit(cactus_img, (cactus_x, cactus_y))

    screen.blit(dino_img, (dino_x, dino_y))

    screen.blit(bird_img, (bird_x, bird_y))

# draw score

def draw_score():

    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))

    screen.blit(score_text, (10, 10))

# check for collision

def check_collision():

    if dino_rect.colliderect(cactus_rect) or dino_rect.colliderect(bird_rect):

        return True

    return False

# create new cactus

def new_cactus():

    global cactus_x, cactus_y, score, cactus_speed, cactus_gap, cactus_rect

    cactus_gap = random.randint(100, 150)

    cactus_x -= cactus_speed

    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)

    if cactus_x < -cactus_width:

        cactus_x = SCREEN_WIDTH

        score += 1

        cactus_speed += 0.2

# create new bird

def new_bird():

    global bird_x, bird_y, bird_speed, bird_rect

    bird_x -= bird_speed

    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

    if bird_x < -bird_width:

        bird_x = SCREEN_WIDTH

        bird_y = random.randint(60, 180)

        bird_speed += 0.2

# jump dino

def jump_dino():

    global dino_jump, dino_jump_speed, dino_y, dino_rect

    dino_jump = True

    dino_jump_speed = 14

    dino_y -= dino_jump_speed

    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

# update dino position

def update_dino():

    global dino_jump, dino_jump_speed, dino_y, dino_rect

    if dino_jump:

        if dino_jump_speed >= -14:

            dino_y -= dino_jump_speed

            dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

            dino_jump_speed -= 1

        else:

            dino_jump = False

            dino_jump_speed = 14

            dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

    else:

        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

# main game loop

while not game_over:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not dino_jump:

                jump_dino()

    # update cactus, bird, and dino

    new_cactus()

    new_bird()

    update_dino()

    # check collision and game over

    if check_collision():

        game_over = True

    # draw objects and score

    draw_background()

    draw_objects()

    draw_score()

    pygame.display.update()

# quit pygame

pygame.quit()
