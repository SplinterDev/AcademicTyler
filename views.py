import pygame
print("Shut up pygame, community! :(")
from constants import *
from pygame.locals import *
from pygame.color import Color

class View:
    def __init__(self, width, height, anchor_pos):
        self._width  = width
        self._height = height
        self._size   = (self._width, self._height)

        self._anchor_pos = anchor_pos

        self._surface = pygame.Surface((width, height))
        self._rect = self._surface.get_rect()
        self._rect.topleft = anchor_pos

    # we dont need this but it's a nice example
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self._width = val
        self._size  = (self._width, self._height)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val
        self._size   = (self._width, self._height)

    def blitSurface(self, surface, position):
        self._surface.blit(surface, position)

    def getSurface(self):
        return self._surface

    def getRect(self):
        return self._rect

class MainView(View):
    def __init__(self, width=1024, height=576, window_caption="Tyler"):
        # Calls init of parent class, disregard anchor_pos
        super().__init__(width, height, (0, 0))

        # Creates the screen surface. Anything draw on this appears on-screen
        # Since this is the MainView, we define the _surface as the screen surface.
        self._surface = pygame.display.set_mode(self._size)

        self._backgroundColor = BACKGROUND_COLOR

        # Title for the window
        pygame.display.set_caption(window_caption)

        self._hudinf = HUDView(width, 200, (0, height-200))

    def drawSubViews(self):
        self._hudinf.draw()
        self.blitSurface(self._hudinf.getSurface(), self._hudinf._anchor_pos)

    def draw(self):
        self.drawSubViews()

        pygame.display.flip()

    # For now, this handleInput only cares about mouse information.
    # m_info is a tuple of format (BUTTON_PRESSED, POS)
    # TODO This function can certainly be cleaner
    def handleInput(self, m_info):
        mouse_pos = m_info[1]

        print(m_info)

        print("HUDView Rect {}".format(self._hudinf.getRect()))

        if(m_info[0] == 1): # MOUSE LEFT CLICK
            if self._hudinf.getRect().collidepoint(mouse_pos):
                self._hudinf.checkButtonClick(mouse_pos)

    def quit(self):
        self.run = False
        # https://stackoverflow.com/questions/19882415/closing-pygame-window
        print("View is quitting")
        pygame.display.quit()

class HUDView(View):
    def __init__(self, width, height, anchor_pos):
        super().__init__(width, height, anchor_pos)

        self._buttons = [Button((anchor_pos[0], anchor_pos[1], 32, 32), Color('tomato1'), "hur", self.button1),
                         Button((anchor_pos[0] + 32, anchor_pos[1], 32, 32), Color('tomato3'), "hur", self.button1)]

    def checkButtonClick(self, mouse_pos):
        print("[checkButtonClick]")
        print(mouse_pos)
        for b in self._buttons:
            if b.collidepoint(mouse_pos):
                b.onClick()

    def button1(self):
        print("oi")

    def draw(self):
        self._surface.fill(Color("turquoise"))
        
        for b in self._buttons:
            pygame.draw.rect(self._surface, (255, 255, 255), b)

# TODO Figure out the buttons stuff
class Button(Rect):
    def __init__(self, rect_info, color, text, callback_fn):
        super().__init__(*rect_info)

        self._callback_fn = callback_fn
        
        self._color = color
        
        self._text = text

    def onClick(self):
        self._callback_fn()
