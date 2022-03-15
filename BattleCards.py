import pygame

from Component import Component
from Card import Card, CARD_WIDTH, CARD_HEIGHT

class BattleCard(Component, pygame.sprite.Sprite):
    def __init__(self, screen, card, position, image_path=None) -> None:
        pygame.sprite.Sprite.__init__(self)
        Component.__init__(self, position, [CARD_WIDTH, CARD_HEIGHT])
        self.card = card
        self.screen = screen
        if (image_path):
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, self.size)
            self.image = image
        self.type = type

    def update(self, event):
        self.screen.blit(self.image, self.position)
        if (self.is_clicked(event)):
            print(f"card {self.card.name} clicked")

class BattleCards(Component):
    battle_cards = []

    def __init__(self, screen, position) -> None:
        Component.__init__(self, position, [0,0])
        self.screen = screen
        self.init_battle_cards_list()

    def update(self, event):
        for battle_card in self.battle_cards:
            battle_card.update(event)

    def get_battle_cards(self):
        # TODO: complete this
        return [
            Card("yek", "is good", "battle"),
            Card("Do", "is good", "battle"),
            Card("Se", "is good", "battle"),
        ]

    def init_battle_cards_list(self):
        cards = self.get_battle_cards()
        for i, card in enumerate(cards):
            self.battle_cards.append(
                BattleCard(
                    self.screen,
                    card,
                    [self.position[0] + (i * CARD_WIDTH), self.position[1]],
                    image_path="magic.jpg"
                )
            )
