import pygame

from Component import Component
from Card import Card, CardTypes
from ViewCard import ViewCard, CARD_HEIGHT, CARD_WIDTH
from Colors import Colors


class HeroComponent(Component, pygame.sprite.Sprite):
    def __init__(self, game, position, size, hero) -> None:
        Component.__init__(self, position, size)
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image_width_border = 220
        self.image_height_border = 20
        
        image = pygame.image.load(hero.image_path).convert_alpha()
        image = pygame.transform.scale(image, [size[0] - self.image_width_border, 4 * (size[1] // 5) - self.image_height_border])
        self.image = image
        self.cards_in_row = size[0] // CARD_WIDTH
        self.hero = hero
        self.components = []
        self.draw_to_board()

    def update(self, event):
        for componenet in self.components:
            componenet.update(event)

    def draw_to_board(self):
        font = pygame.font.Font("freesansbold.ttf", 55)
        name = font.render(
            self.hero.name, True, Colors.BLACK
        )
        name = pygame.transform.scale(
            name, [(self.size[0] // 2) - 40, (self.size[1] // 5) - 10]
        )
        self.game.screen.blit(
            name,
            [
                self.position[0] + (self.size[0] // 2) - (name.get_width() // 2),
                self.position[1] + 4 * (self.size[1] // 5) + 5,
            ],
        )
        self.game.screen.blit(
            self.image,
            [
                self.position[0] + (self.image_width_border // 2),
                self.position[1] + (self.image_height_border // 2),
            ],
        )
