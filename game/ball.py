import pygame
import random
from settings import *
from player_class import *


velocity = [i for i in range(-7, -3)] + [i for i in range(4, 7)]

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.dx = random.choice(velocity)
        self.dy = random.choice(velocity)
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - 25:
            self.dy *= -1
            bounce_sound.play()
        if self.rect.x <= 0:
            self.rect.x, self.rect.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
            self.dx = random.choice(velocity)
            self.dy = random.choice(velocity)
            player.score += 1
            #score_sound.play()
        if self.rect.x >= SCREEN_WIDTH:
            self.rect.x, self.rect.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
            self.dx = random.choice(velocity)
            self.dy = random.choice(velocity)
            player1.score += 1
            #score_sound.play()
    

sp1 = Ball()
