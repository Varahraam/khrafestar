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
        WIDTH_BORDER = 80
        HEIGHT_BORDER = 20
        font = pygame.font.SysFont("notosansmono", 55)
        ghorbanies = font.render(
            f"ghorbani: {self.resources_info[0]}", True, Colors.BLACK
        )
        ghorbanies = pygame.transform.scale(
            ghorbanies, [(self.size[0] // 2) - WIDTH_BORDER, (self.size[1] // 2) - HEIGHT_BORDER]
        )

        farreh1 = font.render(f"farreh1: {self.resources_info[1]}", True, Colors.BLACK)
        farreh1 = pygame.transform.scale(
            farreh1, [(self.size[0] // 2) - WIDTH_BORDER, (self.size[1] // 2) - HEIGHT_BORDER]
        )

        farreh2 = font.render(f"farreh2: {self.resources_info[2]}", True, Colors.BLACK)
        farreh2 = pygame.transform.scale(
            farreh2, [(self.size[0] // 2) - WIDTH_BORDER, (self.size[1] // 2) - HEIGHT_BORDER]
        )

        farreh3 = font.render(f"farreh3: {self.resources_info[3]}", True, Colors.BLACK)
        farreh3 = pygame.transform.scale(
            farreh3, [(self.size[0] // 2) - WIDTH_BORDER, (self.size[1] // 2) - HEIGHT_BORDER]
        )

        self.game.screen.blit(ghorbanies, [self.position[0] + (WIDTH_BORDER // 2), self.position[1] + (HEIGHT_BORDER // 2)])
        self.game.screen.blit(
            farreh1, [self.position[0] + (self.size[0] // 2) + (WIDTH_BORDER // 2), self.position[1] + (HEIGHT_BORDER // 2)]
        )
        self.game.screen.blit(
            farreh2, [self.position[0] + (WIDTH_BORDER // 2), self.position[1] + (self.size[1] // 2) + (HEIGHT_BORDER // 2)]
        )
        self.game.screen.blit(
            farreh3,
            [
                self.position[0] + (self.size[0] // 2) + (WIDTH_BORDER // 2),
                self.position[1] + (self.size[1] // 2) + (HEIGHT_BORDER // 2),
            ],
        )
