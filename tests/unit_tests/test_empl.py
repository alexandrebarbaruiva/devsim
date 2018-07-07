import unittest
from game.employee import Employee


class TestEmployeeBasics(unittest.TestCase):
    def setUp(self):
        self.emp = Employee()

    def test_employee_attributes(self):
        """Check if employee has all the right attributes"""
        self.assertEqual(
            self.emp.stats,
            {
                "name": "",
                "type": "employee",
                "happy": 0,
                "stress": 0,
            },
            msg="Missing Employee attributes")
