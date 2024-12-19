from abc import ABC


class Card(ABC):
    """
    Abstract class for a card object.
    Every card instance typically consist of one of the animal 
    type. The animal type is used for matching purposes, 
    enabling the game to have a memory-card like feature.
    """

    def __init__(self, animal):
        """
        This method initializes the card object.

        input:
        - animal: the animal type of the card

        return: None
        """
        self.animal_type = animal

    def get_animal(self):
        """
        The getter method for the animal type of the card.

        return: AnimalType
        """
        return self.animal_type
