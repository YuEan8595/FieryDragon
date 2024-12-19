from gamepage.page import Page
from gamepage.end import End
from display import Display
from dragon import Dragon
from board.gameboard import GameBoard
from gamecard.chit_card import ChitCard
from gamecard.animal_type import AnimalType
from action.forward_action import ForwardAction
from action.backward_action import BackwardAction

import pygame
import random
import time


class Game(Page):
    """
    This class is used to create a game object.
    The game object is the main object that controls the game.
    It is responsible for creating the gameboard, dragons and chit cards.
    It controls the overall game logic.
    """

    def __init__(self, page_controller, window, player_num, size=24,
                 animal_num=4):
        """
        This method initializes the game object.

        input:
        - page_controller: the page controller object
        - window: the window object
        - player_num: the number of players
        - size: the number of volcanoes on the gameboard
        - animal_num: the number of animal types in the game

        return: None
        """
        super().__init__(page_controller, window)
        self.player_num = player_num
        # Variable named players for better readability
        self.players = self._create_dragons()
        self.chit_cards = self._create_cc()
        self.gameboard = GameBoard(self.window, self.players, size,
                                   animal_num)

    def run(self):
        """ 
        The game engine.
        Handle the game logic.
        If the game ends, the game will change to the end page.

        return: None
        """
        end = False
        current_player = 0  # Track the current player
        card_reveal = 0     # Track the number of chit cards revealed
        self.update_gameboard()
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.quit()

            animal_type = None
            step = None
            end_turn = False

            # Check if all chit cards are revealed
            if card_reveal > len(self.chit_cards) - 1:
                current_player, card_reveal = self._next_player(
                    current_player, card_reveal)

            for chit_card in self.chit_cards:
                # If a chit card is clicked
                if chit_card.is_clicked():
                    self.update_gameboard()
                    animal_type = chit_card.get_animal()
                    step = chit_card.get_animal_num()
                    card_reveal += 1
                    break

            player = self.players[current_player]
            pos = player.get_board_pos()

            if animal_type is None:
                continue

            # When card drawn is a penalty card
            elif animal_type == AnimalType.DRAGON_PIRATE:
                action = BackwardAction(pos, step, player,
                                        self.gameboard.get_board(),
                                        self.gameboard.get_cave_distance(),
                                        self.players)
                end_turn = action.execute()
                self.update_gameboard()

            # When animal type does not match
            elif self.gameboard.get_board()[pos].get_animal() != animal_type:
                end_turn = True

            # When the animal type matches
            else:
                action = ForwardAction(pos, step, player,
                                       self.gameboard.get_board(),
                                       self.gameboard.get_cave_distance(),
                                       self.players)
                end_turn, end = action.execute()
                self.update_gameboard()

            # if the player's turn ends, change to the next player and reset
            # the chit cards
            if end_turn:
                current_player, card_reveal = self._next_player(
                    current_player, card_reveal)

        # Change to end page to show the winner
        Display.draw_text(self.window, "GAME OVER", 70, (0, 0, 0),
                          self.window.get_width()//2,
                          self.window.get_height()//2)
        time.sleep(1)
        self.change_page(
            End(self.page_controller, self.window, player.get_img_path()))

    def _next_player(self, current_player, card_reveal):
        """
        This method is used to change the turn to the next player.
        The current player index will be increment by 1.
        All the chit cards will be reset.

        input:
        - current_player: the current player index
        - card_reveal: the number of chit cards revealed

        return: int, int
        """
        current_player = (current_player + 1) % self.player_num
        card_reveal = 0
        for chit_card in self.chit_cards:
            chit_card.reset()

        time.sleep(1)
        self.update_gameboard()

        Display.draw_text(self.window, f"Player {current_player + 1}'s turn",
                          25, (0, 0, 0), self.window.get_width()//2,
                          self.window.get_height()//2)
        time.sleep(1)
        self.update_gameboard()

        return current_player, card_reveal

    def update_gameboard(self):
        """
        This method updates the display of the game if there is any player 
        movement or flipping of chit cards, etc.

        return: None
        """
        self.gameboard.draw()
        self._draw_game_element()
        pygame.display.update()

    def _draw_game_element(self):
        """
        This method draws the chit card and dragons on the window.

        return: None
        """
        self._draw_chit_cards()
        self._draw_dragons()

    def _draw_dragons(self):
        """
        This method draws the dragons on the window.

        return: None
        """
        for player in self.players:
            player.draw(self.window)

    def _draw_chit_cards(self):
        """
        This method draws the chit cards on the window.

        return: None
        """
        for chit_card in self.chit_cards:
            chit_card.draw(self.window)

    def _create_dragons(self):
        """
        This method creates the dragons.

        return: list
        """
        # Image path
        img_paths = ["Project/img/pimg/r.png", "Project/img/pimg/y.png",
                     "Project/img/pimg/g.png", "Project/img/pimg/b.png"]
        dragons = []
        scale = 0.11
        for i in range(self.player_num):
            dragons.append(Dragon(i, img_paths[i], scale))

        return dragons

    def _create_cc(self):
        """
        This method creates the chit cards list and the randomized window 
        display position.

        return: list
        """
        x_pos = []
        y_pos = []
        window_w = self.window.get_width()
        window_h = self.window.get_height()
        interval = 75   # The interval between each chit card
        for i in range(1, 4, 2):
            x_pos.append(int(window_w/2 + interval*i/2))
            x_pos.append(int(window_w/2 - interval*i/2))
            y_pos.append(int(window_h/2 + interval*i/2))
            y_pos.append(int(window_h/2 - interval*i/2))

        pos_tuple = [(x, y) for x in x_pos for y in y_pos]
        random.shuffle(pos_tuple)

        # Create chit cards
        chit_cards = []
        scale = 0.05    # The scale of the chit card image
        pos_tuple_index = 0
        for i in range(1, 4):
            # Create baby dragon chit cards
            img_path = f"Project/img/ccimg/baby_d{i}.png"
            back_img_path = "Project/img/ccimg/back.png"
            cc, pos_tuple_index = self._cc_helper(
                img_path, back_img_path, pos_tuple, pos_tuple_index,
                AnimalType.BABY_DRAGON, i, scale)
            chit_cards.append(cc)

            # Create bat chit cards
            img_path = f"Project/img/ccimg/bat{i}.png"
            cc, pos_tuple_index = self._cc_helper(
                img_path, back_img_path, pos_tuple, pos_tuple_index,
                AnimalType.BAT, i, scale)
            chit_cards.append(cc)

            # Create salamander chit cards
            img_path = f"Project/img/ccimg/sal{i}.png"
            cc, pos_tuple_index = self._cc_helper(
                img_path, back_img_path, pos_tuple, pos_tuple_index,
                AnimalType.SALAMANDER, i, scale)
            chit_cards.append(cc)

            # Create spider chit cards
            img_path = f"Project/img/ccimg/spi{i}.png"
            cc, pos_tuple_index = self._cc_helper(
                img_path, back_img_path, pos_tuple, pos_tuple_index,
                AnimalType.SPIDER, i, scale)
            chit_cards.append(cc)

            # Create pirate dragon chit cards
            if i < 3:
                img_path = f"Project/img/ccimg/p{i}.png"
                for _ in range(2):
                    cc, pos_tuple_index = self._cc_helper(
                        img_path, back_img_path, pos_tuple, pos_tuple_index,
                        AnimalType.DRAGON_PIRATE, i, scale)
                    chit_cards.append(cc)

        return chit_cards

    def _cc_helper(self, img_path, back_img_path, pos_tuple, index,
                   animal_type, animal_num, scale):
        """
        Helper function for creating chit card.

        input:
        - img_path: the front image path of the chit card
        - back_img_path: the back image path of the chit card
        - pos_tuple: the list of position tuples
        - index: the index of the position tuple
        - animal_type: the animal type of the chit card
        - animal_num: the animal number of the chit card
        - scale: the scale of the chit card image

        return: ChitCard, int
        """
        x, y = pos_tuple[index]
        index += 1
        chit_card = ChitCard(img_path, back_img_path, scale, animal_type, animal_num)
        chit_card.set_pos(x, y)
        return chit_card, index