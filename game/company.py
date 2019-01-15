"""All things related to Company class."""
from game.software import Software


class Company:
    """Company for aggregating all the information into one class."""
    def __init__(self, name="", rating=0, fans=0):
        self.stats = {
            "name": name,
            "age": 0,
            "rating": rating,
            "fans": fans,
            "employees": {
                "leaders": [0, []],
                "designers": [0, []],
                "developers": [0, []],
                "marketers": [0, []],
            },
            "software": [],
            "financial": {
                "funds": 0,
            },
            "product stats": {
                "software": [0, []],
            },
        }

    def create_software(self, name):
        new_software = Software(name=name)
        self.stats["software"].append(new_software)

    def hire_person(self, person):
        print(person.stats["type"])
        employee_type = "{}s".format(person.stats["type"])
        self.stats["employees"][employee_type][0] += 1
        self.stats["employees"][employee_type][1].append(person)
        return "{} hired".format(person.stats["type"].title())
