import unittest
from game.software import Software


class TestSoftwareBasics(unittest.TestCase):
    def setUp(self):
        self.soft = Software()

    def test_software_attributes(self):
        """Check if software has all the right attributes"""
        self.assertEqual(
            self.soft.stats,
            {
                "completion": 0,
                "bugs": 0,
            },
            msg="Missing Software attributes")

    def test_software_development(self):
        """Check if software development can occur"""
        self.assertEqual(
            self.soft.add_code(), 1,
            msg="Software development not occuring"
        )
