class Employee:
    def __init__(self, happy=0, stress=0, name=""):
        self.stats = {
            "name": name,
            "type": "employee",
            "happy": happy,
            "stress": stress,
        }
