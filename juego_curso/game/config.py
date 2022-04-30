import random

WIDTH = 800
HEIGHT = 600

TITLE = 'See the light'

BACKGROUND_COLOR = (136, 216, 192 )
TRANSPARENT = (125, 125, 125)
GREEN = (0, 128, 0)
RED = (125, 0, 0)
BLUE = (0, 0, 125)

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