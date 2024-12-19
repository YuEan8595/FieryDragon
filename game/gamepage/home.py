from gamepage.page import Page
from button import Button
from gamepage.setup import Setup
from display import Display

import pygame


class Home(Page):
    """ Home page of the game. """

    def __init__(self, page_controller, window):
        """
        This method initializes the home page.

        input:
        - page_controller: the page controller of the game
        - window: the window of the game

        return: None
        """
        super().__init__(page_controller, window)

    def run(self):
        """
        This method runs the home page.
        The home page has two buttons, start and quit.
        The start button will change the page to the setup page.
        The quit button will quit the game.

        return: None
        """
        # Load images
        home_bg = Display.load_bg(
            self.window, 'Project/img/bg_img/home_bg.png')
        start_button_img_path = 'Project/img/button_img/start.png'
        quit_button_img_path = 'Project/img/button_img/quit.png'

        # Set scale and create button instances
        start_button_scale = 0.3
        quit_button_scale = 0.2
        start_button = Button(start_button_img_path, start_button_scale)
        quit_button = Button(quit_button_img_path, quit_button_scale)

        # Set the display position
        start_button.set_pos(self.window.get_width()//2,
                             self.window.get_height()//2)
        quit_button.set_pos(self.window.get_width()//2,
                            self.window.get_height()*2.2//3)

        run = True
        while run:
            self.window.blit(home_bg, (0, 0))
            start_button.draw(self.window)
            quit_button.draw(self.window)

            if start_button.is_clicked():
                run = False
            if quit_button.is_clicked():
                Display.quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.quit()

            pygame.display.update()

        self.change_page(Setup(self.page_controller, self.window))
