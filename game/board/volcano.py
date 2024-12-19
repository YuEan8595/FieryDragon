from gamecard.card import Card
from board.land import Land


class Volcano(Card, Land):
    """
    This class is used to create a volcano object.
    A volcano is where the dragon walks on the board.
    """

    def __init__(self, animal, land, image_path, scale):
        """
        This method initializes the volcano object.

        input:
        - animal: the animal type of the card
        - land: the land type of the card
        - image_path: the image path of the volcano
        - scale: the scale of the volcano image

        return: None
        """
        Card.__init__(self, animal)
        Land.__init__(self, land, image_path, scale)
        self.dragon_id = None

    def can_enter(self, player):
        """
        This method is used to check if the player can enter the volcano.
        The player can enter the volcano if the volcano is not occupied.

        input:
        - player: the dragon instance (not used in this method)

        return: bool
        """
        return not self.occupied

    def set_dragon_occupied(self, dragon_id):
        """
        This method is used to set the dragon id that occupies the volcano.

        input:
        - dragon_id: the id of the dragon that occupies the volcano

        return: None
        """
        self.dragon_id = dragon_id

    def get_dragon_occupied(self):
        """
        The getter method to return the dragon id that occupies the volcano.

        return: int
        """
        return self.dragon_id