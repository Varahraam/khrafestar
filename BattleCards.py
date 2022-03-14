from Component import Component
from Card import Card, CARD_WIDTH

class BattleCards(Component):
    battle_cards = []

    def __init__(self, screen, position) -> None:
        Component.__init__(self, position, [0,0])
        self.screen = screen

    def update(self, event):
        for i, battle_card in enumerate(self.get_battle_cards()):
            battle_card.draw_to_board(self.screen, [self.position[0] + (i * CARD_WIDTH), self.position[1]])

    def get_battle_cards(self):
        # TODO: complete this
        return [
            Card("yek", "is good", "battle", "magic.jpg"),
            Card("Do", "is good", "battle", "magic.jpg"),
            Card("Se", "is good", "battle", "magic.jpg"),
        ]
