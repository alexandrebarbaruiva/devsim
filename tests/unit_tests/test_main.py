import unittest
from unittest.mock import patch
from game.main import start_game


class TestGameMenu(unittest.TestCase):

    def test_start_game(self):
        """Check if game starts properly."""
        expected = 1
        with patch("builtins.input", return_value=expected):
            self.assertEqual(start_game(), expected,
                             msg="Missing Start Game option")

    def test_start_game_with_wrong_input_type(self):
        """Check if game doesn't start when passed wrong input."""
        expected = ("a", 1)
        with patch("builtins.input", side_effect=expected):
            self.assertEqual(start_game(), 1,
                             msg="Missing Start Game option")

    def test_start_game_with_multiple_wrong_input_types(self):
        """Check if game doesn't start when passed multiple wrong inputs."""
        expected = ("a", "b", "c", 2)
        with patch("builtins.input", side_effect=expected):
            self.assertEqual(start_game(), 2,
                             msg="Missing Start Game option")

    def test_start_game_with_wrong_input_number(self):
        """Check if game doesn't start when passed wrong input number."""
        expected = (5, 1)
        with patch("builtins.input", side_effect=expected):
            self.assertEqual(start_game(), 1,
                             msg="Missing Start Game option")
