import assets
import random
import pygame
from snake import *


class Dead(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(assets.dead_img)
        self.rect = self.image.get_rect()
        self.change_location()


    def change_location(self):
        self.rect.x = random.randint(1, 29) * 10
        self.rect.y = random.randint(3, 29) * 10
#ЧЕК ЩО ФРУКТИ НЕ ВИХОДЯТЬ ЗА ГРАНЬ