from pygame.locals import *
from enum import Enum

WIDTH  = 1024
HEIGHT = 576
HUD_HEIGHT = 150

MAP_SPEED = 5

BACKGROUND_COLOR = "#0C0C0C"

class Mouse(Enum):
    BUTTON1 = 0
    BUTTON2 = 1
    BUTTON3 = 2