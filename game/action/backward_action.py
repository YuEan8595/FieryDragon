from action.move_action import MoveAction
from board.land_type import LandType


class BackwardAction(MoveAction):
    """
    This class is used to determine the expected destination of the player
    based on the current position of the player and the steps when a 
    penalty card is drawn by the player.
    """

    def __init__(self, start_pos, step, player, board, cave_distance, players):
        """
        This method initializes the backward action object.

        input:
        - start_pos: the current position of the player
        - step: the number of steps the player is going to move backwards
        - player: the dragon instance
        - board: the gameboard containing the caves and volcanoes in a list
        - cave_distance: the distance between the caves

        return: None
        """
        super().__init__(start_pos, step, player, board)
        self.cave_distance = cave_distance
        self.end_turn = False   # Flag to check if the player's turn ends
        self.destination = self._find_destination()
        self.players = players

    def execute(self):
        """
        This method is used to execute the backward action.
        If destination is not None, the player moves to the destination.
        It then returns the end turn flag to indicate whether the player's 
        turn end.

        return: bool
        """
        if self.destination is not None:
            self.end_turn = self.player.move(self.destination, self.board, self.players, self.cave_distance)
        return self.end_turn

    def _find_destination(self):
        """
        This method is used to find the expected destination of the player.
        It checks whether the player  pass a cave or not during the move.
        If the player is currently in his own cave, destination is set to 
        none and the player will not perform the backward movement.

        return: int
        """
        pos = self.start_pos
        step = self.step
        cave_distance = self.cave_distance
        # If player is not in his cave
        if pos != self.player.get_id() * cave_distance:
            destination = (pos - step) % len(self.board)
            # If destination is not a cave
            if self.board[destination].get_land() != LandType.CAVE:
                prev_cave = (int(pos // cave_distance) *
                             cave_distance) % len(self.board)
                # If the player passed a cave
                if step >= (pos - prev_cave):
                    # If the cave passed is not the player's cave
                    if not self.board[prev_cave].can_enter(self.player):
                        destination = (destination - 1) % len(self.board)
                    else:
                        destination = prev_cave

            # If destination is a cave
            else:
                # If player lands on other player's cave, move one step
                # backward
                if not self.board[destination].can_enter(self.player):
                    destination = (destination - 1) % len(self.board)

        # If player is in his cave
        else:
            # Do nothing as player cannot move beyond his own cave
            destination = None

        return destination
