from food import *
from settings import snake_step
import assets
import pygame

snake_moves = {
    # x, y, rotate
    pygame.K_w: (0, -snake_step, 180),
    pygame.K_a: (-snake_step, 0, -90),
    pygame.K_s: (0, +snake_step, 0),
    pygame.K_d: (+snake_step, 0, 90),
}


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(assets.snake_head_img)
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 40
        self.direction = snake_moves[pygame.K_s]
        self.prev_x = self.rect.x - self.direction[0]
        self.prev_y = self.rect.y - self.direction[1]

    def update(self, *args, **kwargs):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        if self.rect.x < 0:
            self.rect.x = 290
        if self.rect.x > 290:
            self.rect.x = 0
        if self.rect.y > 320:
            self.rect.y = 30
        if self.rect.y < 30:
            self.rect.y = 320

    def change_direction(self, direction):
        self.direction = direction
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(assets.snake_head_img)
        self.image = pygame.transform.rotate(self.image, direction[2])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y