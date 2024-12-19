from main import Main
from gamepage.home import Home
from gamepage.game import Game
from gamepage.page_controller import PageController
from action.forward_action import ForwardAction
from action.backward_action import BackwardAction

import unittest
import pygame

class TestGame(unittest.TestCase):
    # Test the initial state of the game
    def test_game(self):
        self.assertEqual(type(Main().state), Home)

#---------------------test for backward---------------------#
    # Test the position of player after penalty card is drawn
    def test_penalty(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 1
        player2 = game.players[current_player_index]
        player2.set_pos(20, game.gameboard.get_board()[20].get_pos())
        penalty_step = 2
        self.assertEqual(player2.get_board_pos(), 20)   # Check player board position
        action = BackwardAction(player2.get_board_pos(), penalty_step, player2, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 18)    # Check destination for this action
        end_turn = action.execute()
        self.assertEqual(player2.get_board_pos(), 18)   # Check player board position after executing the action
        self.assertEqual(end_turn, False)   # Check the player's turn, supposed to be False
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player2.x-10, player2.y), game.gameboard.get_board()[18].get_pos())  
    
    # Test whether player moves beyond his cave when penalty is drawn
    def test_penalty_beyond_own_cave(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 1
        player2 = game.players[current_player_index]
        player2.set_pos(8, game.gameboard.get_board()[8].get_pos()) # Player 2's cave is in position 7
        penalty_step = 2
        self.assertEqual(player2.get_board_pos(), 8)   # Check player board position
        action = BackwardAction(player2.get_board_pos(), penalty_step, player2, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 7)    # Check destination for this action
        end_turn = action.execute()
        self.assertEqual(player2.get_board_pos(), 7)   # Check player board position after executing the action
        self.assertEqual(end_turn, False)   # Check the player's turn, supposed to be False
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player2.x-10, player2.y), game.gameboard.get_board()[7].get_pos())

    # Test whether player enters other player's cave when penalty is drawn
    def test_penalty_pass_other_cave(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 1
        player2 = game.players[current_player_index]
        player2.set_pos(1, game.gameboard.get_board()[1].get_pos()) # Player 1's cave is in position 0
        penalty_step = 2
        self.assertEqual(player2.get_board_pos(), 1)   # Check player board position
        action = BackwardAction(player2.get_board_pos(), penalty_step, player2, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 26)    # Check destination for this action
        end_turn = action.execute()
        self.assertEqual(player2.get_board_pos(), 26)   # Check player board position after executing the action
        self.assertEqual(end_turn, False)   # Check the player's turn, supposed to be False
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player2.x-10, player2.y), game.gameboard.get_board()[26].get_pos())
        
    # Test landing on position which is occupied
    def test_penalty_destination_is_occupied(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 1
        player2 = game.players[current_player_index]
        player2.set_pos(11, game.gameboard.get_board()[11].get_pos()) # Player 1's cave is in position 0
        penalty_step = 2

        # Player1 will be the one who occupied the expected destination of player2
        player1 = game.players[0]
        player1.set_pos(8, game.gameboard.get_board()[8].get_pos()) # Player 1's cave is in position 0
        # Move player1 to position 9 where position 9 is supposed to be the expected destination of player2
        player1action = ForwardAction(player1.get_board_pos(), 1, player1, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        player1action.execute()

        # Now movw player2 to position 9 where position 9 is occupied by player1
        action = BackwardAction(player2.get_board_pos(), penalty_step, player2, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 9)    # Backward action only determine the final destination, it does not check whether the destination is occupied
        end_turn = action.execute()
        self.assertEqual(player2.get_board_pos(), 11)   # Check player board position after executing the action
        self.assertEqual(end_turn, True)   # Check the player's turn, supposed to be true
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player2.x-10, player2.y), game.gameboard.get_board()[11].get_pos())

