import pygame

from Component import Component
from Card import Card, CardTypes
from ViewCard import ViewCard, CARD_HEIGHT, CARD_WIDTH
from Colors import Colors


class GameStateComponent(Component):
    def __init__(self, game, position, size, game_info) -> None:
        Component.__init__(self, position, size)
        self.game = game
        self.cards_in_row = size[0] // CARD_WIDTH
        self.game_info = game_info
        self.components = []
        self.draw_to_board()

    def update(self, event):
        for componenet in self.components:
            componenet.update(event)

    def draw_to_board(self):
        font = pygame.font.Font("freesansbold.ttf", 55)
        age = font.render(
            f"Age: {self.game_info[0]}", True, Colors.BLACK
        )
        age = pygame.transform.scale(
            age, [(self.size[0] // 2) - 60, (self.size[1] // 4)]
        )

        self.game.screen.blit(age, [self.position[0] + 30, self.position[1] + (self.size[1] * 3) // 8])

        turn = font.render(
            f"Turn: {self.game_info[1]}", True, Colors.BLACK
        )
        turn = pygame.transform.scale(
            turn, [(self.size[0] // 2) - 60, (self.size[1] // 4)]
        )

        self.game.screen.blit(turn, [self.position[0] + self.size[0] // 2 + 30, self.position[1] + (self.size[1] * 3) // 8])
