"""All things related to Company class."""


class Company:
    """Company for aggregating all the information into one class."""

    stats = {}

    def __init__(self, name=""):
        self.stats = {
            "name": name,
            "people": {
                "leaders": [0, []],
                "designers": [0, []],
                "developers": [0, []],
                "marketers": [0, []],
            },
            "resources": {
                "money": 0,
                "fans": 0,
                "rating": 0,
            },
            "software": {
                "software": [0, []],
                "code quality": 0,
            },
        }

    def hire_person(self, person):
        print(person.stats["type"])
        employee_type = "{}s".format(person.stats["type"])
        self.stats["people"][employee_type][0] += 1
        self.stats["people"][employee_type][1].append(person)
        return "{} hired".format(person.stats["type"].title())
