from pygame.locals import *
from enum import Enum

WIDTH  = 1024
HEIGHT = 576
HUD_HEIGHT = 150

MAP_SPEED  = 5
ZOOM_SPEED = 0.1
MAX_ZOOM   = 4
MIN_ZOOM   = 1

BACKGROUND_COLOR = "#0C0C0C"

class Zoom(Enum):
    IN  = 0
    OUT = 1

class Mouse(Enum):
    BUTTON1 = 0
    BUTTON2 = 1
    BUTTON3 = 2
    WHEELUP = 3
    WHEELDOWN = 4