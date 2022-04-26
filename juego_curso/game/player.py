import pygame
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def update_pos(self, dir):
        if dir == pygame.K_RIGHT:
            self.rect.x += 1

        if dir == pygame.K_LEFT:
            self.rect.x -= 1