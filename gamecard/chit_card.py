from button import Button
from gamecard.card import Card
from display import Display

import pygame


class ChitCard(Button, Card):
    """
    This class is used to create a chit card object.
    A chit card is what the player choose and flip to reveal the animal 
    type. If the animal type matches, they can move forward in the game.

    Animal type         : bat, baby dragon, salamander, spider
    Penalty animal type : dragon pirate
    """

    def __init__(self, front_image_path, back_image_path, scale, animal, animal_num):
        """
        This method initializes the chit card object.

        input:
        - front_image_path: the front image path of the chit card (show the animal)
        - back_image_path: the back image path of the chit card
        - scale: the scale of the chit card image
        - animal: the animal type of the chit card
        - animal_num: the animal number on the chit card

        return: None
        """
        Button.__init__(self, back_image_path, scale)
        Card.__init__(self, animal)
        self.animal_num = animal_num
        self.reveal = False  # To detect whether the card is flipped
        self.front_image = Display.load_img(front_image_path, scale)
        self.back_image = Display.load_img(back_image_path, scale)

    def is_clicked(self):
        """
        This method checks if the chit card is clicked.
        If the chit card is clicked, the method returns True and the front 
        image of the chit card is shown.
        It cannot be clicked anymore until the next player's turn.

        return: bool
        """
        rect = self.image.get_rect()
        rect.center = (self.x, self.y)

        pos = pygame.mouse.get_pos()
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked and not self.reveal:
                self.clicked = True
                self.reveal = True
                self.image = self.front_image
                return True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def get_animal_num(self):
        """
        The getter method return the animal number on the chit 
        card.

        return: int
        """
        return self.animal_num

    def reset(self):
        """
        This method resets the chit card to its original state.
        Usually trigered when it is the turn of the next player.

        return: None
        """
        self.reveal = False
        self.image = self.back_image
