import pygame
from pygame.color import Color

class VisualElement:

    def __init__(self, size, relative_pos=(0,0), parent=None):
        # receives two tuples of int
        self._surface = pygame.Surface(size)
        self._parent = parent
        self._rect = pygame.Rect((0,0), size)

        def blit(self, surf, relative_pos):
            self._surface.blit(surf, relative_pos)

        def getSurface(self):
            return self._surface

        def getSize(self):
            return _rect.size



class MainView(VisualElement):
    def __init__(self, size=(1024, 576), window_caption="Tyler"):
        # Calls constructor of parent class
        super().__init__(size)

        # Creates the screen surface. Anything draw on this appears on-screen
        # Since this is the MainView, we define the _surface as the screen surface.
        self._surface = pygame.display.set_mode(size)

        # Title for the window
        pygame.display.set_caption(window_caption)

        self._subviews = []


    def draw(self):
        for view in self._subviews:
            view.draw()

        pygame.display.flip()

    def quit(self):
        self.run = False
        # https://stackoverflow.com/questions/19882415/closing-pygame-window
        print("View is quitting")
        pygame.display.quit()

class GenericView(VisualElement):
    def __init__(self, size, relative_pos, parent, color_name):
        # Calls constructor of parent class
        super().__init__(size, relative_pos, parent)
        self._background = Color(color_name)

    def draw(self):
        self._surface.fill(self._background)


