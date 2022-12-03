import pygame
import random

pygame.init()

#game constant
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
WIDTH = 450
HEIGTH = 300
red = (255,0,0)
orange = (255, 255 , 0)
yellow = (255, 255 , 0)


#game variables
score =0
player_x=50
player_y=200
gravity = 1
Y_change = 0
x_change =0
obstacles = [300, 450 , 600]
obstacle_speed =3
active = False

screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Infinte Runner")
background=BLACK
FPS=60
font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()


running  = True
while running:
    timer.tick(FPS)
    screen.fill(background)
    if not active:
        #instruction_text = font.render(f'Score:{score}', True, WHITE,BLACK)
       # screen.blit(instruction_text,(80,50))
        instruction_text2 = font.render(f'Space Bar Jumps and Start.', True, WHITE,BLACK)
        screen.blit(instruction_text2,(100, 50))

    score_text = font.render(f'Score:{score}', True, WHITE,BLACK)
    screen.blit(score_text,(160, 250))

    floor = pygame.draw.rect(screen, WHITE, [0,220,WIDTH,5])
    #player = pygame.image.load("C:\\Users\\91861\\Desktop\\python\\Assets\\spiderman_stand.png")
    #pygame.transform.scale(player,(20,20))
    player = pygame.draw.rect(screen, GREEN, [player_x,player_y,22,20])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [300, 450, 600]
                player_x = 50
                score=0
                active = True

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and Y_change == 0:
                Y_change = 18
            if event.key == pygame.K_RIGHT:
                Y_change = 2
            if event.key == pygame.K_RIGHT:
                Y_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Y_change = 0
            if event.key == pygame.K_RIGHT:
                Y_change = 0
                
    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] <= 20:
                obstacles[i]  = random.randint(470, 570)
                score += 1
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False
    if 0<= player_x<= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430
    
    if Y_change > 0 or player_y < 200:
        player_y -= Y_change
        Y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and Y_change < 0:
        Y_change = 0

    pygame.display.flip()
pygame.quit()
