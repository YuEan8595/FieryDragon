from drawable import Drawable

import pygame


class Button(Drawable):
    """
    This class is used to create a button object.
    A button object is an object that can be clicked by the user.
    """

    def __init__(self, image_path, scale):
        """
        This method initializes the button object.

        input:
        - image_path: the image path of the button
        - scale: the scale of the button image

        return: None
        """
        super().__init__(image_path, scale)
        self.clicked = False

    def is_clicked(self):
        """
        This method checks if the button is clicked.
        If the button is clicked, the method returns True.

        return: bool
        """
        rect = self.image.get_rect()
        rect.center = (self.x, self.y)

        pos = pygame.mouse.get_pos()
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                return self.clicked
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
