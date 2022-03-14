import pygame
from Component import Component
from Colors import Colors
from Card import Card


class Ability(Component):
    def __init__(self, screen, position, size, card) -> None:
        # TODO: card type must be ability
        Component.__init__(self, position, size)
        self.card = card
        self.screen = screen
        font = pygame.font.Font("freesansbold.ttf", 32)
        self.text = font.render(card.get_line(), True, Colors.BLACK, Colors.GRAY)
        self.text = pygame.transform.scale(self.text, size)

    def update(self, event):
        self.screen.blit(self.text, self.get_dimensions())


class Abilities(Component):
    abilities = []

    def __init__(self, screen, position, size) -> None:
        Component.__init__(self, position, size)
        self.screen = screen
        self.init_ability_list()

    def update(self, event):
        for ability in self.abilities:
            ability.update(event)

    def get_abilitiy_cards(self):
        # TODO: complete this
        return [
            Card("yek", "is good", "ability"),
            Card("Do", "is good", "ability"),
            Card("Se", "is good", "ability"),
        ]

    def init_ability_list(self):
        ability_cards = self.get_abilitiy_cards()
        height_per_ability = self.size[1] // (len(ability_cards) + 5)
        for i, ability_card in enumerate(ability_cards):
            self.abilities.append(
                Ability(
                    self.screen,
                    [self.position[0], self.position[1] + height_per_ability * i],
                    [self.size[0], height_per_ability],
                    ability_card,
                )
            )
