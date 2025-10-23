import uuid

class Item:
    def __init__(self, id=None, condition=0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age


    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
        
    def condition_description(self):
        if self.condition < 1:
            return "Trash"
        if self.condition >= 1 and self.condition < 2:
            return "Heavily used"
        if self.condition >= 2 and self.condition < 3:
            return "Between the rag box and donation"
        if self.condition >= 3 and self.condition < 4:
            return "Moderately used"
        if self.condition >= 4 and self.condition < 5:
            return "Lightly used"
        if self.condition >= 5:
            return "Like new"

    def get_age(self):
        return self.age
