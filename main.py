import pygame
import sys

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255,255,255)
BLACK = (0,0,0)
font_file = "C:\Press_Start_2P\PressStart2P-Regular.ttf"
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

pygame.quit()