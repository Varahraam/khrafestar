import pygame
from ClickableObject import ClickableObject
from Colors import Colors

class Deck(ClickableObject, pygame.sprite.Sprite):
    def __init__(self, screen, position, size, image_path) -> None:
        ClickableObject.__init__(self, position, size)
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, size)
        self.image = image
        self.screen = screen
    
    def update(self, event):
        if self.is_clicked(event):
            print("clicked!")
        self.screen.blit(self.image, self.get_dimensions())
