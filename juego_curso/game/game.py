import pygame
import sys
from .config import * 
from .platform import Platform 
from .player import Player 

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True

    def start(self):
        self.new()

    def new(self):
        self.generateElements()
        self.run()

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def generateElements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top)

        self.sprites = pygame.sprite.Group()
        
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.surface.fill(BACKGROUND_COLOR)
        self.sprites.draw(self.surface)

    def update(self):
        pygame.display.flip()

    def stop(self):
        pass