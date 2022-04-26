import pygame
from .config import *
import random

class Drill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vel_y = 0

        self.image = pygame.Surface((50,50))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, WIDTH-100)
        self.rect.y = 0

    # Ajustar velocidad de caída
    def update_pos(self):
        self.rect.y += 1

        if self.rect.bottom == HEIGHT - 30:
            self.rect.x = random.randrange(100, WIDTH-100)
            self.rect.y = 0