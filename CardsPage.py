import pygame

from Component import Component
from Card import Card, CardTypes
from ViewCard import ViewCard, CARD_HEIGHT, CARD_WIDTH


class CardsPage(Component):
    def __init__(self, game, position, size, cards) -> None:
        Component.__init__(self, position, size)
        self.game = game
        self.cards_in_row = size[0] // CARD_WIDTH
        self.cards = cards
        self.components = []
        self.init_components_list()

    def update(self, event):
        for componenet in self.components:
            componenet.update(event)

    def init_components_list(self):
        row = 0
        for i, card in enumerate(self.cards):
            row = i // self.cards_in_row
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
