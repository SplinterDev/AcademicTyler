import pygame
print("Shut up pygame, community! :(")
from constants import *

class MainView:
    def __init__(self, width=1024, height=576, window_caption="Tyler"):
        # comentarios em ingles ou portugues?
        # lets use @property because yes boi
        # https://www.programiz.com/python-programming/property
        self._width  = width
        self._height = height
        self._size   = (self._width, self._height)

        self._screen = None
        self._backgroundColor = BACKGROUND_COLOR

        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption(window_caption)

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
        self._screen.blit(surface, position)

    def drawTiles(self):
        # to bugando pra gerar uma surface pra cada tile
        # e pra definir o tamanho dos tiles em relação a tela
        # por isso vou fazer desse jeito escroto aqui soh pra ter
        tile_size = 50
        # horizontal lines
        for i in range(0,self._height, tile_size):
            pygame.draw.line(
                self._screen,
                pygame.Color("#FFFFFF"),
                (0, i),
                (self._width, i),
                1
            )
        # vertical lines
        for i in range(0,self._width, tile_size):
            pygame.draw.line(
                self._screen,
                pygame.Color("#FFFFFF"),
                (i, 0),
                (i, self._width),
                1
            )

    def update(self):
        self.drawTiles()

        pygame.display.flip()

    def quit(self):
        self.run = False
        # https://stackoverflow.com/questions/19882415/closing-pygame-window
        print("View is quitting")
        pygame.display.quit()

#############################################################
# this has to go to the controller (that doesn't exist yet) #
#############################################################

if __name__ == '__main__':
    view = View()
    view.init()
    run = True
    while run:
        update(view)
        run = view.run
