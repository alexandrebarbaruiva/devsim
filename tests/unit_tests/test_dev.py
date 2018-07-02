import unittest
from unittest.mock import patch
from game.developer import Developer


class TestDeveloperBasics(unittest.TestCase):
    def setUp(self):
        self.dev = Developer()

    @patch('game.software.Software')
    def test_developer_code(self, software):
        """Check if developer has code method code"""
        self.assertEqual(
            self.dev.develop(software), True,
            msg="Developer has no coding method")

    @patch('game.software.Software')
    def test_developer_code_on_100(self, software):
        """Check if developer cannot code more than 100"""
        software.add_code.return_value = False
        self.assertEqual(
            self.dev.develop(software), False,
            msg="Developer can code beyond 100 completion")

    @patch('game.software.Software')
    def test_developer_release_software(self, software):
        """Check if developer can release software"""
        software.be_released.return_value = True
        self.assertEqual(
            self.dev.release(software), True,
            msg="Developer cannot release software")
