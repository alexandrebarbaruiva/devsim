import unittest
from unittest.mock import patch
from game.main import start_game, display_turn, main,\
    set_up_player, action_turn


class TestGameMenu(unittest.TestCase):
    """Test all functions that generate a menu."""

    def test_start_game(self):
        """Check if game menu starts properly."""
        expected = 1
        with patch("builtins.input", return_value=expected):
            self.assertEqual(start_game(), expected,
                             msg="Missing Start Game option")

    def test_start_game_with_wrong_input_type(self):
        """Check if game menu doesn't start when passed wrong input."""
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
        """Check if game menu doesn't start when passed wrong input number."""
        expected = (5, 1)
        with patch("builtins.input", side_effect=expected):
            self.assertEqual(start_game(), 1,
                             msg="Missing Start Game option")

    def test_player_set_up(self):
        """Check if setup menu accepts input and returns accordingly."""
        expected = "Rich Company"
        with patch("builtins.input", return_value=expected):
            self.assertEqual(
                set_up_player(), "Rich Company",
                msg="Game did not properly run")

    def test_choose_action(self):
        with patch("builtins.input", return_value=1):
            self.assertEqual(
                action_turn(), 1,
                msg="Game did not properly return expected choice")

    def test_choose_action_wrong_input(self):
        expected = ("a", 2)
        with patch("builtins.input", side_effect=expected):
            self.assertEqual(
                action_turn(), 2,
                msg="Game did not properly return expected choice")


class TestTurns(unittest.TestCase):
    """Test what each game turn returns."""
    def test_turn_choice_behavior(self):
        with patch("builtins.input", return_value=1):
            self.assertEqual(
                action_turn(), 1,
                msg="Game did not properly return expected action")


    def test_turn_behavior(self):
        self.assertEqual(display_turn(), 1, msg="Turn not registered successfuly")

    @patch('game.company.Company')
    def test_turn_behavior_with_company(self, company):
        company.stats = {"name": "Test", "age": 0, "fans": 0, "rating": 0}
        with patch.dict(company.stats):
            self.assertEqual(
                display_turn(company=company), 1,
                msg="Turn not registered successfuly"
            )


class TestGamePlayThrough(unittest.TestCase):
    """Test main function. Soon has to be moved to integration test."""
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
