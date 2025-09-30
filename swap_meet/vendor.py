

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            return self.inventory.pop(item)
        else: 
            return False
        
    def get_by_id(self, item_id):
        if item_id not in self.inventory:
            return None
        else:
            return 