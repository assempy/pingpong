import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
font = pygame.font.Font('bit5x3.ttf', 50)
bounce_sound = pygame.mixer.Sound('bounce.wav')
#score_sound = pygame.mixer.Sound('score.wav')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

border = pygame.Surface((15, 15))
border.fill('WHITE')

paddle = pygame.image.load('paddle_final.png')