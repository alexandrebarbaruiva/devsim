"""All things related to software class."""


class Software:
    """Class to be designed, developed, marketed and sold by employees."""
    stats = {}

    def __init__(self, name, completion=0, bugs=0):
        self.stats["name"] = name
        self.stats["completion"] = completion
        self.stats["bugs"] = bugs
        self.stats["released"] = False
        if completion < 100:
            self.stats["releasable"] = False
        else:
            self.stats["completion"] = 100
            self.stats["releasable"] = True

    def add_code(self):
        if self.stats["completion"] >= 99:
            if self.stats["completion"] >= 100:
                self.stats["completion"] = 100
                return False
            self.stats["releasable"] = True
        self.stats["completion"] += 1
        return True

    def be_released(self):
        if self.stats["releasable"] and not self.stats["released"]:
            self.stats["releasable"] = False
            self.stats["released"] = True
            return True
        return False
