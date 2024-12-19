class PageController:
    """
    This class controls the pages of the game.
    It is used to change the state in the main class.
    """

    def __init__(self, main):
        """
        This method initializes the page controller.

        input:
        - main: the main class of the game

        return: None
        """
        self.main = main

    def change_page(self, page):
        """
        Change the state of the main class.

        input:
        - page: the page to change to

        return: None
        """
        self.main.set_state(page)
