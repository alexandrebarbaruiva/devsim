import unittest
from game.main import start_game


class TestGameMenu(unittest.TestCase):
    def test_start_game(self):
        """Check if game starts properly"""
        self.assertEqual(start_game(), True, msg="Missing Employee attributes")
