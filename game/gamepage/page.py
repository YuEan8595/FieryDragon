from abc import ABC, abstractmethod


class Page(ABC):
    """
    Abstract class for a page object.
    A page object is used to represent a state in the game.
    Each page has its own implementation of the run method.
    """

    def __init__(self, page_controller, window):
        """
        This method initializes the page object.

        input:
        - page_controller: the page controller of the game
        - window: the window of the game

        return: None
        """
        self.page_controller = page_controller
        self.window = window

    def change_page(self, page):
        """
        Change the page of the game.

        input:
        - page: the page to change to

        return: None
        """
        self.page_controller.change_page(page)

    @abstractmethod
    def run(self):
        """ 
        Implements the complete functionality of each page in 
        the respective concrete child class.
        """
        pass
