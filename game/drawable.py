from abc import ABC, abstractmethod
from display import Display


class Drawable(ABC):
    """
    Represents an abstract class for a drawable object.
    A drawable object is an object that can be drawn on the screen.
    """

    def __init__(self, image_path, scale):
        """
        Initializes the drawable object.

        input:
        - image_path: the image path of the drawable object
        - scale: the scale of the drawable object's image

        return: None
        """
        self.image = Display.load_img(image_path, scale)
        self.x = None
        self.y = None

    def draw(self, window):
        """
        Call Display static method to draw the image on the 
        window.

        input:
        - window: the window to draw the image on

        return: None
        """
        Display.draw_img(window, self.image, self.x, self.y)

    def set_pos(self, x, y):
        """
        Set the display coordinate of the drawable object.

        input:
        - x: the x-coordinate of the object for display
        - y: the y-coordinate of the object for display

        return: None
        """
        self.x = x
        self.y = y
