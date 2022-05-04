import os
from pickle import TRUE
import pygame
import sys
import random
from pathlib import Path

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
        self.dir_images = os.path.join(self.dir, 'sources/sprites/')

        self.font = pygame.font.match_font(FONT)

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.playing = True
        self.score = 0
        self.level = 0
        self.lives = LIVES
        self.background = pygame.image.load(os.path.join(self.dir_images, 'background.png'))
        self.start_score(self.score)
        self.generate_elements()
        self.run()

    def start_score(self, score):
        print('la puntuación actual es de:', score)
        SCORE_DIRECTORY.write_text(str(score))

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top, self.dir_images)

        # Ajustar margen de aparición en lado derecho
        # self.drill = Drill(random.randrange(100, WIDTH-100), 0)

        self.sprites = pygame.sprite.Group()
        self.drills = pygame.sprite.Group()
        self.cookies = pygame.sprite.Group()
        
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.generate_drills()
        
    def generate_drills(self):
        top_last_position = -100
        if len(self.drills) == 0:
            for drill in range(0, MAX_DRILLS):
                left_random = DRILLS_GRID * random.randrange(1, 15)

                drill = Drill(left_random, top_last_position, self.dir_images)

                random_gap_drills = random.randrange(100, DRILLS_GAP)
                top_last_position = drill.rect.top - random_gap_drills

                self.sprites.add(drill)
                self.drills.add(drill)

            self.level += 1
            self.generate_cookies()

    def generate_cookies(self):
        top_last_position = -800
        if len(self.cookies) == 0:
            for cookie in range(0, MAX_COOKIES):
                left_random = DRILLS_GRID * random.randrange(1, 15)

                cookie = Cookie(left_random, top_last_position, self.dir_images)

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

        if key[pygame.K_SPACE] and not self.playing:
            self.new()

        # Se llama aquí porque no se actualiza la posición con update() en el archivo Drill
        # self.drill.update_pos()


    def draw(self):
        self.surface.blit(self.background, (0,0))
        self.sprites.draw(self.surface)
        self.draw_text()        
        pygame.display.flip()

    def update(self):
        if self.playing:
            # Ejecuta los métodos update de los sprites
            self.sprites.update()

            drill = self.player.collide_with(self.drills)

            if drill:
                self.delete_collided_drill(drill)

            cookie = self.player.collide_with(self.cookies)

            if cookie:
                self.update_score()
                self.read_score()
                self.delete_collided_cookie(cookie)

            self.delete_elements(self.drills)
            self.delete_elements(self.cookies)
            self.generate_drills()
            self.generate_cookies()

    def update_score(self):
        self.score += 1
        SCORE_DIRECTORY.write_text(str(self.score))

    def delete_collided_drill(self, drill):
        self.lost_live()
        sound = pygame.mixer.Sound(os.path.join(self.dir_sound, 'drill.wav'))
        sound.play()
        drill.kill()

    def lost_live(self):
        self.lives -= 1
        
        # Código para mostrar una vida menos
        print('tienes', self.lives, 'vidas')

        # Código para terminar el juego
        if self.lives == 0:
            self.stop()

    def delete_collided_cookie(self, cookie):
        # print('galleta')
        sound = pygame.mixer.Sound(os.path.join(self.dir_sound, 'cookie.wav'))
        sound.play()
        # score = self.read_score(SCORE_DIRECTORY)
        cookie.kill()

    def delete_elements(self, elements):
        for element in elements:
            if element.rect.top > HEIGHT - 30:
                element.kill()

    def read_score(self):
        if SCORE_DIRECTORY.exists() and SCORE_DIRECTORY.name == 'score.txt':
            print(SCORE_DIRECTORY.read_text())

    def stop_elements(self, elements):
        for element in elements:
            element.stop()

    def stop(self):
        self.player.stop()
        self.stop_elements(self.drills)
        self.stop_elements(self.cookies)
        self.playing = False
    
    def score_format(self):
        return 'Score : {}'.format(self.score)

    def level_format(self):
        return 'Level : {}'.format(self.level)

    def lives_format(self):
        contador = ''
        for live in range(self.lives):
            contador += ' x '
        return 'Lives: {}'.format(contador)

    def draw_text(self):
        self.display_text( self.score_format(), FONT_SIZE, BLACK, WIDTH // 2, POS_Y)
        self.display_text( self.level_format(), FONT_SIZE, BLACK, 100, POS_Y)
        self.display_text( self.lives_format(), FONT_SIZE, BLACK, (WIDTH - 180), POS_Y, False)

        if not self.playing:
            self.display_text('Perdiste', FONT_SIZE + 40, BLACK, WIDTH // 2, HEIGHT // 2 - 20)
            self.display_text('Presiona la BARRA DE ESPACIO para volver a jugar', FONT_SIZE - 10, BLACK, WIDTH // 2, HEIGHT // 2 + 50)

    def display_text(self, text, size, color, pos_x, pos_y, align_center = True):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()

        if align_center:
            rect.midtop = (pos_x, pos_y)
        else:
            rect.x = pos_x
            rect.y = pos_y

        self.surface.blit(text, rect)

    def menu(self):
        self.surface.fill(MENU_COLOR)
        self.display_text('Presiona una tecla', FONT_SIZE, WHITE, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        self.wait()

    def wait(self):
        wait = TRUE

        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    wait = False