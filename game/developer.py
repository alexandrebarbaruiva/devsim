"""All things related to developer class."""

from game.employee import Employee


class Developer(Employee):
    """Employee for developing Software and removing bugs."""
    def __init__(self):
        self.stats["type"] = "developer"

    def develop(self, software):
        """Develops 1 unit code on specific software."""
        if software.add_code():
            return True
        return False

    def release(self, software):
        """Release a software when it has 100 completion"""
        return software.be_released()
