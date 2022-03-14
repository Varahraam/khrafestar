from lib2to3 import pygram

import pygame


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (110, 110, 110)
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (0, 120, 0)
    RED = (255, 0, 0)
    LIGHT_RED = (120, 0, 0)


class Board:
    WIDTH = 1024
    HEIGHT = 768

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
        self.screen.fill(Colors.GRAY)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run_game(self):
        while True:
            self.handle_events()
            pygame.display.update()


if __name__ == '__main__':
    Board().run_game()
