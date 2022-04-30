import os
import pygame
import sys
import random
from .config import * 
from .platform import Platform 
from .player import Player 
from .drill import Drill 
from .cookie import Cookie 

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True

        self.clock = pygame.time.Clock()

        self.dir = os.path.dirname(__file__)
        self.dir_sound = os.path.join(self.dir, 'sources/sounds/')

    def start(self):
        self.new()

    def new(self):
        self.generateElements()
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def generateElements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top)
        # Ajustar margen de aparición en lado derecho
        # self.drill = Drill(random.randrange(100, WIDTH-100), 0)

        self.sprites = pygame.sprite.Group()
        self.drills = pygame.sprite.Group()
        self.cookies = pygame.sprite.Group()
        
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.generate_drills()
        self.generate_cookies()
        
    def generate_drills(self):
        top_last_position = -100
        if len(self.drills) == 0:
            for drill in range(0, MAX_DRILLS):
                left_random = DRILLS_GRID * random.randrange(1, 11)

                drill = Drill(left_random, top_last_position)

                random_gap_drills = random.randrange(100, DRILLS_GAP)
                top_last_position = drill.rect.top - random_gap_drills

                self.sprites.add(drill)
                self.drills.add(drill)

    def generate_cookies(self):
        top_last_position = -800
        if len(self.cookies) == 0:
            for cookie in range(0, MAX_COOKIES):
                left_random = DRILLS_GRID * random.randrange(1, 11)

                cookie = Cookie(left_random, top_last_position)

                random_gap_cookies = random.randrange(400, COOKIES_GAP)
                top_last_position = cookie.rect.top - random_gap_cookies

                self.sprites.add(cookie)
                self.cookies.add(cookie)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Este código ejecuta continuamente porque el atributo running sigue siendo true
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player.update_pos_left()
            
        if key[pygame.K_RIGHT]:
            self.player.update_pos_right()

        # Se llama aquí porque no se actualiza la posición con update() en el archivo Drill
        # self.drill.update_pos()


    def draw(self):
        self.surface.fill(BACKGROUND_COLOR)
        self.sprites.draw(self.surface)

    def update(self):
        pygame.display.flip()
        # Ejecuta los métodos update de los sprites
        self.sprites.update()

        drill = self.player.collide_with(self.drills)

        if drill:
            self.delete_collided_drill(drill)

        cookie = self.player.collide_with(self.cookies)

        if cookie:
            self.delete_collided_cookie(cookie)

        self.delete_elements(self.drills)
        self.delete_elements(self.cookies)
        self.generate_drills()
        self.generate_cookies()

    def delete_collided_drill(self, drill):
        print('chocaste')
        sound = pygame.mixer.Sound(os.path.join(self.dir_sound, 'drill.wav'))
        sound.play()
        drill.kill()

    def delete_collided_cookie(self, cookie):
        print('galleta')
        sound = pygame.mixer.Sound(os.path.join(self.dir_sound, 'cookie.wav'))
        sound.play()
        cookie.kill()

    def delete_elements(self, elements):
        for element in elements:
            if element.rect.top > HEIGHT - 30:
                element.kill()

    def stop(self):
        print('coli')