from board.cave import Cave
from board.volcano import Volcano
from board.land_type import LandType
from gamecard.animal_type import AnimalType

import random
import pygame
import math


class GameBoard:
    """
    This class is used to create the gameboard.
    The gameboard contains the caves and volcanoes.
    The gameboard manages the creation and arrangement of the caves and 
    volcanoes on the gameboard.
    The board is represented as a list and every 7th element is a cave, 
    others are volcanoes.
    """
    MIN_CAVE = 4    # Minimum number of caves

    def __init__(self, window, players, size, animal_num):
        """
        This method initializes the gameboard.

        input:
        - window: the pygame window
        - players: the list of players
        - size: the number of volcanoes
        - animal_num: the number of animal types

        return: None
        """
        self.window = window
        self.players = players
        self.size = size
        self.animal_num = animal_num
        self.player_num = len(self.players)
        # Distance between caves
        self.cave_distance = int(
            self.size / max(GameBoard.MIN_CAVE, self.player_num)) + 1
        self.caves = self._create_caves()
        self.volcanoes = self._create_volcanoes()
        self._set_position()    # Set caves and volcanoes' display position
        self.board = self._create_board()

    def get_board(self):
        """
        The getter method to return the gameboard array.

        return: list
        """
        return self.board

    def get_cave_distance(self):
        """
        The getter method to return the distance between caves.

        return: int
        """
        return self.cave_distance

    def draw(self):
        """
        This method is used to draw the gameboard on the window display.

        return: None
        """
        self.window.fill((221, 209, 178))
        for volcano in self.volcanoes:
            volcano.draw(self.window)
        for cave in self.caves:
            cave.draw(self.window)

    def _create_board(self):
        """
        This method creates the gameboard array.
        The gameboard array is a list that represents the gameboard.
        The gameboard array contains the caves and volcanoes.
        It helps to arrange the caves and volcanoes on the gameboard.

        return: list
        """
        board_size = self.size + max(GameBoard.MIN_CAVE, self.player_num)
        board = [None] * board_size
        cave_index_list = [i for i in range(0, board_size, self.cave_distance)]

        # Place the caves on the board
        for i in range(len(self.caves)):
            board[cave_index_list[i]] = self.caves[i]

        # Mark the position of the players
        for i in range(len(self.players)):
            self.players[i].set_pos(
                cave_index_list[i], board[cave_index_list[i]].get_pos())

        # For 2 players case, the caves will be placed opposite to each other
        # Specific for 2 players only
        if self.player_num == 2:
            # Change player id to 2 to match the cave id which will be used
            # to determine the player's cave
            self.players[1].set_id(2)
            # Set the position for the second player based on the player's
            # new cave
            self.players[1].set_pos(
                cave_index_list[2], board[cave_index_list[2]].get_pos())

        # Place the volcanoes on the remaining board
        i = 0
        for volcano in self.volcanoes:
            while board[i] is not None:
                i += 1
            board[i] = volcano

        return board

    def _create_caves(self):
        """
        This method creates the caves.
        The minimum number of caves is 4.

        return: list
        """
        # Load cave images path
        cave_images_path = ["Project/img/cimg/ba_cave.png", "Project/img/cimg/bd_cave.png",
                            "Project/img/cimg/sa_cave.png", "Project/img/cimg/sp_cave.png"]
        # Create caves
        caves = []
        scale = 0.055
        for i in range(max(GameBoard.MIN_CAVE, self.player_num)):
            caves.append(
                Cave(i, AnimalType(i), LandType.CAVE, cave_images_path[i], scale))

        return caves

    def _create_volcanoes(self):
        """
        This method creates the volcanoes and shuffle the position.

        return: list
        """
        # Load volcano images
        volcano_images_path = ["Project/img/vimg/ba.png", "Project/img/vimg/bd.png",
                               "Project/img/vimg/sa.png", "Project/img/vimg/sp.png"]
        # Create volcanoes
        volcanoes = []
        scale = 0.055
        # A total of (board_size/animal_num) volcanoes will be created for
        # each type of animal
        for i in range(self.animal_num):
            for _ in range(int(self.size//self.animal_num)):
                volcanoes.append(
                    Volcano(AnimalType(i), LandType.VOLCANO, volcano_images_path[i], scale))
        random.shuffle(volcanoes)
        return volcanoes

    def _set_position(self):
        """
        This method sets the display position of the caves and volcanoes.

        return: None
        """
        window_w = self.window.get_width()
        window_h = self.window.get_height()

        self._set_cave_pos(window_w, window_h)
        self._set_vol_pos(window_w, window_h)

    def _set_cave_pos(self, window_w, window_h):
        """
        This method sets the display position of the caves.
        It arranges the caves in a circular pattern where the radius is 
        slightly larger than the volcanoes' circular pattern.
        Tile size and tile density control the radius of the circular 
        pattern.
        The higher the tile density, the smaller the interval between the 
        caves.

        input:
        - window_w: the width of the window
        - window_h: the height of the window

        return: None
        """
        tile_num = len(self.caves)
        tile_size = 43
        tile_density = 0.6

        for i in range(tile_num):
            x = window_w // 2 + (tile_size * (tile_num // tile_density)) * (
                pygame.math.Vector2(1, 0).rotate_rad(
                    i * 2 * math.pi / tile_num)
            ).x
            y = window_h // 2 + (tile_size * (tile_num // tile_density)) * (
                pygame.math.Vector2(1, 0).rotate_rad(
                    i * 2 * math.pi / tile_num)
            ).y
            self.caves[i].set_pos(x, y)

    def _set_vol_pos(self, window_w, window_h):
        """
        This method sets the display position of the volcanoes.
        It arranges the volcanoes in a circular pattern where the radius is 
        slightly smaller than the caves' circular pattern.
        Tile size and tile density control the radius of the circular 
        pattern.
        The higher the tile density, the smaller the interval between the 
        volcanoes.

        input:
        - window_w: the width of the window
        - window_h: the height of the window

        return: None
        """
        tile_num = self.size
        tile_size = 43
        tile_density = 4.5

        for i in range(tile_num):
            x = window_w // 2 + (tile_size * (tile_num // tile_density)) * (
                pygame.math.Vector2(1, 0).rotate_rad(
                    i * 2 * math.pi / tile_num)
            ).x
            y = window_h // 2 + (tile_size * (tile_num // tile_density)) * (
                pygame.math.Vector2(1, 0).rotate_rad(
                    i * 2 * math.pi / tile_num)
            ).y
            self.volcanoes[i].set_pos(x, y)
