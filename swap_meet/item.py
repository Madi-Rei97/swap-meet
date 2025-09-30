import uuid

class Item:
    def __init__(self, id = None):
        self.id = uuid.uuid4().int if id is None else id

    def get_category(self):
        return "Item"
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory[my_item] = their_item
            other_vendor.inventory[their_item] = my_item
            return True
        
        return False

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
        

