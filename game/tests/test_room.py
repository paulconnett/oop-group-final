"""
Unittesting Shop and Dungeon classes
"""

__author__ = "Paul Connett"

import unittest
from unittest.mock import MagicMock, patch

from room import Shop, Dungeon
from player import Player


class TestShop(unittest.TestCase):
    """
    Unittest shop class
    """
    def setUp(self) -> None:
        self.player = Player()
        self.shop = Shop(level=1, player=self.player)

    @patch.object(Shop, "buy_items")
    @patch("builtins.input")
    def test_shop_play_room_yes(self, mock_input, mock_buy_items) -> None:
        """
        Tests that play_room calls buy_items when user answers y
        """
        mock_input.side_effect = ["", "y"]
        self.shop.play_room(self.player)
        mock_buy_items.assert_called_once_with(self.shop._items)

    @patch("builtins.input")
    def test_shop_play_room_no(self, mock_input) -> None:
        """
        Tests that play_room returns when user enters n
        """
        mock_input.side_effect = ["", "n", ""]
        result = self.shop.play_room(self.player)
        self.assertIsNone(result)

    @patch("builtins.input", return_value="1")
    def test_shop_buy_items(self, _mock_input) -> None:
        """
        Tests that buy_items calls player's spend_money
        """
        mock_player = MagicMock()
        mock_player.spend_money.return_value = True
        shop = Shop(level=1, player=mock_player)

        shop.buy_items(shop._items)
        mock_player.spend_money.assert_called_once()

    @patch("builtins.input", return_value="1")
    def test_buy_items_cannot_afford(self, _mock_input) -> None:
        """
        Tests that buy_items returns "You can't affor that!" when out of money
        """
        mock_player = MagicMock()
        mock_player.spend_money.return_value = False
        shop = Shop(level=1, player=mock_player)

        with patch("builtins.input") as mock_input2:
            shop.buy_items(shop._items)
            mock_input2.assert_called_with("You can't afford that!")


class TestDungeon(unittest.TestCase):
    """
    Unittesting Dungeon class
    """
    def setUp(self) -> None:
        self.player = Player("Tester")
        self.dungeon = Dungeon(level=1, player=self.player)

    @patch.object(Dungeon, "combat")
    def test_dungeon_play_room(self, mock_combat) -> None:
        """
        Tests that play_room calls combat()
        """
        self.dungeon.play_room(self.player)

        mock_combat.assert_called_once()

    def test_dungeon_str(self) -> None:
        """
        Tests that __str__ returns empty string
        """
        self.assertEqual(str(self.dungeon), "")
