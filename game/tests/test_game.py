"""
Unittesting Game class
"""

__author__ = "Paul Connett"

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys

from game import Game
from room import Room, Shop, Dungeon
from player import Player


class TestGame(unittest.TestCase):
    """
    Unittesting Game class
    """

    def setUp(self) -> None:
        """
        Setup method - creates a Game object every time a test is run
        """
        self.game = Game()

    @patch("builtins.input", return_value="")
    def test_play_game(self, _mock_input) -> None:
        """
        Tests that play_game calls play_room
        """
        test_room = MagicMock()
        self.game._rooms = [test_room]

        self.game.play_game()

        test_room.play_room.assert_called_once_with(self.game.player)

    @patch.object(Game, "play_game")
    def test_main(self, mock_play_game) -> None:
        """
        Tests main static method creates a Game instance and calls play_game()
        """
        Game.main()

        mock_play_game.assert_called_once()
