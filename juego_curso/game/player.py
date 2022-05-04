import os
import pygame
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom, dir_image):
        pygame.sprite.Sprite.__init__(self)

        # self.image = pygame.Surface((40, 40))
        # self.image.fill(GREEN)

        self.images = (
            pygame.image.load(os.path.join(dir_image, 'steven_right.png')),
            pygame.image.load(os.path.join(dir_image, 'steven_left.png'))
        )

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.can_move = True

    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def update_pos_right(self):
        if self.rect.right < WIDTH and self.can_move:
            self.image = self.images[0]
            self.rect.x += PLAYER_SPEED

    def update_pos_left(self):
        if self.rect.left > 0 and self.can_move:
            self.image = self.images[1]
            self.rect.x -= PLAYER_SPEED

    def stop(self):
        self.can_move = False