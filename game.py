from controllers import *
from models import *
from views import *
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()

        self.mainView = MainView()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            elif event.type == KEYDOWN:
                # is this ugly?
                # is this pretty?
                # who knows man
                # who...
                # knows...
                if event.key == K_a:
                    print("Pressed a.")

    def run(self):
        self.run = True

        while self.run:
            self.mainView.update()

            self.handleInput()

            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()

    game.run()
