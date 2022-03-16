import pygame


class Component:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def is_clicked(self, event):
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if (
                self.position[0] < mouse[0] < self.position[0] + self.size[0]
                and self.position[1] < mouse[1] < self.position[1] + self.size[1]
            ):
                return True
        return False

    def get_dimensions(self):
        return self.position + self.size
