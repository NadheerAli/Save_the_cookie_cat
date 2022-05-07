import os
import pygame
import random
from .config import *


class Drill(pygame.sprite.Sprite):
    def __init__(self, left, top):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(SPRITES_DIRECTORY / 'drill.png')

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

        self.vel_y = FALL_SPEED

    def update(self):
        pygame.sprite.Sprite.update(self)
        self.rect.top += self.vel_y        

    def stop(self):
        self.vel_y = 0