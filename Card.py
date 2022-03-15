import pygame

CARD_WIDTH = 100
CARD_HEIGHT = 150


class Card():
    def __init__(self, name, description, type) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.description = description
        self.type = type

    def get_line(self):
        return f"{self.name}: {self.description}"
