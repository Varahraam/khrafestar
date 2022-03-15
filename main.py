import pygame
from Button import Button
from HeroComponent import HeroComponent
from StatusComponent import StatusComponent
from ViewCard import CARD_WIDTH, CARD_HEIGHT
from PageHandler import PageId
from Card import Card, CardTypes
from CardsPage import CardsPage
from SingleCardPage import SingleCardPage

from Player import Player
from Colors import Colors
from Hero import Hero

ASSETS_FOLDER = "assets/"

def get_temp_cards(player, type):
    # TODO: complete this
    cards = []
    if player == 0:
        for i in range(22):
            cards.append(Card(str(i), "is good", type, ASSETS_FOLDER + "magic.jpg"))
    else:
        for i in range(40):
            cards.append(Card(str(i), "is good", type, ASSETS_FOLDER + "magic.jpg"))
    return cards


def get_temp_resources(player):
    if player == 0:
        return [200, 10, 4, 5]
    else:
        return [180, 11, 3, 2]


def get_temp_hero(player):
    if player == 0:
        return Hero("ghodrat","bi bak va dalir", ASSETS_FOLDER + "ghodrat.jpg")
    else:
        return Hero("donda","bi bak va dalir", ASSETS_FOLDER + "donda.jpg")

class Game:
    WIDTH = 1200
    HEIGHT = 1000

    YOU = 0
    OPPONENT = 1

    prev_page = []

    page_id = PageId.MAIN
    page_player = 0
    page_card = None

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.music.load(ASSETS_FOLDER + "theme.mp3")  
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.player = Player()
        self.components = []
        self.draw_board()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for component in self.components:
                component.update(event)

    def set_page_info(self, page_id, page_player=0, card=None):
        self.prev_page = [self.page_id, self.page_player]
        self.page_id = page_id
        self.page_player = page_player
        self.page_card = card
        self.components = []
        self.draw_board()

    def run_game(self):
        while True:
            self.handle_events()
            pygame.display.flip()

    def draw_board(self):
        if self.page_id == PageId.MAIN:
            self.draw_main_page()
        elif self.page_id == PageId.TROOPS:
            self.draw_card_type_page(CardTypes.TROOP)
        elif self.page_id == PageId.BUILDINGS:
            self.draw_card_type_page(CardTypes.BUILDING)
        elif self.page_id == PageId.ABILITIES:
            self.draw_card_type_page(CardTypes.ABILITY)
        elif self.page_id == PageId.CARD:
            self.draw_single_card_page()

    def draw_main_page(self):
        print("here")
        self.screen.fill(Colors.GRAY)
        self.components.append(
            Button(
                self,
                [0 + 20, (2 * (self.HEIGHT // 5)) + 20],
                [(self.WIDTH // 3) - 40, (self.HEIGHT // 5) - 40],
                ASSETS_FOLDER + "troops.png",
                PageId.TROOPS,
                self.YOU,
            )
        )
        self.components.append(
            Button(
                self,
                [2 * (self.WIDTH // 3) + 20, (2 * (self.HEIGHT // 5)) + 20],
                [(self.WIDTH // 3) - 40, (self.HEIGHT // 5) - 40],
                ASSETS_FOLDER + "troops.png",
                PageId.TROOPS,
                self.OPPONENT,
            )
        )
        self.components.append(
            Button(
                self,
                [0 + 20, (3 * (self.HEIGHT // 5)) + 20],
                [(self.WIDTH // 3) - 40, (self.HEIGHT // 5) - 40],
                ASSETS_FOLDER + "buildings.png",
                PageId.BUILDINGS,
                self.YOU,
            )
        )
        self.components.append(
            Button(
                self,
                [2 * (self.WIDTH // 3) + 20, (3 * (self.HEIGHT // 5)) + 20],
                [(self.WIDTH // 3) - 40, (self.HEIGHT // 5) - 40],
                ASSETS_FOLDER + "buildings.png",
                PageId.BUILDINGS,
                self.OPPONENT,
            )
        )
        # TODO:
        self.components.append(
            Button(
                self,
                [0 + 20, (4 * (self.HEIGHT // 5)) + 20],
                [(self.WIDTH // 3) - 40, (self.HEIGHT // 5) - 40],
                ASSETS_FOLDER + "abilities.png",
                PageId.ABILITIES,
                self.YOU,
            )
        )
        self.components.append(
            Button(
                self,
                [2 * (self.WIDTH // 3) + 20, (4 * (self.HEIGHT // 5)) + 20],
                [(self.WIDTH // 3) - 40, (self.HEIGHT // 5) - 40],
                ASSETS_FOLDER + "abilities.png",
                PageId.ABILITIES,
                self.OPPONENT,
            )
        )
        your_resources_info = get_temp_resources(self.YOU)
        self.components.append(
            StatusComponent(
                self,
                [0, (1 * (self.HEIGHT // 5))],
                [self.WIDTH // 3, self.HEIGHT // 5],
                your_resources_info,
            )
        )
        oponent_resources_info = get_temp_resources(self.OPPONENT)
        self.components.append(
            StatusComponent(
                self,
                [2 * (self.WIDTH // 3), (1 * (self.HEIGHT // 5))],
                [self.WIDTH // 3, self.HEIGHT // 5],
                oponent_resources_info,
            )
        )
        your_hero = get_temp_hero(self.YOU)
        self.components.append(
            HeroComponent(
                self,
                [0, 0],
                [self.WIDTH // 3, self.HEIGHT // 5],
                your_hero
            )
        )
        opponents_hero = get_temp_hero(self.OPPONENT)
        self.components.append(
            HeroComponent(
                self,
                [2 * (self.WIDTH // 3), 0],
                [self.WIDTH // 3, self.HEIGHT // 5],
                opponents_hero
            )
        )
        # MIDDLE BUTTONS
        self.components.append(
            Button(
                self,
                [(self.WIDTH // 3) + 20, ((self.HEIGHT // 4)) + 20],
                [(self.WIDTH // 6) - 40, (self.HEIGHT // 4) - 40],
                ASSETS_FOLDER + "sacrifice.jpg",
                PageId.MAIN,
                self.YOU,
            )
        )
        self.components.append(
            Button(
                self,
                [(self.WIDTH // 2) + 20, ((self.HEIGHT // 4)) + 20],
                [(self.WIDTH // 6) - 40, (self.HEIGHT // 4) - 40],
                ASSETS_FOLDER + "troopDeck.png",
                PageId.MAIN,
                self.YOU,
            )
        )
        self.components.append(
            Button(
                self,
                [(self.WIDTH // 3) + 20, ((self.HEIGHT // 2)) + 20],
                [(self.WIDTH // 6) - 40, (self.HEIGHT // 4) - 40],
                ASSETS_FOLDER + "buildingDeck.png",
                PageId.MAIN,
                self.YOU,
            )
        )
        self.components.append(
            Button(
                self,
                [(self.WIDTH // 2) + 20, ((self.HEIGHT // 2)) + 20],
                [(self.WIDTH // 6) - 40, (self.HEIGHT // 4) - 40],
                ASSETS_FOLDER + "abilityDeck.png",
                PageId.MAIN,
                self.YOU,
            )
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [self.WIDTH // 3, 0],
            [self.WIDTH // 3, self.HEIGHT],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [2 * (self.WIDTH // 3), 0],
            [2 * (self.WIDTH // 3), self.HEIGHT],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [self.WIDTH // 2, self.HEIGHT // 4],
            [self.WIDTH // 2, 3 * (self.HEIGHT // 4)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [self.WIDTH // 3, self.HEIGHT // 2],
            [2 * (self.WIDTH // 3), self.HEIGHT // 2],
        )

        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [self.WIDTH // 3, self.HEIGHT // 4],
            [2 * (self.WIDTH // 3), self.HEIGHT // 4],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [self.WIDTH // 3, 3 * (self.HEIGHT // 4)],
            [2 * (self.WIDTH // 3), 3 * (self.HEIGHT // 4)],
        )

        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [0, self.HEIGHT // 5],
            [self.WIDTH // 3, (self.HEIGHT // 5)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [0, 2 * (self.HEIGHT // 5)],
            [self.WIDTH // 3, 2 * (self.HEIGHT // 5)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [0, 3 * (self.HEIGHT // 5)],
            [self.WIDTH // 3, 3 * (self.HEIGHT // 5)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [0, 4 * (self.HEIGHT // 5)],
            [self.WIDTH // 3, 4 * (self.HEIGHT // 5)],
        )

        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [2 * (self.WIDTH // 3), self.HEIGHT // 5],
            [self.WIDTH, (self.HEIGHT // 5)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [2 * (self.WIDTH // 3), 2 * (self.HEIGHT // 5)],
            [self.WIDTH, 2 * (self.HEIGHT // 5)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [2 * (self.WIDTH // 3), 3 * (self.HEIGHT // 5)],
            [self.WIDTH, 3 * (self.HEIGHT // 5)],
        )
        pygame.draw.line(
            self.screen,
            Colors.BLACK,
            [2 * (self.WIDTH // 3), 4 * (self.HEIGHT // 5)],
            [self.WIDTH, 4 * (self.HEIGHT // 5)],
        )

    def draw_card_type_page(self, card_type):
        # TODO: get player card_type cards
        cards = get_temp_cards(self.page_player, card_type)
        print(f"in {card_type} page!!!")
        self.screen.fill(Colors.LIGHT_RED)
        self.components.append(
            CardsPage(self, [0, 0], [self.WIDTH, self.HEIGHT - CARD_HEIGHT], cards)
        )
        self.components.append(
            Button(
                self,
                [
                    (self.WIDTH // 2) - (self.WIDTH // 12),
                    self.HEIGHT - CARD_HEIGHT + 20,
                ],
                [self.WIDTH // 6, CARD_HEIGHT - 40],
                ASSETS_FOLDER + "back.png",
                PageId.MAIN,
                self.OPPONENT,
            )
        )

    def draw_single_card_page(self):
        print(f"in card: {self.page_card.name} page!!!")
        self.screen.fill(Colors.LIGHT_BLUE)
        self.components.append(
            SingleCardPage(
                self, [0, 0], [self.WIDTH, self.HEIGHT - CARD_HEIGHT], self.page_card
            )
        )
        self.components.append(
            Button(
                self,
                [
                    (self.WIDTH // 2) - (self.WIDTH // 12),
                    self.HEIGHT - CARD_HEIGHT + 20,
                ],
                [self.WIDTH // 6, CARD_HEIGHT - 40],
                ASSETS_FOLDER + "back.png",
                self.prev_page[0],
                self.prev_page[1],
            )
        )


if __name__ == "__main__":
    Game().run_game()
