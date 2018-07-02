import unittest
from game.software import Software


class TestSoftwareBasics(unittest.TestCase):
    def setUp(self):
        self.soft = Software()

    def test_software_attributes(self):
        """Check if software has all the right attributes."""
        self.assertEqual(
            self.soft.stats,
            {
                "completion": 0,
                "bugs": 0,
                "releasable": False,
                "released": False,
            },
            msg="Incorrect Software attributes")

    def test_completed_software(self):
        """Check for releasability when creating a complete software."""
        self.soft = Software(completion=100)
        self.assertEqual(self.soft.stats["releasable"], True)

    def test_software_development(self):
        """Check if software development can occur."""
        self.assertEqual(
            self.soft.add_code(), True,
            msg="Software development not occuring"
        )

    def test_software_completion(self):
        """Check for change in releasable stat when software reaches 100."""
        self.soft.stats["completion"] = 99
        self.soft.add_code()
        self.assertEqual(
            self.soft.stats["releasable"], True,
            msg="Software release readiness not occuring"
        )

    def test_software_completed(self):
        """Check for change in releasable stat when software reaches 100."""
        self.soft = Software(100)
        self.soft.add_code()
        self.assertEqual(
            self.soft.add_code(), False,
            msg="Software overdevelopment"
        )

    def test_software_to_be_released(self):
        """Check if software is released with be_released."""
        self.soft = Software(100)
        self.assertEqual(
            self.soft.be_released(), True,
            msg="Software release not occuring"
        )
        self.assertEqual(
            self.soft.stats["releasable"], False,
            msg="Software releasable stat wrong"
        )
        self.assertEqual(
            self.soft.stats["released"], True,
            msg="Software released stat wrong"
        )

    def test_software_rerelease(self):
        """Check if software once released cannot be rereleased."""
        self.soft = Software(100)
        self.soft.be_released()
        self.assertEqual(
            self.soft.be_released(), False,
            msg="Software rerelease occuring"
        )
        self.assertEqual(
            self.soft.stats["releasable"], False,
            msg="Software releasable stat wrong"
        )
        self.assertEqual(
            self.soft.stats["released"], True,
            msg="Software released stat wrong"
        )
