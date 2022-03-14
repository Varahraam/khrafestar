from lib2to3 import pygram

import pygame
from Deck import Deck

from Player import Player
from Colors import Colors


class Board:
    WIDTH = 1024
    HEIGHT = 768

    def __init__(self) -> None:
        pygame.init()
        self.player = Player()
        self.screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
        self.deck = Deck(self.screen, [200,300], [100,200], "Deck.png")
        self.screen.fill(Colors.GRAY)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            self.deck.update(event)
            
            
    
    def draw(self):
        pass

    def run_game(self):
        while True:
            self.handle_events()
            pygame.display.update()


if __name__ == '__main__':
    Board().run_game()
