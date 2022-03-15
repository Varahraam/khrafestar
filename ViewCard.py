import pygame

from Component import Component
from Card import Card
from PageHandler import PageId


CARD_WIDTH = 100
CARD_HEIGHT = 150


class ViewCard(Component, pygame.sprite.Sprite):
    def __init__(self, game, card, position) -> None:
        pygame.sprite.Sprite.__init__(self)
        Component.__init__(self, position, [CARD_WIDTH, CARD_HEIGHT])
        self.card = card
        self.game = game
        image = pygame.image.load(self.card.image_path).convert_alpha()
        image = pygame.transform.scale(image, self.size)
        self.image = image
        self.type = type
        self.game.screen.blit(self.image, self.position)

    def update(self, event):
        if self.is_clicked(event):
            self.game.set_page_info(PageId.CARD, card=self.card)
