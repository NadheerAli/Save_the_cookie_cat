import pygame
import sys
import random

from .config import * 
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
        self.clock.tick(FPS)

        self.background = pygame.image.load(SPRITES_DIRECTORY / 'background.png')

        self.font = pygame.font.match_font(FONT)
        self.play_theme()

    def play_theme(self):
        pygame.mixer.music.load(SOUNDS_DIRECTORY / 'theme.mp3')
        pygame.mixer.music.set_volume(GAME_VOL)
        pygame.mixer.music.play(-1, 0.0)

    def start(self):
        self.start_menu()
        self.new()

    def new(self):
        self.playing = True
        self.score = 0
        self.level = 0
        self.prev_score = int(self.read_score())
        self.fall_speed = FALL_SPEED
        self.lives = LIVES
        self.generate_elements()
        self.run()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def generate_elements(self):
        self.player = Player(100, HEIGHT - 30)

        self.sprites = pygame.sprite.Group()
        self.drills = pygame.sprite.Group()
        self.cookies = pygame.sprite.Group()
        
        self.sprites.add(self.player)
        self.generate_drills()
        
    def generate_drills(self):
        drill_initial_pos_y = -100

        if len(self.drills) == 0:
            for drill in range(0, DRILLS_PER_LEVEL):
                left_random = COLUMN_FOR_OBJECTS_FALL * random.randrange(0, 15)

                drill = Drill(left_random, drill_initial_pos_y, self.fall_speed)

                random_gap_drills = random.randrange(100, DRILLS_GAP)
                drill_initial_pos_y = drill.rect.top - random_gap_drills

                self.sprites.add(drill)
                self.drills.add(drill)

            self.update_level()
            self.generate_cookies()

    def update_level(self):
        self.level += 1
        if(self.level % LEVEL_TO_INCREASE_SPEED == 0):
            self.fall_speed += SPEED_INCREASE

    def generate_cookies(self):
        top_last_position = -800
        if len(self.cookies) == 0:
            for cookie in range(0, COOKIES_PER_LEVEL):
                left_random = COLUMN_FOR_OBJECTS_FALL * random.randrange(0, 15)

                cookie = Cookie(left_random, top_last_position, self.fall_speed)

                random_gap_cookies = random.randrange(400, COOKIES_GAP)
                top_last_position = cookie.rect.top - random_gap_cookies

                self.sprites.add(cookie)
                self.cookies.add(cookie)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        if key[pygame.K_f] and not self.playing:
            self.start()
            
        if key[pygame.K_SPACE] and not self.playing:
            self.new()

        if key[pygame.K_LEFT]:
            self.player.update_pos_left()

        if key[pygame.K_RIGHT]:
            self.player.update_pos_right()

    def draw(self):
        self.surface.blit(self.background, (0,0))
        self.sprites.draw(self.surface)
        self.draw_text()        
        pygame.display.flip()

    def update(self):
        if self.playing:
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

    def save_score(self):
        if SCORE_DIRECTORY.exists() and SCORE_DIRECTORY.name == 'score.txt':

            if self.score > self.prev_score:
                new_score = str(self.score)

                SCORE_DIRECTORY.write_text(new_score)

    def read_score(self):
        if SCORE_DIRECTORY.exists() and SCORE_DIRECTORY.name == 'score.txt':
            content = SCORE_DIRECTORY.read_text()
            if content == '':
                SCORE_DIRECTORY.write_text('0')

            return SCORE_DIRECTORY.read_text()

    def delete_collided_drill(self, drill):
        self.lost_live()
        sound = pygame.mixer.Sound(SOUNDS_DIRECTORY / 'drill.wav')
        sound.play()
        drill.kill()

    def lost_live(self):
        self.lives -= 1
        
        if self.lives == 0:
            self.save_score()
            self.stop()

    def delete_collided_cookie(self, cookie):
        sound = pygame.mixer.Sound(SOUNDS_DIRECTORY / 'cookie.wav')
        sound.play()
        cookie.kill()

    def delete_elements(self, elements):
        for element in elements:
            if element.rect.top > HEIGHT - 30:
                element.kill()   

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
            self.end_menu()

    def show_lose_message(self):
            self.display_text(str(self.score), FONT_SIZE + 40, BLACK, 215 , 240)
            self.display_text(str(self.prev_score), FONT_SIZE + 40, BLACK, 580 , 240)

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

    def start_menu(self):
        wait = True

        menu_img = pygame.image.load(SPRITES_DIRECTORY / 'start_menu.jpg')
        rect = menu_img.get_rect()
        rect.center = (WIDTH // 2, HEIGHT // 2)

        actual_menu = 'start'
        show_score = True

        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

                key = pygame.key.get_pressed()

                if actual_menu == 'start':
                    if key[pygame.K_RIGHT]:
                        menu_img = pygame.image.load(SPRITES_DIRECTORY / 'controls_menu.jpg')
                        actual_menu = 'controls'
                        show_score = False                        

                    if key[pygame.K_LEFT]:
                        menu_img = pygame.image.load(SPRITES_DIRECTORY / 'credits.jpg')
                        actual_menu = 'credits'
                        show_score = False                        

                    if key[pygame.K_SPACE]:
                        wait = False

                if actual_menu == 'controls':
                    if key[pygame.K_LEFT]:
                        menu_img = pygame.image.load(SPRITES_DIRECTORY / 'start_menu.jpg')
                        actual_menu = 'start'
                        show_score = True

                    if key[pygame.K_SPACE]:
                        wait = False

                if actual_menu == 'credits':
                    if key[pygame.K_RIGHT]:
                        menu_img = pygame.image.load(SPRITES_DIRECTORY / 'start_menu.jpg')
                        actual_menu = 'start'
                        show_score = True

            self.surface.blit(menu_img, rect)
            if show_score:
                self.show_higher_score()
            pygame.display.update()

    def end_menu(self):
        wait = True

        menu_img = self.get_end_menu_img()

        rect = menu_img.get_rect()
        rect.center = (WIDTH // 2, HEIGHT // 2)

        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    wait = False

                if key[pygame.K_f]:
                    wait = False

            self.surface.blit(menu_img, rect)
            self.show_lose_message()
            pygame.display.update()

    def get_end_menu_img(self):
        menu_img = ''
        if self.score > self.prev_score:
            menu_img = pygame.image.load(SPRITES_DIRECTORY / 'end_menu_new_record.jpg')
        elif self.score < self.prev_score:
            menu_img = pygame.image.load(SPRITES_DIRECTORY / 'end_menu_lower_score.jpg')
        else:
            menu_img = pygame.image.load(SPRITES_DIRECTORY / 'end_menu_higher_score.jpg')

        return menu_img

    def show_higher_score(self):
        higher_score = str(self.read_score())
        self.display_text(higher_score, FONT_SIZE + 40, BLACK, 560 , 245)