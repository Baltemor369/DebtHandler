class Person:
    def __init__(self, name, debt=0):
        self.name = name
        self.debt = debt

    def to_dict(self):
        return {
            "name": self.name,
            "debt": self.debt
        }