#---------------------test for forward---------------------#
    # Test the position of player after a matching chitcard is drawn
    def test_forward(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 3
        player4 = game.players[current_player_index]
        player4.set_pos(22, game.gameboard.get_board()[22].get_pos())
        forward_step = 2
        action = ForwardAction(player4.get_board_pos(), forward_step, player4, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 24)
        end_turn, end_game = action.execute()
        self.assertEqual(player4.get_board_pos(), 24)   # Check player board position after executing the action
        self.assertEqual(end_turn, False)   # Check the player's turn, supposed to be false
        self.assertEqual(end_game, False)   # Check the game's end, supposed to be false
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player4.x-10, player4.y), game.gameboard.get_board()[24].get_pos())

    # Test when player pass a cave (supposed to skip a cave)
    def test_forward_pass_cave(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 3
        player4 = game.players[current_player_index]
        player4.set_pos(27, game.gameboard.get_board()[27].get_pos())
        forward_step = 2
        action = ForwardAction(player4.get_board_pos(), forward_step, player4, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 2)
        end_turn, end_game = action.execute()
        self.assertEqual(player4.get_board_pos(), 2)   # Check player board position after executing the action
        self.assertEqual(end_turn, False)   # Check the player's turn, supposed to be false
        self.assertEqual(end_game, False)   # Check the game's end, supposed to be false
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player4.x-10, player4.y), game.gameboard.get_board()[2].get_pos())

    # Test whether player pass his own cave (supposed to remain in the same position)
    def test_forward_move_beyond_own_cave(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 3
        player4 = game.players[current_player_index]
        player4.set_pos(20, game.gameboard.get_board()[20].get_pos())
        forward_step = 2
        action = ForwardAction(player4.get_board_pos(), forward_step, player4, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, None)
        end_turn, end_game = action.execute()
        self.assertEqual(player4.get_board_pos(), 20)   # Check player board position after executing the action
        self.assertEqual(end_turn, True)   # Check the player's turn, supposed to be true
        self.assertEqual(end_game, False)   # Check the game's end, supposed to be false
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player4.x-10, player4.y), game.gameboard.get_board()[20].get_pos())
        
    # Test landing on position which is occupied
    def test_forward_destination_is_occupied(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 1
        player2 = game.players[current_player_index]
        player2.set_pos(7, game.gameboard.get_board()[7].get_pos())
        forward_step = 2

        # Manually move player1 to position 9
        player1 = game.players[0]
        player1.set_pos(8, game.gameboard.get_board()[8].get_pos()) # Player 1's cave is in position 0
        # Move player1 to position 9 where position 9 is supposed to be the expected destination of player2
        player1action = ForwardAction(player1.get_board_pos(), 1, player1, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        player1action.execute()
        
        action = ForwardAction(player2.get_board_pos(), forward_step, player2, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 9) # Forward action only determine the final destination, it does not check whether the destination is occupied
        end_turn, end_game = action.execute()
        self.assertEqual(player2.get_board_pos(), 7)   # Check player board position after executing the action
        self.assertEqual(end_turn, True)   # Check the player's turn, supposed to be false
        self.assertEqual(end_game, False)   # Check the game's end, supposed to be false
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player2.x-10, player2.y), game.gameboard.get_board()[7].get_pos())
        
    # Test whether the game stop if a player wins
    def test_win(self):
        window = pygame.display.set_mode((800, 800))
        page_controller = PageController(Main())
        game = Game(page_controller, window, 4)
        current_player_index = 3
        player4 = game.players[current_player_index]
        player4.set_pos(19, game.gameboard.get_board()[19].get_pos())
        forward_step = 2
        action = ForwardAction(player4.get_board_pos(), forward_step, player4, game.gameboard.get_board(), game.gameboard.get_cave_distance())
        self.assertEqual(action.destination, 21)
        end_turn, end_game = action.execute()
        self.assertEqual(player4.get_board_pos(), 21)   # Check player board position after executing the action
        self.assertEqual(end_turn, False)   # Check the player's turn, supposed to be false
        self.assertEqual(end_game, True)   # Check the game's end, supposed to be true
        # Check player's display x and y coordinate, noted that player's x coordinate is increased by 10 so that it does not block the animal image
        self.assertEqual((player4.x-10, player4.y), game.gameboard.get_board()[21].get_pos())

if __name__ == '__main__':
    unittest.main()