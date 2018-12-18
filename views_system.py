import pygame
from pygame.color import Color
from constants import WIDTH, HEIGHT



class VisualElement:

    def __init__(self, size, rel_pos=(0,0), parent=None):
        # receives two tuples of int
        self._surface = pygame.Surface(size)
        self._parent = parent
        self._rel_rect = pygame.Rect(rel_pos, size)
        if parent:
            abs_left = rel_pos[0] + parent.getAbsRect().left
            abs_top  = rel_pos[1] + parent.getAbsRect().top

        else:
            abs_left = rel_pos[0]
            abs_top  = rel_pos[1]
        self._abs_rect = pygame.Rect((abs_left, abs_top), size)

    def getAbsRect(self):
        return self._abs_rect

    def getRelRect(self):
        return self._rel_rect

    def getRelTopLeft(self):
        return self._rel_rect.topleft

    # blit receives a VisualElement
    def blit(self, vis_elem):
        self._surface.blit(vis_elem.getSurface(), vis_elem.getRelTopLeft())

    def getSurface(self):
        return self._surface

    def getSize(self):
        return _rect.size



class MainView(VisualElement):
    def __init__(self, size=(WIDTH, HEIGHT), window_caption="Tyler"):
        # Calls constructor of parent class
        super().__init__(size)

        # Creates the screen surface. Anything draw on this appears on-screen
        # Since this is the MainView, we define the _surface as the screen surface.
        self._surface = pygame.display.set_mode(size)

        # Title for the window
        pygame.display.set_caption(window_caption)

        self._subviews = []
        self.createExampleSubviews()

    def createExampleSubviews(self):
        size = (WIDTH/2., HEIGHT/2.)
        rel_pos = (0, 0)
        topleft = GenericView(size, rel_pos, self, "chocolate")
        self._subviews.append(topleft)

        rel_pos = (WIDTH/2., 0)
        topright = GenericView(size, rel_pos , self, "chocolate1")
        self._subviews.append(topright)

        rel_pos = (WIDTH*0.25, HEIGHT/2.)
        midbottom = GenericView(size, rel_pos , self, "chocolate2")
        self._subviews.append(midbottom)

    def draw(self):
        for view in self._subviews:
            view.draw()
            self.blit(view)

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


