from gamepage.page import Page
from display import Display

import pygame


class End(Page):
    """
    End page of the game.
    Used to show the winner of the game and let the player to redirect to 
    the home page if they want to play the game again.
    """

    def __init__(self, page_controller, window, winner_img_path):
        """
        This method initializes the end page.

        input:
        - page_controller: the page controller of the game
        - window: the window of the game
        - winner_img_path: the image path of the winning player

        return: None
        """
        super().__init__(page_controller, window)
        self.winner_img_path = winner_img_path

    def run(self):
        """
        This method runs the end page of the game which shows the winner.
        The player is able to play again by pressing the space bar.
        After pressing space bar, the player will be directed back to the 
        home page.

        return: None
        """
        end_bg = Display.load_bg(self.window, 'Project/img/bg_img/end_bg.png')

        run = True
        while run:
            self.window.blit(end_bg, (0, 0))
            Display.draw_text(self.window, "Game Winner:", 40, (0, 0, 0),
                              self.window.get_width()//6, 
                              self.window.get_height()//15, False)
            Display.draw_text(self.window, "Press SPACE to play again", 18, (0, 0, 0),
                              self.window.get_width()//2, 
                              self.window.get_height()*2.9//3, False)

            # Load player image (token)
            winner_img = Display.load_img(self.winner_img_path, 1)
            # Draw player image (token)
            Display.draw_img(self.window, winner_img, self.window.get_width()//2, 
                             self.window.get_height()//2)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False

        # If the player clicks space bar they will be directed back to the
        # home page
        # The import is done inside the method to avoid circular import
        from gamepage.home import Home
        self.change_page(Home(self.page_controller, self.window))
