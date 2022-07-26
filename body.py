from food import *
import assets
import pygame


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, previous_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(assets.snake_body_img)
        self.rect = self.image.get_rect()
        self.rect.x = previous_sprite.prev_x
        self.rect.y = previous_sprite.prev_y
        self.prev_x = previous_sprite.prev_x
        self.prev_y = previous_sprite.prev_y
        self.previous_sprite = previous_sprite

    def update(self, *args, **kwargs):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.rect.x = self.previous_sprite.prev_x
        self.rect.y = self.previous_sprite.prev_y
        # print('Body update: ', self.rect.x, self.rect.y)

        # if self.rect.x < 0:
        #      self.rect.x = 400
        # if self.rect.x > 400:
        #     self.rect.x = 0
        # if self.rect.y > 400:
        #     self.rect.y = 0
        # if self.rect.y < 0:
        #     self.rect.y = 400