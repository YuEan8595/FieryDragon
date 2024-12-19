import pygame
import sys


class Display:
    """
    This class is basically the utility class.
    It is used to manipulate the display of the game.
    """
    @staticmethod
    def draw_text(window, text, size, color, x, y, update_display=True):
        """
        This method draws text on the window.

        input:
        - window: the window to draw the text on
        - text: the text to draw
        - size: the size of the text
        - color: the color of the text
        - x: the x-coordinate of the text
        - y: the y-coordinate of the text
        - update_display: whether to update the display or not

        return: None
        """
        font = pygame.font.SysFont('arial', size)
        text_output = font.render(text, True, color)
        text_rect = text_output.get_rect()
        text_rect.center = (x, y)
        window.blit(text_output, text_rect)

        if update_display:
            pygame.display.update()

    @staticmethod
    def draw_img(window, image, x, y):
        """
        This method draws image on the window.

        input:
        - window: the window to draw the image on
        - image: the image to draw
        - x: the x-coordinate of the image
        - y: the y-coordinate of the image

        return: None
        """
        rect = image.get_rect()
        rect.center = (x, y)
        window.blit(image, (rect.x, rect.y))

    @staticmethod
    def load_bg(window, path):
        """
        This method loads the background image from the path and 
        scale the image.

        input:
        - path: the path of the background image

        return: The scaled background image
        """
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.smoothscale(
            img, (window.get_width(), window.get_height()))
        return img

    @staticmethod
    def load_img(path, scale):
        """
        This method loads the image from the path and scale the 
        image.

        input:
        - path: the path of the image
        - scale: the scale of the image

        return: The scaled image
        """
        img = pygame.image.load(path).convert_alpha()
        width = img.get_width()
        height = img.get_height()
        scale_img = pygame.transform.smoothscale(
            img, (int(width * scale), int(height * scale)))
        return scale_img

    @staticmethod
    def quit():
        """
        This method quits the game and close the window.

        return: None
        """
        pygame.quit()
        sys.exit()
