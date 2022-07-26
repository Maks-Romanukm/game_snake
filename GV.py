import pygame

import logger
from settings import *



def draw_text(text, font, text_col, x, y, game_screen):
    img = font.render(text, True, text_col)
    game_screen.blit(img, (x, y))


def game_over(fade_counter, FPS, game_screen, score):
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        if fade_counter < screen_width:
            fade_counter += 5
            for y in range(0, 8, 2):
                pygame.draw.rect(game_screen, (BLACK), (0, y * 42, fade_counter, 42))
                pygame.draw.rect(game_screen, (BLACK), (screen_width - fade_counter, (y + 1) * 42, screen_width, 42))
        draw_text('GAME OVER!', pygame.font.SysFont('Lucida Sans', 16), WHITE, 106, 100, game_screen)
        draw_text('SCORE: ' + str(score), pygame.font.SysFont('Lucida Sans', 12), WHITE, 125, 125, game_screen)
        draw_text('PRESS SPACE TO PLAY AGAIN', pygame.font.SysFont('Lucida Sans', 12), WHITE, 70, 150, game_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                logger.info(event.key)
                if event.key == pygame.K_SPACE:
                    running = False
                    break

        pygame.display.update()

