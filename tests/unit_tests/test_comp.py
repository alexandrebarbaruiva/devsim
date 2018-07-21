import unittest
from unittest.mock import patch
from game.company import Company


class TestCompanyBasics(unittest.TestCase):
    def setUp(self):
        self.comp = Company()

    def test_company_attributes(self):
        """Check if company has all the right attributes"""
        self.assertEqual(
            self.comp.stats,
            {
                "name": "",
                "age": 0,
                "rating": 0,
                "fans": 0,
                "employees": {
                    "leaders": [0, []],
                    "designers": [0, []],
                    "developers": [0, []],
                    "marketers": [0, []],
                },
                "financial": {
                    "funds": 0,
                },
                "product stats": {
                    "software": [0, []],
                },
            },
            msg="Missing Company attributes")

    @patch('game.developer.Developer')
    def test_company_hire(self, dev):
        """Check if company can hire people."""
        dev.stats = {}
        with patch.dict(dev.stats, {"type": "developer"}):
            self.assertEqual(
                self.comp.hire_person(dev), "Developer hired",
                msg="Company hasn't hired any developers")
