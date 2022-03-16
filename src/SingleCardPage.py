import pygame

from Component import Component
from Card import Card, CardTypes
from ViewCard import ViewCard, CARD_HEIGHT, CARD_WIDTH
from Colors import Colors


class SingleCardPage(Component):
    def __init__(self, game, position, size, card) -> None:
        Component.__init__(self, position, size)
        self.game = game
        self.cards_in_row = size[0] // CARD_WIDTH
        self.card = card
        self.components = []
        self.draw_to_board()

    def update(self, event):
        for componenet in self.components:
            componenet.update(event)

    def draw_to_board(self):
        font = pygame.font.Font("freesansbold.ttf", 55)
        name_text = font.render(self.card.get_line(), True, Colors.BLACK)
        type_text = font.render(self.card.type, True, Colors.BLACK)
        # name_text = pygame.transform.scale(name_text, [200,200])
        self.game.screen.blit(
            name_text,
            [
                self.size[0] // 2 - (name_text.get_width() // 2),
                self.size[1] // 2 - (name_text.get_height() // 2),
            ],
        )
        self.game.screen.blit(
            type_text,
            [
                self.size[0] // 2 - (type_text.get_width() // 2),
                self.size[1] // 2 + (name_text.get_height() // 2) + 20,
            ],
        )
