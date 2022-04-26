import pygame
import sys
import random
from .config import * 
from .platform import Platform 
from .player import Player 
from .drill import Drill 

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True
        self.clock = pygame.time.Clock()

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
        # Ajustar margen de aparición en lado derecho
        self.drill = Drill(random.randrange(100, WIDTH-100), 0)

        self.sprites = pygame.sprite.Group()
        
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.sprites.add(self.drill)
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Este código ejecuta continuamente porque el atributo running sigue siendo true
        key = pygame.key.get_pressed()
        if key:
            self.player.update_pos(key)

        # Se llama aquí porque no se actualiza la posición con update() en el archivo Drill
        # self.drill.update_pos()


    def draw(self):
        self.surface.fill(BACKGROUND_COLOR)
        self.sprites.draw(self.surface)

    def update(self):
        # pygame.display.flip()
        # Ejecuta los métodos update de los sprites
        self.sprites.update()

    def stop(self):
        pass