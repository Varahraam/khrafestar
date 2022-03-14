import pygame
from Abilities import Abilities
from BattleCards import BattleCards
from Deck import Deck
from Card import CARD_WIDTH, CARD_HEIGHT

from Player import Player
from Colors import Colors


class Board:
    WIDTH = 1024
    HEIGHT = 768

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
        self.player = Player()
        self.components = []
        self.components.append(
            Deck(
                self.screen,
                [self.WIDTH - CARD_WIDTH - 20, 20],
                [CARD_WIDTH, CARD_HEIGHT],
                "Deck.png",
            )
        )
        self.components.append(Abilities(self.screen, [500, 200], [100, 300]))
        self.components.append(BattleCards(self.screen, [20, self.HEIGHT - CARD_HEIGHT - 20]))
        # self.c
        self.screen.fill(Colors.GRAY)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for component in self.components:
                component.update(event)

    def run_game(self):
        while True:
            self.handle_events()
            pygame.display.update()


if __name__ == "__main__":
    Board().run_game()
