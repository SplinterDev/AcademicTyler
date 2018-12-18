from views_system import *
import pygame
from random import sample
from constants import *

class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()

        self.mainView = MainView()
        self.mainView.setClickCallback('btn', Mouse.BUTTON1, self.moveButtonLeft)
        self.mainView.setClickCallback('btn', Mouse.BUTTON2, self.epilepsy)
        self.mainView.setClickCallback('btn', Mouse.BUTTON3, self.moveButtonRight)

        self.clock = pygame.time.Clock()

    # TODO this is just an example function.
    def epilepsy(self):
        self.mainView.subviews_dict['btn']._background = Color(sample(pygame.colordict.THECOLORS.keys(), 1)[0])
        self.mainView.subviews_dict[0]._background = Color(sample(pygame.colordict.THECOLORS.keys(), 1)[0])
        self.mainView.subviews_dict[1]._background = Color(sample(pygame.colordict.THECOLORS.keys(), 1)[0])
        self.mainView.subviews_dict[2]._background = Color(sample(pygame.colordict.THECOLORS.keys(), 1)[0])

    def moveButtonRight(self):
        self.mainView.subviews_dict['btn'].move((5,0))

    def moveButtonLeft(self):
        self.mainView.subviews_dict['btn'].move((-5,0))




    def handleInput(self):
        # Updates event queue and checks for QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        # Check for other key presses
        keys = pygame.key.get_pressed()

        if keys[K_a]:
            print('a')

        # Check for mouse events
        mouse_btns = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        self.mainView.handleMouseEvents(mouse_pos, mouse_btns)

        # if mouse_btns[0] == True:
        #     self.mainView.handleInput((1, mouse_pos))

    def run(self):
        self.run = True

        while self.run:
            # Handle inputs
            self.handleInput()

            # Update Game States

            # Render Screen
            self.mainView.draw()

            self.clock.tick(60)

        # Loop has finished, let's end the game
        self.mainView.quit()

        pygame.quit()

if __name__ == "__main__":
    game = Game()

    game.run()
