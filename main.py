import pygame
from Abilities import Abilities
from BattleCards import BattleCards
from Deck import Deck
from Card import CARD_WIDTH, CARD_HEIGHT

from Player import Player
from Colors import Colors


class Board:
    WIDTH = 1920
    HEIGHT = 1080

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
        self.player = Player()
        self.components = []
        # self.components.append(
        #     Deck(
        #         self.screen,
        #         [self.WIDTH - CARD_WIDTH - 20, 20],
        #         [CARD_WIDTH, CARD_HEIGHT],
        #         "Deck.png",
        #     )
        # )
        # self.components.append(Abilities(self.screen, [500, 200], [100, 300]))
        # self.components.append(BattleCards(self.screen, [20, self.HEIGHT - CARD_HEIGHT - 20]))
        # self.c
        self.screen.fill(Colors.GRAY)
        pygame.draw.line(self.screen, Colors.BLACK, [self.WIDTH // 3, 0], [self.WIDTH // 3, self.HEIGHT])
        pygame.draw.line(self.screen, Colors.BLACK, [2 * (self.WIDTH // 3), 0], [2 * (self.WIDTH // 3), self.HEIGHT])
        pygame.draw.line(self.screen, Colors.BLACK, [self.WIDTH // 2, self.HEIGHT // 4], [self.WIDTH // 2, 3 * (self.HEIGHT // 4)])
        pygame.draw.line(self.screen, Colors.BLACK, [self.WIDTH // 3, self.HEIGHT // 2], [2 * (self.WIDTH // 3), self.HEIGHT // 2])
        
        pygame.draw.line(self.screen, Colors.BLACK, [self.WIDTH // 3, self.HEIGHT // 4], [2 * (self.WIDTH // 3), self.HEIGHT // 4])
        pygame.draw.line(self.screen, Colors.BLACK, [self.WIDTH // 3, 3 * (self.HEIGHT // 4)], [2 * (self.WIDTH // 3), 3 * (self.HEIGHT // 4)])

        pygame.draw.line(self.screen, Colors.BLACK, [0, self.HEIGHT // 5],       [self.WIDTH // 3, (self.HEIGHT // 5)])
        pygame.draw.line(self.screen, Colors.BLACK, [0, 2 * (self.HEIGHT // 5)], [self.WIDTH // 3, 2 * (self.HEIGHT // 5)])
        pygame.draw.line(self.screen, Colors.BLACK, [0, 3 * (self.HEIGHT // 5)], [self.WIDTH // 3, 3 * (self.HEIGHT // 5)])
        pygame.draw.line(self.screen, Colors.BLACK, [0, 4 * (self.HEIGHT // 5)], [self.WIDTH // 3, 4 * (self.HEIGHT // 5)])

        pygame.draw.line(self.screen, Colors.BLACK, [2 * (self.WIDTH // 3), self.HEIGHT // 5],       [self.WIDTH, (self.HEIGHT // 5)])
        pygame.draw.line(self.screen, Colors.BLACK, [2 * (self.WIDTH // 3), 2 * (self.HEIGHT // 5)], [self.WIDTH, 2 * (self.HEIGHT // 5)])
        pygame.draw.line(self.screen, Colors.BLACK, [2 * (self.WIDTH // 3), 3 * (self.HEIGHT // 5)], [self.WIDTH, 3 * (self.HEIGHT // 5)])
        pygame.draw.line(self.screen, Colors.BLACK, [2 * (self.WIDTH // 3), 4 * (self.HEIGHT // 5)], [self.WIDTH, 4 * (self.HEIGHT // 5)])

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
