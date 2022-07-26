import pygame
import settings


class InfoPanel:
    def __init__(self, game_screen, font):
        self.font = font
        self.game_screen = game_screen

        # '''Best_score'''
        # f1 = pygame.font.Font(None, 36)
        # text1 = f1.render('Best: ' + file.read(), 0.2, (255, 255, 255))
        # game_screen.blit(text1, (90, 1.5))

    def _draw_text(self, text, position):
        self.game_screen.blit(self.font.render(text, True, settings.white_color), position)

    def draw(self, fps, score):
        pygame.draw.rect(self.game_screen, settings.info_panel_bg_color, (0, 0, 400, 25))
        self._draw_text(f'Score: {score}', (0, 1.5))
        self._draw_text(f'FPS: {fps}', (190, 1.5))
