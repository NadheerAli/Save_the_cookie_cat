import os
import pygame
from .config import *

class Cookie(pygame.sprite.Sprite):
    def __init__(self, left, top, dir_image):
        pygame.sprite.Sprite.__init__(self)

        # self.image = pygame.Surface((50,50))
        # self.image.fill(BLUE)
        self.image = pygame.image.load(os.path.join(dir_image, 'cookie_cat.png'))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.vel_y = DRILLS_SPEED

    # Ajustar velocidad de caída
    def update(self):
        pygame.sprite.Sprite.update(self)
        self.rect.top += self.vel_y

    def stop(self):
        self.vel_y = 0