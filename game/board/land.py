from drawable import Drawable

from abc import ABC, abstractmethod


class Land(Drawable, ABC):
    """
    Abstract class for a land object.
    Land instance form the board of the game.
    This is where the dragon stands on or started from.
    """

    def __init__(self, land, image_path, scale):
        """
        This method initializes the land object.

        input:
        - land: the land type of the card
        - image_path: the image path of the land
        - scale: the scale of the land image

        return: None
        """
        super().__init__(image_path, scale)
        self.land_type = land
        self.occupied = False

    def get_land(self):
        """
        The getter method to return the land type of the card.

        return: LandType
        """
        return self.land_type

    def get_pos(self):
        """
        The getter method to return the display position of the land.

        return: tuple
        """
        return (self.x, self.y)

    def set_occupied_status(self, status):
        """
        The setter method to set the occupied status of the land.

        input:
        - status: the status of the land (True if occupied, False otherwise)

        return: None
        """
        self.occupied = status

    @abstractmethod
    def can_enter(self, player):
        """
        Abstract method to check if the dragon can enter the land.

        input:
        - player: the dragon instance

        return: bool
        """
        pass
