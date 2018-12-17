from views_system import *
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()

        self.mainView = MainView()

        self.clock = pygame.time.Clock()

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

        if mouse_btns[0] == True:
            self.mainView.handleInput((1, mouse_pos))

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
