class Employee:
    stats = {}

    def __init__(self, happy=0, stress=0):
        self.stats["happy"] = happy
        self.stats["stress"] = stress
