import unittest
from unittest.mock import patch
from game.main import start_game, play_turn, main


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


class TestTurnBased(unittest.TestCase):

    def test_turn_behavior(self):
        self.assertEqual(play_turn(), 1, msg="Turn not registered successfuly")


class TestGamePlayThrough(unittest.TestCase):
    def test_main_game_with_start(self):
        expected = 1
        with patch("builtins.input", return_value=expected):
            self.assertEqual(
                main(), 0,
                msg="Game did not properly run")

    def test_main_game_with_load(self):
        expected = 2
        with patch("builtins.input", return_value=expected):
            self.assertEqual(
                main(), 0,
                msg="Game did not properly run")
