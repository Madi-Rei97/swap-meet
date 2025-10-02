from .item import Item

class Decor(Item):

    def __init__(self, id=None, condition=0, age=0, width=0, length=0):
        super().__init__(id, condition, age)
        self.width = width if width ==0 else width
        self.length = length if length ==0 else length

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space."
