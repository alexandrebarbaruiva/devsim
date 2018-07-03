import unittest
from game.company import Company
from game.developer import Developer


class TestWorkingCompany(unittest.TestCase):
    def setUp(self):
        self.comp = Company()
        self.dev = Developer()

    def test_company_hiring_developer(self):
        """Check if company has expected behaviour when hiring devs"""
        self.assertEqual(
            self.comp.stats["people"]["developers"][0], 0,
            msg="Company has more than 0 developers")
        self.assertEqual(
            self.comp.hire_person(self.dev), "Developer hired",
            msg="Company hasn't hired any developers")
        self.assertEqual(
            self.comp.stats["people"]["developers"][0], 1,
            msg="Company has more than 1 developer")
