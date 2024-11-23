import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple):
        super().__init__()
        self.image = paddle
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        if pos == (30, 0):
            self.up_button = pygame.K_w
            self.down_button = pygame.K_s
        else:
            self.up_button = pygame.K_UP
            self.down_button = pygame.K_DOWN
        self.score = 0
        self.dy = -5
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[self.up_button]:
            self.dy = -5
        elif pressed_keys[self.down_button]:
            self.dy = 5
        else:
            self.dy = 0
        if self.dy > 0:
            self.rect.y = min(SCREEN_HEIGHT - 100, self.rect.y + self.dy)
        else:
            self.rect.y = max(0, self.rect.y + self.dy)

player = Player((30, 0), (20, 100))
player1 = Player((750, 0), (20, 100))