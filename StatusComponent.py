import pygame

from Component import Component
from Card import Card, CardTypes
from ViewCard import ViewCard, CARD_HEIGHT, CARD_WIDTH
from Colors import Colors


class StatusComponent(Component):
    def __init__(self, game, position, size, resources_info) -> None:
        Component.__init__(self, position, size)
        self.game = game
        self.cards_in_row = size[0] // CARD_WIDTH
        self.resources_info = resources_info
        self.components = []
        self.draw_to_board()

    def update(self, event):
        for componenet in self.components:
            componenet.update(event)

    def draw_to_board(self):
        font = pygame.font.Font("freesansbold.ttf", 55)
        ghorbanies = font.render(
            f"ghorbani: {self.resources_info[0]}", True, Colors.BLACK
        )
        ghorbanies = pygame.transform.scale(
            ghorbanies, [(self.size[0] // 2) - 40, (self.size[1] // 2) - 20]
        )

        far1 = font.render(f"far1: {self.resources_info[1]}", True, Colors.BLACK)
        far1 = pygame.transform.scale(
            far1, [(self.size[0] // 2) - 40, (self.size[1] // 2) - 20]
        )

        far2 = font.render(f"far2: {self.resources_info[2]}", True, Colors.BLACK)
        far2 = pygame.transform.scale(
            far2, [(self.size[0] // 2) - 40, (self.size[1] // 2) - 20]
        )

        far3 = font.render(f"far3: {self.resources_info[3]}", True, Colors.BLACK)
        far3 = pygame.transform.scale(
            far3, [(self.size[0] // 2) - 40, (self.size[1] // 2) - 20]
        )

        self.game.screen.blit(ghorbanies, self.position)
        self.game.screen.blit(
            far1, [self.position[0] + (self.size[0] // 2), self.position[1]]
        )
        self.game.screen.blit(
            far2, [self.position[0], self.position[1] + (self.size[1] // 2)]
        )
        self.game.screen.blit(
            far3,
            [
                self.position[0] + (self.size[0] // 2),
                self.position[1] + (self.size[1] // 2),
            ],
        )
