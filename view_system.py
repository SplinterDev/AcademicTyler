import pygame
from pygame.color import Color
from constants import *

class View:
    def __init__(self, size=(0,0), rel_pos=(0,0), parent=None,
                 color_name="black", debug_name=""):
        # to create a view we need the size as a tuple of int
        # rel_pos is the topleft relative to the parent
        # (MainView doesn't have a parent)
        # color_name is used when the default draw method is used
        self._surface = pygame.Surface(size)
        self._parent = parent

        # _rel_rect stores the position relative to the parent
        # _abs_rect stores the position relative to the window
        self._rel_rect = pygame.Rect(rel_pos, size)

        self._setAbsRect()
        if parent:
            parent.addSubView(self)

        self._subviews = []
        self._background_color = Color(color_name)
        self._image = None
        self._debug_name = debug_name

        self._click_cb = {
            Mouse.BUTTON1: None,
            Mouse.BUTTON2: None,
            Mouse.BUTTON3: None,
        }

    def _setAbsRect(self):
        # not a setter! Misguiding name, I know.
        # calculates absolute position based on parent's position
        if self._parent:
            abs_x = self.rel_pos[0] + self._parent.getAbsRect().x
            abs_y = self.rel_pos[1] + self._parent.getAbsRect().y
        else:
            abs_x = self.rel_pos[0]
            abs_y = self.rel_pos[1]
        self._abs_rect = pygame.Rect((abs_x, abs_y), self._rel_rect.size)

    def loadImage(self, img_path):
        self._image    = img_path
        self._surface  = pygame.image.load(img_path)
        self._rel_rect.topleft = self.rel_pos
        self._rel_rect.size    = self._surface.get_size()
        self._setAbsRect()
    
    def clearImage(self):
        self._image = None
        self._surface = pygame.Surface(self._surface.get_size())

    def resize(self, new_size):
        self._rel_rect.size = new_size
        self._surface = pygame.transform.scale(self._surface, new_size)

        self._setAbsRect()


    def draw(self):
        if not self._image:
            self._surface.fill(self._background_color)

        for view in self._subviews:
            view.draw()
            self.blit(view)

    def printViewTree(self):
        print(self)
        if len(self._subviews) > 0:
            for subview in self._subviews:
                subview.printViewTree()

    # blit receives a View
    def blit(self, view):
        self._surface.blit(view.getSurface(), view.rel_pos)

    # Recursively iterates through all subviews until the clicked leaf (view)
    # is found and returns its instance.
    def getClickedInstance(self, mouse_pos):
        # Does this view has subviews?
        if len(self._subviews) > 0:
            for s in self._subviews: # For each subview
                if s.getAbsRect().collidepoint(mouse_pos): # Was the subview clicked?
                    return s.getClickedInstance(mouse_pos) # Not my problem now
        return self

    def onClick(self, mouse_btns):
        # python's enum is dumb
        if mouse_btns[Mouse.BUTTON1.value] and self._click_cb[Mouse.BUTTON1]:
            self._click_cb[Mouse.BUTTON1]()
        if mouse_btns[Mouse.BUTTON2.value] and self._click_cb[Mouse.BUTTON2]:
            self._click_cb[Mouse.BUTTON2]()
        if mouse_btns[Mouse.BUTTON3.value] and self._click_cb[Mouse.BUTTON3]:
            self._click_cb[Mouse.BUTTON3]()

    # GETTERS AND SETTERS
    # rel_pos doesn't actually exist but shhh...
    @property
    def rel_pos(self):
        return self._rel_rect.topleft

    @rel_pos.setter
    def rel_pos(self, pos):
        self._rel_rect.topleft = pos
        self._setAbsRect()#self._parent)

    # _surface ########################
    def getSurface(self):
        return self._surface

    # parent ##########################
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, p):
        self._parent = p
        self._setAbsRect()
        p.addSubView(self)
    
    # _rel_rect #######################
    def getRelRect(self):
        return self._rel_rect

    # size ############################
    def getSize(self):
        return self._rel_rect.size
    
    # _abs_rect #######################
    def getAbsRect(self):
        return self._abs_rect

    # _subviews #######################
    def addSubView(self, view):
        self._subviews.append(view)

    # _background_color ###############
    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, color_name):
        self._background_color = Color(color_name)

    # _click_cb #######################
    def setClickCallback(self, mouse_btn, cb_fn):
        self._click_cb[mouse_btn] = cb_fn

    # MAGIC METHODS
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
        self.createSubViews()

    def createSubViews(self):
        self.subviews_dict["render"] = RenderView()
        self.subviews_dict["render"].parent = self
        self.subviews_dict["render"].background_color = "palegreen3"

        self.subviews_dict["hud"] = HUDView()
        self.subviews_dict["hud"].parent = self
        self.subviews_dict["hud"].background_color = "royalblue2"

    def subview(self, name):
        return self.subviews_dict[name]

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

    def moveMap(self, direction):
        map_view = self.subview("render").subview("map")
        old_pos = map_view.rel_pos
        if direction == K_UP:
            if old_pos[1]+MAP_SPEED <= 0:
                map_view.rel_pos = (old_pos[0], old_pos[1]+MAP_SPEED)

        if direction == K_RIGHT:
            # max_x is the width of the render minus the width of the map
            max_x = self.subview("render").getSize()[0]-map_view.getSize()[0]
            if old_pos[0]-MAP_SPEED >= max_x:
                map_view.rel_pos = (old_pos[0]-MAP_SPEED, old_pos[1])

        if direction == K_DOWN:
            # max_y is the height of the render minus the height of the map
            max_y = self.subview("render").getSize()[1]-map_view.getSize()[1]
            if old_pos[1]-MAP_SPEED >= max_y:
                map_view.rel_pos = (old_pos[0], old_pos[1]-MAP_SPEED)

        if direction == K_LEFT:
            if old_pos[0]+MAP_SPEED <= 0:
                map_view.rel_pos = (old_pos[0]+MAP_SPEED, old_pos[1])


    def quit(self):
        self.run = False
        # https://stackoverflow.com/questions/19882415/closing-pygame-window
        print("View is quitting")
        pygame.display.quit()

class RenderView(View):
    def __init__(self):
        super().__init__((WIDTH, HEIGHT-HUD_HEIGHT))
        self.subviews_dict = {}
        self.subviews_dict["map"] = View(parent=self)
        self.subviews_dict["map"].background_color = "coral1"
        self.subviews_dict["map"].loadImage("test_img.jpg")
        # self.subviews_dict["map"].clearImage()
        # self.subviews_dict["map"].resize(self.subviews_dict["map"].parent.getSize())

    def subview(self, name):
        return self.subviews_dict[name]


class HUDView(View):
    def __init__(self):
        super().__init__((WIDTH, HUD_HEIGHT),rel_pos=(0, HEIGHT-HUD_HEIGHT))
