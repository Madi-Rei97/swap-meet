

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
        
    def get_by_id(self, item_id):

        for item in self.inventory:
            if item.id == item_id:
                return item 

        return None
    
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item) 
            self.inventory.append(their_item)
            other_vendor.inventory.remove(their_item)
            other_vendor.inventory.append(my_item)
            return True
        
        return False