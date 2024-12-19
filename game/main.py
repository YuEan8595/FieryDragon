from gamepage.home import Home
from gamepage.page_controller import PageController

import pygame


class Main:
    """
    This class is the main class of the game.
    The game can be started by running this class.
    """

    # Display window
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_TITLE = "Fiery Dragons"

    def __init__(self):
        """
        This method initializes the main class.

        return: None
        """
        pygame.init()
        self.window = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.WINDOW_TITLE)
        self.page_controller = PageController(self)
        self.state = Home(self.page_controller, self.window)

    def set_state(self, state):
        """
        Set the state of the game

        input:
        - state: the state of the game

        return: None
        """
        self.state = state

    def run(self):
        """
        Run the game

        return: None
        """
        while self.state is not None:
            self.state.run()


if __name__ == "__main__":
    main = Main()
    main.run()
