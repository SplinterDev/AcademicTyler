import pygame
from pygame.color import Color
from constants import WIDTH, HEIGHT



class View:
    def __init__(self, size, rel_pos=(0,0), parent=None, color_name="black", debug_name=""):
        # to create a view we need the size as a tuple of int
        # rel_pos is the topleft relative to the parent
        # (MainView doesn't have a parent)
        # color_name is used when the default draw method is used
        self._surface = pygame.Surface(size)
        self._parent = parent

        # _rel_rect stores the position relative to the parent
        # _abs_rect stores the position relative to the window
        self._rel_rect = pygame.Rect(rel_pos, size)
        if parent:
            abs_x = rel_pos[0] + parent.getAbsRect().x
            abs_y = rel_pos[1] + parent.getAbsRect().y
            parent.addSubView(self)
        else:
            abs_x = rel_pos[0]
            abs_y = rel_pos[1]
        self._abs_rect = pygame.Rect((abs_x, abs_y), size)

        self._subviews = []
        self._background = Color(color_name)
        self._debug_name = debug_name

    def draw(self):
        self._surface.fill(self._background)
        for view in self._subviews:
            view.draw()
            self.blit(view)

    def addSubView(self, view):
        self._subviews.append(view)

    def getAbsRect(self):
        return self._abs_rect

    def getRelRect(self):
        return self._rel_rect

    def getRelTopLeft(self):
        return self._rel_rect.topleft

    # blit receives a View
    def blit(self, view):
        self._surface.blit(view.getSurface(), view.getRelTopLeft())

    def getSurface(self):
        return self._surface

    def getSize(self):
        return _rect.size

    def printViewTree(self):
        print(self)
        if len(self._subviews) > 0:
            for subview in self._subviews:
                subview.printViewTree()

    def __str__(self):
        return "View {} at {}(abs)".format(self._debug_name, self._abs_rect)



class MainView(View):
    def __init__(self, size=(WIDTH, HEIGHT), window_caption="Tyler"):
        # Calls constructor of parent class
        super().__init__(size)

        # Creates the screen surface. Anything draw on this appears on-screen
        # Since this is the MainView, we define the _surface as the screen surface.
        self._surface = pygame.display.set_mode(size)

        # Title for the window
        pygame.display.set_caption(window_caption)

        self.createExampleSubviews()

    def createExampleSubviews(self):
        size = (WIDTH/2., HEIGHT/2.)
        rel_pos = (0, 0)
        topleft = View(size, rel_pos, self, "chocolate", debug_name="topleft")

        rel_pos = (WIDTH/2., 0)
        topright = View(size, rel_pos , self, "darkolivegreen1", debug_name="topright")

        rel_pos = (WIDTH*0.25, HEIGHT/2.)
        midbottom = View(size, rel_pos , self, "darksalmon", debug_name="midbottom")

        View((100,100), (50,50), topleft, "dodgerblue1", debug_name="sub topleft")
        View((100,100), (150,50), topright, "darkorchid1", debug_name="sub topright")
        last_view = View((200,150), (50,50), midbottom, "deeppink1", debug_name="last_view")

        Button((100,100), print_button, (25,25), last_view, "firebrick2", debug_name="button")

        self.printViewTree()

    def handleMouseEvents(self, mouse_pos, mouse_btns):
        if 1 in mouse_btns:
            print("Mouse status: {} at {}".format(mouse_btns, mouse_pos))




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

class Button(View):
    def __init__(self, size, callback_fn, rel_pos=(0,0), parent=None, 
                 color_name="black", debug_name=""):
        super().__init__(size, rel_pos, parent, color_name, debug_name)
        self._callback_fn = callback_fn

    def onClick(self, *args):
        self._callback_fn(*args)


def print_button(btn):
    print("Clicked {} button at {}.".format(btn, btn.getAbsRect()))

