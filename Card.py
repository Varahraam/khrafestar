import pygame


class CardTypes:
    TROOP = "troop"
    BUILDING = "building"
    ABILITY = "ability"


class Card:
    def __init__(self, name, description, type, image_path) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.description = description
        self.type = type
        self.image_path = image_path

    def get_line(self):
        return f"{self.name}: {self.description}"
