from player_class import Player
from ball import Ball
import pygame
from settings import bounce_sound

colision_tolerance = 10

def check_collisions(sprite1: Ball, sprite2: Player):
    if not pygame.Rect.colliderect(sprite1.rect, sprite2.rect):
        return
    if abs(sprite1.rect.top - sprite2.rect.bottom) < colision_tolerance and sprite1.dy < 0:
        sprite1.dy *= -1
        sprite1.dx *= -1
    if abs(sprite1.rect.bottom - sprite2.rect.top) < colision_tolerance and sprite1.dy > 0:
        sprite1.dy *= -1
        sprite1.dx *= -1
    if abs(sprite1.rect.left - sprite2.rect.right) < colision_tolerance and sprite1.dx < 0:
        sprite1.dx *= -1
    if abs(sprite1.rect.right - sprite2.rect.left) < colision_tolerance and sprite1.dx > 0:
        sprite1.dx *= -1
    bounce_sound.play()