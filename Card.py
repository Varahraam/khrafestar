import pygame

CARD_WIDTH = 100
CARD_HEIGHT = 150


class Card(pygame.sprite.Sprite):
    def __init__(self, name, description, type, image_path=None) -> None:
        pygame.sprite.Sprite.__init__(self)
        if (image_path):
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, [CARD_WIDTH, CARD_HEIGHT])
            self.image = image
        self.name = name
        self.description = description
        self.type = type

    def get_line(self):
        return f"{self.name}: {self.description}"

    def draw_to_board(self, screen, position):
        screen.blit(self.image, position + [CARD_WIDTH, CARD_HEIGHT])