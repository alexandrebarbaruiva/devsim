from game.employee import Employee


class Developer(Employee):
    def develop(self, software):
        software.stats["completion"] += 1
        return True
