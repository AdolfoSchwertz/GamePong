import pygame
import sys

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_WIDHT = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 6



WHITE = (255,255,255)
BLACK = (0,0,0)
font_file = "C:\Press_Start_2P\PressStart2P-Regular.ttf"
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

#pygame.rect(x,y,width,height)
paddle_a = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,PADDLE_WIDHT, PADDLE_HEIGHT)
paddle_b = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDHT, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,PADDLE_WIDHT, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < SCREEN_HEIGHT:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < SCREEN_HEIGHT:
        paddle_b.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y -= ball_dy

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_dx = -ball_dx
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_dy = -ball_dy

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball.x = SCREEN_WIDTH //2 - BALL_SIZE//2
        ball.y = SCREEN_HEIGHT //2 - BALL_SIZE//2


    #Atualizar a tela
    pygame.display.flip()

    # Controlar fps
    clock = pygame.time.Clock()
    clock.tick(60)

