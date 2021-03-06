from view_system import *
import pygame
from random import sample
from constants import *

class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()

        self.mainView = MainView()
        self.mainView.setClickCallback('render', Mouse.BUTTON1, lambda:print("raindeer"))
        self.mainView.setClickCallback('hud', Mouse.BUTTON1, lambda:print("hudson"))

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

        self.mainView.handleMouseEvents(mouse_pos, mouse_btns)

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
