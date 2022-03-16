import pygame
from Component import Component
from Colors import Colors
from PageHandler import PageId


class Button(Component, pygame.sprite.Sprite):
    def __init__(
        self, game, position, size, image_path, callback_page, callback_player
    ) -> None:
        Component.__init__(self, position, size)
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, size)
        self.image = image
        self.callback_page = callback_page
        self.callback_player = callback_player
        self.game = game
        self.game.screen.blit(self.image, self.get_dimensions())

    def update(self, event):
        if self.is_clicked(event):
            self.game.set_page_info(self.callback_page, self.callback_player)
