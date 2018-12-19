from view_system import *
import pygame
from random import sample
from constants import *

class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()

        self._mainView = MainView()
        self._mainView.setClickCallback("render", Mouse.BUTTON1, lambda:print("raindeer"))
        self._mainView.setClickCallback("hud", Mouse.BUTTON1, lambda:print("hudson"))

        self._clock = pygame.time.Clock()

    def handleInput(self):
        # Updates event queue and checks for QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Check for other key presses
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_UP]:
            self._mainView.moveMap(K_UP)
        if keys_pressed[K_RIGHT]:
            self._mainView.moveMap(K_RIGHT)
        if keys_pressed[K_DOWN]:
            self._mainView.moveMap(K_DOWN)
        if keys_pressed[K_LEFT]:
            self._mainView.moveMap(K_LEFT)



        # Check for mouse events
        mouse_btns = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        self._mainView.handleMouseEvents(mouse_pos, mouse_btns)

    def run(self):
        self.run = True

        while self.run:
            # Handle inputs
            self.handleInput()

            # Update Game States

            # Render Screen
            self._mainView.draw()

            self._clock.tick(60)

        # Loop has finished, let's end the game
        self._mainView.quit()

        pygame.quit()

if __name__ == "__main__":
    game = Game()

    game.run()
