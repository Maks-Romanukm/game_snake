import pygame
from pygame import mixer
import logger
from button import Button
import assets
import global_storage
import settings
import high_score


class Menu:
    def __init__(self, screen, font):
        self.font = font
        self.screen = screen
        self.resume_button = self.create_button(75, 20, assets.menu_resume)
        self.exit_button = self.create_button(75, 200, assets.menu_quit)
        self.options_button = self.create_button(75, 110, assets.menu_options)
        self.fps_button = self.create_button(75, 20, assets.menu_fps)
        self.help_button = self.create_button(75, 82, assets.menu_help)
        self.music_button = self.create_button(75, 160, assets.menu_music)
        self.x_button = self.create_button(265, 5, assets.menu_x)
        self.on_button = self.create_button(50, 50, assets.menu_on)
        self.off_button = self.create_button(50, 50, assets.menu_off)
        self.L_button = self.create_button(75, 125, assets.menu_L)
        self.R_button = self.create_button(200, 125, assets.menu_R)
        self.back_button = self.create_button(113, 255, assets.menu_back)

    def create_button(self, x, y, img_uri):
        return Button(x, y, pygame.image.load(img_uri).convert_alpha(), 1)

    def draw_text(self, text, form, text_color, x, y):
        img = form.render(text, True, text_color)
        self.screen.blit(img, (x, y))

    def fps_page(self):
        pygame.display.set_caption('Fps')
        logger.debug('FPS page opened')
        while True:
            self.screen.fill(settings.bg_color)
            back_button = self.create_button(113, 255, assets.menu_back)
            self.screen.blit(self.font.render(str(global_storage.fps), True, (69, 196, 176)), (137, 128))
            if back_button.draw(self.screen):
                logger.debug('FPS page closed')
                break
            if self.L_button.draw(self.screen):
                if global_storage.fps > 0:
                    global_storage.fps -= 1
                    self.font.render(str(global_storage.fps), True, (69, 196, 176))
                    self.screen.blit(self.font.render(str(global_storage.fps), True, (69, 196, 176)), (137, 128))
            if self.R_button.draw(self.screen):
                if global_storage.fps < 100:
                    global_storage.fps += 1
                    self.font.render(str(global_storage.fps), True, (69, 196, 176))
                    self.screen.blit(self.font.render(str(global_storage.fps), True, (69, 196, 176)), (137, 128))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def help_page(self):
        pygame.display.set_caption('Help')
        logger.debug('Help page opened')

        while True:
            self.screen.fill(settings.bg_color)
            self.screen.blit(self.font.render('W = Вперед', True, (69, 196, 176)), (75, 35))
            self.screen.blit(self.font.render('S = Назад', True, (69, 196, 176)), (75, 70))
            self.screen.blit(self.font.render('A = Вліво', True, (69, 196, 176)), (75, 135))
            self.screen.blit(self.font.render('D = Вправо', True, (69, 196, 176)), (75, 170))
            back_button = self.create_button(113, 255, assets.menu_back)
            if back_button.draw(self.screen):
                logger.debug('Help page closed')
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def music_page(self):
        pygame.display.set_caption('Music')
        logger.debug('Music page opened')

        while True:
            self.screen.fill(settings.bg_color)
            back_button = self.create_button(113, 255, assets.menu_back)
            self.screen.blit(self.font.render(str(int(global_storage.music_volume) / 10), True, (69, 196, 176)), (137, 128))
            if back_button.draw(self.screen):
                logger.debug('Music page closed')
                break
            if self.L_button.draw(self.screen) and global_storage.music_volume > 0:
                self._change_music_volume(-1)
                logger.info('music_volume -1')
                print(global_storage.music_volume)
            if self.R_button.draw(self.screen) and global_storage.music_volume < 10:
                self._change_music_volume(+1)
                logger.info('music_volume +1')
                print(global_storage.music_volume)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def _change_music_volume(self, change):
        initial_volume = global_storage.music_volume
        global_storage.music_volume += change
        self.font.render(str(int(global_storage.music_volume) / 10), True, (69, 196, 176))
        self.screen.blit(self.font.render(str(int(global_storage.music_volume) / 10), True, (69, 196, 176)), (137, 128))
        logger.debug(f'Music volume changed from {initial_volume} to {global_storage.music_volume}')

    def options_page(self):
        pygame.display.set_caption('Options')
        logger.debug('Options page opened')
        while True:
            self.screen.fill(settings.bg_color)
            back_button = self.create_button(113, 255, assets.menu_back)
            if self.fps_button.draw(self.screen):
                self.fps_page()
            if self.help_button.draw(self.screen):
                self.help_page()
            if self.music_button.draw(self.screen):
                self.music_page()
            if back_button.draw(self.screen):
                logger.debug('Options page closed')
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def open_menu(self):
        pygame.display.set_caption('Menu')
        logger.info('Menu opened')
        while True:
            self.screen.fill(settings.bg_color)
            self.screen.blit(pygame.font.Font(None, 20).render(f' high score:{high_score.read()}', True, (255, 255, 255)), (80, 70))

            if self.resume_button.draw(self.screen):
                break
            if self.exit_button.draw(self.screen):
                pygame.quit()
            if self.options_button.draw(self.screen):
                self.options_page()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
