class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):

        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item

    def get_by_id(self, item_id):

        for item in self.inventory:
            if item.id == item_id:
                return item 

        return None
    
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
            
        self.inventory.remove(my_item) 
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)
        return True

    
    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

        # self.inventory.append(other_vendor.inventory[0])
        # other_vendor.inventory.append(self.inventory[0])
        # self.inventory.remove(self.inventory[0]) 
        # other_vendor.inventory.remove(other_vendor.inventory[0])
        
        
    def get_by_category(self, category):
        
        # list_of_items = []

        # for item in self.inventory:
        #     if item.get_category() == category:
        #         list_of_items.append(item)

        # return list_of_items
    
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):

        best_item = None
        best_condition = -1

        if not self.inventory:
            return best_item

        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item

                    if best_condition == 5:
                        return best_item
        
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        swap = self.swap_items(other_vendor, my_item, their_item)

        return swap

    def get_newest(self):

        newest_item = None

        if not self.inventory:
            return newest_item

        newest_item = self.inventory[0]

        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item

        return newest_item

    def swap_by_newest(self, other_vendor):
        
        my_item = self.get_newest()
        their_item = other_vendor.get_newest()
        swap = self.swap_items(other_vendor, my_item, their_item)

        return swap

