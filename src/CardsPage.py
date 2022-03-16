import pygame

from Component import Component
from Card import Card, CardTypes
from ViewCard import ViewCard, CARD_HEIGHT, CARD_WIDTH
from Colors import Colors


class CardsPage(Component):
    def __init__(self, game, position, size, cards, page_name) -> None:
        Component.__init__(self, position, size)
        self.game = game
        self.cards_in_row = size[0] // CARD_WIDTH
        self.cards = cards
        self.components = []
        self.page_name = page_name
        self.init_components_list()
        self.draw_to_board()

    def update(self, event):
        for componenet in self.components:
            componenet.update(event)

    def init_components_list(self):
        row = 0
        for i, card in enumerate(self.cards):
            row = (i // self.cards_in_row) + 1
            self.components.append(
                ViewCard(
                    self.game,
                    card,
                    [
                        self.position[0] + ((i % self.cards_in_row) * CARD_WIDTH),
                        self.position[1] + (row * CARD_HEIGHT),
                    ],
                )
            )
    
    def draw_to_board(self):
        TEXT_WIDTH = 400
        font = pygame.font.Font("freesansbold.ttf", 55)
        age = font.render(
            f"Viewing {self.page_name} cards", True, Colors.BLACK
        )
        age = pygame.transform.scale(
            age, [TEXT_WIDTH, CARD_HEIGHT - 60]
        )

        self.game.screen.blit(age, [self.position[0] + (self.size[0] // 2) - 200, self.position[1] + 30])

