import pygame
from ball import *
from player_class import *
from settings import *
from collisions import *


clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player1)
all_sprites.add(sp1)

def draw_border(screen):
    screen.fill('BLACK')
    for i in range(SCREEN_HEIGHT // 15):
        if i % 2 == 1:
            continue
        screen.blit(border, (SCREEN_WIDTH // 2, i * 15))

def show_score(screen):
    score1 = font.render(str(player.score), True, 'WHITE')
    score2 = font.render(str(player1.score), True, 'WHITE')
    screen.blit(score1, (SCREEN_WIDTH // 2 + score1.get_width() + 20, 0))
    screen.blit(score2, (SCREEN_WIDTH // 2 - score1.get_width() - 30, 0))

def re_game(screen):
    restart = font.render('Press Space to Continue', True, 'WHITE')
    screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 200))

def main():
    game = True
    player.score = 0
    player1.score = 0
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                return
    
        draw_border(screen)
        show_score(screen)
        all_sprites.update()
        check_collisions(sp1, player)
        check_collisions(sp1, player1)
        all_sprites.draw(screen)

        if player.score == 10:
            game = False
            return
        if player1.score == 10:
            game = False
            return

        clock.tick(80)
        pygame.display.update()
        pygame.display.flip()

def restart():
    credit = True
    while credit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                credit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        re_game(screen)
        pygame.display.update()
        pygame.display.flip()

restart()
pygame.quit()