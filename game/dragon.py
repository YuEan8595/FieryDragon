from drawable import Drawable
from board.land_type import LandType


class Dragon(Drawable):
    """
    This class is used to create a dragon object.
    Dragon is basically the pieces control by the player.
    It is the thing that moves around the board.
    """

    def __init__(self, id, img_path, scale):
        """
        This method initializes the dragon object.

        input:
        - id: the id of the dragon
        - img_path: the path of the dragon image
        - scale: the scale of the dragon image

        return: None
        """
        super().__init__(img_path, scale)
        self.id = id
        self.img_path = img_path
        self.board_pos = None

    def get_id(self):
        """
        The getter method to return the id of the dragon.

        return: int
        """
        return self.id

    def get_img_path(self):
        """
        The getter method to return the image path of the dragon.

        return: str
        """
        return self.img_path

    def set_id(self, id):
        """
        The setter method to set the id of the dragon.

        input:
        - id: the id of the dragon

        return: None
        """
        self.id = id

    def get_board_pos(self):
        """
        The getter method to return the board position of the dragon.

        return: int
        """
        return self.board_pos

    def set_pos(self, new_board_pos, new_xy):
        """
        The setter method to set the position of the dragon.

        input:
        - new_board_pos: the new board position of the dragon
        - new_xy: the new x and y display coordinate of the dragon 
                  (in tuple)

        return: None
        """
        self.board_pos = new_board_pos
        super().set_pos(new_xy[0]+10, new_xy[1])

    def move(self, destination, board, players, cave_distance):
        """
        This method moves the dragon to the destination.
        It checks if the destination is valid or not.
        A destination is valid if:
            - the cave belongs to the dragon
            - the volcano is not occupied by other dragon

        input:
        - destination: the destination index on the game board
        - board: the board object

        return: bool
        """
        end_turn = False    # Flag to check if the player's turn ends
        if board[destination].can_enter(self):
            board[self.get_board_pos()].set_occupied_status(False)
            board[destination].set_occupied_status(True)
            if board[destination].get_land() == LandType.VOLCANO:
                board[destination].set_dragon_occupied(self.get_id())
            self.set_pos(destination, board[destination].get_pos())
        else:
            # if the destination is occupied by other dragon, the player will occupy the destination
            # and the other dragon will move one step backward
            if board[destination].get_land() == LandType.VOLCANO:
                board[self.get_board_pos()].set_occupied_status(False)
                other_dragon_id = board[destination].get_dragon_occupied()
                board[destination].set_dragon_occupied(self.get_id())
                self.set_pos(destination, board[destination].get_pos())
                board[destination].set_occupied_status(True)
                # find the volcano card that is not occupied by any dragon for the other dragon to move to
                find_volcano = False
                while not find_volcano:
                    destination = (destination - 1) % len(board)
                    if board[destination].get_land() == LandType.VOLCANO:
                        find_volcano = True
                        board[destination].set_occupied_status(True)
                        board[destination].set_dragon_occupied(other_dragon_id)
                        players[other_dragon_id].set_pos(destination, board[destination].get_pos())

            else:
                end_turn = True
        # else:
        #     # if the destination is occupied by other dragon, the player will occupy the destination
        #     # and the other dragon will be moved to his cave
        #     if board[destination].get_land() == LandType.VOLCANO:
        #         board[self.get_board_pos()].set_occupied_status(False)
        #         other_dragon_id = board[destination].get_dragon_occupied()
        #         board[destination].set_dragon_occupied(self.get_id())
        #         self.set_pos(destination, board[destination].get_pos())
        #         board[destination].set_occupied_status(True)

        #         # move the dragon to his cave
        #         print("players: ", players)
        #         print("other dragon id: ", other_dragon_id)
        #         print("cave distance: ", other_dragon_id * cave_distance)
        #         if len(players) == 2:
        #             if other_dragon_id == 2:
        #                 other_dragon_id = 1
        #                 board[(other_dragon_id + 1) * cave_distance].set_occupied_status(True)
        #                 players[other_dragon_id].set_pos((other_dragon_id + 1) * cave_distance, board[(other_dragon_id + 1) * cave_distance].get_pos())
        #             else:
        #                 board[other_dragon_id * cave_distance].set_occupied_status(True)
        #                 players[other_dragon_id].set_pos(other_dragon_id * cave_distance, board[other_dragon_id * cave_distance].get_pos())
        #         else:
        #             board[other_dragon_id * cave_distance].set_occupied_status(True)
        #             players[other_dragon_id].set_pos(other_dragon_id * cave_distance, board[other_dragon_id * cave_distance].get_pos())
        #     else:
        #         end_turn = True
        # else:
        #     end_turn = True
        return end_turn
