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

        self.can_move = True

    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def update_pos_right(self):
        if self.rect.x < WIDTH - 140 and self.can_move:
            self.rect.x += PLAYER_SPEED

    def update_pos_left(self):
        if self.rect.x > 100 and self.can_move:
            self.rect.x -= PLAYER_SPEED

    def stop(self):
        self.can_move = False