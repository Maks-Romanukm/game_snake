import assets
import random
import pygame
from snake import *

food_var = (
    {'img': 'assets/food.png', 'score': 1},
    {'img': 'assets/light.png', 'score': 3}
)


# ({'img': 'assets/food.png', 'score': 1}, {'img': 'assets/light.png', 'score': 5})

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice(food_var)['img'])
        self.score = 0
        self.rect = self.image.get_rect()
        self.change_location()

    def change_location(self):
        self.rect.x = random.randint(1, 29) * 10
        self.rect.y = random.randint(3, 29) * 10
        food = random.choice(food_var)
        self.image = pygame.image.load(food['img'])
        self.score = food['score']
