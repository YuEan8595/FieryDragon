from gamepage.page import Page
from display import Display
from gamepage.game import Game

import pygame
import time


class Setup(Page):
    """
    Setup page of the game.
    Used to get the number of players from the user.
    """

    def __init__(self, page_controller, window):
        """
        This method initializes the setup page.

        input:
        - page_controller: the page controller of the game
        - window: the window of the game

        return: None
        """
        super().__init__(page_controller, window)

    def run(self):
        """
        This method runs the setup page.

        return: None
        """
        player_num = self._get_player_num()
        self.change_page(Game(self.page_controller, self.window,
                              player_num))

    def _get_player_num(self):
        """
        Get the number of players from the user.
        If the input is invalid, display an error message and ask for 
        input again.

        return: int
        """
        # Load image
        setup_bg = Display.load_bg(
            self.window, 'Project/img/bg_img/setup_bg.png')

        input = ""
        run = True
        while run:
            self.window.blit(setup_bg, (0, 0))
            Display.draw_text(self.window,
                              "Enter the number of players. (2-4)", 24,
                              (255, 255, 255), self.window.get_width()//2,
                              self.window.get_height()//3, False)

            Display.draw_text(self.window, input, 32, (255, 255, 255),
                              self.window.get_width()//2,
                              self.window.get_height()*1.5//3, True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.quit()
                elif event.type == pygame.KEYDOWN:
                    # Check if the user pressed enter (indicates the user
                    # has finished the input)
                    if event.key == pygame.K_RETURN:
                        # Check valid input
                        valid = ['2', '3', '4']
                        if input in valid:
                            return int(input)
                        # If input is invalid, display error message and
                        # prompt user to input again
                        else:
                            input = ""
                            self.window.blit(setup_bg, (0, 0))
                            Display.draw_text(self.window, "Invalid input!",
                                              50, (255, 255, 255),
                                              self.window.get_width()//2,
                                              self.window.get_height()*1.6//4)
                            time.sleep(1)
                    # Check if the user pressed backspace
                    elif event.key == pygame.K_BACKSPACE:
                        input = input[:-1]
                    else:
                        input += event.unicode
