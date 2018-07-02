import sys
import os
import unittest
from unittest.mock import patch
from game.developer import Developer


class TestDeveloperBasics(unittest.TestCase):
    def setUp(self):
        self.dev = Developer()

    @patch('game.software.Software')
    def test_developer_code(self, soft):
        """Check if developer has code method code"""
        self.assertEqual(
            self.dev.develop(soft), True,
            msg="Developer has no coding method")
