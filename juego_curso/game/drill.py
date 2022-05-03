import pygame
import random
from .config import *


class Drill(pygame.sprite.Sprite):
    def __init__(self, left, top):
        pygame.sprite.Sprite.__init__(self)
        # self.vel_y = 0

        self.image = pygame.Surface((50,50))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

        self.vel_y = DRILLS_SPEED

    # Ajustar velocidad de caída
    def update(self):
        pygame.sprite.Sprite.update(self)
        self.rect.top += self.vel_y
        

        # if self.rect.bottom == HEIGHT - 30:
        #     self.rect.x = random.randrange(100, WIDTH-100)
        #     self.rect.y = 0

    def stop(self):
        self.vel_y = 0