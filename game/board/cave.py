from gamecard.card import Card
from board.land import Land


class Cave(Card, Land):
    """
    This class is used to create a cave object.
    A cave is where the dragon starts and end in the game.
    A cave does not allow other dragons to enter.
    """

    def __init__(self, id, animal, land, image_path, scale):
        """
        This method initializes the cave object.

        input:
        - id: the id of the cave (match with the owner's id)
        - animal: the animal type of the card
        - land: the land type of the card
        - image_path: the image path of the cave
        - scale: the scale of the cave image

        return: None
        """
        Card.__init__(self, animal)
        Land.__init__(self, land, image_path, scale)
        self.id = id

    def get_id(self):
        """
        This method is used to get the id of the cave.

        return: int
        """
        return self.id

    def can_enter(self, player):
        """
        This method is used to check if the player can enter the cave.
        Only the owner of the cave can enter the cave.

        input:
        - player: the dragon instance

        return: bool
        """
        return player.get_id() == self.id
