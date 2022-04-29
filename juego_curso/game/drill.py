import pygame
import random
from .config import *


class Drill(pygame.sprite.Sprite):
    def __init__(self, top):
        pygame.sprite.Sprite.__init__(self)
        # self.vel_y = 0

        self.image = pygame.Surface((50,50))
        self.image.fill(RED)

        # Hasta aquí sigue la posibilidad de que aparezcan en un mismo espacio
        self.drills_area = SURFACE_RIGHT_MARGIN - SURFACE_LEFT_MARGIN # 600 - área en el que puede aparacer
        self.drills_grid = self.drills_area / 10 # divide el área en espacios de 60
        self.drill_random_position = self.drills_grid * random.randrange(1, 11) # define un número entre 1 y 10 (60 y 600) para posicionar el taladro

        self.rect = self.image.get_rect()
        self.rect.left = self.drill_random_position
        print(self.rect.left)
        self.rect.top = top

    # Ajustar velocidad de caída
    def update(self):
        pygame.sprite.Sprite.update(self)
        self.rect.top += 1
        

        # if self.rect.bottom == HEIGHT - 30:
        #     self.rect.x = random.randrange(100, WIDTH-100)
        #     self.rect.y = 0