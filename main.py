# Import libraries
import pygame
# Import Random
import random as rd
#sounds
from pygame import mixer 
# Initialize pygame
pygame.init()

# Colors
background_color = (233, 255, 4)
player2_color = (2, 21, 122)
player1_color = (255, 0, 4)
ball_color = (2, 99, 50)
line_color = (255, 255, 255)

#music
mixer.music.load("ambiente.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.3)
# window size
screen_width = 800
screen_height = 600

# Size variable
size = (screen_width, screen_height)

#  Display the window
screen = pygame.display.set_mode( size )

# Players size
player_width = 15
player_height = 90

# Player 1 coordinates
player_1_x = 50
player_1_y = 300 - (player_height/2)
player_1_y_speed = 0

# Player 2 coordinates
player_2_x = 750 - player_width
player_2_y = player_1_y
player_2_y_speed = 0

# Ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

ball_speed_x = 0.6
ball_speed_y = 0.6

# Title
pygame.display.set_caption("Pong")

#score variables
player1_score = 0
player2_score = 0

#score font
score_font = pygame.font.Font("abcde.ttf", 34)

#won font
won_font = pygame.font.Font("abcde.ttf", 64 )

#score position in the screen player 1
player1_scoreX = 14
player1_scoreY = 14
#score position in the screen player 2
player2_scoreX = 640
player2_scoreY = 14

#won position
won_X = 200
won_Y = 250

#player 1 score F
def scoreP(x,y):
    score1 = score_font.render("jugador A:" + str(player1_score), True, (255, 4, 0)) 
    screen.blit( score1, (x, y))

def scoreC(x,y):
    score2 = score_font.render("jugador B:" + str(player2_score), True, (0, 4, 255)) 
    screen.blit( score2, (x, y))

# Icon
icon = pygame.image.load("pong-icon.png")
pygame.display.set_icon( icon )

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Players key controls
        if event.type == pygame.KEYDOWN:

            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -1

            if event.key == pygame.K_s:
                player_1_y_speed = 1

            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -1

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 1

        if event.type == pygame.KEYUP:

            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = 0

            if event.key == pygame.K_s:
                player_1_y_speed = 0

            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = 0

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0

    # Players movement
    player_1_y  += player_1_y_speed
    player_2_y += player_2_y_speed

    # Ball movement

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball boundaries: top or buttton
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1

#bola bordes derecha e isquierda
    if ball_x > screen_width:
        ball_lose = mixer.Sound("choque.wav")
        ball_lose.play()


        player1_score += 1      

        ball_x = screen_width /2
        ball_y = screen_height /2
        ball_speed_x *= rd.choice([-1, 1])

    elif ball_x < 0:
        ball_lose = mixer.Sound("choque.wav")
        ball_lose.play()

        player2_score += 1

        ball_x = screen_width /2
        ball_y = screen_height /2
        ball_speed_x *= rd.choice([-1, 1])    
    # Players boundaries

    # Player 1
    if player_1_y <= 0:
        player_1_y = 0

    if player_1_y >= screen_height - player_height:
        player_1_y = screen_height - player_height

    # Player 2
    if player_2_y <= 0:
        player_2_y = 0

    if player_2_y >= screen_height - player_height:
        player_2_y = screen_height - player_height




    # Fill the screen with color
    screen.fill( background_color )

    # Drowing area

    # Define the player 1 - left
    player_1 = pygame.draw.rect( screen, player1_color, (player_1_x, player_1_y, player_width, player_height))

    # Define the player 2 - right
    player_2 = pygame.draw.rect( screen, player2_color, (player_2_x, player_2_y, player_width, player_height))

    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/2, 0), (screen_width/2, screen_height))

    # Define the ball
    ball = pygame.draw.circle( screen, ball_color, (ball_x, ball_y), ball_radius)

   #collitions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        ball_sound = mixer.Sound("choque.wav")
        ball_sound.play()

    #show won text
    if player1_score == 3:
        ball_victory = mixer.Sound("victoria.wav")
        ball_victory.play()
        mixer.music.set_volume(0.1)
        ball_speed_x = 0
        ball_speed_Y = 0
        player_1_y_speed = 0
        player_2_y_speed = 0
        won_text = won_font.render("Jugador A Gano!!", True, (2,255,7) )
        screen.blit(won_text, (won_X, won_Y))

    elif player2_score == 3:
        ball_victory = mixer.Sound("victoria.wav")
        ball_victory.play()
        mixer.music.set_volume(0.1)
        won_text = won_font.render("Jugador B Gano!!", True, (2,255,7) )
        screen.blit(won_text, (won_X, won_Y))
 
    # call score 
    scoreP(player1_scoreX, player1_scoreY)

    scoreC(player2_scoreX, player2_scoreY)


    # Refresh the window
    pygame.display.flip()