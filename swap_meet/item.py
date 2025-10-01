import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition


    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
        
    def condition_description(self):
        if self.condition == 0:
            return "Trash"
        if self.condition == 1:
            return "Heavily used"
        if self.condition == 3:
            return "Moderately used"
        if self.condition == 4:
            return "Lightly used"
        if self.condition == 5:
            return "Like new"

