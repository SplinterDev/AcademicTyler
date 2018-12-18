import pygame
from pygame.color import Color
from constants import *

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


        self._click_cb = {
            Mouse.BUTTON1: None,
            Mouse.BUTTON2: None,
            Mouse.BUTTON3: None,
        }

    def draw(self):
        self._surface.fill(self._background)
        for view in self._subviews:
            view.draw()
            self.blit(view)

    def printViewTree(self):
        print(self)
        if len(self._subviews) > 0:
            for subview in self._subviews:
                subview.printViewTree()

    # Recursively iterates through all subviews until the clicked leaf (view)
    # is found and returns its instance.
    def getClickedInstance(self, mouse_pos):
        # Does this view has subviews?
        if len(self._subviews) > 0:
            for s in self._subviews: # For each subview
                if s.getAbsRect().collidepoint(mouse_pos): # Was the subview clicked?
                    return s.getClickedInstance(mouse_pos) # It's his problem now

        return self

    # blit receives a View
    def blit(self, view):
        self._surface.blit(view.getSurface(), view.getRelTopLeft())

    def onClick(self, mouse_btns):
        # python's enum is dumb
        if mouse_btns[Mouse.BUTTON1.value] and self._click_cb[Mouse.BUTTON1]:
            self._click_cb[Mouse.BUTTON1]()
        if mouse_btns[Mouse.BUTTON2.value] and self._click_cb[Mouse.BUTTON2]:
            self._click_cb[Mouse.BUTTON2]()
        if mouse_btns[Mouse.BUTTON3.value] and self._click_cb[Mouse.BUTTON3]:
            self._click_cb[Mouse.BUTTON3]()
        # for btn in mouse_btns:
        #     try:
        #         self._click_cbs[btn]()
        #     except Exception:
        #         pass

    def addSubView(self, view):
        self._subviews.append(view)

    def move(self, increments):
        new_x = self.rel_pos[0] + increments[0]
        new_y = self.rel_pos[1] + increments[1]
        self.rel_pos = (new_x, new_y)


    # GETTERS AND SETTERS
    @property
    def rel_pos(self):
        return self._rel_rect.topleft

    @rel_pos.setter
    def rel_pos(self, pos):
        self._rel_rect.topleft = pos

        if self._parent:
            abs_x = pos[0] + self._parent.getAbsRect().x
            abs_y = pos[1] + self._parent.getAbsRect().y
        else:
            abs_x = pos[0]
            abs_y = pos[1]
        self._abs_rect.topleft = (abs_x, abs_y)

    def getAbsRect(self):
        return self._abs_rect

    def getRelRect(self):
        return self._rel_rect

    def getRelTopLeft(self):
        return self._rel_rect.topleft

    def getSurface(self):
        return self._surface

    def getSize(self):
        return _rect.size

    def setClickCallback(self, mouse_btn, cb_fn):
        self._click_cb[mouse_btn] = cb_fn

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

        self.subviews_dict = {}
        self.createExampleSubviews()

    def createExampleSubviews(self):
        size = (WIDTH/2., HEIGHT/2.)
        rel_pos = (0, 0)
        self.subviews_dict[0] = View(size, rel_pos, self, "chocolate", debug_name="topleft")

        rel_pos = (WIDTH/2., 0)
        self.subviews_dict[1] = View(size, rel_pos , self, "darkolivegreen1", debug_name="topright")

        rel_pos = (WIDTH*0.25, HEIGHT/2.)
        self.subviews_dict[2] = View(size, rel_pos , self, "darksalmon", debug_name="midbottom")

        View((100,100), (50,50), self.subviews_dict[1], "dodgerblue1", debug_name="sub topleft")
        View((100,100), (150,50), self.subviews_dict[1], "darkorchid1", debug_name="sub topright")
        last_view = View((300,250), (50,50), self.subviews_dict[2], "deeppink1", debug_name="last_view")

        self.subviews_dict['btn'] = View((100,100), (25,25), last_view, "firebrick2", debug_name="btn")

        self.printViewTree()

    def setClickCallback(self, view_name, mouse_btn, cb_fn):
        self.subviews_dict[view_name].setClickCallback(mouse_btn, cb_fn)

    def handleMouseEvents(self, mouse_pos, mouse_btns):
        if 1 in mouse_btns:
            self.getClickedInstance(mouse_pos).onClick(mouse_btns)

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
