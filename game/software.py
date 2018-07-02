class Software:
    stats = {}

    def __init__(self, completion=0, bugs=0):
        self.stats["completion"] = completion
        self.stats["bugs"] = bugs

    def add_code(self):
        self.stats["completion"] += 1
        return self.stats["completion"]
