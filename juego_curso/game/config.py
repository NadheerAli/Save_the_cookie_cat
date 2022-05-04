import os
import random
from pathlib import Path

LIVES = 3

WIDTH = 800
HEIGHT = 600

TITLE = 'See the light'

BACKGROUND_COLOR = (136, 216, 192 )
# TRANSPARENT = 
GREEN = (0, 128, 0)
RED = (125, 0, 0)
BLUE = (0, 0, 125)
WHITE = (255, 255, 255)
BLACK = (0 ,0 ,0)
MENU_COLOR = (200, 0, 0)

DRILLS_GAP = 300
COOKIES_GAP = 800
SURFACE_MARGIN_LEFT = 0
SURFACE_MARGIN_RIGHT = WIDTH - 70

FPS = 60
PLAYER_SPEED = 10
DRILLS_SPEED = 10

MAX_DRILLS = 8
MAX_COOKIES = 5

# Hasta aquí sigue la posibilidad de que aparezcan en un mismo espacio
DRILLS_GRID = int((SURFACE_MARGIN_RIGHT - SURFACE_MARGIN_LEFT) / 14) # 730 - área en el que puede aparacer

# Paths(?)
CURRENT_DIRECTORY = Path.cwd()
PATH = Path(CURRENT_DIRECTORY)
SCORE_DIRECTORY = PATH / 'game/sources/score.txt'

FONT = 'Arial bold'
POS_Y = 20
FONT_SIZE = 36