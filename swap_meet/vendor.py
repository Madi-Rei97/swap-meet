

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
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        elif self.inventory and other_vendor.inventory:
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0]) 
            other_vendor.inventory.remove(other_vendor.inventory[0])
            return True
        
    def get_by_category(self, category):
        
        list_of_items = []

        for item in self.inventory:
            if item.get_category() == category:
                list_of_items.append(item)

        return list_of_items

    def get_best_by_category(self, category):

        if self.inventory: 
            dictionary = {}

            for item in self.inventory:
                if item.get_category() == category:
                    dictionary[item] = item.condition
    
            for item, condition in dictionary.items():
                if condition == 5:
                    return item
    
            for item, condition in dictionary.items():
                if condition == 4:
                    return item
                
            for item, condition in dictionary.items():
                if condition == 3:
                    return item
                
            
            for item, condition in dictionary.items():
                if condition == 2:
                    return item
            
            for item, condition in dictionary.items():
                if condition == 1:
                    return item
            
            for item, condition in dictionary.items():
                if condition == 0:
                    return item
        else: 
            return None


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        swap = self.swap_items(other_vendor, my_item, their_item)

        return swap





"""

Optional Enhancements
Should a project be completed before submission, and there is a desire for optional enhancements, consider this idea:

Items have age

Add an age attribute to all Items
Implement a Vendor method named swap_by_newest, using any logic that seems appropriate
Write unit tests for swap_by_newest
Take a look for error handling opportunities

What issues could arise if we pass a string (or any object other than an integer) for the id of an Item? How could we prevent that?
What other opportunities for error handling do you see?
What is our test suite missing?

Identify gaps or edge cases it'd be helpful to cover
Write tests for the cases you identify
"""


