import random
from pathlib import Path

LIVES = 3

POS_Y = 20
FONT_SIZE = 30

WIDTH = 800
HEIGHT = 600

TITLE = 'See the light'

BACKGROUND_COLOR = (136, 216, 192 )
TRANSPARENT = (125, 125, 125)
GREEN = (0, 128, 0)
RED = (125, 0, 0)
BLUE = (0, 0, 125)
WHITE = (255, 255, 255)

DRILLS_GAP = 600
COOKIES_GAP = 1000
SURFACE_LEFT_MARGIN = 100
SURFACE_RIGHT_MARGIN = WIDTH - 100

FPS = 60
PLAYER_SPEED = 10
DRILLS_SPEED = 10

MAX_DRILLS = 8
MAX_COOKIES = 5
# Hasta aquí sigue la posibilidad de que aparezcan en un mismo espacio
DRILLS_GRID = int((SURFACE_RIGHT_MARGIN - SURFACE_LEFT_MARGIN) / 10) # 600 - área en el que puede aparacer

# Paths(?)
CURRENT_DIRECTORY = Path.cwd()
PATH = Path(CURRENT_DIRECTORY)
SCORE_DIRECTORY = PATH / 'game/sources/score.txt'

FONT = 'Arial'