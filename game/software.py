"""All things related to software class."""


class Software:
    """Class to be designed, developed, marketed and sold by employees."""
    def __init__(self, name, progress=0, bugs=0):
        self.stats = {"name": name, "progress": progress, "bugs": bugs, "released": False}
        if progress < 100:
            self.stats["releasable"] = False
        else:
            self.stats["progress"] = 100
            self.stats["releasable"] = True

    def get_name(self):
        return self.stats.get("name", "Name not found.")

    def get_progress(self):
        return self.stats.get("progress", 0)

    def add_code(self):
        if self.stats["progress"] >= 99:
            if self.stats["progress"] >= 100:
                self.stats["progress"] = 100
                return False
            self.stats["releasable"] = True
        self.stats["progress"] += 1
        return True

    def be_released(self):
        if self.stats["releasable"] and not self.stats["released"]:
            self.stats["releasable"] = False
            self.stats["released"] = True
            return True
        return False
