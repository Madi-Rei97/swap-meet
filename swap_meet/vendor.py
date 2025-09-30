

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
    
    def swap_first_item():
        """It takes one argument: an instance of another Vendor (other_vendor), representing the friend that the vendor is swapping with
This method considers the first item in the instance's inventory, and the first item in the friend's inventory
It removes the first item from its inventory, and adds the friend's first item
It removes the first item from the friend's inventory, and adds the instances first item
It returns True
If either itself or the friend have an empty inventory, the method returns False"""
        pass

    def get_by_category():

        """Vendor objects have an instance method named get_by_category

This method takes one argument: a string, representing a category
This method returns a list of objects in the inventory with that category
If there are no items in the inventory that match the category argument, the method returns an empty list
"""
        pass

    def get_best_by_category():

        """It takes one argument: a string that represents a category
This method looks through the instance's inventory for the item with the highest condition and matching category
It returns this item
If there are no items in the inventory that match the category, it returns None
It returns a single item even if there are duplicates (two or more of the same item with the same condition)"""

        pass

    def swap_best_by_category():

        """The remaining tests in wave 6 imply:

Vendors have a method named swap_best_by_category, which will swap the best item of certain categories with another Vendor
It takes in three arguments
other_vendor, which represents another Vendor instance to trade with
my_priority, which represents a category that the Vendor wants to receive
their_priority, which represents a category that other_vendor wants to receive
The best item in my inventory that matches their_priority category is swapped with the best item in other_vendor's inventory that matches my_priority
It returns True
If the Vendor has no item that matches their_priority category, swapping does not happen, and it returns False
If other_vendor has no item that matches my_priority category, swapping does not happen, and it returns False
"""
        pass




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



