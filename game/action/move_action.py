from abc import ABC, abstractmethod


class MoveAction(ABC):
    """
    Abstract class for a move action.
    This class determines the expected destination of the player based on 
    the current position of the player and the steps.
    It checks whether the player will pass a cave or not during the move.
    Since the player is not supposed to enter other player's cave, if they 
    are detected to pass a cave, they move one extra steps forward/backward.
    """

    def __init__(self, start_pos, step, player, board):
        """
        This method initializes the move action object.

        input:
        - start_pos: the current position of the player
        - step: the number of steps the player is going to move
        - player: the dragon instance
        - board: the gameboard containing the caves and volcanoes in a list

        return: None
        """
        self.start_pos = start_pos
        self.step = step
        self.player = player
        self.board = board

    @abstractmethod
    def execute(self):
        """
        This method is used to execute the move action.
        """
        pass

    @abstractmethod
    def _find_destination(self):
        """
        This method is used to find the expected destination of the player.
        """
        pass
