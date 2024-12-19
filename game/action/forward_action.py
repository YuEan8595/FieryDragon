from action.move_action import MoveAction
from board.land_type import LandType


class ForwardAction(MoveAction):
    """
    This class is used to determine the expected destination of the player
    based on the current position of the player and the steps when a 
    matching card is drawn by the player.
    """

    def __init__(self, start_pos, step, player, board, cave_distance, players):
        """
        This method initializes the forward action object.

        input:
        - start_pos: the current position of the player
        - step: the number of steps the player is going to move forward
        - player: the dragon instance
        - board: the gameboard containing the caves and volcanoes in a list
        - cave_distance: the distance between the caves

        return: None
        """
        super().__init__(start_pos, step, player, board)
        self.cave_distance = cave_distance
        self.end_turn = False   # Flag to check if the player's turn ends
        self.end_game = False   # Flag to check if the game ends
        self.destination = self._find_destination()
        self.players = players

    def execute(self):
        """
        This method is used to execute the forward action.
        If destination is not None, the player moves to the destination.
        It then returns the end turn and end game flag to indicate whether 
        the player's turn end or the game end.

        return: bool, bool
        """
        if self.destination is not None:
            self.end_turn = self.player.move(self.destination, self.board, self.players, self.cave_distance)
        return self.end_turn, self.end_game

    def _find_destination(self):
        """
        This method is used to find the expected destination of the player.
        It checks whether the player pass a cave or not during the move.
        If the player is almost reach his cave but does not get the exact 
        number of steps, the player will remain at the initial position and 
        hence the destination is set to none. Meanwhile, if the player 
        successfully lands on its own cave in the exact number of steps, 
        the game ends.

        return: int
        """
        pos = self.start_pos
        step = self.step
        cave_distance = self.cave_distance
        destination = (pos + step) % len(self.board)
        # If destination is not a cave
        if self.board[destination].get_land() != LandType.CAVE:
            prev_cave = int(destination // cave_distance) * cave_distance
            # If the player passed a cave
            if step > destination - prev_cave:
                # If the cave passed is not the player's cave
                if not self.board[prev_cave].can_enter(self.player):
                    destination = (destination + 1) % len(self.board)

                # If the cave passed is the player's cave, the player
                # remain at the initial position until he get the exact
                # number to the his cave
                else:
                    destination = None
                    self.end_turn = True

            # If the player does not pass a cave
            else:
                pass

        # If destination is a cave
        else:
            # Check if player lands on other player's cave
            if destination != self.player.get_id() * cave_distance:
                destination = (destination + 1) % len(self.board)

            # Check if player lands on its own cave
            else:
                self.end_game = True

        return destination
