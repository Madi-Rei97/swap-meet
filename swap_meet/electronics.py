class Electronics:

    """Has an attribute id that is by default a unique integer
Has an attribute type that is by default the string "Unknown"
This attribute describes what kind of electronic device this is. Some example values might be 
“Kitchen Appliance”, “Game Console”, or “Health Tracker”
When we initialize an instance of Electronics, we can optionally pass in a string with the
 keyword argument type
Has an function get_category that returns "Electronics"
Has a stringify method that returns "An object of type Electronics with id <id value>. 
This is a <type value> device."
For example, if we had an Electronics instance with an id of 123435 and type attribute of 
"Mobile Phone", its stringify method should return "An object of type Electronics with id 12345.
 This is a Mobile Phone device."
All three new classes and the Item class have an attribute called condition, which can be optionally 
provided in the initializer. The default value should be 0

All three new classes and the Item class have an instance method named condition_description, 
which should describe the condition in words based on the value, assuming they all range from 0 to 5.

These can be basic descriptions (eg. 'mint', 'heavily used') but feel free to have fun with these 
(e.g. 'You probably want a glove for this one...").
The one requirement is that all the classes share the same condition_description behavior.


Tip: Importing Item
You'll need to refer to Item in order to declare it as a parent. To reference the Item class from these modules, try this import line:

from swap_meet.item import Item

"""
    pass

    def __init__():
        pass

